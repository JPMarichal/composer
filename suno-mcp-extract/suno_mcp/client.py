"""HTTP client for Suno studio API using Clerk JWT from the browser session."""

from __future__ import annotations

import base64
import json
import time
from pathlib import Path
from typing import Any

import httpx

from .browser import get_browser_session
from .config import SUNO_API_BASE


class SunoClient:
    """Authenticated client for studio-api.prod.suno.com."""

    def __init__(self) -> None:
        self._token: str | None = None
        self._token_expiry: float = 0
        self._http = httpx.AsyncClient(
            base_url=SUNO_API_BASE,
            timeout=60.0,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                ),
                "Content-Type": "application/json",
            },
        )

    async def close(self) -> None:
        await self._http.aclose()

    async def _ensure_token(self) -> str:
        if self._token and time.time() * 1000 < self._token_expiry:
            return self._token

        session = get_browser_session()
        token = await session.get_token()
        self._token = token

        try:
            payload_b64 = token.split(".")[1]
            padding = "=" * (-len(payload_b64) % 4)
            payload = json.loads(base64.urlsafe_b64decode(payload_b64 + padding))
            self._token_expiry = (payload["exp"] * 1000) - (5 * 60 * 1000)
        except Exception:
            self._token_expiry = time.time() * 1000 + 50 * 60 * 1000

        return token

    async def _request(self, method: str, path: str, **kwargs) -> Any:
        token = await self._ensure_token()
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {token}"

        response = await self._http.request(method, path, headers=headers, **kwargs)
        if response.status_code == 401:
            self._token = None
            token = await self._ensure_token()
            headers["Authorization"] = f"Bearer {token}"
            response = await self._http.request(method, path, headers=headers, **kwargs)

        if not response.is_success:
            raise RuntimeError(f"API {path} {response.status_code}: {response.text[:300]}")

        return response.json()

    async def get_credits(self) -> Any:
        return await self._request("GET", "/api/billing/info/")

    async def get_song_status(self, ids: list[str]) -> Any:
        ids_param = ",".join(ids)
        return await self._request("GET", f"/api/feed/v2?ids={ids_param}")

    async def get_recent_songs(self, page: int = 1) -> Any:
        return await self._request("GET", f"/api/project/default?page={page}")

    async def get_recent_songs(self, page: int = 1) -> Any:
        return await self._request("GET", f"/api/project/default?page={page}")

    @staticmethod
    def _extract_clip_ids(project: Any) -> set[str]:
        ids: set[str] = set()
        for entry in project.get("project_clips") or []:
            clip = entry.get("clip") or entry
            clip_id = clip.get("id")
            if clip_id:
                ids.add(clip_id)
        return ids

    @staticmethod
    def _extract_clips(project: Any) -> list[dict[str, Any]]:
        clips: list[dict[str, Any]] = []
        for entry in project.get("project_clips") or []:
            clip = entry.get("clip") or entry
            if clip.get("id"):
                clips.append(clip)
        return clips

    async def _poll_for_new_clips(self, before_ids: set[str], *, attempts: int = 20, interval: float = 2.0) -> list[dict[str, Any]]:
        import asyncio

        for _ in range(attempts):
            await asyncio.sleep(interval)
            project = await self.get_recent_songs()
            new_clips = [c for c in self._extract_clips(project) if c["id"] not in before_ids]
            if new_clips:
                return new_clips
        return []

    async def generate_song(self, *, lyrics: str, style: str) -> dict[str, Any]:
        before_ids = self._extract_clip_ids(await self.get_recent_songs())
        session = get_browser_session()
        result = await session.drive_generate(mode="custom", lyrics=lyrics, style=style)
        if result.get("clips"):
            return result

        new_clips = await self._poll_for_new_clips(before_ids)
        if new_clips:
            return {"clips": new_clips, "message": "Song generation started (detected via library poll)"}

        detail = result.get("message") or "Generation did not start."
        prepared = result.get("prepared")
        hint = ""
        if prepared:
            hint = f" Prepared click at ({prepared.get('clickX')}, {prepared.get('clickY')})."
        raise RuntimeError(
            f"{detail}{hint} "
            "Make sure the Suno MCP browser window is visible (SUNO_HEADLESS=false), "
            "you are logged in at suno.com/create, and complete any hCaptcha if prompted."
        )

    async def generate_from_description(self, description: str) -> dict[str, Any]:
        before_ids = self._extract_clip_ids(await self.get_recent_songs())
        session = get_browser_session()
        result = await session.drive_generate(mode="simple", simple_prompt=description)
        if result.get("clips"):
            return result

        new_clips = await self._poll_for_new_clips(before_ids)
        if new_clips:
            return {"clips": new_clips, "message": "Song generation started (detected via library poll)"}

        detail = result.get("message") or "Generation did not start."
        raise RuntimeError(
            f"{detail} "
            "Make sure the Suno MCP browser window is visible (SUNO_HEADLESS=false), "
            "you are logged in at suno.com/create, and complete any hCaptcha if prompted."
        )

    async def wait_for_songs(
        self,
        ids: list[str],
        max_wait: int = 180,
        poll_interval: int = 5,
    ) -> list[dict[str, Any]]:
        import asyncio

        deadline = time.time() + max_wait
        while time.time() < deadline:
            status = await self.get_song_status(ids)
            clips = status if isinstance(status, list) else status.get("clips", status)
            if isinstance(clips, list) and clips:
                done = all(c.get("status") in ("complete", "streaming") for c in clips)
                if done:
                    return [
                        {
                            "id": c["id"],
                            "title": c.get("title"),
                            "audio_url": c.get("audio_url"),
                            "image_url": c.get("image_url"),
                            "status": c.get("status"),
                            "suno_url": f"https://suno.com/song/{c['id']}",
                        }
                        for c in clips
                    ]
            await asyncio.sleep(poll_interval)

        raise TimeoutError(f"Songs not ready after {max_wait}s: {ids}")

    async def download_song(self, song_id: str, folder: str, filename: str | None = None) -> dict[str, Any]:
        status = await self.get_song_status([song_id])
        clips = status if isinstance(status, list) else status.get("clips", [])
        song = next((c for c in clips if c.get("id") == song_id), None)
        if not song:
            raise RuntimeError(f"Song not found: {song_id}")
        if song.get("status") not in ("complete", "streaming"):
            raise RuntimeError(f"Song not ready. Status: {song.get('status')}")

        audio_url = song.get("audio_url") or f"https://cdn1.suno.ai/{song_id}.mp3"
        if "cdn" not in audio_url:
            audio_url = f"https://cdn1.suno.ai/{song_id}.mp3"

        out_dir = Path(folder).expanduser()
        out_dir.mkdir(parents=True, exist_ok=True)

        base = filename or song.get("title") or song_id
        safe = "".join(ch if ch.isalnum() or ch in "-_ " else "" for ch in base)
        safe = "-".join(safe.split()).lower() or song_id
        out_path = out_dir / f"{safe}.mp3"

        async with httpx.AsyncClient(timeout=120.0) as dl:
            resp = await dl.get(audio_url)
            resp.raise_for_status()
            out_path.write_bytes(resp.content)

        return {
            "path": str(out_path),
            "size": out_path.stat().st_size,
            "song_id": song_id,
            "title": song.get("title"),
            "audio_url": audio_url,
            "suno_url": f"https://suno.com/song/{song_id}",
        }


_client: SunoClient | None = None


def get_client() -> SunoClient:
    global _client
    if _client is None:
        _client = SunoClient()
    return _client

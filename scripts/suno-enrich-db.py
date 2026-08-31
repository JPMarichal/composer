"""Enrich the Suno SQLite database from the authenticated Suno feed API."""

import json
import os
import sqlite3
import time
from pathlib import Path

import httpx


PROJECT_ROOT = Path("C:\\own\\composer")
DB_PATH = PROJECT_ROOT / "canciones" / "audio" / "bksuno" / "_downloads.sqlite"
ENV_PATH = PROJECT_ROOT / ".env"
API_URL = "https://studio-api.prod.suno.com/api/feed/v2"
BATCH_SIZE = 50


def read_jwt():
    direct_jwt = os.environ.get("SUNO_JWT")
    if direct_jwt:
        return direct_jwt.strip().strip('"').strip("'")

    with open(ENV_PATH, encoding="utf-8") as env_file:
        for line in env_file:
            if line.startswith("SUNO_COOKIE="):
                cookie = line.split("=", 1)[1].strip().strip('"').strip("'")
                for part in cookie.split(";"):
                    part = part.strip()
                    if part.startswith("__session="):
                        return part.split("=", 1)[1]
    return None


def json_text(value):
    return json.dumps(value, ensure_ascii=False) if value is not None else None


def fetch_batch(client, ids):
    for attempt in range(6):
        response = client.get(API_URL, params={"ids": ",".join(ids)})
        if response.status_code == 200:
            return response.json().get("clips", [])
        if response.status_code == 429:
            time.sleep(min(5 * (attempt + 1), 60))
            continue
        if response.status_code in (401, 403):
            raise RuntimeError(
                f"Suno authentication failed (HTTP {response.status_code})"
            )
        raise RuntimeError(
            f"Suno API failed (HTTP {response.status_code}): {response.text[:300]}"
        )
    raise RuntimeError("Suno API rate limit retries exhausted")


def main():
    jwt = read_jwt()
    if not jwt:
        raise SystemExit("ERROR: SUNO_COOKIE with __session was not found in .env")

    conn = sqlite3.connect(DB_PATH)
    ids = [row[0] for row in conn.execute("SELECT id FROM clips ORDER BY id")]
    print(f"Enriching {len(ids)} clips in batches of {BATCH_SIZE}...")

    headers = {
        "Authorization": f"Bearer {jwt}",
        "User-Agent": "Mozilla/5.0",
    }
    updated = 0
    missing = 0

    with httpx.Client(headers=headers, timeout=60.0, verify=False) as client:
        for start in range(0, len(ids), BATCH_SIZE):
            batch_ids = ids[start : start + BATCH_SIZE]
            clips = {clip.get("id"): clip for clip in fetch_batch(client, batch_ids)}

            for clip_id in batch_ids:
                clip = clips.get(clip_id)
                if not clip:
                    missing += 1
                    continue

                metadata = clip.get("metadata") or {}
                project = clip.get("project")
                albums = clip.get("albums")
                media_urls = clip.get("media_urls") or []

                mp3_url = clip.get("audio_url") or ""
                m4a_url = ""
                for media in media_urls:
                    if media.get("content_type") == "mp3":
                        mp3_url = media.get("url") or mp3_url
                    elif media.get("content_type") == "m4a-opus":
                        m4a_url = media.get("url") or m4a_url

                conn.execute(
                    """
                    UPDATE clips SET
                        title = ?, status = ?, created_at = ?, model_name = ?,
                        major_model_version = ?, duration = ?,
                        mp3_url = ?, m4a_url = ?, image_url = ?, image_large_url = ?,
                        lyrics = ?, style_prompt = ?, display_tags = ?,
                        has_stem = ?, has_vocal = ?, stream = ?,
                        uses_latest_model = ?, clip_type = ?, task = ?,
                        video_url = ?, audio_url = ?, media_urls = ?,
                        is_public = ?, is_hidden = ?, is_trashed = ?,
                        is_verified = ?, user_id = ?, project_data = ?, albums_data = ?
                    WHERE id = ?
                    """,
                    (
                        clip.get("title"),
                        clip.get("status"),
                        clip.get("created_at"),
                        clip.get("model_name"),
                        clip.get("major_model_version"),
                        metadata.get("duration"),
                        mp3_url,
                        m4a_url,
                        clip.get("image_url", ""),
                        clip.get("image_large_url", ""),
                        metadata.get("prompt", ""),
                        metadata.get("tags", ""),
                        clip.get("display_tags", ""),
                        metadata.get("has_stem"),
                        metadata.get("has_vocal"),
                        metadata.get("stream"),
                        metadata.get("uses_latest_model"),
                        metadata.get("type"),
                        metadata.get("task"),
                        clip.get("video_url", ""),
                        clip.get("audio_url", ""),
                        json_text(media_urls),
                        clip.get("is_public"),
                        clip.get("is_hidden"),
                        clip.get("is_trashed"),
                        clip.get("is_verified"),
                        clip.get("user_id"),
                        json_text(project),
                        json_text(albums),
                        clip_id,
                    ),
                )
                updated += 1

            conn.commit()
            print(f"  {min(start + BATCH_SIZE, len(ids))}/{len(ids)} clips processed")

    conn.close()
    print(f"Updated: {updated}; missing from API response: {missing}")


if __name__ == "__main__":
    main()

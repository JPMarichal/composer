"""Fetch Suno clips using JWT from __session cookie with full metadata."""

import json, time, httpx, urllib3
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PROJECT_ROOT = Path("C:\\own\\composer")
ENV_PATH = PROJECT_ROOT / ".env"
INDEX_PATH = PROJECT_ROOT / "suno-index.json"
API_BASE = "https://studio-api.prod.suno.com"


def read_cookie():
    """Read SUNO_COOKIE from .env."""
    with open(ENV_PATH, encoding="utf-8") as f:
        for line in f:
            if line.startswith("SUNO_COOKIE="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def extract_jwt_from_cookie(cookie_str):
    """Extract JWT from __session cookie."""
    for part in cookie_str.split(";"):
        part = part.strip()
        if part.startswith("__session="):
            return part.split("=", 1)[1]
    return None


def extract_clip(c):
    """Extract all available fields from a clip object."""
    metadata = c.get("metadata") or {}
    project = c.get("project") or {}
    media_urls = c.get("media_urls") or []

    # Construct URLs directly (API doesn't always include them in feed)
    cid = c.get("id", "")
    mp3_url = f"https://cdn1.suno.ai/{cid}.mp3"
    m4a_url = f"https://d2lwuy8qc234o3.cloudfront.net/1/clip/{cid}.m4a"

    # Try to get from media_urls if available
    for mu in media_urls:
        ct = mu.get("content_type", "")
        if ct == "mp3" and mu.get("url"):
            mp3_url = mu["url"]
        elif ct == "m4a-opus" and mu.get("url"):
            m4a_url = mu["url"]

    # Fallback to audio_url if provided
    if not mp3_url and c.get("audio_url"):
        mp3_url = c["audio_url"]

    is_instrumental = (
        len(metadata.get("prompt", "")) == 0 or metadata.get("can_remix") is False
    )

    return {
        "id": c.get("id"),
        "title": c.get("title"),
        "status": c.get("status"),
        "created_at": c.get("created_at"),
        "model_name": c.get("model_name"),
        "major_model_version": c.get("major_model_version"),
        "project_id": project.get("id") if isinstance(project, dict) else None,
        "project_name": project.get("name") if isinstance(project, dict) else None,
        "project_description": project.get("description")
        if isinstance(project, dict)
        else None,
        "duration": metadata.get("duration"),
        "audio_url": c.get("audio_url", ""),
        "mp3_url": mp3_url,
        "m4a_url": m4a_url,
        "image_url": c.get("image_url", ""),
        "image_large_url": c.get("image_large_url", ""),
        "lyrics": metadata.get("prompt", ""),
        "style_prompt": metadata.get("tags", ""),
        "display_tags": c.get("display_tags", ""),
        "is_instrumental": is_instrumental,
        "can_remix": metadata.get("can_remix"),
        "has_stem": metadata.get("has_stem"),
        "play_count": c.get("play_count", 0),
        "upvote_count": c.get("upvote_count", 0),
        "user_id": c.get("user_id"),
        "display_name": c.get("display_name"),
        "handle": c.get("handle"),
        "is_public": c.get("is_public", False),
        "is_hidden": c.get("is_hidden", False),
        "is_trashed": c.get("is_trashed", False),
        "explicit": c.get("explicit", False),
        "has_hook": c.get("has_hook", False),
        "batch_index": c.get("batch_index", 0),
        "created_by": c.get("display_name") or c.get("handle"),
    }


def enumerate_all(jwt_token):
    """Fetch all clips using JWT auth."""
    print(f"Using JWT token (first 20 chars: {jwt_token[:20]}...)")

    session = httpx.Client(
        base_url=API_BASE,
        timeout=60.0,
        verify=False,
        headers={
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
        },
    )

    all_clips = []
    page = 1
    retries = 0

    while retries < 10:
        try:
            resp = session.get(
                "/api/feed/v2",
                params={"page": page, "page_size": 50},
            )
        except Exception as e:
            print(f"Page {page}: error {e}")
            break

        if resp.status_code == 429:
            wait = min(2**retries * 5, 120)
            print(f"  Rate limited, waiting {wait}s...")
            time.sleep(wait)
            retries += 1
            continue

        retries = 0

        if resp.status_code == 401:
            print("  Auth expired (401) - JWT may be expired")
            break

        if resp.status_code != 200:
            print(f"  Page {page}: HTTP {resp.status_code} - stopping")
            print(f"  Response: {resp.text[:300]}")
            break

        data = resp.json()
        clips = data.get("clips", [])
        if not clips:
            break

        for c in clips:
            extracted = extract_clip(c)
            all_clips.append(extracted)

        print(f"  Page {page}: {len(clips)} clips (total: {len(all_clips)})")
        page += 1
        time.sleep(1.5)

    print(f"\n  Fetched: {len(all_clips)} clips from feed.")

    # Merge with existing index
    existing = {"clips": []}
    if INDEX_PATH.exists():
        with open(INDEX_PATH, encoding="utf-8") as f:
            existing = json.load(f)

    existing_by_id = {c["id"]: c for c in existing["clips"]}
    new_count = updated_count = 0
    for c in all_clips:
        cid = c["id"]
        if cid not in existing_by_id:
            existing_by_id[cid] = c
            new_count += 1
        else:
            old = existing_by_id[cid]
            # Update if any field changed
            if c != old:
                existing_by_id[cid].update(c)
                updated_count += 1

    existing["clips"] = list(existing_by_id.values())
    existing["total"] = len(existing["clips"])
    existing["generated_at"] = time.time()
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    unchanged = len(existing["clips"]) - new_count - updated_count
    print(f"  Saved: {new_count} new + {updated_count} updated + {unchanged} unchanged")
    print(f"  Total: {existing['total']} clips")

    by_project = {}
    for c in existing["clips"]:
        pn = c["project_name"] or "My Workspace"
        by_project.setdefault(pn, []).append(c)
    print(f"\n  Projects ({len(by_project)}):")
    for pn, pcs in sorted(by_project.items(), key=lambda x: -len(x[1])):
        instr = sum(1 for c in pcs if c.get("is_instrumental"))
        print(f"    {pn}: {len(pcs)} ({instr} instrumental)")

    # Search for "último eslabón"
    print("\n  Searching for 'último eslabón'...")
    matches = [
        c
        for c in existing["clips"]
        if any(
            kw in (c.get("title") or "").lower()
            for kw in ["último", "eslabon", "ultimo", "eslabón"]
        )
    ]
    if matches:
        print(f"  Found {len(matches)} clips:")
        for m in matches:
            print(
                f'    "{m["title"]}" | {m["id"][:8]}... | {m.get("created_at", "?")[:10]} | project: {m.get("project_name", "?")}'
            )
    else:
        print("  NOT FOUND in index")

    session.close()


if __name__ == "__main__":
    cookie_str = read_cookie()
    if not cookie_str:
        print("ERROR: No SUNO_COOKIE found")
        exit(1)

    jwt_token = extract_jwt_from_cookie(cookie_str)
    if not jwt_token:
        print("ERROR: No __session cookie found")
        exit(1)

    enumerate_all(jwt_token)

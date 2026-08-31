"""Get JWT token from SUNO_COOKIE and fetch clips via studio-api."""

import json, time, httpx, urllib3, base64
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
    """Extract JWT token from __client cookie."""
    for part in cookie_str.split(";"):
        part = part.strip()
        if part.startswith("__client="):
            return part.split("=", 1)[1]
    return None


def enumerate_all(token):
    """Fetch all clips using JWT auth."""
    print(f"Using JWT token (first 20 chars: {token[:20]}...)")

    session = httpx.Client(
        base_url=API_BASE,
        timeout=60.0,
        verify=False,
        headers={
            "Authorization": f"Bearer {token}",
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
            print("  Auth expired (401)")
            # Try to refresh by checking if token is still valid
            print("  Token may be expired - cannot refresh without browser")
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
            proj = c.get("project") or {}
            all_clips.append(
                {
                    "id": c.get("id"),
                    "title": c.get("title"),
                    "status": c.get("status"),
                    "created_at": c.get("created_at"),
                    "model_name": c.get("model_name"),
                    "project_id": proj.get("id") if isinstance(proj, dict) else None,
                    "project_name": proj.get("name")
                    if isinstance(proj, dict)
                    else None,
                    "duration": (c.get("metadata") or {}).get("duration"),
                }
            )

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
            if (
                c.get("project_id") != old.get("project_id")
                or c.get("project_name") != old.get("project_name")
                or c.get("title") != old.get("title")
                or c.get("status") != old.get("status")
            ):
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
        pn = c["project_name"] or "Unassigned"
        by_project.setdefault(pn, []).append(c)
    print(f"\n  Projects ({len(by_project)}):")
    for pn, pcs in sorted(by_project.items(), key=lambda x: -len(x[1])):
        print(f"    {pn}: {len(pcs)}")

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
                f'    "{m["title"]}" | {m["id"][:8]}... | {m.get("created_at", "?")[:10]}'
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
        print("ERROR: No __client cookie found")
        exit(1)

    enumerate_all(jwt_token)

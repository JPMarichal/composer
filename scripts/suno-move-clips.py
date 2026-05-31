"""Move Suno clips between projects.
Usage:
  just suno-move-clips <target_project> <clip_title> [<clip_title> ...]
  just suno-move-clips <target_project> --from <source_project> <clip_title> [...]

Searches the local index (suno-index.json) for clip titles, then uses the
Suno API to move each matching clip to the target project.

API endpoint: POST /api/project/{project_id}/clips
Body: {"update_type": "add", "metadata": {"clip_ids": [...]}}
Remove body: {"update_type": "remove", "metadata": {"clip_ids": [...]}}
"""
from __future__ import annotations

import asyncio
import json
import os
import re
import sys
from typing import Any

MCP_SRC = r"C:\Users\JUANPA~1.MAR\AppData\Local\Temp\opencode\suno-ai-mcp\src"
sys.path.insert(0, MCP_SRC)

os.environ["SSL_VERIFY"] = "0"

from suno_mcp.suno_client import SunoClient  # noqa: E402

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")
INDEX_PATH = os.path.join(BASE_DIR, "suno-index.json")


def fatal(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def read_cookie() -> str:
    if not os.path.exists(ENV_PATH):
        fatal(f".env not found at {ENV_PATH}")
    with open(ENV_PATH) as f:
        for line in f:
            if line.startswith("SUNO_COOKIE="):
                raw = line.split("=", 1)[1].strip()
                return raw.strip('"').strip("'")
    fatal("SUNO_COOKIE not found in .env")


def load_index() -> list[dict[str, Any]]:
    if not os.path.exists(INDEX_PATH):
        fatal(f"suno-index.json not found at {INDEX_PATH}. Run 'just suno-index' first.")
    with open(INDEX_PATH, encoding="utf-8") as f:
        return json.load(f)["clips"]


def find_project_id(clips: list[dict[str, Any]], name: str) -> str | None:
    """Search local index for any clip in this project to get its project_id."""
    name_lower = name.lower().strip()
    for c in clips:
        pn = (c.get("project_name") or "").lower().strip()
        if pn == name_lower or (not name_lower and not c.get("project_name")):
            pid = c.get("project_id")
            if pid:
                return pid
    return None


def search_clips(clips: list[dict[str, Any]], terms: list[str]) -> list[dict[str, Any]]:
    """Find clips matching ALL given title terms (case-insensitive)."""
    matches: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for c in clips:
        cid = c.get("id")
        if not cid or cid in seen_ids:
            continue
        title = (c.get("title") or "").lower()
        if all(t.lower() in title for t in terms):
            matches.append(c)
            seen_ids.add(cid)
    return matches


async def resolve_project_id(client: SunoClient, name: str) -> str | None:
    """Search Suno API for a project by name. Returns project id or None."""
    resp = await client._api("GET", "/api/project/me")
    if resp.status_code != 200:
        return None
    for p in resp.json().get("projects", []):
        if p.get("name", "").lower().strip() == name.lower().strip():
            return p["id"]
    return None


async def remove_from_project(client: SunoClient, project_id: str, clip_ids: list[str]) -> bool:
    """Remove clips from a project."""
    body = {"update_type": "remove", "metadata": {"clip_ids": clip_ids}}
    resp = await client._api("POST", f"/api/project/{project_id}/clips", json_body=body)
    return resp.status_code == 204


async def add_to_project(client: SunoClient, project_id: str, clip_ids: list[str]) -> bool:
    """Add clips to a project."""
    body = {"update_type": "add", "metadata": {"clip_ids": clip_ids}}
    resp = await client._api("POST", f"/api/project/{project_id}/clips", json_body=body)
    return resp.status_code == 204


async def verify_project_content(client: SunoClient, project_id: str) -> list[dict[str, Any]]:
    """Return list of {title, id} for clips in a project."""
    resp = await client._api("GET", f"/api/project/{project_id}")
    if resp.status_code != 200:
        return []
    clips = resp.json().get("project_clips", [])
    return [{"title": pc["clip"]["title"], "id": pc["clip"]["id"]} for pc in clips]


def print_summary(ok: list[str], fail: list[tuple[str, str]]) -> None:
    if ok:
        print(f"\n  Moved: {len(ok)} clip(s)")
        for cid in ok:
            print(f"    OK  {cid}")
    if fail:
        print(f"\n  Failed: {len(fail)} clip(s)")
        for cid, reason in fail:
            print(f"    FAIL {cid}: {reason}")
    print()


async def main() -> None:
    args = sys.argv[1:]
    if not args or "-h" in args or "--help" in args:
        print(__doc__)
        sys.exit(0)

    target_project_name: str | None = None
    source_project_name: str | None = None
    search_terms: list[str] = []
    i = 0

    # Parse: [--from <source>] <target> <title...>
    if i < len(args) and args[i] == "--from":
        i += 1
        if i >= len(args):
            fatal("--from requires a project name")
        source_project_name = args[i]
        i += 1

    if i >= len(args):
        fatal("Missing target project name")
    target_project_name = args[i]
    i += 1
    search_terms = args[i:] if i < len(args) else []

    if not search_terms:
        fatal("No clip title(s) provided")

    cookie = read_cookie()
    clips = load_index()

    # Search index for matching clips
    matched = search_clips(clips, search_terms)
    if not matched:
        print(f"No clips found matching: {' '.join(search_terms)}")
        print("Tip: use 'just suno-search <term>' to verify titles in the index.")
        sys.exit(1)

    print(f"Found {len(matched)} clip(s) matching '{' '.join(search_terms)}':")
    for c in matched:
        print(f"  {c['id']} | {c['title']} | {c['project_name'] or 'Unassigned'}")
    print()

    async with SunoClient(cookie) as client:
        # Resolve target project id
        target_id = await resolve_project_id(client, target_project_name)
        if not target_id:
            fatal(f"Target project '{target_project_name}' not found via API. "
                  f"Use 'just suno-list-projects' to list available projects.")
        print(f"Target project: {target_project_name} ({target_id})")

        # Resolve source project id (if specified)
        source_id: str | None = None
        if source_project_name:
            source_id = await resolve_project_id(client, source_project_name)
            if not source_id:
                fatal(f"Source project '{source_project_name}' not found via API.")
            print(f"Source project: {source_project_name} ({source_id})")

        # Collect full clip IDs (from the index, which has full UUIDs)
        clip_ids = [c["id"] for c in matched]

        # Remove from source project first, if specified
        if source_id:
            print(f"\nRemoving {len(clip_ids)} clip(s) from '{source_project_name}'...")
            if await remove_from_project(client, source_id, clip_ids):
                print("  Removed successfully.")
            else:
                print("  Warning: remove failed (clips may already be outside that project).")

        # Add to target project
        print(f"\nAdding {len(clip_ids)} clip(s) to '{target_project_name}'...")
        ok: list[str] = []
        fail: list[tuple[str, str]] = []

        # Try batch first
        if await add_to_project(client, target_id, clip_ids):
            ok = clip_ids[:]
            print("  Batch add succeeded.")
        else:
            # Fall back to one-by-one
            print("  Batch add failed, trying one at a time...")
            for cid in clip_ids:
                if await add_to_project(client, target_id, [cid]):
                    ok.append(cid)
                else:
                    fail.append((cid, "API rejected this clip ID"))

        # Verify
        print("\nVerifying target project...")
        final = await verify_project_content(client, target_id)
        print(f"  {target_project_name} now has {len(final)} clip(s):")
        for c in sorted(final, key=lambda x: x["title"]):
            mark = " <<" if c["id"] in clip_ids else ""
            print(f"    {c['title']} ({c['id']}){mark}")

        # Check source after removal (if applicable)
        if source_id:
            src_final = await verify_project_content(client, source_id)
            print(f"\n  {source_project_name} now has {len(src_final)} clip(s):")
            for c in sorted(src_final, key=lambda x: x["title"]):
                print(f"    {c['title']} ({c['id']})")

        print_summary(ok, fail)


if __name__ == "__main__":
    asyncio.run(main())

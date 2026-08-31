"""Fetch full lyrics from Suno API for a specific clip."""

import json, httpx, urllib3

urllib3.disable_warnings()

# Read cookie
with open(".env", encoding="utf-8") as f:
    for line in f:
        if line.startswith("SUNO_COOKIE="):
            cookie_str = line.split("=", 1)[1].strip().strip('"').strip("'")
            break

jwt = None
for part in cookie_str.split(";"):
    if part.strip().startswith("__session="):
        jwt = part.split("=", 1)[1]
        break

cid = "bbc56d30-077e-42ed-84f3-bbb0eb3f8306"  # Eres tu mi amanecer (Otros90s)

session = httpx.Client(
    base_url="https://studio-api.prod.suno.com",
    timeout=60,
    verify=False,
    headers={
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
    },
)

resp = session.get("/api/feed/v2", params={"ids": cid})
data = resp.json()
clip = data["clips"][0]

meta = clip.get("metadata") or {}
prompt = meta.get("prompt", "")

print(f"Title: {clip.get('title')}")
print(f"Project: {clip.get('project', {}).get('name')}")
print(f"\nLyrics ({len(prompt)} chars):")
print("-" * 70)
print(prompt)
print("-" * 70)

session.close()

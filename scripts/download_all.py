"""Batch download MP3s for all matched canciones/ songs."""
import json, os, re, unicodedata, sys, requests, urllib3
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

INDEX_PATH = 'suno-index.json'
CANCIONES_DIR = 'canciones'
AUDIO_DIR = 'audio'
os.makedirs(AUDIO_DIR, exist_ok=True)

def normalize(s):
    s = re.sub(r'\s*\(.*?\)\s*$', '', s)
    s = s.strip().lower()
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r'[^a-z0-9 ]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Load index
with open(INDEX_PATH, encoding='utf-8') as f:
    idx = json.load(f)

# Build normalized lookup
clip_by_norm = {}
for c in idx['clips']:
    key = normalize(c['title'])
    if key not in clip_by_norm:
        clip_by_norm[key] = c  # take first match

# List songs
song_files = [f for f in os.listdir(CANCIONES_DIR) if f.endswith('.md')]
matched = []
for sf in song_files:
    name = sf.replace('.md', '')
    norm = normalize(name.replace('-', ' '))
    clip = clip_by_norm.get(norm)
    if clip:
        matched.append((name, clip))
    else:
        print(f"  SKIP (no match): {name}")

print(f"\nDownloading {len(matched)} songs to {AUDIO_DIR}/ ...")
session = requests.Session()
ok = 0
fail = 0
for name, clip in matched:
    cid = clip['id']
    title = clip['title']
    # Sanitize filename
    safe = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
    fpath = os.path.join(AUDIO_DIR, f"{safe}.mp3")
    if os.path.exists(fpath) and os.path.getsize(fpath) > 100000:
        print(f"  EXISTS: {title}")
        ok += 1
        continue
    url = f"https://cdn1.suno.ai/{cid}.mp3"
    try:
        r = session.get(url, timeout=30, verify=False)
        r.raise_for_status()
        with open(fpath, 'wb') as f:
            f.write(r.content)
        size_mb = len(r.content) / (1024*1024)
        print(f"  OK: {title} ({size_mb:.1f} MB)")
        ok += 1
    except Exception as e:
        print(f"  FAIL: {title} ({e})")
        fail += 1

print(f"\nDone: {ok} OK, {fail} failed")

"""Download thumbnails for songs distributed by OffStep (or another distributor).

Usage:
    suno-thumbs.py                        # OffStep songs
    suno-thumbs.py --distributor "Distro" # custom distributor
    suno-thumbs.py "Song title"           # single song (fuzzy match)
"""
import asyncio, json, os, re, sys, unicodedata

os.environ['SSL_VERIFY'] = '0'

MCP_SRC = r'C:\Users\JUANPA~1.MAR\AppData\Local\Temp\opencode\suno-ai-mcp\src'
sys.path.insert(0, MCP_SRC)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE, 'suno-index.json')
CANCIONES = os.path.join(BASE, 'canciones')
THUMBS = os.path.join(CANCIONES, 'thumbs')

STOP_WORDS = {'los', 'las', 'del', 'con', 'por', 'para', 'como', 'mas', 'que'}

def slug_to_searchable(slug: str) -> set[str]:
    s = slug.lower().replace('-', ' ')
    words = set(re.findall(r'\w+', s))
    return {w for w in words if len(w) > 2 and w not in STOP_WORDS}

def normalize_text(t: str) -> str:
    return unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode('ascii').lower()

def find_best_clips(title_slug: str, index_clips: list[dict]) -> list[dict]:
    words = slug_to_searchable(title_slug)
    nwords = len(words)
    if nwords == 0:
        return []
    scored: list[tuple[float, dict]] = []
    for c in index_clips:
        ct = c.get('title', '')
        ct_words = set(re.findall(r'\w+', normalize_text(ct)))
        matching = words & ct_words
        n_match = len(matching)
        if n_match == 0:
            continue
        ratio = n_match / nwords
        if ratio >= 0.6 and n_match >= max(1, nwords - 1):
            score = ratio
            # bonus for exact prefix match
            if ct.lower().startswith(title_slug.replace('-', ' ')):
                score += 0.5
            scored.append((score, c))
    scored.sort(key=lambda x: -x[0])
    # Return only best matches (within 90% of top score)
    if not scored:
        return []
    top = scored[0][0]
    return [c for s, c in scored if s >= top * 0.9]

def extract_titles_from_md(filepath: str) -> dict:
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
    title_match = re.search(r'\*\*T\u00edtulo de la canci\u00f3n:\*\*\s*(.+)$', text, re.MULTILINE)
    dist_match = re.search(r'\*\*Distribuidor:\*\*\s*(.+)$', text, re.MULTILINE)
    suno_match = re.search(r'\*\*T\u00edtulo Suno:\*\*\s*(.+)$', text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else None
    distributor = dist_match.group(1).strip() if dist_match else None
    suno_title = suno_match.group(1).strip() if suno_match else None
    return {'title': title, 'distributor': distributor, 'suno_title': suno_title, 'file': filepath}

async def download_thumbs(target_distributor: str | None = None, single_search: str | None = None):
    from suno_mcp.suno_client import SunoClient

    env_path = os.path.join(BASE, '.env')
    if not os.path.exists(env_path):
        print("ERROR: .env not found")
        sys.exit(1)
    with open(env_path) as f:
        cookie = None
        for line in f:
            if line.startswith('SUNO_COOKIE='):
                cookie = line.split('=', 1)[1].strip().strip('"').strip("'")
                break
    if not cookie:
        print("ERROR: SUNO_COOKIE not found in .env")
        sys.exit(1)

    if not os.path.exists(INDEX_PATH):
        print("ERROR: suno-index.json not found. Run 'just suno-index' first.")
        sys.exit(1)
    with open(INDEX_PATH, encoding='utf-8') as f:
        idx = json.load(f)
    all_clips = idx['clips']

    targets = []
    if single_search:
        md_path = os.path.join(CANCIONES, single_search if single_search.endswith('.md') else f'{single_search}.md')
        if os.path.exists(md_path):
            meta = extract_titles_from_md(md_path)
            if meta['title']:
                targets.append(meta)
        else:
            for fn in os.listdir(CANCIONES):
                if not fn.endswith('.md'):
                    continue
                if normalize_text(single_search) in normalize_text(fn):
                    meta = extract_titles_from_md(os.path.join(CANCIONES, fn))
                    if meta['title']:
                        targets.append(meta)
    elif target_distributor:
        for fn in sorted(os.listdir(CANCIONES)):
            if not fn.endswith('.md'):
                continue
            fp = os.path.join(CANCIONES, fn)
            meta = extract_titles_from_md(fp)
            if meta['distributor'] and target_distributor.lower() in meta['distributor'].lower():
                targets.append(meta)

    if not targets:
        print("No songs matched.")
        return

    os.makedirs(THUMBS, exist_ok=True)

    async with SunoClient(cookie) as client:
        for song in targets:
            title = song['title']
            slug = os.path.splitext(os.path.basename(song['file']))[0]

            print()
            print(f"== {title} ==")
            print(f"   File: {slug}.md")

            # Strategy 1: slug-based fuzzy match
            matches = find_best_clips(slug, all_clips)
            # Strategy 2: explicit Título Suno if slug failed
            if not matches and song.get('suno_title'):
                suno_slug = song['suno_title'].lower().replace(' ', '-')
                matches = find_best_clips(suno_slug, all_clips)
                if matches:
                    print(f"   -> matched via Título Suno: {song['suno_title']}")
            # Strategy 3: full canción title as slug if both failed
            if not matches and song.get('title'):
                title_slug = song['title'].lower().replace(' ', '-')
                matches = find_best_clips(title_slug, all_clips)
                if matches:
                    print(f"   -> matched via título: {song['title']}")
            if not matches:
                print("   - No matches in Suno index")
                continue

            print(f"   Matches: {len(matches)}")
            clip_ids = [m['id'] for m in matches]

            clips_data = []
            try:
                clips_data = await client.get_songs(clip_ids)
            except Exception:
                pass
            # Fallback per-clip for anything not in feed response
            if len(clips_data) < len(clip_ids):
                got_ids = {c['id'] for c in clips_data}
                for cid in clip_ids:
                    if cid not in got_ids:
                        try:
                            raw = await client.get_clip(cid)
                            clips_data.append(raw)
                        except Exception as e:
                            print(f"   - get_clip {cid[:8]}: {e}")

            downloaded = 0
            for clip_data in clips_data:
                img_url = clip_data.get('image_url')
                if not img_url:
                    continue
                clip_title = clip_data.get('title', 'unknown')
                safe_title = re.sub(r'[^\w\-]+', '_', clip_title)[:60]
                ext = os.path.splitext(img_url.split('?')[0])[1] or '.jpg'
                out_name = f"{slug}_{clip_data['id'][:8]}_{safe_title}{ext}"
                out_path = os.path.join(THUMBS, out_name)

                if os.path.exists(out_path):
                    print(f"   + exists: {out_name}")
                    downloaded += 1
                    continue

                import httpx
                try:
                    async with httpx.AsyncClient(verify=False) as hc:
                        resp = await hc.get(img_url, timeout=30)
                        resp.raise_for_status()
                        with open(out_path, 'wb') as f:
                            f.write(resp.content)
                        print(f"   + saved: {out_name} ({len(resp.content)} bytes)")
                        downloaded += 1
                except Exception as e:
                    print(f"   - download error for {clip_title[:40]}: {e}")

            if downloaded == 0:
                print("   - no image_url found for any match")

    print()
    print(f"Done. Thumbnails saved to: {THUMBS}")

if __name__ == '__main__':
    args = sys.argv[1:]
    target_distributor = None
    single_search = None

    if not args:
        target_distributor = 'OffStep'
    elif args[0] == '--distributor' and len(args) >= 2:
        target_distributor = args[1]
    else:
        single_search = ' '.join(args)

    asyncio.run(download_thumbs(target_distributor, single_search))

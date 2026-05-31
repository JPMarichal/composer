"""Enumerate ALL Suno clips via paginated feed and build local index."""
import asyncio, json, os, sys, time

# Add MCP source to path for SunoClient
MCP_SRC = r'C:\Users\JUANPA~1.MAR\AppData\Local\Temp\opencode\suno-ai-mcp\src'
sys.path.insert(0, MCP_SRC)

from suno_mcp.suno_client import SunoClient  # noqa: E402

os.environ['SSL_VERIFY'] = '0'

ENV_PATH = os.path.join(os.path.dirname(__file__), '..', '.env')
INDEX_PATH = os.path.join(os.path.dirname(__file__), '..', 'suno-index.json')
PAGE_SIZE = 50


def read_cookie():
    if not os.path.exists(ENV_PATH):
        print(f"ERROR: .env not found at {ENV_PATH}")
        sys.exit(1)
    with open(ENV_PATH) as f:
        for line in f:
            if line.startswith('SUNO_COOKIE='):
                return line.split('=', 1)[1].strip().strip('"').strip("'")
    print("ERROR: SUNO_COOKIE not found in .env")
    sys.exit(1)


async def enumerate_all():
    cookie = read_cookie()
    async with SunoClient(cookie) as client:
        all_clips = []
        page = 1
        retries = 0
        while retries < 10:
            resp = await client._api(
                'GET', '/api/feed/v2',
                params={'page': page, 'page_size': PAGE_SIZE}
            )
            if resp.status_code == 429:
                wait = min(2 ** retries * 5, 120)
                print(f'page {page}: 429 rate limited, waiting {wait}s...')
                await asyncio.sleep(wait)
                retries += 1
                continue
            retries = 0
            if resp.status_code != 200:
                print(f'page {page}: {resp.status_code} - stopping')
                break
            data = resp.json()
            clips = data.get('clips', [])
            if not clips:
                break
            for c in clips:
                proj = c.get('project') or {}
                all_clips.append({
                    'id': c.get('id'),
                    'title': c.get('title'),
                    'status': c.get('status'),
                    'created_at': c.get('created_at'),
                    'model_name': c.get('model_name'),
                    'project_id': proj.get('id') if isinstance(proj, dict) else None,
                    'project_name': proj.get('name') if isinstance(proj, dict) else None,
                    'duration': (c.get('metadata') or {}).get('duration'),
                })
            print(f'page {page}: {len(clips)} clips (total so far: {len(all_clips)})')
            page += 1
            await asyncio.sleep(1.5)

        print(f'\nDone. Got {len(all_clips)} clips from feed.')

        # Merge with existing index
        existing = {'clips': []}
        if os.path.exists(INDEX_PATH):
            with open(INDEX_PATH, encoding='utf-8') as f:
                existing = json.load(f)

        existing_by_id = {c['id']: c for c in existing['clips']}
        new_count = 0
        updated_count = 0
        for c in all_clips:
            cid = c['id']
            if cid not in existing_by_id:
                existing_by_id[cid] = c
                new_count += 1
            else:
                # Update project info and other mutable fields
                old = existing_by_id[cid]
                if (c.get('project_id') != old.get('project_id')
                        or c.get('project_name') != old.get('project_name')
                        or c.get('title') != old.get('title')
                        or c.get('status') != old.get('status')):
                    existing_by_id[cid].update(c)
                    updated_count += 1

        existing['clips'] = list(existing_by_id.values())
        existing['total'] = len(existing['clips'])
        existing['generated_at'] = time.time()
        with open(INDEX_PATH, 'w', encoding='utf-8') as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)

        print(f'Saved {new_count} new + {updated_count} updated + {len(existing["clips"]) - new_count - updated_count} unchanged')
        print(f'Total: {existing["total"]} clips in {INDEX_PATH}')

        # Summary by project
        by_project = {}
        for c in existing['clips']:
            pn = c['project_name'] or 'Unassigned'
            by_project.setdefault(pn, []).append(c)
        print(f'\nProjects ({len(by_project)}):')
        for pn, clips in sorted(by_project.items(), key=lambda x: -len(x[1])):
            print(f'  {pn}: {len(clips)}')

if __name__ == '__main__':
    asyncio.run(enumerate_all())

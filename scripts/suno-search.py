"""Search the local Suno index by title keyword."""
import json, os, sys

INDEX_PATH = os.path.join(os.path.dirname(__file__), '..', 'suno-index.json')

if not os.path.exists(INDEX_PATH):
    print("ERROR: suno-index.json not found. Run 'just suno-index' first.")
    sys.exit(1)

query = ' '.join(sys.argv[1:]).lower()
if not query:
    print("Usage: suno-search.py <search term>")
    sys.exit(1)

with open(INDEX_PATH, encoding='utf-8') as f:
    idx = json.load(f)

matches = [c for c in idx['clips'] if query in c['title'].lower()]

if not matches:
    print(f"No matches for '{query}' in {len(idx['clips'])} clips.")
    sys.exit(0)

print(f"Matches: {len(matches)}")
for c in sorted(matches, key=lambda x: x.get('created_at') or '', reverse=True):
    print(f"  {c['id']} | {c['title']} | {c['project_name'] or 'Unassigned'} | {c.get('created_at','')[:10]}")

"""Show catalog summary from local Suno index."""
import json, os, sys

INDEX_PATH = os.path.join(os.path.dirname(__file__), '..', 'suno-index.json')

if not os.path.exists(INDEX_PATH):
    print("ERROR: suno-index.json not found. Run 'just suno-index' first.")
    sys.exit(1)

with open(INDEX_PATH, encoding='utf-8') as f:
    idx = json.load(f)

clips = idx['clips']
by_project = {}
for c in clips:
    pn = c.get('project_name') or 'Unassigned'
    by_project.setdefault(pn, []).append(c)

print(f"Total: {len(clips)} clips (last indexed: {idx.get('generated_at','?')})")
print(f"Projects: {len(by_project)}")
for pn, cs in sorted(by_project.items(), key=lambda x: -len(x[1])):
    print(f"  {pn}: {len(cs)}")

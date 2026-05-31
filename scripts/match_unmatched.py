import json

INDEX_PATH = 'suno-index.json'
with open(INDEX_PATH, encoding='utf-8') as f:
    idx = json.load(f)

terms = ['alma', 'coreografia', 'danza', 'extranos', 'farolas', 'hojas', 'porque', 'pensar', 'estan', 'cerium', 'disprosium', 'erbium', 'europium', 'galium', 'indium', 'iridium', 'kobalt', 'lanthanum', 'lithium', 'lutetium', 'niobium', 'osmium', 'promethium', 'rhenium', 'ruthenium', 'samarium', 'scandium', 'tantalum', 'terbium', 'ytterbium', 'yttrium', 'misma', 'lluvia', 'suelo']
for term in terms:
    matches = [c for c in idx['clips'] if term.lower() in c['title'].lower()]
    for m in matches:
        print(f"  {m['title']} | {m['project_name']}")
    if not matches:
        print(f"  [{term}] no matches")
    print()

import os, re, sys, shutil

APPLY = '--apply' in sys.argv
D = r'C:\Users\jpmar\OneDrive\Documents\Obsidian Vault\Canciones'
BK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.backup', 'frontmatter')

ORDER = ['notion-id', 'base', 'Género', 'Historia composición', 'Álbum',
         'Fecha de composición', 'Fecha de lanzamiento', 'TaggedLyrics',
         'Distribuidor', 'Tipo', 'Año', 'Estilo SUNO', 'Descripción', 'UPC',
         'Estado de publicación', 'Temas', 'ISRC', 'Generador']
DROP = {'"Música "'}
DEFAULTS = {
    'notion-id': '""',
    'base': '"[[Canciones de JPMarichal.base]]"',
    'Género': '[]', 'Álbum': '[]', 'Distribuidor': '[]', 'Temas': '[]',
    'Tipo': 'Canción', 'Estado de publicación': 'Sin procesar',
}

def split_blocks(fm, eol):
    blocks, cur = [], None
    for line in fm.split(eol):
        m = re.match(r'^([^\s:#-][^:]*):(.*)$', line)
        if m:
            cur = [m.group(1), [line]]
            blocks.append(cur)
        elif cur is not None:
            cur[1].append(line)
    return blocks

stats = {'reordered': 0, 'added_fm': 0, 'unchanged': 0, 'unknown_keys': set()}
os.makedirs(BK, exist_ok=True)
for f in sorted(os.listdir(D)):
    if not f.endswith('.md'):
        continue
    p = os.path.join(D, f)
    raw = open(p, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    t = raw.decode('utf-8-sig')
    eol = '\r\n' if '\r\n' in t else '\n'
    m = re.match(r'^---\r?\n(.*?)\r?\n---(\r?\n|\Z)', t, re.S)
    if m:
        blocks = split_blocks(m.group(1), eol)
        body = t[m.end():]
    else:
        blocks, body = [], t
        stats['added_fm'] += 1
    byk = {}
    for k, lines in blocks:
        if k in DROP:
            continue
        if k not in ORDER:
            stats['unknown_keys'].add(k)
        byk[k] = lines
    out = []
    for k in ORDER:
        if k in byk:
            out.extend(byk[k])
        else:
            out.append('%s: %s' % (k, DEFAULTS.get(k, '""')))
    for k, lines in byk.items():          # unknown keys kept at the end
        if k not in ORDER:
            out.extend(lines)
    new = '---' + eol + eol.join(out) + eol + '---' + eol + body
    if new == t:
        stats['unchanged'] += 1
        continue
    if m:
        stats['reordered'] += 1
    if APPLY:
        shutil.copy2(p, os.path.join(BK, f))
        data = new.encode('utf-8')
        open(p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + data)

print('APPLY' if APPLY else 'DRY-RUN', {k: (sorted(v) if isinstance(v, set) else v) for k, v in stats.items()})

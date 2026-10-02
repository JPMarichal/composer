"""Sincroniza P:\\Canciones\\audio\\{mp3,wav} -> bunny.net Storage (zona jpmarichal-cancionero), en subdirectorios mp3/ y wav/.

Uso: python bunny_audio.py [--apply] [--prune-root]
  (sin flags)   simula: muestra qué subiría
  --apply       sube archivos nuevos o con tamaño distinto (con checksum SHA256)
  --prune-root  borra de la RAÍZ de la zona los .mp3/.wav que ya tienen copia idéntica
                (mismo SHA256) en mp3/ o wav/. Es la limpieza de la migración; nunca borra
                nada que no tenga copia verificada.
- Solo toca mp3 y wav de las dos carpetas. NO toca bksuno ni Demos.
- Requiere la CLI `bunny` autenticada.
"""
import hashlib, json, os, subprocess, sys, unicodedata

APPLY = '--apply' in sys.argv
PRUNE = '--prune-root' in sys.argv
ZONE = 'jpmarichal-cancionero'
ROOT = r'P:\Canciones\audio'
FORMATS = ('mp3', 'wav')
nf = lambda s: unicodedata.normalize('NFC', s)

def bunny(args):
    return subprocess.run(['bunny'] + args, capture_output=True, text=True, encoding='utf-8', shell=True)

def remote_list(path):
    r = bunny(['storage', 'files', 'list', path, '--zone', ZONE, '-o', 'json'])
    try:
        data = json.loads(r.stdout)
    except ValueError:
        return []        # directorio aún inexistente
    return [i for i in data if not i.get('isDirectory')]

todo = []
for fmt in FORMATS:
    ldir = os.path.join(ROOT, fmt)
    local = {nf(f): f for f in os.listdir(ldir) if f.lower().endswith('.' + fmt)}
    remote = {nf(i['objectName']): i for i in remote_list(fmt + '/')}
    new = sorted(n for n in local if n not in remote)
    diff = sorted(n for n in local if n in remote and os.path.getsize(os.path.join(ldir, local[n])) != int(remote[n]['length']))
    extra = sorted(set(remote) - set(local))
    print('[%s] local=%d zona=%d nuevos=%d distintos=%d solo_en_zona=%d' % (fmt, len(local), len(remote), len(new), len(diff), len(extra)), flush=True)
    for label, names in (('  Nuevos', new), ('  Distintos', diff), ('  Solo en zona (no se borra)', extra)):
        if names:
            print(label + ':', names, flush=True)
    todo += [(fmt, os.path.join(ldir, local[n]), n) for n in new + diff]

if APPLY:
    for i, (fmt, path, n) in enumerate(todo, 1):
        r = bunny(['storage', 'files', 'upload', path, '--zone', ZONE, '--to', '%s/%s' % (fmt, n), '--checksum'])
        print('%s [%d/%d] %s/%s %s' % ('OK   ' if r.returncode == 0 else 'FALLO', i, len(todo), fmt, n, (r.stderr or '')[:200] if r.returncode else ''), flush=True)

if PRUNE:
    subs = {fmt: {nf(i['objectName']): i for i in remote_list(fmt + '/')} for fmt in FORMATS}
    for i in remote_list('/'):
        n, ext = nf(i['objectName']), i['objectName'].lower().rsplit('.', 1)[-1]
        if ext not in FORMATS:
            continue
        twin = subs[ext].get(n)
        if twin and (twin['checksum'] or '').upper() == (i['checksum'] or '').upper():
            r = bunny(['storage', 'files', 'remove', n, '--zone', ZONE, '--force'])
            print('%s raíz/%s' % ('BORRADO' if r.returncode == 0 else 'FALLO  ', n), flush=True)
        else:
            print('CONSERVADO raíz/%s (sin copia idéntica en %s/)' % (n, ext), flush=True)

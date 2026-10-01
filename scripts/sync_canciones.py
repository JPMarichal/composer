"""Sync Obsidian Canciones -> pCloud letras (Obsidian is the source of truth).
Usage: python sync_canciones.py [--apply]
- Copies new/changed files with kebab-case names.
- Reports (never deletes) files in pCloud with no Obsidian counterpart.
"""
import os, re, sys, shutil, unicodedata, filecmp

APPLY = '--apply' in sys.argv
SRC = r'C:\Users\jpmar\OneDrive\Documents\Obsidian Vault\Canciones'
DST = r'P:\Canciones\letras'

def kebab(name):
    n = os.path.splitext(name)[0].lower()
    n = ''.join(c for c in unicodedata.normalize('NFD', n) if unicodedata.category(c) != 'Mn')
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]', '-', n)).strip('-') + '.md'

src = {kebab(f): f for f in os.listdir(SRC) if f.endswith('.md')}
dst = {f for f in os.listdir(DST) if f.endswith('.md')}
new, changed = [], []
for k, f in sorted(src.items()):
    sp, dp = os.path.join(SRC, f), os.path.join(DST, k)
    if k not in dst:
        new.append(k)
    elif not filecmp.cmp(sp, dp, shallow=False):
        changed.append(k)
    else:
        continue
    if APPLY:
        shutil.copy2(sp, dp)
orphans = sorted(dst - set(src))
print('APPLY' if APPLY else 'DRY-RUN', 'new=%d changed=%d orphans_in_pcloud=%d' % (len(new), len(changed), len(orphans)))
for label, names in (('New', new), ('Changed', changed)):
    if names:
        print('%s:' % label, names)
if orphans:
    print('Only in pCloud:', orphans)

import os, re

files = [
    'la-oficina-de-objetos-perdidos.md', 'que-triste-esta-todo-sin-ti.md',
    'escucha-al-tiempo-hablar-por-mi.md', 'en-mi-cajon-izquierdo.md',
    'la-hija-del-dragon.md', 'para-escuchar-te-amo.md',
    'confession.md', 'ayer-me-encontre-a-ese-nino.md',
    'claveles.md', 'al-encuentro-del-amor.md',
    'farolas-sin-luz.md', 'hoy-necesito-escribir-una-cancion-de-amor.md',
    'vuelve-otra-vez.md'
]

headers = ["Cancion", "Lanzamiento", "Estado", "ISRC", "UPC"]
print(f"{headers[0]:40s} {headers[1]:15s} {headers[2]:30s} {headers[3]:20s} {headers[4]:15s}")
print("-" * 120)
for f in files:
    path = os.path.join('canciones', f)
    with open(path, encoding='utf-8') as fh:
        content = fh.read()
    lanz = re.search(r'Fecha de lanzamiento:\s*(.*)', content)
    est = re.search(r'Estado de publicacion:\s*(.*)', content)
    isrc = re.search(r'ISRC:\s*(.*)', content)
    upc = re.search(r'UPC:\s*(.*)', content)
    name = f.replace('.md', '').replace('-', ' ').title()
    print(f"{name:40s} {lanz.group(1) if lanz else 'MISSING':15s} {est.group(1) if est else 'MISSING':30s} {isrc.group(1) if isrc else 'MISSING':20s} {upc.group(1) if upc else 'MISSING':15s}")

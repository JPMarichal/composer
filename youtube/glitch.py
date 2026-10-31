"""Capa analógica y de glitch por código sobre las imágenes base de una canción.

Uso:
  python youtube/glitch.py youtube/<slug>/scenes.json youtube/<slug>/imgs youtube/<slug>/final

Cada escena de scenes.json lleva "glitch": 0..5. 5 = copias muy desplazadas, franjas
corridas y color separado; 0 = solo grano, líneas de barrido y viñeta suaves. Es
determinista (semilla por id), así que la misma imagen siempre sale igual.
La zona inferior (22 %) no recibe franjas, para no ensuciar los controles del reproductor.
"""
import json
import os
import sys
import zlib

import numpy as np
from PIL import Image

scenes_path, src_dir, out_dir = sys.argv[1:4]
os.makedirs(out_dir, exist_ok=True)
scenes = json.load(open(scenes_path, encoding="utf-8"))["scenes"]


def shift(a, dx):
    return np.roll(a, int(dx), axis=1)


for sc in scenes:
    sid, lv = sc["id"], float(sc.get("glitch", 0))
    f = os.path.join(src_dir, sid + ".png")
    if not os.path.exists(f):
        continue
    rng = np.random.default_rng(zlib.crc32(sid.encode()))
    a = np.asarray(Image.open(f).convert("RGB")).astype(np.float32)
    h, w, _ = a.shape
    k = lv / 5.0

    # copia fantasma desplazada (la «otra versión» del mismo mundo)
    ghost = shift(a, w * 0.012 * lv)
    a = a * (1 - 0.24 * k) + ghost * (0.24 * k)

    # separación de color
    d = 1 + 2.2 * lv
    a[..., 0] = shift(a[..., 0], d)
    a[..., 2] = shift(a[..., 2], -d)

    # franjas corridas en la parte alta y media
    for _ in range(int(2 + 2 * lv)):
        y0 = int(rng.integers(0, int(h * 0.78) - 40))
        hh = int(rng.integers(4, 10 + int(30 * k)))
        a[y0:y0 + hh] = shift(a[y0:y0 + hh], rng.integers(-1, 2) * (4 + 10 * lv) * rng.random())

    # líneas de barrido, grano de cinta y viñeta
    a[::3] *= 0.96
    a += rng.normal(0, 5.5, a.shape[:2])[..., None]
    yy, xx = np.mgrid[0:h, 0:w]
    v = 1 - 0.22 * (((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2) / 2
    a *= v[..., None]

    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(os.path.join(out_dir, sid + ".png"))
    print(sid, "glitch", lv)

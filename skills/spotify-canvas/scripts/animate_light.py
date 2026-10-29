"""Anima una ilustración fija como Canvas en bucle perfecto, sin IA de video: ola de luz sobre elementos,
empuje de cámara, brasas y estrellas. Todo es periódico en el número de frames, así que el último frame enlaza
con el primero. Requiere numpy, Pillow, scipy y ffmpeg en el PATH.

  python animate_light.py config.json salida.mp4

config.json:
{
  "image": "base.png",                      # ilustración 9:16 (se escala a 1080x1920)
  "frames": 191, "fps": 24,                 # 191 frames a 24 fps = 7.958 s (no usar 8.000 s exactos)
  "groups": {"left": [[x0,x1,y0,y1], ...],  # rectángulos en píxeles de la imagen original, de CERCA a LEJOS
             "right": [...]},
  "origin": [x, y],                         # punto hacia el que empuja la cámara (px de la imagen original)
  "push": 0.045,                            # zoom máximo extra
  "sky_y": 480,                             # estrellas solo por encima de esta y (px originales)
  "seed": 7
}
"""
import json, subprocess, sys
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

W, H = 1080, 1920
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
out = sys.argv[2]
N, FPS = cfg.get("frames", 191), cfg.get("fps", 24)
rng = np.random.default_rng(cfg.get("seed", 7))

src = Image.open(cfg["image"]).convert("RGB")
sx, sy = W / src.width, H / src.height
base = np.asarray(src.resize((W, H), Image.LANCZOS), dtype=np.float32) / 255.0
base += rng.normal(0, 0.006, base.shape[:2])[..., None].astype(np.float32)  # grano fijo: evita bandas en degradados
base = np.clip(base, 0, 1)

mx, mn = base.max(2), base.min(2)
sat = (mx - mn) / np.maximum(mx, 1e-3)
gray = np.clip(1 - (sat - 0.18) / 0.15, 0, 1)  # pilares grises = 1, cielo saturado = 0

AMBER = np.array([1.0, 0.66, 0.28], np.float32)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)

# --- elementos (pilares): máscara, punto caliente y charco de luz, con fase según profundidad ---
elems = []
for gi, (name, rects) in enumerate(cfg["groups"].items()):
    n = len(rects)
    for i, (x0, x1, y0, y1) in enumerate(rects):
        x0, x1, y0, y1 = x0 * sx, x1 * sx, y0 * sy, y1 * sy
        rect = ((xx >= x0) & (xx <= x1) & (yy >= y0) & (yy <= y1)).astype(np.float32)
        rect = gaussian_filter(rect, 1.5) * gray
        cx, cy = (x0 + x1) / 2, y0 + 0.62 * (y1 - y0)  # donde "está grabado" el nombre
        hot = np.exp(-(((xx - cx) / ((x1 - x0) * 0.9)) ** 2 + ((yy - cy) / ((y1 - y0) * 0.22)) ** 2))
        shade = rect * (0.55 + 0.45 * hot)
        pool = np.exp(-(((xx - cx) / ((x1 - x0) * 1.6)) ** 2 + ((yy - (y1 + 6)) / 22.0) ** 2))
        elems.append(dict(shade=shade.astype(np.float32), pool=pool.astype(np.float32),
                          phase=(n - 1 - i) * 0.09 + gi * 0.02))  # lejos primero: la luz viene hacia el espectador

WIDTH = 0.42  # fracción del ciclo que dura cada elemento encendido


def lit(phase, u):
    k = (u - phase) % 1.0
    return float(np.sin(np.pi * k / WIDTH) ** 2) if k < WIDTH else 0.0


# --- partículas y estrellas (periódicas) ---
NP = 55
ep = dict(x=rng.uniform(0.1, 0.9, NP) * W, y=rng.uniform(0.55, 0.95, NP) * H, p=rng.uniform(0, 1, NP),
          a=rng.uniform(10, 40, NP), m=rng.integers(1, 4, NP), r=rng.uniform(1.6, 3.2, NP))
sky_y = cfg.get("sky_y", 480) * sy
NS = 90
st = dict(x=rng.uniform(0.04, 0.96, NS) * W, y=rng.uniform(0.02, 1, NS) * sky_y, f=rng.uniform(0, np.pi, NS),
          m=rng.integers(1, 4, NS), r=rng.uniform(0.9, 1.8, NS))
ok = sat[st["y"].astype(int), st["x"].astype(int)] > 0.35  # solo sobre cielo, no sobre losas grises
st = {k: v[ok] for k, v in st.items()}

ox, oy = cfg.get("origin", [src.width / 2, src.height * 0.78])
ox, oy = ox * sx, oy * sy
push = cfg.get("push", 0.045)


def stamp(img, x, y, r, a, color):
    r = max(r, 0.8); k = int(r * 3) + 1
    x0, y0 = int(round(x)), int(round(y))
    if x0 - k < 0 or y0 - k < 0 or x0 + k >= W or y0 + k >= H:
        return
    gy, gx = np.mgrid[-k:k + 1, -k:k + 1]
    g = np.exp(-((gx + x0 - x) ** 2 + (gy + y0 - y) ** 2) / (2 * (r * 0.7) ** 2)).astype(np.float32) * a
    patch = img[y0 - k:y0 + k + 1, x0 - k:x0 + k + 1]
    patch[:] = 1 - (1 - patch) * (1 - g[..., None] * color)


enc = subprocess.Popen(
    ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
     "-i", "-", "-an", "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-maxrate", "6M", "-bufsize", "12M",
     "-pix_fmt", "yuv420p", "-movflags", "+faststart", out], stdin=subprocess.PIPE)

for f in range(N):
    u = f / N
    # luz sobre los pilares
    inten = np.zeros((H, W), np.float32)
    pools = np.zeros((H, W), np.float32)
    for e in elems:
        g = 0.10 + 0.90 * lit(e["phase"], u)  # 0.10: el grabado se insinúa siempre
        inten += e["shade"] * g
        pools += e["pool"] * g
    bloom = np.kron(gaussian_filter(inten[::4, ::4], 7), np.ones((4, 4), np.float32))[:H, :W]
    light = np.clip(inten * 0.85 + bloom * 0.9 + pools * 0.35, 0, 1.2)[..., None] * AMBER
    img = 1 - (1 - base) * (1 - np.clip(light, 0, 1))
    # respiración cálida del horizonte
    hz = np.exp(-(((xx - W / 2) / 420) ** 2 + ((yy - 1380 * (H / 1920)) / 130) ** 2)) * (0.05 + 0.05 * np.sin(2 * np.pi * u))
    img = 1 - (1 - img) * (1 - hz[..., None] * np.array([1.0, 0.5, 0.2], np.float32))
    # empuje de cámara periódico
    s = 1 + push * (0.5 - 0.5 * np.cos(2 * np.pi * u))
    bx, by = ox - ox / s, oy - oy / s
    im = Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8)).resize(
        (W, H), Image.BICUBIC, box=(bx, by, bx + W / s, by + H / s))
    img = np.asarray(im, dtype=np.float32) / 255.0
    # estrellas
    for x, y, ph, m, r in zip(st["x"], st["y"], st["f"], st["m"], st["r"]):
        stamp(img, x, y, r, 0.25 + 0.75 * np.sin(np.pi * m * u + ph) ** 2, np.array([0.9, 0.92, 1.0], np.float32))
    # brasas ascendentes (alfa 0 en el salto => sin corte)
    for x, y, p, a, m, r in zip(ep["x"], ep["y"], ep["p"], ep["a"], ep["m"], ep["r"]):
        k = (u + p) % 1.0
        stamp(img, x + a * np.sin(2 * np.pi * m * k), y - 520 * k, r, 0.95 * np.sin(np.pi * k) ** 2, AMBER)
    enc.stdin.write((np.clip(img, 0, 1) * 255).astype(np.uint8).tobytes())
    if f % 20 == 0:
        print(f"{f}/{N}", flush=True)

enc.stdin.close()
enc.wait()
print("listo", out)

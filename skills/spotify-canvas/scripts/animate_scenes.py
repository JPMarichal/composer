"""Compone un Canvas multiescena en bucle perfecto a partir de ilustraciones fijas: movimiento de cámara lento por
plano, disolvencias suaves, brillo onírico (bloom + enfoque suave), bokeh y brasas continuos que unen los planos.
El último plano disuelve al primero, y todo lo continuo es periódico en N frames, así que el bucle enlaza.

  python animate_scenes.py render.json salida.mp4

render.json:
{
  "dir": "work2",                       # carpeta con <id>.png (relativa a este json)
  "frames": 191, "fps": 24,             # 191 frames a 24 fps = 7.958 s
  "dissolve": 16,                       # frames de cada disolvencia (centrada en el límite entre planos)
  "seed": 7,
  "particle_color": [1.0, 0.68, 0.30], "leak_color": [1.0, 0.55, 0.30],   # opcionales: color de bokeh/brasas y del velo
  "transitions": "auto",                # opcional: elige transiciones variadas automáticamente (ver CYCLE); si no, "dissolve"
  "transition_default": "dissolve",      # opcional: la que se usa si un plano no declara la suya
  "scenes": [                           # en orden de aparición; duran N/len(scenes) cada una
    {"id": "s1_calle",
     "transition": "zoom",              # cómo pasa AL SIGUIENTE plano: dissolve | zoom | blur | light | wipe_right | wipe_left | wipe_up | push_up | push_left
     "zoom": [1.0, 1.08],               # zoom inicial y final durante el plano
     "pan": [[0.5, 0.42], [0.5, 0.38]], # centro de cámara (fracción de la imagen) al inicio y al final
     "glow": {"x": 0.45, "y": 0.4, "r": 0.18, "amp": 0.6, "k": 2, "color": [1.0, 0.68, 0.3]}}   # opcional: halo que late (k latidos)
  ]
}
Requiere numpy, Pillow, scipy y ffmpeg en el PATH.
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

W, H = 1080, 1920
cfgp = sys.argv[1]
cfg = json.load(open(cfgp, encoding="utf-8"))
out = sys.argv[2]
N, FPS, D = cfg.get("frames", 191), cfg.get("fps", 24), cfg.get("dissolve", 16)
rng = np.random.default_rng(cfg.get("seed", 7))
scenes = cfg["scenes"]; n = len(scenes); L = N / n
folder = os.path.join(os.path.dirname(os.path.abspath(cfgp)), cfg.get("dir", "."))
AMBER = np.array([1.0, 0.68, 0.30], np.float32)  # color por defecto del halo
PCOL = np.array(cfg.get("particle_color", [1.0, 0.68, 0.30]), np.float32)  # bokeh y brasas
LEAK = np.array(cfg.get("leak_color", [1.0, 0.55, 0.30]), np.float32)  # velo que barre
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)

for s in scenes:
    im = Image.open(os.path.join(folder, s["id"] + ".png")).convert("RGB").resize((W, H), Image.LANCZOS)
    a = np.asarray(im, np.float32) / 255.0
    s["img"] = Image.fromarray((np.clip(a + rng.normal(0, 0.006, (H, W))[..., None], 0, 1) * 255).astype(np.uint8))
    g = s.get("glow")
    s["gmask"] = None if not g else np.exp(-(((xx - g["x"] * W) ** 2 + (yy - g["y"] * H) ** 2) / (2 * (g["r"] * W) ** 2))).astype(np.float32)


def smooth(x):
    x = min(max(x, 0.0), 1.0)
    return x * x * (3 - 2 * x)


def scene_frame(i, pos):
    """Fotograma del plano i en la posición pos (frames), con cámara y halo."""
    s = scenes[i]
    tt = min(max(((pos - i * L + D / 2) % N) / (L + D), 0), 1)
    e = 0.5 - 0.5 * np.cos(np.pi * tt)  # arranque y frenado suaves
    z0, z1 = s.get("zoom", [1.0, 1.06])
    (px0, py0), (px1, py1) = s.get("pan", [[0.5, 0.5], [0.5, 0.5]])
    z = z0 + (z1 - z0) * e
    cx, cy = (px0 + (px1 - px0) * e) * W, (py0 + (py1 - py0) * e) * H
    bw, bh = W / z, H / z
    x0 = min(max(cx - bw / 2, 0), W - bw); y0 = min(max(cy - bh / 2, 0), H - bh)
    fr = np.asarray(s["img"].resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + bw, y0 + bh)), np.float32) / 255.0
    g = s.get("glow")
    if g:
        # el halo se mueve con la cámara: recalcular su centro en pantalla
        gx = ((g["x"] * W) - x0) * z; gy = ((g["y"] * H) - y0) * z
        m = np.exp(-(((xx - gx) ** 2 + (yy - gy) ** 2) / (2 * (g["r"] * W * z) ** 2)))
        amp = g.get("amp", 0.5) * (0.6 + 0.4 * np.sin(2 * np.pi * g.get("k", 2) * pos / N))
        fr = 1 - (1 - fr) * (1 - np.clip(m[..., None] * amp, 0, 1) * np.array(g.get("color", AMBER), np.float32))
    return fr


# --- transiciones entre planos: la del plano i es la que lo une con el siguiente (el último, con el primero) ---
CYCLE = ["zoom", "wipe_right", "blur", "push_up", "light", "wipe_up", "push_left", "dissolve"]
AUTO = cfg.get("transitions") == "auto"
_off = cfg.get("seed", 7) % len(CYCLE)  # canciones de un álbum con seeds distintas arrancan en transiciones distintas


def kind(i):
    t = scenes[i].get("transition")
    if t is None:
        t = CYCLE[(_off + i) % len(CYCLE)] if AUTO else cfg.get("transition_default", "dissolve")
    return t


def zoom_img(a, z):
    bw, bh = W / z, H / z
    im = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    return np.asarray(im.resize((W, H), Image.BICUBIC, box=((W - bw) / 2, (H - bh) / 2, (W + bw) / 2, (H + bh) / 2)), np.float32) / 255.0


def blur_img(a, sigma):
    if sigma < 0.3:
        return a
    sm = a[::4, ::4]
    return np.kron(np.stack([gaussian_filter(sm[..., k], sigma / 4) for k in range(3)], -1), np.ones((4, 4, 1), np.float32))[:H, :W]


def transition(i, t, A, B):
    """A = plano que sale, B = plano que entra, t = avance suavizado 0..1."""
    k = kind(i)
    if k == "zoom":  # zoom cruzado: A se acerca mientras se funde, B llega desde cerca
        return (1 - t) * zoom_img(A, 1 + 0.30 * t) + t * zoom_img(B, 1 + 0.30 * (1 - t))
    if k == "blur":  # el plano sale de foco y el siguiente se enfoca
        m = 18.0
        return (1 - t) * blur_img(A, m * t) + t * blur_img(B, m * (1 - t))
    if k == "light":  # swell suave de luz cálida (nunca destello brusco)
        w = 0.5 * np.sin(np.pi * t) ** 2
        return ((1 - t) * A + t * B) * (1 - w) + np.array([1.0, 0.93, 0.80], np.float32) * w
    if k.startswith("wipe"):  # cortina de borde suave
        edge = 320.0
        if k == "wipe_up":
            pos = H - t * (H + edge) + edge  # el borde sube
            m = np.clip((yy[:, :1] - (pos - edge)) / edge, 0, 1)[..., None]
        else:
            pos = t * (W + edge)
            xs = xx[:1, :] if k != "wipe_left" else (W - xx[:1, :])
            m = np.clip((pos - xs) / edge, 0, 1)[..., None]
        return (1 - m) * A + m * B
    if k.startswith("push"):  # B empuja a A
        out = np.empty_like(A)
        if k == "push_up":
            o = int(round(t * H)); out[:H - o] = A[o:]; out[H - o:] = B[:o]
        else:
            o = int(round(t * W)); out[:, :W - o] = A[:, o:]; out[:, W - o:] = B[:, :o]
        return out
    return (1 - t) * A + t * B  # dissolve


# capas continuas (periódicas)
NB = 14
bk = dict(x=rng.uniform(0.05, 0.95, NB) * W, y=rng.uniform(0.1, 0.9, NB) * H, p=rng.uniform(0, 1, NB),
          a=rng.uniform(30, 90, NB), m=rng.integers(1, 3, NB), r=rng.uniform(18, 46, NB))
NP = 50
ep = dict(x=rng.uniform(0.1, 0.9, NP) * W, y=rng.uniform(0.45, 0.95, NP) * H, p=rng.uniform(0, 1, NP),
          a=rng.uniform(10, 40, NP), m=rng.integers(1, 4, NP), r=rng.uniform(1.6, 3.4, NP))
vig = (1 - 0.38 * (((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H * 0.45) / (H * 0.75)) ** 2))[..., None].astype(np.float32)


def stamp(img, x, y, r, a, color):
    r = max(r, 0.8); k = int(r * 2.5) + 1
    x0, y0 = int(round(x)), int(round(y))
    if x0 - k < 0 or y0 - k < 0 or x0 + k >= W or y0 + k >= H:
        return
    gy, gx = np.mgrid[-k:k + 1, -k:k + 1]
    g = np.exp(-((gx + x0 - x) ** 2 + (gy + y0 - y) ** 2) / (2 * (r * 0.7) ** 2)).astype(np.float32) * a
    p = img[y0 - k:y0 + k + 1, x0 - k:x0 + k + 1]
    p[:] = 1 - (1 - p) * (1 - g[..., None] * color)


enc = subprocess.Popen(
    ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
     "-an", "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-maxrate", "6M", "-bufsize", "12M",
     "-pix_fmt", "yuv420p", "-movflags", "+faststart", out], stdin=subprocess.PIPE)

for f in range(N):
    u = f / N
    c = int(f // L); dp = f - c * L; dn = (c + 1) * L - f
    if dp < D / 2:
        a = smooth((dp + D / 2) / D); img = transition((c - 1) % n, a, scene_frame((c - 1) % n, f), scene_frame(c, f))
    elif dn <= D / 2:
        b = smooth((dn + D / 2) / D); img = transition(c, 1 - b, scene_frame(c, f), scene_frame((c + 1) % n, f))
    else:
        img = scene_frame(c, f)
    # brillo onírico: bloom de las luces + enfoque suave
    small = img[::4, ::4]
    hl = np.clip(small - 0.55, 0, 1)
    bloom = np.kron(np.stack([gaussian_filter(hl[..., k], 6) for k in range(3)], -1), np.ones((4, 4, 1), np.float32))[:H, :W]
    soft = np.kron(np.stack([gaussian_filter(small[..., k], 5) for k in range(3)], -1), np.ones((4, 4, 1), np.float32))[:H, :W]
    img = 0.88 * img + 0.12 * soft
    img = 1 - (1 - img) * (1 - np.clip(bloom * 0.7, 0, 1))
    # velo cálido que barre suavemente (periódico)
    leak = np.exp(-(((xx - W * (0.5 + 0.45 * np.sin(2 * np.pi * u))) / 260.0) ** 2)) * 0.09
    img = 1 - (1 - img) * (1 - leak[..., None] * LEAK)
    img = img * vig
    # bokeh y brasas continuos (alfa 0 en el reinicio => sin corte)
    for x, y, p, a_, m, r in zip(bk["x"], bk["y"], bk["p"], bk["a"], bk["m"], bk["r"]):
        k = (u + p) % 1.0
        stamp(img, x + a_ * np.sin(2 * np.pi * m * k), y - 160 * k, r, 0.16 * np.sin(np.pi * k) ** 2, PCOL)
    for x, y, p, a_, m, r in zip(ep["x"], ep["y"], ep["p"], ep["a"], ep["m"], ep["r"]):
        k = (u + p) % 1.0
        stamp(img, x + a_ * np.sin(2 * np.pi * m * k), y - 520 * k, r, 0.95 * np.sin(np.pi * k) ** 2, PCOL)
    enc.stdin.write((np.clip(img, 0, 1) * 255).astype(np.uint8).tobytes())
    if f % 20 == 0:
        print(f"{f}/{N}", flush=True)

enc.stdin.close(); enc.wait()
print("listo", out)

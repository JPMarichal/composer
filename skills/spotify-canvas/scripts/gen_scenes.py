"""Genera las ilustraciones de todas las escenas de scenes.json con gen.py, midiendo el tiempo de cada una.

  python gen_scenes.py scenes.json carpeta_salida [metrics.csv]

Cada imagen se copia a carpeta_salida/<id>.png. Si se pasa metrics.csv se añade una línea epoch,etapa por escena.
Solo las escenas cuyo PNG no existe se generan (permite reintentar una sola borrando su archivo).
"""
import json, os, shutil, subprocess, sys, time, glob

cfg = json.load(open(sys.argv[1], encoding="utf-8"))
out = sys.argv[2]; os.makedirs(out, exist_ok=True)
metrics = sys.argv[3] if len(sys.argv) > 3 else None
here = os.path.dirname(os.path.abspath(__file__))
comfy_out = os.environ.get("COMFY_OUTPUT", r"D:\ComfyUI\output")

for s in cfg["scenes"]:
    dst = os.path.join(out, s["id"] + ".png")
    if os.path.exists(dst):
        print("ya existe", dst); continue
    t0 = time.time()
    r = subprocess.run([sys.executable, os.path.join(here, "gen.py"), "image", "--prompt", cfg.get("style", "") + s["prompt"],
                        "--seed", str(s["seed"]), "--width", str(cfg["width"]), "--height", str(cfg["height"]),
                        "--prefix", "c2_" + s["id"]], capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    newest = max(glob.glob(os.path.join(comfy_out, "c2_" + s["id"] + "_*.png")), key=os.path.getmtime)
    shutil.copy(newest, dst)
    dt = time.time() - t0
    print(f"{s['id']}: {dt:.0f} s", flush=True)
    if metrics:
        open(metrics, "a").write(f"{int(time.time())},02_imagen_{s['id']}_{dt:.0f}s\n")

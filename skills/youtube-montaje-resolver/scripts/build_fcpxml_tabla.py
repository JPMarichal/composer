"""Genera un FCPXML 1.9 para DaVinci Resolver a partir de una tabla de escenas (tabla.json), el audio y letra.srt.

Uso (desde la carpeta de la canción):
  python build_fcpxml_tabla.py --tabla tabla.json --imgs imgs --audio "P:\\...\\cancion.wav" \
      --srt ../letra.srt --copiar-a "P:\\...\\montaje_imgs" --out montaje.fcpxml --titulo "Nombre de la canción"

tabla.json: lista de {"id": "03_acusacion", "t": 11.2, ...} con t = segundo de entrada de cada imagen.
Las imágenes deben llamarse <id>.png en --imgs. Se copian a --copiar-a con nombres SIN dígitos
(foto_acusacion.png) porque Resolver toma los nombres numerados por secuencias de imágenes.
Cada plano lleva zoom o paneo suave con keyframes (escala máxima 1,05, sin repetir movimiento seguido).
Los títulos de la letra salen de --srt; el primero es el nombre de la canción (1,0 a 4,5 s).
No incluye transiciones (cortes directos).
"""
import argparse, json, pathlib, re, shutil, urllib.parse, wave
from xml.sax.saxutils import escape

ap = argparse.ArgumentParser()
ap.add_argument("--tabla", required=True)
ap.add_argument("--imgs", required=True)
ap.add_argument("--audio", required=True)
ap.add_argument("--srt", required=True)
ap.add_argument("--copiar-a", required=True)
ap.add_argument("--out", default="montaje.fcpxml")
ap.add_argument("--titulo", required=True)
ap.add_argument("--fps", type=int, default=24)
ap.add_argument("--trans", help="transiciones.json: activa transiciones, easing, fundidos de títulos y marcadores")
a = ap.parse_args()

FPS = a.fps
W, H = 1920, 1080
def fr(sec): return round(sec * FPS)
def rt(frames): return f"{frames*100}/{FPS*100}s"
def uri(p): return "file:///" + urllib.parse.quote(str(p).replace("\\", "/"), safe="/:")

tabla = json.load(open(a.tabla, encoding="utf-8"))
audio = pathlib.Path(a.audio)
with wave.open(str(audio)) as w: adur = w.getnframes() / w.getframerate()
total = fr(adur)

dest = pathlib.Path(a.copiar_a); dest.mkdir(parents=True, exist_ok=True)
names = []
for s in tabla:
    nm = "foto_" + re.sub(r"\d+", "", s["id"].split("_", 1)[1]).strip("_") + ".png"
    assert nm not in names, f"nombre repetido {nm}"
    names.append(nm)
    shutil.copy2(pathlib.Path(a.imgs) / f"{s['id']}.png", dest / nm)

MOV = [(1.0, 1.035, 0, 0, 0, 0), (1.05, 1.05, 2.2, -2.2, 0, 0), (1.05, 1.0, 0, 0, 0, 0),
       (1.05, 1.05, -2.2, 2.2, 0, 0), (1.0, 1.05, 0, 0, 0, 0), (1.05, 1.05, 0, 0, 1.2, -1.2)]

def tc(t):
    h, m, r = t.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(r)
subs = []
for blk in open(a.srt, encoding="utf-8-sig").read().strip().split("\n\n"):
    ls = blk.splitlines()
    x, y = ls[1].split(" --> "); subs.append((fr(tc(x)), fr(tc(y)), " ".join(ls[2:])))
subs.insert(0, (fr(1.0), fr(4.5), a.titulo))

CFG = json.load(open(a.trans, encoding="utf-8")) if a.trans else None
EASE = ' interp="ease"' if CFG else ""

def fade_blend(dur, fin=6, fout=6):
    """Opacidad 0 -> 1 al entrar y 1 -> 0 al salir (en cuadros)."""
    fin = min(fin, dur // 3); fout = min(fout, dur // 3)
    ks = [(0, 0), (fin, 1), (dur - fout, 1), (dur, 0)]
    kk = "".join(f'<keyframe time="{rt(t)}" value="{v}"/>' for t, v in ks)
    return f'<adjust-blend><param name="amount"><keyframeAnimation>{kk}</keyframeAnimation></param></adjust-blend>'

nt = [0]
def title_xml(f0, f1, text, base, ind):
    nt[0] += 1; n = nt[0]
    big = n == 1
    parts = [
        f'{ind}<title ref="fx" lane="1" name="{escape(text)}" offset="{rt(f0-base)}" start="0s" duration="{rt(f1-f0)}">',
        f'{ind}  <text><text-style ref="ts{n}">{escape(text)}</text-style></text>',
        f'{ind}  <text-style-def id="ts{n}"><text-style font="Helvetica" fontSize="{90 if big else 60}" fontFace="Bold" fontColor="1 1 1 1" shadowColor="0 0 0 0.8" shadowOffset="4 315" alignment="center"/></text-style-def>',
        f'{ind}  <adjust-transform position="0 {-5 if big else -38}"/>',
    ]
    if CFG: parts.append(f'{ind}  ' + fade_blend(f1 - f0))
    parts.append(f'{ind}</title>')
    return chr(10).join(parts)

edges = [fr(s["t"]) for s in tabla] + [total]
edges[0] = 0
assets, clips = [], []
for i, s in enumerate(tabla):
    f0, f1 = edges[i], edges[i + 1]; dur = f1 - f0
    aid = f"a{i+1}"
    assets.append(f'    <asset id="{aid}" name="{s["id"]}" start="0s" duration="0s" hasVideo="1" format="r2"><media-rep kind="original-media" src="{uri(dest / names[i])}"/></asset>')
    s0, s1, x0, x1, y0, y1 = MOV[i % len(MOV)]
    t1 = rt(dur)
    aud = (f'          <asset-clip ref="aud" lane="-1" name="{escape(a.titulo)}" offset="0s" start="0s" duration="{rt(total)}" audioRole="dialogue"/>\n' if i == 0 else "")
    tit = "\n".join(title_xml(max(p, f0), q, t, f0, "          ") for p, q, t in subs if f0 <= p < f1)
    blend = ""
    if CFG and i == len(tabla) - 1:  # fundido a negro al final (opacidad 1 -> 0 en los últimos 2 s)
        d = min(dur, 2 * FPS)
        blend = f'\n          <adjust-blend><param name="amount"><keyframeAnimation><keyframe time="0s" value="1"/><keyframe time="{rt(dur - d)}" value="1"/><keyframe time="{t1}" value="0"/></keyframeAnimation></param></adjust-blend>'
    mark = ""
    if CFG and i > 0:
        c = CFG.get("cortes", {}).get(str(i), CFG.get("default", {}))
        if c.get("tipo", "Cross Dissolve") != "Cross Dissolve" or c.get("nota"):
            txt = f'Transición: {c["tipo"]} {c["dur"]} s' + (f' - {c["nota"]}' if c.get("nota") else "")
            mark = f'\n          <marker start="0s" duration="{rt(1)}" value="{escape(txt)}"/>'
    clips.append(f'''        <asset-clip ref="{aid}" name="{s["id"]}" offset="{rt(f0)}" start="0s" duration="{t1}" format="r2" tcFormat="NDF">
          <adjust-transform>
            <param name="scale"><keyframeAnimation><keyframe time="0s" value="{s0} {s0}"{EASE}/><keyframe time="{t1}" value="{s1} {s1}"{EASE}/></keyframeAnimation></param>
            <param name="position"><keyframeAnimation><keyframe time="0s" value="{x0} {y0}"{EASE}/><keyframe time="{t1}" value="{x1} {y1}"{EASE}/></keyframeAnimation></param>
          </adjust-transform>{blend}
{aud}{tit}{mark}
        </asset-clip>''')
    if CFG and i < len(tabla) - 1:
        c = CFG.get("cortes", {}).get(str(i + 1), CFG.get("default", {"dur": 0.5}))
        nxt = edges[i + 2] - edges[i + 1]
        d = max(2, min(fr(c["dur"]), dur, nxt) // 2 * 2)
        clips.append(f'        <transition name="Cross Dissolve" offset="{rt(f1 - d // 2)}" duration="{rt(d)}"><filter-video ref="fxdis" name="Cross Dissolve"/></transition>')

nl = chr(10)
xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.9">
  <resources>
    <format id="r1" name="FFVideoFormat1080p{FPS}" frameDuration="{rt(1)}" width="{W}" height="{H}" colorSpace="1-1-1 (Rec. 709)"/>
    <format id="r2" name="FFVideoFormatRateUndefined" width="{W}" height="{H}" colorSpace="1-1-1 (Rec. 709)"/>
{nl.join(assets)}
{('    <effect id="fxdis" name="Cross Dissolve" uid="FxPlug:4731E73A-8DAC-4113-9A30-AE85B1761265"/>' + nl) if CFG else ''}    <effect id="fx" name="Basic Title" uid=".../Titles.localized/Bumper:Opener.localized/Basic Title.localized/Basic Title.moti"/>
    <asset id="aud" name="{escape(a.titulo)}" start="0s" duration="{rt(total)}" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000"><media-rep kind="original-media" src="{uri(audio)}"/></asset>
  </resources>
  <library>
    <event name="{escape(a.titulo)}">
      <project name="{escape(a.titulo)} - video">
        <sequence format="r1" duration="{rt(total)}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
          <spine>
{nl.join(clips)}
          </spine>
        </sequence>
      </project>
    </event>
  </library>
</fcpxml>
'''
open(a.out, "w", encoding="utf-8").write(xml)
print("ok", len(tabla), "planos,", total, "cuadros,", round(adur, 2), "s,", nt[0], "titulos")

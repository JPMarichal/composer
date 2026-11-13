"""Genera montaje.fcpxml (FCPXML 1.9) para DaVinci Resolver desde PLAN.md: cortes, audio y movimientos (keyframes)."""
import re, wave, urllib.parse, pathlib, shutil

FPS = 24
AUDIO = pathlib.Path(r"P:\Canciones\audio\wav\love\Mentira que te mentí.wav")
IMGS = pathlib.Path(r"P:\Canciones\audio\wav\love\assets\fotogramas\mentira-que-te-menti\montaje_imgs")
W, H = 1920, 1080

def secs(t):
    m, s = t.split(":"); return int(m) * 60 + float(s)
def fr(sec): return round(sec * FPS)
def rt(frames): return f"{frames*100}/{FPS*100}s"
def uri(p): return "file:///" + urllib.parse.quote(str(p).replace("\\", "/"), safe="/:")

rows = []
for l in open("PLAN.md", encoding="utf-8"):
    m = re.match(r"\| (\d+) \| `([^`]+)` \| ([\d:.]+) \| ([\d:.]+) \|.*\| ([^|]+) \| ([^|]+) \|\s*$", l)
    if m: rows.append((m[2], secs(m[3]), secs(m[4]), m[5].strip()))
assert len(rows) == 30, len(rows)

with wave.open(str(AUDIO)) as w: adur = w.getnframes() / w.getframerate()
total = fr(adur)

# movimiento -> (escala ini, escala fin, x ini, x fin, y ini, y fin); x,y en % de altura de cuadro (+x derecha, +y arriba)
def motion(mv):
    if mv == "zoom-in lento": return (1.0, 1.035, 0, 0, 0, 0)
    if mv == "zoom-in": return (1.0, 1.05, 0, 0, 0, 0)
    if mv == "zoom-out": return (1.05, 1.0, 0, 0, 0, 0)
    if mv.startswith("pan izq"): return (1.05, 1.05, 2.2, -2.2, 0, 0)   # cámara a la derecha
    if mv.startswith("pan der"): return (1.05, 1.05, -2.2, 2.2, 0, 0)
    if "arriba" in mv: return (1.05, 1.05, 0, 0, 1.2, -1.2)
    raise ValueError(mv)

from xml.sax.saxutils import escape
def tc(t):
    h, m, r = t.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(r)
subs = []
for blk in open("letra.srt", encoding="utf-8-sig").read().strip().split("\n\n"):
    ls = blk.splitlines()
    a, b = ls[1].split(" --> "); subs.append((fr(tc(a)), fr(tc(b)), " ".join(ls[2:])))
subs.insert(0, (fr(1.0), fr(4.5), "Mentira que te mentí"))
nt = [0]
def title_xml(f0, f1, text, base, ind):
    nt[0] += 1; n = nt[0]
    big = n == 1
    size = 90 if big else 60
    y = -5 if big else -38
    parts = [
        f'{ind}<title ref="fx" lane="1" name="{escape(text)}" offset="{rt(f0-base)}" start="0s" duration="{rt(f1-f0)}">',
        f'{ind}  <text><text-style ref="ts{n}">{escape(text)}</text-style></text>',
        f'{ind}  <text-style-def id="ts{n}"><text-style font="Helvetica" fontSize="{size}" fontFace="Bold" fontColor="1 1 1 1" shadowColor="0 0 0 0.8" shadowOffset="4 315" alignment="center"/></text-style-def>',
        f'{ind}  <adjust-transform position="0 {y}"/>',
        f'{ind}</title>',
    ]
    return chr(10).join(parts)
assets, clips, bounds = [], [], []
# cortes en cuadros, contiguos
edges = [fr(r[1]) for r in rows] + [total]
edges[0] = 0
for i, (sid, a, b, mv) in enumerate(rows):
    f0, f1 = edges[i], edges[i + 1]; dur = f1 - f0
    aid = f"a{i+1}"
    p = IMGS / f"foto_{sid.split(chr(95),1)[1]}.png"; assert p.exists(), p
    assets.append(f'    <asset id="{aid}" name="{sid}" start="0s" duration="0s" hasVideo="1" format="r2"><media-rep kind="original-media" src="{uri(p)}"/></asset>')
    s0, s1, x0, x1, y0, y1 = motion(mv)
    t1 = rt(dur)
    clips.append(f'''        <asset-clip ref="{aid}" name="{sid}" offset="{rt(f0)}" start="0s" duration="{t1}" format="r2" tcFormat="NDF">
          <adjust-transform>
            <param name="scale"><keyframeAnimation><keyframe time="0s" value="{s0} {s0}"/><keyframe time="{t1}" value="{s1} {s1}"/></keyframeAnimation></param>
            <param name="position"><keyframeAnimation><keyframe time="0s" value="{x0} {y0}"/><keyframe time="{t1}" value="{x1} {y1}"/></keyframeAnimation></param>
          </adjust-transform>
''' + (f'''          <asset-clip ref="aud" lane="-1" name="Mentira que te mentí" offset="0s" start="0s" duration="{rt(total)}" audioRole="dialogue"/>
''' if i == 0 else "") + "\n".join(title_xml(max(a, f0), b, t, f0, "          ") for a, b, t in subs if f0 <= a < f1) + "\n        </asset-clip>")

xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.9">
  <resources>
    <format id="r1" name="FFVideoFormat1080p{FPS}" frameDuration="{rt(1)}" width="{W}" height="{H}" colorSpace="1-1-1 (Rec. 709)"/>
    <format id="r2" name="FFVideoFormatRateUndefined" width="{W}" height="{H}" colorSpace="1-1-1 (Rec. 709)"/>
{chr(10).join(assets)}
    <effect id="fx" name="Basic Title" uid=".../Titles.localized/Bumper:Opener.localized/Basic Title.localized/Basic Title.moti"/>
    <asset id="aud" name="Mentira que te mentí" start="0s" duration="{rt(total)}" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000"><media-rep kind="original-media" src="{uri(AUDIO)}"/></asset>
  </resources>
  <library>
    <event name="Mentira que te mentí">
      <project name="Mentira que te mentí - video">
        <sequence format="r1" duration="{rt(total)}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
          <spine>
{chr(10).join(clips)}
          </spine>
        </sequence>
      </project>
    </event>
  </library>
</fcpxml>
'''
open("montaje.fcpxml", "w", encoding="utf-8").write(xml)
print("ok", total, "cuadros", round(adur, 2), "s")

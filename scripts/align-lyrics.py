"""Alinea la letra conocida contra el audio con stable-ts y escribe un .srt.

Uso (entorno aparte, el del sistema no tiene stable-ts):
  D:\\myapps\\audio-venv\\Scripts\\python.exe scripts/align-lyrics.py "<letra.md>" "<audio.wav>" "<salida.srt>" [modelo]

Un renglon de la letra = un subtitulo (original_split). Los renglones vacios
separan estrofas y se ignoran. Escribe tambien <salida>.json con los tiempos.
"""
import json
import re
import sys

import stable_whisper

lyrics_path, audio_path, out_srt = sys.argv[1:4]
model_name = sys.argv[4] if len(sys.argv) > 4 else "medium"

text = open(lyrics_path, encoding="utf-8").read()
text = re.sub(r"\A---.*?---\s*", "", text, flags=re.S)
lines = [l.strip() for l in text.splitlines() if l.strip()]

model = stable_whisper.load_model(model_name, device="cpu")
result = model.align(audio_path, "\n".join(lines), language="es", original_split=True)
result.to_srt_vtt(out_srt, word_level=False)

segs = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in result.segments]
json.dump(segs, open(out_srt + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for s in segs:
    print(f"{s['start']:7.2f} {s['end']:7.2f}  {s['text']}")

# Camtasia lee como ANSI un .srt UTF-8 sin BOM y rompe los acentos: reescribir con BOM.
data = open(out_srt, encoding="utf-8-sig").read()
open(out_srt, "w", encoding="utf-8-sig", newline="").write(data)

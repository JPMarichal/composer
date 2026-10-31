"""Mapa de secciones y pulso de una canción para decidir cortes de imagen/video.

  D:\myapps\audio-venv\Scripts\python.exe scripts/audio-sections.py "ruta.wav" [n_secciones]

Imprime: duración, tempo, y una tabla de secciones (inicio, fin, energía relativa) por segmentación
aglomerativa sobre chroma+MFCC; más los instantes de compás aproximados. Requiere librosa (venv en D:\myapps\audio-venv).
"""
import sys
import numpy as np
import librosa

path = sys.argv[1]
k = int(sys.argv[2]) if len(sys.argv) > 2 else 10
y, sr = librosa.load(path, sr=22050, mono=True)
dur = len(y) / sr
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
tempo = float(np.atleast_1d(tempo)[0])
bt = librosa.frames_to_time(beats, sr=sr)
chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
feat = librosa.util.sync(np.vstack([librosa.util.normalize(chroma, axis=1), librosa.util.normalize(mfcc, axis=1)]), beats)
bounds = librosa.segment.agglomerative(feat, k)
btimes = np.concatenate([[0.0], bt[np.clip(bounds, 0, len(bt) - 1)], [dur]])
btimes = np.unique(np.round(btimes, 2))
rms = librosa.feature.rms(y=y)[0]
rt = librosa.frames_to_time(np.arange(len(rms)), sr=sr)
print(f"duracion {dur:.1f} s  tempo {tempo:.1f} BPM  compas ~{4*60/tempo:.2f} s  pulsos {len(bt)}")
print("seccion  inicio   fin   dur  energia")
for i in range(len(btimes) - 1):
    a, b = btimes[i], btimes[i + 1]
    e = rms[(rt >= a) & (rt < b)].mean() if b > a else 0
    print(f"{i+1:>7} {a:7.1f} {b:6.1f} {b-a:5.1f}  {e:.3f}")

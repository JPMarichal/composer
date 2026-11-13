import sys, glob, os
from PIL import Image
files = sys.argv[2:]
th = [Image.open(f).convert("RGB").resize((640, 360)) for f in files]
cols = 3; rows = (len(th) + cols - 1) // cols
s = Image.new("RGB", (cols * 640, rows * 360), "black")
for i, t in enumerate(th): s.paste(t, ((i % cols) * 640, (i // cols) * 360))
s.save(sys.argv[1], quality=85)

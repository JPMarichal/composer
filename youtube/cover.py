"""Portada estandar de YouTube: imagen + titulo + autor, con zonas seguras (ver ESTRATEGIA.md).

  python cover.py imagen.png "Titulo" carpeta_salida [--author JPMarichal]

Salidas: portada_1920x1080.png y miniatura_1280x720.png. Layout sobre 1080 de alto:
  libre: 12 % superior y 22 % inferior (controles del reproductor); margenes laterales >= 8 %.
  titulo centrado en 58 %, autor centrado en 68 %, degradado oscuro suave detras del bloque.
"""
import argparse, os, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = r"C:\Windows\Fonts\cambriab.ttf"   # serif del titulo
FONT_AUTHOR = r"C:\Windows\Fonts\bahnschrift.ttf"  # sans ligera del autor
CREAM = (250, 243, 228)

def fit_lines(draw, text, W, max_w, size0):
    size = size0
    while size > 40:
        f = ImageFont.truetype(FONT, size)
        if draw.textlength(text, font=f) <= max_w:
            return [text], f
        lines = textwrap.wrap(text, width=max(8, len(text) // 2 + 3))
        if len(lines) <= 2 and all(draw.textlength(l, font=f) <= max_w for l in lines):
            return lines, f
        size -= 4
    return [text], ImageFont.truetype(FONT, 40)

def spaced(draw, xy_center, text, font, fill, tracking):
    widths = [draw.textlength(c, font=font) for c in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = xy_center[0] - total / 2
    for c, w in zip(text, widths):
        draw.text((x, xy_center[1]), c, font=font, fill=fill, anchor="lm")
        x += w + tracking

def compose(img, title, author, W, H, title_size, with_author=True):
    img = img.convert("RGB").resize((W, H), Image.LANCZOS)
    # degradado oscuro que se desvanece antes de la zona inferior libre
    band = Image.new("L", (1, H), 0)
    top, mid, bot = int(H * .40), int(H * .62), int(H * .76)
    for y in range(top, bot):
        a = (y - top) / (mid - top) if y < mid else (bot - y) / (bot - mid)
        band.putpixel((0, y), int(150 * max(0, min(1, a))))
    shade = Image.new("RGB", (W, H), (20, 14, 8))
    img = Image.composite(shade, img, band.resize((W, H)))
    d = ImageDraw.Draw(img)
    lines, f = fit_lines(d, title, W, W * .84, title_size)
    lh = f.size * 1.12
    cy = H * .58 - (len(lines) - 1) * lh / 2
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    for i, l in enumerate(lines):
        gd.text((W / 2, cy + i * lh), l, font=f, fill=(0, 0, 0, 170), anchor="mm")
    img = Image.alpha_composite(img.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(H * .008))).convert("RGB")
    d = ImageDraw.Draw(img)
    for i, l in enumerate(lines):
        d.text((W / 2, cy + i * lh), l, font=f, fill=CREAM, anchor="mm")
    if with_author:
        fa = ImageFont.truetype(FONT_AUTHOR, int(H * .042))
        spaced(d, (W / 2, H * .70 + (len(lines) - 1) * lh / 2), author, fa, CREAM, fa.size * .35)
    return img

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("image"); p.add_argument("title"); p.add_argument("out")
    p.add_argument("--author", default="JPMarichal")
    a = p.parse_args()
    os.makedirs(a.out, exist_ok=True)
    src = Image.open(a.image)
    compose(src, a.title, a.author, 1920, 1080, 130).save(os.path.join(a.out, "portada_1920x1080.png"))
    compose(src, a.title, a.author, 1280, 720, 100, with_author=False).save(os.path.join(a.out, "miniatura_1280x720.png"))

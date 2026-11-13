"""Tarjeta final de YouTube: imagen + titulo + autoria + boton blanco «Suscribete al canal».

  python endcard.py imagen.png "Titulo" salida.png [--author "por Juan Pablo Marichal"] [--boton "Suscríbete al canal"]

Layout sobre 1080 de alto (zonas libres: 12 % superior y 22 % inferior): titulo en 38 %, autoria en 52 %,
boton en 66 %. Reutiliza compose() de cover.py para el titulo (misma tipografia y degradado oscuro).
"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import cover

DARK = (30, 24, 22)
RED = (204, 0, 0)

def rounded_shadow(img, box, radius, blur=14, alpha=120):
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([box[0], box[1] + 8, box[2], box[3] + 8], radius, fill=(0, 0, 0, alpha))
    return Image.alpha_composite(img.convert("RGBA"), sh.filter(ImageFilter.GaussianBlur(blur))).convert("RGB")

def card(src, title, author, button, W=1920, H=1080, ytitle=.36, ybtn=.70):
    base = src.convert("RGB").resize((W, H), Image.LANCZOS)
    # degradado oscuro suave en toda la franja central para que se lea el bloque completo
    band = Image.new("L", (1, H), 0)
    c = (ytitle + ybtn) / 2
    top, mid, bot = int(H * max(.02, c - .34)), int(H * c), int(H * min(.98, c + .34))
    for y in range(top, bot):
        a = (y - top) / (mid - top) if y < mid else (bot - y) / (bot - mid)
        band.putpixel((0, y), int(170 * max(0, min(1, a))))
    base = Image.composite(Image.new("RGB", (W, H), (14, 10, 10)), base, band.resize((W, H)))
    d = ImageDraw.Draw(base)
    lines, f = cover.fit_lines(d, title, W, W * .80, 120)
    lh = f.size * 1.12
    cy = H * ytitle - (len(lines) - 1) * lh / 2
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    for i, l in enumerate(lines):
        gd.text((W / 2, cy + i * lh), l, font=f, fill=(0, 0, 0, 180), anchor="mm")
    base = Image.alpha_composite(base.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(H * .008))).convert("RGB")
    d = ImageDraw.Draw(base)
    for i, l in enumerate(lines):
        d.text((W / 2, cy + i * lh), l, font=f, fill=cover.CREAM, anchor="mm")
    fa = ImageFont.truetype(cover.FONT_AUTHOR, int(H * .048))
    ya = cy + (len(lines) - 1) * lh / 2 + f.size * .85
    cover.spaced(d, (W / 2, ya), author, fa, cover.CREAM, fa.size * .30)
    # boton blanco con texto oscuro y un pequeno triangulo rojo (play)
    fb = ImageFont.truetype(cover.FONT_AUTHOR, int(H * .045))
    tw = d.textlength(button, font=fb)
    bh = int(H * .105); pad = int(H * .06)
    icon = int(bh * .46)
    bw = int(tw + pad * 2 + icon + pad * .6)
    x0 = int((W - bw) / 2); y0 = int(H * ybtn - bh / 2)
    box = (x0, y0, x0 + bw, y0 + bh)
    base = rounded_shadow(base, box, bh // 2)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle(box, bh // 2, fill=(255, 255, 255))
    ix = x0 + pad; iy = y0 + bh // 2
    d.rounded_rectangle([ix, iy - icon // 2 - 4, ix + icon + 8, iy + icon // 2 + 4], icon // 4, fill=RED)
    d.polygon([(ix + icon * .32, iy - icon * .26), (ix + icon * .32, iy + icon * .26), (ix + icon * .78, iy)], fill=(255, 255, 255))
    d.text((ix + icon + pad * .6 + 8, iy), button, font=fb, fill=DARK, anchor="lm")
    return base

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("image"); p.add_argument("title"); p.add_argument("out")
    p.add_argument("--author", default="por Juan Pablo Marichal")
    p.add_argument("--boton", default="Suscríbete al canal")
    p.add_argument("--ytitle", type=float, default=.36, help="altura del título (fracción del alto)")
    p.add_argument("--ybtn", type=float, default=.70, help="altura del botón (fracción del alto)")
    a = p.parse_args()
    card(Image.open(a.image), a.title, a.author, a.boton, ytitle=a.ytitle, ybtn=a.ybtn).save(a.out)
    print("ok", a.out)

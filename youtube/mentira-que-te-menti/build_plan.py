"""Genera PLAN.md de la versión onírica final de «Mentira que te mentí» reutilizando los cortes ya calculados."""
import glob
import json
import re

old = open("v2_nocturna/PLAN.md", encoding="utf-8").read()
rows = [l for l in old.splitlines() if re.match(r"\| \d+ \|", l)]
assert len(rows) == 30, len(rows)
scenes = sorted(s["id"] for s in json.load(open("scenes.json", encoding="utf-8"))["scenes"])
assert len(scenes) == 30

CONCEPTO = [
    "Marco dorado vacío en una pradera; un listón coral lo atraviesa (la acusación)",
    "Columpio colgado de una nube, con un sombrero en la hierba (humor)",
    "Espejo gigante que refleja otro cielo; él extiende la mano, ella de espaldas",
    "Casa de cristal en forma de corazón con un cerezo y un río dentro",
    "Un río en meandro con listones coral retorcidos: la trenza hecha de agua",
    "Escalera de trenza que sube de la mano hacia la luna",
    "Él arrodillado con el ramo; ella lo mira de reojo con media sonrisa",
    "Remolino de mariposas y pétalos sobre la pradera",
    "Horizonte torcido sobre el mar; una esfera de cristal dobla un rayo y una mujer diminuta lo mira de reojo",
    "Pasillo de espejos inclinados con los reflejos mirando hacia otro lado",
    "Nube-frasco que vuelca jazmín y canela sobre el mar",
    "Sendero de pétalos de jazmín que sube hasta un sol dorado",
    "Atardecer: él con el ramo, ella de brazos cruzados que sonríe",
    "Listones coral y dorados que bailan en espiral sobre el mar",
    "Silueta en un tejado cuyo grito se vuelve una bandada de pájaros de luz",
    "Escalera en espiral hecha de alas y plumas, con un ave grande arriba",
    "Concha de nácar del tamaño de una casa, como un oído, con pájaros dorados",
    "Espejo dorado de la vanidad: el reflejo lleva corona y él se desespera",
    "Espejo que muestra a la pareja de la mano mientras ella corre por el prado",
    "Listón coral que se estira al horizonte; ella y él lo recorren corriendo",
    "Luna de nácar con forma de frente sobre colinas de terciopelo rojo",
    "Hombre que sube por una trenza que cuelga de una nube",
    "Galaxia de estrellas que él enciende y ella toca con la mano",
    "Caja de cristal con un paisaje que canta (el pulmón), con su mano sobre el cristal",
    "Arco de nubes al amanecer con una figura que vuela bajo él",
    "Manos atando un listón coral en la muñeca",
    "Espiral de pétalos y estrellas doradas hacia el alba",
    "Dos rastros de huellas que se juntan en uno en un prado florecido",
    "Pareja sentada en una nube viendo el amanecer, con el listón en lazo",
    "Prado en flor con el espejo que refleja el mismo cielo que el real",
]

table = []
for i, (r, sid, c) in enumerate(zip(rows, scenes, CONCEPTO), 1):
    cols = [x.strip() for x in r.strip("|").split("|")]
    num, _, entra, sale, dur, letra, _g, mov, trans = cols
    table.append(f"| {i} | `{sid}` | {entra} | {sale} | {dur} | {letra} | {c} | {mov} | {trans} |")

meta = old[old.index("## Borrador de metadatos"):old.index("## Métricas")]
meta = meta.replace("y un clavel rojo", "y un listón coral")

out = f"""# Plan de montaje — "Mentira que te mentí" (versión onírica pictórica, 30 imágenes)

Audio: `P:\\Canciones\\audio\\wav\\love\\Mentira que te mentí.wav` (198,0 s = 3:18). Cortes de `letra.srt` (alineada con `scripts/align-lyrics.py`, modelo medium, sobre la mezcla completa), ajustados al pulso con librosa. Tempo: picos de autocorrelación a 172,3, 117,5 y 86,1 BPM; groove probablemente ≈ 172 BPM a medio tiempo con hemiola de 3 contra 4 (hipótesis; no se ha escuchado). Estilo musical según el prompt de la canción: groove minimalista experimental, drum and bass, funky, almohadillas etéreas.

Entrega: `imgs/` (30 imágenes a 1920×1080 sin ruido ni glitch), `hoja.jpg`, `cover/`, `letra.srt` (UTF-8 con BOM). Todo se copia a la carpeta de fotogramas.

| # | Escena | Entra | Sale | Dur. | La letra dice | Imagen | Movimiento | Transición hacia la siguiente |
|---|---|---|---|---|---|---|---|---|
{chr(10).join(table)}

Reglas: no repetir movimiento en planos consecutivos; zoom máximo ≈ 105 % (las imágenes ya vienen a 1920×1080); en las entradas de estribillo, corte con un destello breve; pantalla final calmada, sin texto; título de portada solo 3–4 s al inicio.

## Concepto y estilo (versión final)
- **Idea:** la mentira es el pretexto; él «se defiende» desgranando pruebas de su amor, y cada prueba es una metáfora de la letra hecha objeto o paisaje imposible (trenzas-río, aromas que llueven, oído de nácar, pecho de cristal con paisaje que canta, espejo que muestra la verdad). Las personas son escala y emoción, no el tema: ≈ la mitad de las imágenes no tienen personas, otras tienen una sola figura pequeña, y solo unas pocas muestran a la pareja (diálogo y coqueteo).
- **Estilo:** pintura digital al óleo, onírica y luminosa; pincelada visible, degradados suaves; nada de fotografía, ruido ni glitch. Una idea imposible por imagen, presentada con calma.
- **Color por emoción:** duda y burla en turquesa, limón y oro; picardía en menta y coral; ardor de la tarde en ámbar y magenta; sinceridad en azul cielo y blanco; vanidad en dorado frío; estallido en coral, magenta y oro; reconciliación en oro y rosa de amanecer.
- **Personajes:** adultos jóvenes de escala equilibrada, ropa larga y recatada, caras ocultas o muy simples; listón coral como motivo recurrente.
- **Descartadas (archivadas):** versión mexicana serigrafiada (`v1_mexicana/`), versión nocturna con glitch (`v2_nocturna/`) y las pruebas fotográficas (`prueba/`, `prueba2/`, `prueba3/`).

## Portada y miniatura
`cover/portada_1920x1080.png` y `cover/miniatura_1280x720.png` (de `21_luna_frente`); alterna en `cover_25_arco_nubes/`. Copia en `P:\\Canciones\\audio\\wav\\love\\assets\\youtube\\mentira-que-te-menti\\`.

{meta}## Métricas
- 30 imágenes base a 1920×1080 ≈ 125 s cada una; con las regeneraciones de esta versión se generaron ≈ 70 imágenes (≈ 2,5 h de GPU). Alineación de la letra (CPU) ≈ 4 min.
- Causas de rechazo: persona de más o duplicada (≈ 10), pose que se lee como caída o suspensión (≈ 6), imagen negra por NaN en la generación a este tamaño (4), concepto no logrado (≈ 4).

## Pendientes para el autor
- Revisar las imágenes en `P:\\Canciones\\audio\\wav\\love\\assets\\fotogramas\\mentira-que-te-menti\\` (las versiones descartadas están en las subcarpetas `v1-descartada`, `v2-descartada`, `v3-reemplazadas` y `v4-reemplazadas`).
- Imágenes que aceptó mi revisión pero que pueden discutirse: 19 (una mujer corre delante del espejo que muestra a la pareja), 22 (él cuelga de la trenza), 24, 25 y 27 (una figura vuela en diagonal).
- Aportar la historia de la canción para la descripción.
"""
open("PLAN.md", "w", encoding="utf-8").write(out)
print("ok", len(table))

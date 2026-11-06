"""Divide las 8 escenas rechazadas en dos tandas con distinto prefijo de estilo.

scenes_np.json: escenas SIN personas, con un prefijo que no menciona personas (las menciones atraen figuras).
scenes_pp.json: escenas con personas controladas, con el prefijo original.
"""
import json

d = json.load(open("scenes.json", encoding="utf-8"))
by_id = {s["id"]: s for s in d["scenes"]}

style_np = (
    "Digital oil painting in a luminous dreamlike surrealist style, visible soft brushstrokes with gentle impasto texture, "
    "smooth glowing gradients, rich harmonious saturated palette, one single impossible idea presented with total calm, "
    "large calm negative space, weightless drifting motion, tender whimsical mood, "
    "clean smooth image with no noise and no grain, not photorealistic, no text, no letters. "
)

NP = {
    "05_dos_trenzas_caminos": "Palette of mint green, coral and lemon yellow. Two long thick braided ropes of dark hair with coral ribbons at the ends lie side by side across a green valley and wind toward the horizon like two roads, a painterly landscape of rolling hills under a bright sky",
    "14_listones_baile": "Palette of amber, magenta and gold. Many long coral and gold satin ribbons twirl in a great graceful spiral across a magenta sunset sky above a calm sea, lively motion",
    "16_espiral_alas": "Palette of sky blue, white and gold. A grand spiral staircase made entirely of white and golden bird wings and feathers winding up through clouds into the sky, glowing, the steps are feathers",
    "28_huellas": "Palette of gold and sky blue. Seen from above at an angle, a meadow full of flowers with two trails of small footprints in the grass, one trail from the left and one from the right, curving toward each other and merging into a single trail at the center, petals drifting in the wind",
    "30_prado_florecido": "Palette of soft gold and pale blue. A meadow in full bloom at dawn with a giant tall standing mirror in the middle reflecting exactly the same dawn sky as the real one, a coral ribbon lying on the grass, calm",
}
PP = ["09_horizonte_torcido", "19_espejo_reflejo_juntos", "22_cascada_trenza"]

np_scenes = []
for k, (i, p) in enumerate(NP.items()):
    np_scenes.append({"id": i, "seed": 95000 + k * 23 + 3, "prompt": p + ", the lower third is calm with little detail"})
json.dump({"style": style_np, "width": 1920, "height": 1080, "scenes": np_scenes},
          open("scenes_np.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

pp_scenes = [dict(by_id[i], seed=96000 + n * 29 + 5) for n, i in enumerate(PP)]
json.dump({"style": d["style"], "width": 1920, "height": 1080, "scenes": pp_scenes},
          open("scenes_pp.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(np_scenes), len(pp_scenes))

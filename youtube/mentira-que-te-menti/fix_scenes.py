"""Reescribe los prompts de las 8 escenas rechazadas (sin palabras de ausencia: el modelo las llena con una figura)."""
import json

NEW = {
    "05_dos_trenzas_caminos": "Palette of mint green, coral and lemon yellow. Two winding rivers braid around each other across a vast green valley like a braid made of water, coral ribbons floating above them in the breeze, a painterly landscape of rolling hills under a bright sky",
    "09_horizonte_torcido": "Palette of mint green, coral and lemon yellow. A crooked tilted horizon over a calm sea where the whole sea surface slopes like a tilted table, a large glass sphere on the shore bends a ray of golden light sideways, a tiny woman in a long dress stands upright on the shore for scale watching the ray with a sly sideways glance, whimsical",
    "14_listones_baile": "Palette of amber, magenta and gold. Many long coral and gold satin ribbons twirl in a great graceful spiral across a magenta sunset sky above a calm sea, lively motion",
    "16_espiral_alas": "Palette of sky blue, white and gold. A grand spiral staircase made entirely of white and golden bird wings and feathers winding up through clouds into the sky, glowing, the steps are feathers",
    "19_espejo_reflejo_juntos": "Palette of lavender and turquoise. A single colossal standing mirror in a meadow of grass and flowers, the reflection inside the mirror shows a young man and a young woman standing side by side holding hands, while the meadow in front of the mirror is just grass and flowers, the two reflected people are the only people in the picture",
    "22_cascada_trenza": "Palette of coral and magenta. A tall hill made of soft clouds under a magenta sky, a long thick dark braid with a coral ribbon hangs down the side of the hill like a rope, a young man in a white shirt stands firmly on the hill climbing the braid hand over hand with both feet planted on the cloud, only one person",
    "28_huellas": "Palette of gold and sky blue. Seen from above at an angle, a meadow full of flowers with two trails of small footprints in the grass, one trail from the left and one from the right, curving toward each other and merging into a single trail at the center, petals drifting in the wind",
    "30_prado_florecido": "Palette of soft gold and pale blue. A meadow in full bloom at dawn with a giant tall standing mirror in the middle reflecting exactly the same dawn sky as the real one, a coral ribbon lying on the grass, calm",
}

d = json.load(open("scenes.json", encoding="utf-8"))
for k, s in enumerate(d["scenes"]):
    if s["id"] in NEW:
        s["prompt"] = NEW[s["id"]] + ", the lower third is calm with little detail"
        s["seed"] = 90000 + k * 19 + 11
json.dump(d, open("scenes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(sorted(NEW))

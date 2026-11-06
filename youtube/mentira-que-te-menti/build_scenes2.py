"""scenes.json v3 de «Mentira que te mentí»: más conceptual, menos personajes.

Las escenas ya aprobadas (03, 06, 07, 13, 18, 20, 23) conservan su imagen; el resto se regenera.
"""
import json

style = (
    "Digital oil painting in a luminous dreamlike surrealist style, visible soft brushstrokes with gentle impasto texture, "
    "smooth glowing gradients, rich harmonious saturated palette, one single emotion tints the whole world, weightless drifting motion, "
    "tender whimsical humorous romantic mood, one impossible idea per picture presented with total calm, large calm negative space, "
    "include only the people explicitly mentioned in the scene and no others, any people are young adults in long modest clothing of balanced realistic scale "
    "with faces hidden or very simple, upright and stable and never falling, clean smooth image with no noise and no grain, not photorealistic, no text, no letters. "
)

NEW = [
    ("01_marco_vacio", "Palette of turquoise, lemon yellow and gold. A huge empty ornate picture frame standing alone in a sunny meadow under swirling painterly clouds, a coral ribbon passes through the frame and flutters away into the sky, no people at all, open airy composition with motion"),
    ("02_columpio_nube", "Palette of turquoise, lemon yellow and gold. An empty rope swing hanging from a single fluffy cloud swaying gently in the breeze above a meadow, a straw hat lying in the grass below, a coral ribbon tied to the rope, no people at all, playful"),
    ("04_casa_corazon", "Palette of peach, rose and gold. A small house made of clear glass in the shape of a heart standing in a soft meadow with a tiny river and a blossoming tree flowing inside it, the door open and a path of petals leading in, no people at all, tender light"),
    ("05_dos_trenzas_caminos", "Palette of mint green, coral and lemon yellow. Two enormous parallel braids of dark hair with coral ribbons run across a green valley like two winding roads side by side toward the horizon, landscape scale, bright sky, no people at all and no faces anywhere"),
    ("08_mariposas", "Palette of lemon yellow, coral and sky blue. A sky full of hundreds of butterflies and flower petals swirling in a great spiral above a sunny meadow, a few wildflowers falling from the swirl, dynamic composition, no people at all"),
    ("09_horizonte_torcido", "Palette of mint green, coral and lemon yellow. A landscape with a tilted crooked horizon where the river flows sideways uphill and the sea and sky are slanted, a large glass sphere in the foreground bends a ray of golden light, whimsical, no people at all"),
    ("10_pasillo_espejos", "Palette of mint green and coral. A long hall of tall tilted mirrors opening onto a green sky, in the mirrors the reflections of a single young woman in a long yellow dress with a long dark braid, each reflection turning her head to look in a different direction, only one real figure seen from behind, no other people"),
    ("11_lluvia_jazmin", "Palette of mint, coral and jasmine white. Clouds shaped like glass perfume bottles pouring white jasmine flowers and cinnamon sticks as rain over a calm sea in golden light, swirling coral and gold ribbons of scent, a sky of mint and peach, no people at all"),
    ("12_sendero_petalos", "Palette of mint, coral and gold. A winding path made of white jasmine petals rises in the air toward a large golden sun, a single small young woman in a long yellow dress with a long dark braid seen from behind walks up the path, no other people, whimsical"),
    ("14_listones_baile", "Palette of amber, magenta and gold. Many long coral and gold ribbons dancing in a great spiral across a magenta sunset sky as if they were dancing partners, over a calm sea, lively motion, no people at all"),
    ("15_grito_pajaros", "Palette of sky blue, white and golden light. A single small silhouette of a young man in a white shirt on a rooftop with his hands cupped around his mouth, from his shout flocks of white and golden birds made of light fly out across a vast sky, only one person"),
    ("16_espiral_alas", "Palette of sky blue, white and gold. A huge spiral staircase made of white and golden bird wings rising through the clouds into the sky, glowing, no people at all"),
    ("17_concha_oido", "Palette of sky blue and pearl. A gigantic mother-of-pearl seashell the size of a house standing in a meadow like an enormous ear, golden birds of light flying into the shell, soft pearly glow, no people at all"),
    ("19_espejo_reflejo_juntos", "Palette of lavender and turquoise. A colossal mirror standing alone in an empty meadow, in the reflection a young man and a young woman stand together hand in hand while in front of the mirror the meadow is empty, no real people in front of the mirror"),
    ("21_luna_frente", "Palette of coral, magenta, gold and iridescent pearl. A huge pearly mother-of-pearl moon shaped like a calm smooth forehead above rolling hills of red velvet, no people at all"),
    ("22_cascada_trenza", "Palette of coral and magenta. A high hill made of clouds with a long thick dark braid with a coral ribbon cascading down its side like a waterfall of hair, a single tiny young man in a white shirt climbing the braid, only one person, magenta sky"),
    ("24_pecho_cristal_canta", "Palette of gold, rose and turquoise. A chest made of clear glass with a small singing landscape inside it, birds, a blossoming tree and glass bells, a single hand and one ear of a young woman with a long dark braid pressed gently against the glass, close composition, soft light, no other people"),
    ("25_arco_nubes", "Palette of gold and rose sunrise. A great empty arch made of clouds over a calm sea at sunrise, golden light streaming through it, a coral ribbon in the wind, no people at all"),
    ("26_atando_liston", "Palette of gold and rose. Close-up of a young man's hand tying a coral ribbon around a young woman's wrist, warm light, soft brushstrokes, only hands and wrists visible, no faces"),
    ("27_espiral_petalos", "Palette of gold, rose and pale blue. A spiral of flower petals and golden stars swirling up into a dawn sky, joyful motion, no people at all"),
    ("28_huellas", "Palette of gold and sky blue. Two trails of footprints in a blossoming meadow that start far apart and curve toward each other and merge into one, seen from above at an angle with wind-blown flower petals, no people at all"),
    ("29_amanecer_juntos", "Palette of gold, rose and lavender dawn. Two small figures, a young woman with a long braid and a young man, sitting side by side on a soft cloud seen from behind watching the sunrise, a coral ribbon forms a loose bow above them, only these two, tiny against the vast sky"),
    ("30_prado_florecido", "Palette of soft gold and pale blue. A meadow in full bloom with flowers everywhere, a giant mirror reflecting exactly the same dawn sky as the real one, a coral ribbon resting on the grass, calm, no people at all"),
]

KEPT = ["03_espejo_otro_cielo", "06_escalera_trenza", "07_ramo_gigante", "13_atardecer_espalda",
        "18_espejo_vanidad", "20_liston_horizonte", "23_pecho_galaxia"]

old = {s["id"]: s for s in json.load(open("v2_nocturna/../scenes_v2_prompts.json", encoding="utf-8"))["scenes"]} \
    if False else {}

scenes = [{"id": i, "seed": 70000 + k * 13 + 5, "prompt": p + ", the lower third is calm with little detail"}
          for k, (i, p) in enumerate(NEW)]
for kid in KEPT:
    scenes.append({"id": kid, "seed": 0, "prompt": "(imagen conservada de la tanda anterior)"})
scenes.sort(key=lambda s: s["id"])
json.dump({"style": style, "width": 1920, "height": 1080, "scenes": scenes},
          open("scenes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(scenes))

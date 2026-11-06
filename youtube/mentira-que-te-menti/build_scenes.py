"""Genera scenes.json de la versión onírica pictórica de «Mentira que te mentí»."""
import json

style = (
    "Digital oil painting in a luminous dreamlike surrealist style, visible soft brushstrokes with gentle impasto texture, "
    "smooth glowing gradients, rich harmonious saturated palette, one single emotion tints the whole world, weightless drifting motion, "
    "tender whimsical humorous romantic flirtatious mood, the two characters are young adults in their twenties of similar realistic "
    "proportions with balanced scale between them and neither is giant, faces idealized and simple or hidden, long modest clothing, "
    "all figures upright and stable and never falling, clean smooth image with no noise and no grain, not photorealistic, no text, no letters. "
    "She is a young woman with a long dark braid tied with a coral ribbon in a long flowing yellow dress; "
    "he is a young man in a white shirt and beige trousers. "
)

S = [
    ("01_pradera_pregunta", "Palette of turquoise, lemon yellow and gold. A wide sunny meadow with swirling painterly clouds, far away the young woman stands seen from behind, the young man runs toward her through the grass, a coral ribbon flies across the sky like a question mark, airy open composition with motion"),
    ("02_columpio_nube", "Palette of turquoise, lemon yellow and gold. The young woman sits on a swing hanging from a single fluffy cloud, laughing with her head thrown back and her braid flying, below on the grass the young man holds his hat in his hand looking up at her, playful"),
    ("03_espejo_otro_cielo", "Palette of pale lavender and peach with a golden sunrise. A vast calm meadow with a colossal rectangular mirror reflecting a different sky, a golden sunrise over blossoming trees with birds, the two young figures seen from behind in front of it, he holds out one hand toward the mirror, she stands with her arms crossed, a coral ribbon floats between them"),
    ("04_pecho_ventana", "Palette of peach, rose and gold. The young man presses a hand to his chest which opens like a glass window showing a tiny glowing landscape with a river and blossoming trees inside, the young woman stands facing him at a normal distance with one eyebrow raised and a teasing half smile, soft meadow"),
    ("05_dos_trenzas_caminos", "Palette of mint green, coral and lemon yellow. Two enormous braids of dark hair with coral ribbons run parallel across a green valley like two winding roads, the young man walks between them toward the horizon, bright sky, no woman visible"),
    ("06_escalera_trenza", "Palette of turquoise and gold. The young woman and the young man walk hand in hand up a long winding sky staircase woven like a braided rope of dark hair with a coral ribbon toward a luminous mother-of-pearl moon, seen from behind, clouds below, petals drifting upward"),
    ("07_ramo_gigante", "Palette of turquoise, lemon yellow and gold. The young man kneels on one knee offering an enormous bouquet of wildflowers to the young woman who looks at him sideways over her shoulder with a teasing raised eyebrow and a half smile, arms crossed, wind blowing a coral ribbon, sunny meadow with swirling clouds"),
    ("08_mariposas", "Palette of lemon yellow, coral and sky blue. The bouquet has burst into hundreds of butterflies and petals swirling in the air, the young woman runs laughing after them with her skirt flying, the young man chases behind her, dynamic diagonal composition, bright meadow"),
    ("09_mirada_esfera", "Palette of mint green, coral and lemon yellow. The young woman in profile looks sideways with a sly glance, a ray of golden light bends inside a large glass sphere in front of her and veers toward the young man at the edge of the picture, tilted windows in the distance, playful"),
    ("10_ventanas_inclinadas", "Palette of mint green and coral. A hall of tilted windows and mirrors opening onto a green sky, the young woman turns her head away with a smile and every reflection looks in a different direction, the young man tilts his neck sideways to follow her gaze comically"),
    ("11_lluvia_jazmin", "Palette of mint, coral and jasmine white. It rains white jasmine flowers and cinnamon sticks from clouds shaped like perfume bottles, the young woman stands with her arms wide open and her eyes closed in the fragrant rain, swirling ribbons of coral and gold scent, a sky of mint and peach"),
    ("12_sendero_petalos", "Palette of mint, coral and gold. The young woman walks up a path of jasmine petals toward the sun looking back over her shoulder with a mischievous smile, far behind the young man leans casually on a lamppost pretending not to be waiting, whimsical"),
    ("13_atardecer_espalda", "Palette of amber, magenta and warm gold. A sunset sky, the young man stands holding a bouquet, the young woman has her arms crossed and turns her back to him but smiles in profile, long shadows, wind in her braid, warm rich light"),
    ("14_baile_nube", "Palette of amber, magenta and gold. The young couple dances on a soft cloud, her long dress spinning, a coral ribbon tracing circles around them, magenta sunset, lively motion"),
    ("15_grito_pajaros", "Palette of sky blue, white and golden light. The young man on a rooftop with his hands cupped around his mouth shouts joyfully, his words flying away as flocks of white and golden birds made of light toward the distant young woman on a cloud balcony"),
    ("16_espiral_alas", "Palette of sky blue, white and gold. The birds of light form a spiral staircase of wings rising from the rooftop to a cloud balcony where the young woman leans listening, the young man at the bottom of the spiral looking up"),
    ("17_concha_oido", "Palette of sky blue and pearl. A gigantic mother-of-pearl seashell stands in a meadow like a house-sized ear, the young woman sits beside it with her eyes closed listening, golden birds of light flying into the shell, soft pearly glow"),
    ("18_espejo_vanidad", "Palette of cold gold and white. The young woman admires herself in a large golden ornate mirror where her reflection wears a small crown, behind her grey opaque paper butterflies bounce off the mirror, the young man in the background raises his hands in comic despair, humorous"),
    ("19_espejo_juntos", "Palette of lavender and turquoise. A colossal mirror in a meadow, in the reflection the young man and woman stand together hand in hand while in front of the mirror they stand apart, both seen from behind"),
    ("20_liston_horizonte", "Palette of lavender, turquoise and coral. A long coral ribbon stretches from the young woman's hand across a wide meadow to the horizon while the young man runs along it joyfully, dynamic diagonal composition"),
    ("21_luna_frente", "Palette of coral, magenta, gold and iridescent pearl. A huge pearly mother-of-pearl moon shaped like a calm forehead over rolling hills of red velvet, the young couple small in the foreground seen from behind seated side by side on a hill"),
    ("22_cascada_trenza", "Palette of coral and magenta. The young woman stands on top of a high cloud hill, her long thick dark braid with a coral ribbon cascades down the hill like a waterfall of hair, the young man climbs it joyfully with both hands, magenta sky"),
    ("23_pecho_galaxia", "Palette of coral, magenta and gold. The young man's chest ignites into a spiral galaxy of golden stars and coral light, the young woman beside him of the same height reaches to touch the light, both upright on a hill, dramatic sky"),
    ("24_pecho_cristal_canta", "Palette of gold, rose and turquoise. The young man's chest is clear glass with a small singing landscape inside it, birds, a blossoming tree and glass bells, the young woman rests her forehead and hand against the glass with her eyes closed, both standing upright, soft light"),
    ("25_arco_nubes", "Palette of gold and rose sunrise. The young couple stand upright side by side under a great arch of clouds, seen from behind, her braid and a coral ribbon moving in the wind"),
    ("26_atando_liston", "Palette of gold and rose. Medium shot of the young man handing a coral ribbon to the young woman who ties it around her wrist smiling, warm light, both at similar scale"),
    ("27_giro_petalos", "Palette of gold, rose and pale blue. The young couple twirls together hand in hand among drifting petals and golden stars, joyful motion"),
    ("28_correr_prado", "Palette of gold and sky blue. The young woman holds the young man's hand pulling him along as they run through a blossoming meadow laughing, wind, dynamic composition"),
    ("29_amanecer_juntos", "Palette of gold, rose and lavender dawn. The young couple sit side by side on a soft cloud seen from behind watching the sunrise, a coral ribbon forms a loose bow above them"),
    ("30_prado_florecido", "Palette of soft gold and pale blue. The original meadow now in bloom with flowers everywhere, the giant mirror reflecting exactly the same dawn sky as the real one, nobody visible, calm, a coral ribbon resting on the grass"),
]

scenes = [
    {"id": i, "seed": 60000 + k * 11 + 3, "prompt": p + ", the lower third is calm with little detail"}
    for k, (i, p) in enumerate(S)
]
json.dump({"style": style, "width": 1920, "height": 1080, "scenes": scenes},
          open("scenes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(scenes))

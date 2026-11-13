"""Tabla de 60 escenas de la versión narrativa de «Mentira que te mentí» -> scenes.json + PLAN_narrativa.md.

Cada fila: (id, inicio_seg, letra, kind, paleta, prompt). kind: P = con personas, N = sin personas, R = imagen reutilizada de las pruebas.
"""
import json

HER = "a young woman in a long yellow dress with long sleeves and a long dark braid"
HIM = "a young man in a white shirt with rolled sleeves and dark trousers"

STYLE_P = ("Surreal cinematic photograph in the spirit of Magritte and dreamlike editorial photography, dramatic yet luminous light, "
           "rich saturated color, shallow depth of field, perfectly clean and sharp image with no noise and no grain, "
           "one large impossible dreamlike phenomenon dominates the frame, only the people explicitly mentioned appear and nobody else, "
           "long modest clothing, no text, no letters. ")
STYLE_N = ("Surreal cinematic photograph in the spirit of Magritte and dreamlike editorial photography, dramatic yet luminous light, "
           "rich saturated color, shallow depth of field, perfectly clean and sharp image with no noise and no grain, "
           "one large impossible dreamlike phenomenon dominates the frame, wide composition, no text, no letters. ")

COLD = "Palette of cold teal, deep blue and a warm yellow accent. "
TURN = "Palette of teal turning to warm gold. "
WARM = "Palette of warm gold, coral and rose. "
GLOW = "Palette of gold, rose and pale blue sunrise. "
MINT = "Palette of mint green, coral and lemon yellow. "
AMBER = "Palette of amber, magenta and gold. "
SKY = "Palette of sky blue, white and gold. "

S = [
 ("01_plaza_mascaras", 0.0, "intro", "N", COLD + "An empty stormy plaza at dusk with a long coral ribbon lying on the ground and dozens of translucent white porcelain masks beginning to gather in the dark sky, wide cinematic shot, ominous and quiet"),
 ("02_duda_mascaras", 5.6, "intro", "R", "T1_duda_mascaras.png"),
 ("03_acusacion", 11.2, "Que es una mentira dices", "R", "P1_acusacion.png"),
 ("04_mascara_se_rompe", 13.9, "Mentira que te mentí", "P", COLD + f"{HER} stands with her arms crossed and {HIM} stands facing her, between them a large white porcelain mask floating at eye level is shattering into thousands of white jasmine petals, both seen in profile, medium wide shot"),
 ("05_corazon_dice", 16.5, "Que el corazón me lo dice", "P", TURN + f"Close composition of {HIM} seen in profile with one hand pressed on his chest, a warm golden heart-shaped glow shining through his white shirt, calm sincere expression, soft light"),
 ("06_pajaros_palabras", 18.9, "Y yo te lo digo a ti", "P", WARM + f"{HIM} holds out his open hand toward {HER} who stands a few steps away, from his open palm a flock of luminous white birds flies toward her across a quiet street at golden hour, wide cinematic shot"),
 ("07_trenza_rio", 21.9, "Las trenzas de tu cabello", "P", WARM + f"Seen from behind, {HER} stands on a hillside, her long dark braid turns into a flowing river that runs down her back and across the whole valley, golden light, wide shot"),
 ("08_rios_paralelos", 24.6, "Se tejen en paralelo", "N", MINT + "Aerial view of two long braided rivers, one blue and one gold, running side by side in parallel across a vast green valley toward the horizon, coral ribbons floating above them"),
 ("09_sube_trenza", 27.1, "Con las trenzas de tu pelo", "P", WARM + f"A single person alone in the frame. Seen from behind, {HIM} climbs along the surface of one single colossal braid of dark hair, the interlocking thick strands of braided hair are the whole ground under his feet and fill the entire bottom and sides of the frame edge to edge, the braid rises steeply ahead of him into pink clouds until it vanishes in the haze, there is no asphalt and no road markings, only braided hair, no end of the braid is visible, low-angle shot, the sky is much larger"),
 ("10_cima_trenza", 29.7, "Se puede alcanzar el cielo", "P", GLOW + f"{HIM} stands on the very top of an enormous dark braid of hair that arcs up among golden clouds, he stretches one arm up toward the sun, backlit, {HER} seen small far below on the street looking up, wide shot, tender and joyful"),
 ("11_escepticismo", 33.2, "Que es una mentira dices", "P", TURN + f"Close shot of {HER} in profile with a skeptical sideways look, holding a white porcelain mask lowered at her side, blurred stormy plaza behind, cold light starting to warm"),
 ("12_ramo_de_reojo", 35.5, "Mentira que te mentí", "P", WARM + f"{HIM} kneels on one knee offering a bouquet of white jasmine and a coral ribbon, {HER} stands looking away to the side with a hint of a smile, quiet street at golden hour, medium shot"),
 ("13_casa_amapolas", 38.7, "Mentira que te mentí", "P", MINT + f"A small turquoise house in a desert street with enormous poppies in coral, orange and white growing from its roof, {HIM} walks toward its door holding a bouquet, wide shot under a deep blue sky"),
 ("14_giro_listones", 41.2, "Mentira que te mentí", "P", AMBER + f"{HER} spins in a field, long coral and gold ribbons whirl around her in streaks of motion blur, her face smiling in profile, magenta sunset, dynamic"),
 ("15_petalos_cielo", 46.0, "(instrumental)", "N", AMBER + "A vast sky full of thousands of butterflies and flower petals swirling in a great spiral above an empty golden street at sunset"),
 ("16_ojo_iris", 51.6, "Tus ojos me miran locos", "P", WARM + f"Extreme close-up of the eye of {HER}, wide and curious, the iris swirls with warm colors and holds a tiny reflection of {HIM}, cinematic macro"),
 ("17_horizonte_torcido", 53.8, "Cuando tuerces la mirada", "P", MINT + f"A plaza whose whole floor and horizon tilt sideways at a steep angle, {HER} stands upright looking sideways with a sly glance, {HIM} stands upright watching her, whimsical dutch angle"),
 ("18_pasillo_espejos", 56.8, "Cuando me miras sesgada", "P", MINT + f"A single person alone in the frame. Close three-quarter portrait of {HER} in the foreground glancing sideways toward the edge of the picture with a sly sideways look, behind her a long mint green corridor lined with tall tilted empty mirrors in perspective that reflect only the green room and the sky, whimsical, only one person"),
 ("19_reflejo_equivocado", 59.3, "Me miras equivocada", "P", COLD + f"{HER} stands before a tall ornate mirror in an empty plaza frowning with her arms crossed, her reflection in the mirror is smiling warmly, eerie and funny"),
 ("20_frascos_aromas", 62.1, "Con cien aromas surtidos", "N", MINT + "Hundreds of glass perfume bottles floating in a sunny sky over a meadow, each releasing a ribbon of colored scent in mint, coral and gold"),
 ("21_aroma_tarde", 64.5, "Te aromaste por la tarde", "P", AMBER + f"Seen from behind, {HER} walks in a golden afternoon meadow, a halo of colored fragrant mist floats around her like a soft cloud of perfume"),
 ("22_lluvia_canela", 67.3, "De canela, de jazmines", "N", MINT + "A cloud shaped like a giant glass perfume bottle pours white jasmine flowers and cinnamon sticks as rain over a quiet street in golden light"),
 ("23_sendero_jazmin", 70.0, "Para salir a buscarme", "P", GLOW + f"{HER} seen from behind walks away up a winding path made of white jasmine petals that rises in the air toward a large golden sun"),
 ("24_caen_mascaras", 72.7, "Que es una mentira dices", "P", TURN + f"{HER} looks at {HIM} with her arms slowly uncrossing while white porcelain masks fall one by one from the sky and dissolve into petals, light turning warm, medium wide shot"),
 ("25_manos_vacias", 75.2, "Mentira que te mentí", "P", WARM + f"{HIM} laughs showing both open empty hands with nothing to hide, a single person alone in the frame, golden afternoon light behind him, medium shot"),
 ("26_ofrece_liston", 77.9, "Mentira que te mentí", "P", WARM + f"{HIM} extends a long coral ribbon toward {HER}, who takes the end of it with a curious hand, their hands nearly touching, close shot"),
 ("27_liston_tenso", 80.7, "Mentira que te mentí", "P", AMBER + f"{HER} and {HIM} stand far apart pulling gently on both ends of a long coral ribbon that stretches across a field to the sunset horizon like a playful line, wide shot"),
 ("28_listones_baile", 86.0, "(instrumental)", "N", AMBER + "Dozens of long coral and gold satin ribbons dance in a great spiral over an empty field at magenta sunset, motion streaks"),
 ("29_giro_alegre", 91.0, "(instrumental)", "P", AMBER + f"A single person alone in the frame, {HER} twirls laughing in an empty field of golden light, her yellow dress and a long coral ribbon blurred in motion, wide shot"),
 ("30_grito_azotea", 96.5, "Cuando te dije te amo", "P", SKY + f"{HIM} stands on a rooftop at dusk with his hands cupped around his mouth shouting to the sky, from his shout a huge flock of luminous white birds flies out over the city, seen from the side"),
 ("31_verdad_luz", 98.9, "Yo te dije la verdad", "P", SKY + f"Close portrait of {HIM} in profile, calm honest face lit by golden light, one white feather floating in front of him, soft sky background"),
 ("32_brazos_abiertos", 101.1, "Con toda sinceridad", "P", SKY + f"{HIM} stands with arms open wide in a vast field of tall grass, white birds circling around him, wind in his shirt, wide shot from behind"),
 ("33_espiral_aves", 103.6, "Lo que yo siento lo clamo", "N", SKY + "A giant spiral of white and golden birds rising in a column from a quiet rooftop skyline into a glowing sky"),
 ("34_oido_nacar", 107.0, "Cuando tus tiernos oídos", "P", SKY + f"{HER} stands beside a gigantic mother-of-pearl seashell shaped like an ear taller than a house, she cups her hand at her ear with eyes closed listening, soft pearly light"),
 ("35_pajaros_oido", 109.5, "Me escuchan esta verdad", "N", SKY + "Golden birds of light flying into the opening of a gigantic mother-of-pearl seashell shaped like an ear standing in a meadow, soft pearly glow"),
 ("36_espejo_vanidad", 112.0, "Tu mente por vanidad", "P", COLD + f"{HER} stands before a huge ornate golden mirror, her reflection wears a gold crown and looks proud, cold golden light, dark teal room"),
 ("37_mascaras_espejo", 114.6, "La transforma en falsedad", "P", COLD + f"From the surface of a golden mirror dozens of white porcelain masks push out into the room like a swarm, {HER} steps back with her hand raised, {HIM} stands calm in the background, tense"),
 ("38_espejo_pareja", 118.0, "Que es una mentira dices", "P", TURN + f"A colossal standing mirror in a meadow whose reflection shows {HER} and {HIM} standing hand in hand, while in front of the mirror she stands alone looking at it"),
 ("39_el_espera", 120.5, "Mentira que te mentí", "P", WARM + f"{HIM} stands calm and patient beside a tall mirror in a meadow looking at {HER} with a gentle smile, golden light rising behind them"),
 ("40_toca_espejo", 123.2, "Mentira que te mentí", "P", WARM + f"{HER} touches the surface of a giant mirror with her fingertips, ripples spreading outward like water across the glass, warm light"),
 ("41_liston_horizonte", 125.5, "Mentiraaa que te mentí", "P", AMBER + f"{HER} and {HIM} run side by side holding a long coral ribbon that stretches to the horizon over an empty road at sunset, wide shot from behind, joyful"),
 ("42_frente_nacar", 131.8, "Tienes de nácar la frente", "N", GLOW + "A huge pearly mother-of-pearl moon shaped like a calm smooth forehead rising above rolling hills at dawn"),
 ("43_colinas_terciopelo", 133.9, "Los labios de terciopelo", "N", WARM + "Rolling dunes and hills made of deep red velvet under a rose sky with soft folds like curtains, wide empty landscape"),
 ("44_camino_pelo", 137.5, "Quiero subirme en tu pelo", "P", WARM + f"{HIM} seen from behind walks up a vast winding road made of long dark braided hair that rises into pink clouds, wide low-angle shot"),
 ("45_mano_nube", 139.7, "Yo quiero alcanzar el cielo", "P", GLOW + f"{HIM} stands on top of a braided road among golden clouds reaching his hand up toward the sun, backlit silhouette"),
 ("46_pecho_estrella", 142.5, "Y estallar como una estrella", "P", COLD + f"Double exposure portrait, the profile silhouette of {HIM} looking up with closed eyes, inside his chest and torso a whole galaxy of glowing stars and nebulae bursting outward, soft sunset sky background, only him and nobody else"),
 ("47_estrella_explota", 145.6, "Rebozante de emoción", "P", AMBER + f"{HIM} laughs with his arms open as a burst of golden light particles and stars explodes outward from his chest into the sunset sky, joyful"),
 ("48_oreja_pecho", 148.2, "Y que oigas de mi pulmón", "P", WARM + f"{HER} and {HIM} both stand upright in profile facing each other in a field at sunset, she leans slightly forward and holds her hand open a few centimeters from his chest listening with her eyes closed, a warm golden glow shines from his chest toward her hand, they do not embrace, only two people, medium side shot"),
 ("49_pecho_paisaje", 150.5, "De nuevo mis sentimientos", "P", GLOW + f"Close shot of the chest of {HIM} as a clear glass window showing a tiny singing landscape inside with birds, a blossoming tree and glass bells, {HER}'s hand resting on the glass"),
 ("50_sonrisa", 153.9, "Que es una mentira dices", "P", WARM + f"{HER} smiles slightly looking at {HIM}, arms uncrossed, warm golden light, medium close shot in profile"),
 ("51_liston_muneca", 156.4, "Mentira que te mentí", "P", WARM + f"Close-up of the hands of {HIM} tying a coral ribbon around the wrist of {HER}, warm soft light, extreme close-up showing only two hands and one wrist against a softly blurred plain golden background, only these two people"),
 ("52_lluvia_petalos", 159.7, "Mentira que te mentí", "P", GLOW + f"{HER} stands laughing with her face lifted in a rain of white petals that falls from the sky where the masks have turned into flowers, {HIM} beside her, joyful"),
 ("53_arco_nubes", 161.9, "Mentira que te mentí", "P", GLOW + f"{HER} and {HIM} stand tiny beneath a great arch made of clouds at sunrise, a coral ribbon waves in the wind between them, wide shot"),
 ("54_caminan_alba", 167.6, "Que es una mentira dices", "P", GLOW + f"{HIM} in a white shirt and {HER} in a long yellow dress with long sleeves and a long braid walk away from the camera holding hands on a long empty seaside road toward a glowing sunrise, a coral ribbon tied at their hands floats behind them in the wind, wide cinematic shot"),
 ("55_frente_con_frente", 170.5, "Mentira que te mentí", "P", GLOW + f"Silhouettes of {HER} and {HIM} standing with their foreheads touching in profile, a halo of pink and gold light glowing around them, soft gradient sky background"),
 ("56_cielo_reflejado", 173.6, "Mentira que te mentí", "R", "T3_cielo_reflejado.png"),
 ("57_espiral_petalos", 175.8, "Mentira que te mentí", "N", GLOW + "A spiral of flower petals and golden stars swirling up into a dawn sky above a calm sea, joyful motion"),
 ("58_huellas", 179.9, "Mentira que te mentí", "N", GLOW + "Aerial view of a meadow full of flowers with two trails of footprints curving toward each other and merging into one, petals drifting in the wind"),
 ("59_amanecer_juntos", 182.4, "Mentira que te mentí", "P", GLOW + f"Exactly two people, a woman on the left and a man on the right: {HER} and {HIM} sit side by side seen from behind on the edge of a high terrace watching the sunrise over the sea, a coral ribbon forms a loose bow above them"),
 ("60_prado_espejo", 189.0, "(cierre)", "N", GLOW + "A meadow in full bloom at dawn with a giant tall standing mirror in the middle reflecting exactly the same dawn sky as the real one, a coral ribbon lying on the grass, calm"),
]
assert len(S) == 60, len(S)

scenes = []
for i, (sid, t, letra, kind, a, *rest) in enumerate(S):
    if kind == "R":
        continue
    prompt = (STYLE_P if kind == "P" else STYLE_N) + a
    scenes.append({"id": sid, "seed": 83000 + i * 11, "prompt": prompt})
json.dump({"style": "", "width": 1920, "height": 1080, "scenes": scenes},
          open("scenes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump([{"id": s[0], "t": s[1], "letra": s[2], "kind": s[3], "ref": s[4] if s[3] == "R" else None} for s in S],
          open("tabla.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def mmss(t): return f"{int(t//60)}:{t%60:04.1f}"
rows = []
for i, (sid, t, letra, kind, a, *rest) in enumerate(S):
    end = S[i + 1][1] if i + 1 < len(S) else 198.0
    desc = a if kind == "R" else a.split(". ", 1)[1] if ". " in a else a
    desc = desc.replace(HER, "ella").replace(HIM, "él")
    rows.append(f"| {i+1} | `{sid}` | {mmss(t)} | {mmss(end)} | {end-t:.1f} s | {letra} | {desc[:140]} |")
open("PLAN_narrativa.md", "w", encoding="utf-8").write(
    "# Versión narrativa — «Mentira que te mentí» (60 imágenes)\n\n"
    "Estilo: fotografía cinematográfica surrealista, un fenómeno imposible grande por imagen. Arco: frío (ella duda) → cálido (él argumenta) → dorado (reconciliación).\n"
    "Personajes: ella = vestido amarillo de manga larga y trenza; él = camisa blanca arremangada; listón coral como motivo.\n\n"
    "| # | Escena | Entra | Sale | Dur. | Letra | Imagen (resumen en inglés) |\n|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
print(len(scenes), "a generar;", sum(1 for s in S if s[3] == "R"), "reutilizadas")

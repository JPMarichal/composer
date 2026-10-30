# Canvas — Los postes de la calle central

## Concepto (8 s, loop de rebote)

Letra clave: "Coloqué tu nombre en treinta postes", "Los postes de la calle central",
"Tu sonrisa resplandece como la única realidad". Imagen concreta, sin personas cantando.

Plano único, vertical 9:16: travelling lento hacia delante por una calle de barrio al
atardecer. A ambos lados, postes de madera de luz con etiquetas de papel escritas a mano
que se mecen con el viento (sin texto legible). Al fondo, una farola que se enciende
cálida. Luz dorada, tono cálido-indie-folk, contenido importante en el centro del encuadre
(los bordes pueden recortarse en el teléfono).

Cumple la política: sin logos, sin texto promocional, sin cortes rápidos ni destellos,
sin voz ni letra cantada.

## Prompt (Wan2.2 TI2V 5B, imagen inicial con z_image_turbo)

Imagen inicial:
> Vertical photo, quiet neighborhood street at golden hour, rows of old wooden utility
> poles on both sides, each with a small hand-written paper tag tied with string, warm
> light, shallow depth of field, film grain, centered composition, no text, no people.

Video:
> Slow steady dolly forward along the street, paper tags swaying gently in the breeze,
> warm sunset light flickering softly through leaves, a street lamp glowing at the far end.
> Calm, smooth motion, no camera shake, no cuts.

Negativo: text, letters, logo, watermark, people, fast motion, flashing, camera shake.

## Especificaciones de entrega

- MP4, H.264, yuv420p, 9:16, 1080x1920 (recomendado; mínimo 720x1280), **sin pista de audio**.
- Duración: Spotify documenta 3–8 s. Hay reportes de rechazo con exactamente 8.00 s,
  así que `make-canvas.ps1` genera una sola versión de 191 frames (7.958 s).
- Tamaño: Spotify no publica un límite. Objetivo ≤ 15 MB (margen de seguridad).

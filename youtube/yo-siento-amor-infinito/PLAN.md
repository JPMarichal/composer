# Plan de montaje — "Yo siento amor infinito por ti" (prueba del flujo de imágenes)

Audio: `P:\Canciones\audio\wav\love\Yo siento amor infinito por ti.wav` (243,2 s = 4:03; tempo ≈ 117,5 BPM; compás ≈ 2,04 s). Cortes alineados con la letra (`letra.srt`, `scripts/align-lyrics.py`) y ajustados al pulso con librosa.

**Alineación real:** los cortes salen de `letra.srt` (stable-ts, modelo medium, sobre la mezcla completa) ajustados al pulso más cercano con librosa. Los versos (19–140 s) quedaron bien alineados; en los estribillos finales (140–243 s) los tiempos de cada renglón no son fiables (hay interludios instrumentales y el mismo renglón se repite 12 veces), así que ahí se usaron los cambios de sección detectados en el audio. Escuchar una vez con la tabla y mover a oído lo que haga falta.

| # | Escena | Entra | Sale | Dur. | Qué dice la letra en ese tramo | Movimiento | Transición hacia la siguiente |
|---|---|---|---|---|---|---|---|
| 1 | `01_prado_manana` | 0:00.0 | 0:26.6 | 26.6 s | intro; «Más de una vez… te encontré entre la naturaleza» | zoom-in lento | disolvencia larga |
| 2 | `02_brisa` | 0:26.6 | 0:31.2 | 4.6 s | «en la brisa suave» | pan derecha→izquierda | disolvencia corta |
| 3 | `03_flor_lluvia` | 0:31.2 | 0:37.4 | 6.2 s | «en cada flor, en cada lluvia, en cada ave» | zoom-out | zoom cruzado (flor → árbol) |
| 4 | `04_arbol_amanecer` | 0:37.4 | 0:52.9 | 15.5 s | estribillo 1 | zoom-in lento | desenfoque (entra el sueño) |
| 5 | `05_sueno` | 0:52.9 | 0:57.5 | 4.6 s | «te he visto al soñar» | pan izquierda→derecha | disolvencia |
| 6 | `06_despertar` | 0:57.5 | 1:10.4 | 12.9 s | «te he rencontrado al despertar… sueño despierto» | zoom-out | cortina suave a la derecha |
| 7 | `07_arbol_lluvia` | 1:10.4 | 1:44.8 | 34.4 s | estribillo 2 + interludio instrumental | zoom-in muy lento | disolvencia larga |
| 8 | `08_desierto` | 1:44.8 | 1:53.1 | 8.3 s | «se agolpa el secreto… en cada desierto» | pan derecha→izquierda | zoom cruzado (del desierto al brote) |
| 9 | `09_brote_flor` | 1:53.1 | 2:01.8 | 8.7 s | «brote oculto… cada pieza de mi naturaleza» | zoom-in lento | disolvencia |
| 10 | `10_ave_atardecer` | 2:01.8 | 2:09.1 | 7.3 s | «en cada tarde escucha al ave» | pan izquierda→derecha | empuje lento hacia arriba (el ave se eleva) |
| 11 | `11_ave_horizonte` | 2:09.1 | 2:19.9 | 10.8 s | «mi amor te susurra… más allá de la tumba» | zoom-out | disolvencia larga |
| 12 | `12_arbol_atardecer` | 2:19.9 | 3:04.7 | 44.8 s | estribillos 3 a 5 | zoom-in | desenfoque (cae la noche) |
| 13 | `13_arbol_noche` | 3:04.7 | 3:46.2 | 41.5 s | estribillos 6 a 8 | zoom-out | disolvencia muy lenta (cierre) |
| 14 | `14_cierre` | 3:46.2 | 4:03.2 | 17.0 s | último estribillo y final | zoom-out muy lento | — (fin) |

**Limitación:** el tramo final (estribillos, 2:20–3:46) tiene 3 escenas para 86 s, y la 7 dura 34 s. No hay más imágenes porque cada estribillo repite el mismo texto. Si se ve monótono: generar 2–3 variaciones del almendro (p. ej. con luciérnagas, con luna, con el ave posada) y repartirlas ahí.

Reglas aplicadas: no repetir movimiento en planos consecutivos; zoom máximo ≈ 110 %; 4 tipos de transición (disolvencia, zoom cruzado, desenfoque, cortina/empuje), sin destellos; pantalla final calmada (escena 14) sin texto; el título de portada solo 3–4 s al inicio.

## Estilo y tono (decididos para esta canción)
- **Estilo:** diorama de papel recortado en capas con luz trasera cálida (distinto del gouache y el carbón de las otras canciones).
- **Color:** arco del día a la noche: verde primavera y oro de amanecer → verdes y plata de lluvia → ocre del desierto → rosa y lavanda del atardecer → índigo con estrellas doradas.
- **Tono:** luminoso, tierno y sereno; sin pérdida ni espera (amor pleno).
- **Motivo que vuelve:** un almendro en flor, siempre el mismo, cambia de luz (amanecer, lluvia, atardecer, noche, lejos). Personas sin rostro (silueta, de espaldas, hecha de pétalos).

## Portada y miniatura
Escena `13_arbol_noche` (alto contraste, centro calmado). `cover/portada_1920x1080.png` y `cover/miniatura_1280x720.png`; copia en `P:\Canciones\audio\wav\love\assets\youtube\yo-siento-amor-infinito\`. La versión con el amanecer tapaba el árbol y el nombre del autor no se leía sobre fondo claro: elegir escenas oscuras o con el sujeto fuera del centro.

## Borrador de metadatos (sin publicar; el autor debe aportar la historia de la canción)
Título: `Yo siento amor infinito por ti – JPMarichal`
```
«Yo siento amor infinito por ti».

[Aquí va la historia real de la canción en las palabras del autor: de dónde nació, a quién va. No inventarla.]

Una canción donde el amor aparece en cada cosa bella: la brisa, las flores, la lluvia, las aves. Te encuentro al soñar y te reencuentro al despertar, y ese amor trasciende más allá de la tumba.

Si alguna vez has visto a alguien que quieres en cada cosa bella, esta canción es para ti.

CRÉDITOS
Letra y melodía: JPMarichal
Voz y arreglos: producidos con herramientas de IA bajo su dirección
Video: realizado con herramientas de IA y edición digital

Este video usa contenido generado o alterado con IA.
```

## Métricas
- 14 imágenes de 1280×720 + 2 regeneradas por fallo de la autorrevisión (escena 3 sin flor; escena 12 con rosas en vez del almendro) = 16 imágenes × ≈ 60 s ≈ 16 min de generación.
- Revisión: 3 hojas de contacto de 6 imágenes (en vez de 14 imágenes sueltas).
- Incidente: la sesión se reinició a mitad de la generación y la instalación de librosa quedó corrupta (caché de uv dañada tras el reinicio); se resolvió con `uv pip install --no-cache`.

## Pendientes para el autor
- Revisar los fotogramas en `P:\Canciones\audio\wav\love\assets\fotogramas\yo-siento-amor-infinito\` (puerta 2 diferida porque estuvo ausente).
- Aportar la historia de la canción para la descripción.
- Montar en Camtasia según la tabla y alinear a oído con la letra; generar `.srt` (requiere `stable-ts`, no instalado).

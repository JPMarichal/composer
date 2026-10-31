# Plan de montaje — "Yo siento amor infinito por ti" (prueba del flujo de imágenes)

Audio: `P:\Canciones\audio\wav\love\Yo siento amor infinito por ti.wav` (243,2 s = 4:03; tempo ≈ 117,5 BPM; compás ≈ 2,04 s). Cortes ajustados al pulso más cercano con `scripts/audio-sections.py` (librosa).

**Aviso:** el reparto de escenas es en partes iguales (≈ 17,3 s ≈ 8,5 compases) porque no hay alineación letra-audio (falta `stable-ts`). Las escenas están pensadas por sección de la letra; **ajustar a oído en Camtasia** para que el árbol de los coros caiga en cada estribillo. Los primeros 15 s ya traen movimiento (zoom-in desde el cuadro 0).

| # | Escena | Entra | Sale | Dur. | Movimiento | Transición hacia la siguiente |
|---|---|---|---|---|---|---|
| 1 | `01_prado_manana` | 0:00.0 | 0:17.2 | 17.2 s | zoom-in lento | disolvencia larga |
| 2 | `02_brisa` | 0:17.2 | 0:34.9 | 17.6 s | pan derecha→izquierda | disolvencia larga |
| 3 | `03_flor_lluvia` | 0:34.9 | 0:52.3 | 17.5 s | zoom-out | zoom cruzado (flor → árbol) |
| 4 | `04_arbol_amanecer` | 0:52.3 | 1:09.3 | 17.0 s | zoom-in lento | desenfoque (entra el sueño) |
| 5 | `05_sueno` | 1:09.3 | 1:26.8 | 17.5 s | pan izquierda→derecha | disolvencia larga |
| 6 | `06_despertar` | 1:26.8 | 1:44.3 | 17.5 s | zoom-out | cortina suave hacia la derecha (llega la mañana) |
| 7 | `07_arbol_lluvia` | 1:44.3 | 2:01.8 | 17.5 s | zoom-in | disolvencia larga |
| 8 | `08_desierto` | 2:01.8 | 2:18.8 | 17.0 s | pan derecha→izquierda | zoom cruzado (del desierto al brote) |
| 9 | `09_brote_flor` | 2:18.8 | 2:36.3 | 17.5 s | zoom-in lento | disolvencia larga |
| 10 | `10_ave_atardecer` | 2:36.3 | 2:53.9 | 17.5 s | pan izquierda→derecha | empuje lento hacia arriba (el ave se eleva) |
| 11 | `11_ave_horizonte` | 2:53.9 | 3:10.9 | 17.0 s | zoom-out | disolvencia larga |
| 12 | `12_arbol_atardecer` | 3:10.9 | 3:28.4 | 17.6 s | zoom-in | desenfoque (cae la noche) |
| 13 | `13_arbol_noche` | 3:28.4 | 3:45.7 | 17.2 s | zoom-out | disolvencia muy lenta (cierre) |
| 14 | `14_cierre` | 3:45.7 | 4:03.2 | 17.5 s | zoom-out muy lento | — (fin) |

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

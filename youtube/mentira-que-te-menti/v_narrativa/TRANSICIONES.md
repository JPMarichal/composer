# Transiciones de la versión narrativa

Todos los demás cortes (45) llevan **Cross Dissolve de 0,5 s**. Fundido a negro de 2 s al final de la última imagen.
En `montaje_narrativo_transiciones.fcpxml` todas entran como Cross Dissolve (única que Resolver importa con seguridad) y las especiales llevan un **marcador** en la línea de tiempo con la transición que hay que poner a mano (Efectos > Video Transitions). Las duraciones de los destellos son de 4 cuadros.

| Corte | Entra en | De → a | Transición | Dur. | Para qué |
|---|---|---|---|---|---|
| 2→3 | 0:11.2 | 02_duda_mascaras → 03_acusacion | Cross Dissolve | 1.0 s | de la intro al primer verso, paso de tiempo |
| 9→10 | 0:29.7 | 09_sube_trenza → 10_cima_trenza | Push Up | 0.8 s | sube por la trenza (Motion > Push Up, Motion Blur activado) |
| 10→11 | 0:33.2 | 10_cima_trenza → 11_escepticismo | Brightness Flash | 0.17 s | entra el estribillo 1 (Fusion Transitions, 4 cuadros) |
| 14→15 | 0:46.0 | 14_giro_listones → 15_petalos_cielo | Zoom In and Out | 1.0 s | del estribillo al instrumental (Fusion Transitions) |
| 15→16 | 0:51.6 | 15_petalos_cielo → 16_ojo_iris | Oval Iris | 1.0 s | el iris se cierra sobre el ojo de la escena 16 (Iris > Oval Iris) |
| 23→24 | 1:12.7 | 23_sendero_jazmin → 24_caen_mascaras | Brightness Flash | 0.17 s | entra el estribillo 2 (4 cuadros) |
| 27→28 | 1:26.0 | 27_liston_tenso → 28_listones_baile | Blur Dissolve | 1.0 s | entra el instrumental, desenfoque (Dissolve > Blur Dissolve) |
| 29→30 | 1:36.5 | 29_giro_alegre → 30_grito_azotea | Cross Dissolve | 1.0 s | del instrumental al verso 3, paso de tiempo |
| 37→38 | 1:58.0 | 37_mascaras_espejo → 38_espejo_pareja | Brightness Flash | 0.17 s | entra el estribillo 3 (4 cuadros) |
| 41→42 | 2:11.8 | 41_liston_horizonte → 42_frente_nacar | Cross Dissolve | 1.5 s | tras la nota larga, entra el verso 4 |
| 49→50 | 2:33.9 | 49_pecho_paisaje → 50_sonrisa | Brightness Flash | 0.17 s | entra el estribillo 4 (4 cuadros) |
| 53→54 | 2:47.6 | 53_arco_nubes → 54_caminan_alba | Brightness Flash | 0.17 s | entra el estribillo 5, el de la reconciliación (4 cuadros) |
| 58→59 | 3:02.4 | 58_huellas → 59_amanecer_juntos | Cross Dissolve | 1.0 s | hacia el final |
| 59→60 | 3:09.0 | 59_amanecer_juntos → 60_prado_espejo | Cross Dissolve | 2.0 s | cierre; al final hay fundido a negro |

## Animación
- Cada plano: zoom o paneo con keyframes y suavizado (ease), escala máxima 1,05.
- Títulos de la letra sin fundido (el keyframe de opacidad en los títulos hacía que Resolver los descartara al importar).

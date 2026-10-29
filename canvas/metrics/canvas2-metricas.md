# Métricas — Canvas 2 "Los postes de la calle central" (multiescena)

Datos crudos: `canvas2_metrics.csv` (epoch de cada hito). Hardware: RTX 3050 6 GB, ComfyUI `--lowvram`.
Los tiempos son de reloj, incluyen la interacción del agente (escribir scripts, revisar imágenes) y una corrección del usuario a mitad de proceso.

| Etapa | Tiempo | Acumulado |
|---|---|---|
| Investigación web (multiescena) + arranque del servidor | 49 s | 49 s |
| Imágenes s1–s3 (≈60 s cada una, 720×1280) | 180 s | 230 s |
| Corrección del usuario ("pilares de construcción"): s1 y s2 descartadas | — | — |
| Imágenes s4–s5 (≈45 s de media) | 121 s | 351 s |
| Regeneración corregida de s1 y s2 (≈70 s cada una) | 144 s | 495 s |
| Revisión de las 5 imágenes y configuración de cámara/halos | 22 s | 517 s |
| Render (191 frames, 1080×1920, numpy + ffmpeg) | 142 s | 659 s |
| Validación y entrega en `P:` | 21 s | 680 s |
| **Total** | **680 s (11,3 min)** | |

Coste atribuible a la corrección del usuario: 2 imágenes extra = 144 s (21 % del total).

## Resultado
- 1080×1920, H.264 `yuv420p`, 191 frames a 24 fps = 7,958 s, sin audio, 4,1 MB.
- 5 planos de ~1,6 s con disolvencias de 16 frames (0,67 s); el último se funde en el primero.
- Diferencia entre frames en la costura del bucle 4,2 vs 3,8–5,1 en las demás disolvencias: sin salto.

## Comparación con el Canvas 1 (un plano, video generativo + rebote), mediciones de la misma sesión
| | Canvas 1 (Wan2.2 + rebote) | Canvas 2 (5 ilustraciones + animación en código) |
|---|---|---|
| Imagen(es) | 148 s (1 a 576×1024) | ≈ 310 s (7 imágenes de 720×1280, 2 descartadas) |
| Animación | 568 s (Wan2.2, 97 frames a 448×800) | 142 s (render en código a 1080×1920) |
| Artefactos de IA | saltos y cables que aparecen/desaparecen | ninguno (solo hay imágenes fijas) |
| Tamaño del MP4 | 3,8 MB | 4,1 MB |

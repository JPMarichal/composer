# Canvas de Spotify — estado de la línea de trabajo (pausada el 2026-10-29)

Decisión: se **interrumpe** la generación de Canvas por un cambio de estrategia externo. Este archivo documenta lo hecho, lo pendiente y cómo retomarlo. El método reutilizable está en `skills/spotify-canvas/SKILL.md` (léelo primero).

## Videos entregados (en `P:\Canciones\audio\wav\love\assets\canvas\`)
| Canción | Archivo | Estilo | Transiciones |
|---|---|---|---|
| Los postes de la calle central | `Los postes de la calle central.mp4` (antes "2"; el usuario borró la v1) | gouache onírico, 5 planos | disolvencia |
| Canto de sirena | `Canto de sirena.mp4` | gouache nocturno turquesa | disolvencia |
| Trae contigo la lluvia | `Trae contigo la lluvia.mp4` | gouache ocre → esmeralda (sequía → lluvia) | disolvencia |
| Ya no te dejaré | `Ya no te dejaré.mp4` | gouache primaveral (sin nieve: "cuando no haya hielo") | disolvencia |
| También estuve a punto | `También estuve a punto.mp4` | carbón + acuarela suave (triste, no sombrío) | zoom, push_up, blur, wipe_up, dissolve |

Todos: 1080×1920, H.264 yuv420p, 191 frames a 24 fps (7,958 s), sin audio, 4–5 MB, bucle perfecto. Nada se ha subido a Spotify ni se probó en un teléfono.

## Pendiente
- **"Yo siento amor infinito por ti"** (la letra se corrigió el 2026-10-29; el archivo `Canciones\Yo siento amor infinito por ti.md` del vault ya es la buena). Concepto propuesto y **sin aprobar**: diorama de papel recortado en capas, 5 planos (prado y brisa → flor con lluvia → ave que susurra al atardecer → figura dormida con silueta de pétalos → brote en el desierto, horizonte infinito); transiciones zoom, wipe_right, blur, light, dissolve. No se generó ninguna imagen.
- Probar los Canvas en la app móvil y subirlos (nada está verificado por Spotify; las disolvencias y transiciones no están avaladas oficialmente, solo el corte duro).
- Los videos anteriores a la función de transiciones usan solo disolvencia; no se rehicieron (decisión del usuario).

## Cómo retomar
1. Leer `skills/spotify-canvas/SKILL.md`: puertas de aprobación (1: concepto; 2: fotogramas guardados en `P:\Canciones\audio\wav\love\assets\fotogramas\<slug>\` y aprobados antes de renderizar), transiciones (apartado 2b), ubicaciones fijas (paso 0) y lecciones.
2. Letras: `C:\Users\jpmar\OneDrive\Documents\Obsidian Vault\Canciones\<Título>.md` (sin buscar en el disco).
3. ComfyUI: `D:\ComfyUI` (`.venv\Scripts\python.exe main.py --listen 127.0.0.1 --port 8188 --lowvram`). Comprobar antes que el puerto 8188 esté libre.
4. Generar con `skills/spotify-canvas/scripts/gen_scenes.py <scenes.json> <carpeta> [metrics.csv]`, revisar, renderizar con `animate_scenes.py <render.json> <salida.mp4>`.

## Mapa de `canvas/`
- `work2/` y `work_sirena/`, `work_lluvia/`, `work_yantd/`, `work_tambien/`: PNG de cada plano, `scenes.json` (prompts y semillas), `render.json` (cámara, halos, transiciones) y `hoja.jpg` (hoja de contacto). `work_yantd/` es "Ya no te dejaré"; `work2/` es "Los postes…" v2; `work/` es el intento v1 (un solo plano).
- `v_prev/`: imágenes descartadas (corruptas, con nieve, fogata chica, etc.), útiles para ver qué se corrigió.
- `out/`: copias locales de los MP4 entregados (ignorados por git, `*.mp4`).
- `metrics/`: tiempos (`*_metrics.csv`, `canvas2-metricas.md`, `correccion2-metricas.md`).
- Excluidos de git: `raw.bin` (volcados de video intermedios de ~80 MB), logs de ComfyUI y archivos de tiempo sueltos.

## Métricas (tiempo de reloj)
- Imagen: ≈ 60–70 s cada una (z_image_turbo en RTX 3050 6 GB, `--lowvram`); render de 191 frames: 142–170 s.
- Postes v2: 680 s (11,3 min, con 3 correcciones). Canto de sirena: 537 s (8,9 min). Las correcciones tras el render cuestan 5–8 min cada una, de ahí la puerta de aprobación previa.
- Lluvia, Ya no te dejaré y También estuve a punto: el tiempo total fue mucho mayor por incidentes (ver abajo) y por varias rondas de cambios de concepto/estilo pedidas por el usuario; los CSV `lluvia_metrics.csv`, `yantd_metrics.csv` y `tambien_metrics.csv` solo registran los tiempos de cada imagen.

## Incidentes y lecciones (resumen; detalle en el skill)
- Un ComfyUI ajeno ocupaba el puerto 8188 (15 GB de RAM) y saturaba la GPU; mi servidor no arrancó y las imágenes salieron corruptas (ruido de colores que ignora el prompt). Tras apagar todo no mejoró; **reiniciar el PC lo arregló**. Si vuelve: arrancar el propio servidor en otro puerto (`COMFY_API`) y reiniciar si persiste.
- Interpretar las letras con fidelidad: "postes" = pilares de obra; "enero, sin hielo" = sin nieve; quién espera a quién; personajes sin rostro nítido; no ilustrar autolesión ("tirarme yo"); canciones de un álbum con entornos y estilos distintos.
- Autorrevisar los fotogramas contra lo prometido (corbata, objetos de otra escena, figura lejos de bordes) y mostrarlos al usuario antes de renderizar.

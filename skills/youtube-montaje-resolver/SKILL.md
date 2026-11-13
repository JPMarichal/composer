---
name: youtube-montaje-resolver
description: Montar el video musical de YouTube en DaVinci Resolver (versión gratuita) a partir de las imágenes aprobadas, el audio y letra.srt, generando un FCPXML con cortes, audio, movimientos (zoom/paneo con keyframes) y títulos de la letra, que se importa con File > Import > Timeline. Activar cuando se pida "montaje", "montar el video", "Resolver", "timeline" o tras terminar las imágenes con skills/youtube-imagenes. Camtasia queda solo como respaldo.
---

# Montaje en DaVinci Resolver

Herramienta oficial de montaje del canal: **DaVinci Resolver gratuito** (no Studio, así que sin API de scripting externa). Camtasia solo de respaldo. El montaje se entrega como **FCPXML** que el usuario importa; no se maneja la interfaz de Resolver.

## Entradas
- `youtube/<cancion>/PLAN.md`: tabla con filas `| n | \`id_escena\` | entra | sale | dur | letra | imagen | movimiento | transición |` (tiempos `m:ss.s`). Lo produce el skill `youtube-imagenes`.
- `youtube/<cancion>/letra.srt` (alineada con `scripts/align-lyrics.py`).
- Audio WAV y carpeta de imágenes aprobadas.

## Pasos
1. Copiar las imágenes a una subcarpeta `montaje_imgs/` de la carpeta de fotogramas **con nombres SIN números** (`01_marco_vacio.png` → `foto_marco_vacio.png`). Ver «Trampas».
2. Copiar `scripts/build_fcpxml.py` a `youtube/<cancion>/` y ajustar las constantes del inicio (`AUDIO`, `IMGS`, `FPS`). Ejecutarlo desde esa carpeta con el Python de `D:\myapps\audio-venv` (usa `wave` de la biblioteca estándar). Produce `montaje.fcpxml`.
3. Validar el XML (`xml.dom.minidom`) y copiarlo junto a las imágenes.
4. El usuario: borra timeline y clips offline previos, *File > Import > Timeline…* y elige el XML.

## Script genérico por tabla (recomendado)
`scripts/build_fcpxml_tabla.py` toma `tabla.json` (`id` y `t` por imagen, el de `v_narrativa/`), la carpeta de imágenes `<id>.png`, el audio y `letra.srt`; copia las imágenes con nombres sin números y genera el FCPXML. Con `--trans transiciones.json` añade **Cross Dissolve** entre planos (duración por corte), movimiento con *ease*, fundido a negro final y **marcadores** en la línea de tiempo en los cortes que piden otra transición (Push Up, Brightness Flash, Zoom In and Out, Blur Dissolve, iris), porque esas no se importan por XML. Se generan dos archivos: uno solo con cortes (seguro) y otro con transiciones y marcadores. Ejemplo y cortes en `youtube/mentira-que-te-menti/v_narrativa/` (`transiciones.json`, `TRANSICIONES.md`).

## Qué genera el script
- Secuencia 1920×1080 a 24 fps con cortes duros contiguos tomados de `PLAN.md` (ajustados a cuadros) y el audio en la pista de audio.
- Movimiento por plano según la columna «Movimiento» (zoom-in, zoom-in lento, zoom-out, pan izq→der, pan der→izq, pan hacia arriba), con keyframes de escala y posición, escala máxima 1,05.
- Títulos de la letra (uno por línea del `.srt`) y un título inicial con el nombre de la canción (1,0–4,5 s), blancos con sombra, abajo en el cuadro.
- No incluye transiciones (disolvencias, cortinas): los cortes son directos y el plan dice cuál va en cada punto.

## Trampas aprendidas (2026-11-06)
- **Nombres con números → «Media offline».** Resolver trata archivos como `01_x.png`, `02_x.png` como secuencia de imágenes. Usar nombres sin dígitos.
- **Imágenes fijas con `duration="0s"`** en el `<asset>`. Con `3600s` Resolver las toma por secuencia de 86 400 cuadros y las pierde o las muestra un instante.
- **Títulos:** la posición como `<param name="Position">` se ignora; funciona `<adjust-transform position="0 -38"/>` dentro de `<title>` (y `start="0s"`). Si salen mal, bajar *Position Y* de toda la pista V2 en el Inspector.
- **Títulos con `<adjust-blend>` (fundido de opacidad con keyframes) desaparecen** al importar en Resolver (2026-11-13). Dejarlos sin fundido (`--fade-titulos` queda apagado). Las transiciones Cross Dissolve, el *ease* de los keyframes de movimiento, los marcadores y el fundido a negro final del último plano sí se importaron bien.
- **Rutas:** `file:///P:/...` con espacios y tildes codificados; el audio y las imágenes deben estar accesibles en `P:`.
- El audio se ata como clip `lane="-1"` al primer plano con la duración completa.
- Usar `chr(10)` o listas para unir líneas al generar el XML por script; los escapes `\n` dentro de f-strings se rompen al editar con heredocs.

## Referencia de transiciones y animaciones
Inventario completo de las transiciones de Resolver (Dissolve, Iris, Motion, Shape, Wipe, Fusion, audio), sus parámetros, Dynamic Zoom, keyframes, títulos y velocidad, con el mapa hacia la columna «Transición» de `PLAN.md`: `references/transiciones-y-animaciones.md`.

## Pendiente de mejorar
- Transiciones (disolvencia, zoom cruzado, destello) automáticas.
- Exportar también el render final (Deliver) con presets de YouTube 1080p.
- Parametrizar el script por línea de comandos en vez de editar constantes.

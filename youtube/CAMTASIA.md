# Camtasia: notas para montar videos de canción (investigación 2026-10-30)

Fuentes: tutoriales de TechSmith (transiciones, behaviors, animaciones, efectos), guía de exportación de UW-Madison (Camtasia 2024), página de codificación de YouTube. La búsqueda no devolvió la lista completa de transiciones ni efectos: **confirmar los nombres en las pestañas del propio programa**.

## Qué ofrece (confirmado)
- **Transiciones:** más de 175, desde fundidos y disolvencias hasta cortinas (wipe), empujes (push) y efectos estilizados (pasar página, ondas). Se arrastran entre dos clips en la línea de tiempo.
- **Animaciones** (pestaña Animations): zoom-n-pan y animaciones propias con fotogramas clave sobre escala, posición, rotación y opacidad. Es la herramienta para el Ken Burns (deriva lenta).
- **Behaviors:** animaciones prefabricadas con entrada / durante / salida para texto, imágenes y medios. Útiles para títulos y versos del coro.
- **Efectos visuales:** están en pestañas a la izquierda del editor (no verifiqué cuáles hay para desenfoque o viñeta).
- Camtasia 2026 añade colecciones de animaciones personalizables y mejor soporte de Lottie.

## Ajustes sugeridos (a verificar en el programa)
- **Proyecto:** 1920×1080. Fotogramas: 24 o 30 fps; YouTube pide subir con la tasa con la que se creó el video.
- **Exportar:** Export > Local File > MP4 (H.264, bitrate variable). YouTube recomienda 8 Mbps o más a 1080p (24–30 fps) y audio AAC 384 kbps estéreo, 48 kHz. Camtasia por defecto usa bitrate variable.
- **Audio:** importar el WAV maestro, no un MP3.
- **Aviso:** las guías de Camtasia que encontré son genéricas (cursos e institucionales); la documentación oficial de exportación para música no apareció.

## Receta para el piloto (Ken Burns y transiciones)
- Cada imagen: 1920×1080 (reescalada desde 1280×720). Zoom máximo ≈ 110 %.
- Alternar sentido: zoom-in, zoom-out, panorámica izquierda y derecha. No repetir el mismo movimiento en planos consecutivos.
- Transición por defecto: fundido / disolvencia larga (≈ 1–1,5 s). Variar con 2 o 3 más (cortina suave, empuje) siguiendo el paso narrativo del skill de Canvas. Evitar destellos y cortes bruscos.
- Duraciones: 10–18 s la mayoría; sincronizar los cambios con el inicio de cada sección y con el pulso.
- Subtítulos: no quemar la letra; subir `.srt` a YouTube.
- Pantalla final (últimos 15–20 s): plano calmado (el 17), sin texto.

---
name: youtube-imagenes
description: Producir las imágenes (no video) para el video musical de una canción en YouTube del canal JPMarichal: concepto por secciones de la letra, 12–17 ilustraciones 16:9 con ComfyUI (z_image_turbo), revisión con hoja de contacto, aprobación del usuario, portada/miniatura con cover.py y entrega para montar en Camtasia (Ken Burns + transiciones). Activar cuando se pida "imágenes para YouTube", "video de la canción en YouTube", "portada", "miniatura" o continuar el piloto "Trae contigo la lluvia". NO genera video; para el Canvas vertical de Spotify usar skills/spotify-canvas.
---

# Imágenes para el video musical de YouTube

**Diferencia clave con el Canvas de Spotify:** aquí **no se genera ni se renderiza video**. El producto de este skill son **imágenes 16:9 aprobadas** (más portada y miniatura). El movimiento (zoom/pan, transiciones) y el montaje con el audio los hace después **Camtasia** (o ffmpeg), no código propio. Un video de 4 min con el renderizador del Canvas tardaría ≈ 75 min; con imágenes + Camtasia son ≈ 20 min de generación y el resto es montaje.

Documentos hermanos (leer antes de trabajar):
- `youtube/ESTRATEGIA.md`: investigación y decisiones.
- `youtube/CAMTASIA.md`: receta de montaje.
- `youtube/METADATOS-v2.md`: títulos, descripciones y créditos.
- `youtube/cover.py`: portada y miniatura.
- `youtube/trae-contigo-la-lluvia/`: piloto con 17 imágenes, `scenes.json`, `hoja.jpg` y `metrics.csv`.
- `skills/spotify-canvas/SKILL.md` y `canvas/ESTADO.md`: método y lecciones de generación de imágenes.

## Decisiones ya tomadas (no reabrir sin el usuario)
- Formato "D" de la estrategia: **escenas secuenciales sin loop**, una por sección de la letra, con un motivo central que vuelve en los coros. 12–16 escenas de 10–18 s para una canción de ~4 min (el piloto salió con 17).
- 16:9. Generar a **1280×720** y reescalar a 1920×1080 en el montaje. Dejar la **zona inferior calmada y sin detalle** (22 % inferior = controles del reproductor) y el 12 % superior libre.
- Sin video generativo. Sin letra quemada en imágenes ni video: la letra va en `.srt` y en la descripción. Título discreto de 3–4 s al inicio, como máximo.
- Estilo, paleta y transiciones **distintos por canción** (la política de contenido "no auténtico" de YouTube castiga lo plantillado).
- Textos públicos: **no nombrar herramientas** (Suno, ACE Studio, ComfyUI, etc.); español de México. Créditos: "producido con herramientas de IA bajo su dirección" y "Este video usa contenido generado o alterado con IA".

## Flujo

### 0. Ubicaciones y datos
- Letra: `C:\Users\jpmar\OneDrive\Documents\Obsidian Vault\Canciones\<Título>.md`. Ruta directa: **no buscar en el disco**; si el nombre no coincide, listar solo ese directorio.
- Audio maestro (WAV): `P:\Canciones\audio\wav\love\<Título>.wav` (ruta directa). Mapa de pulso y secciones con librosa, que vive en un entorno aparte, `D:\myapps\audio-venv` (el Python del sistema no lo tiene): `D:\myapps\audio-venv\Scripts\python.exe scripts/audio-sections.py "<wav>" [n_secciones]` imprime duración, tempo, compás y una tabla de secciones; `just audio-analyze "<wav>"` ya usa ese entorno. Para repartir cortes, ajustar cada cambio de imagen al pulso más cercano; pasar a Claude solo la tabla de tiempos. Si el entorno falta: `uv venv D:\myapps\audio-venv --python 3.12` y `uv pip install --no-cache --python D:\myapps\audio-venv\Scripts\python.exe librosa soundfile` (tras un reinicio brusco la caché de uv puede quedar corrupta; `--no-cache` lo evita). **Alineación letra-audio (obligatoria antes de la tabla de cortes):** repartir las escenas en partes iguales desfasa imagen y significado. `stable-ts` está instalado en el mismo entorno (PyTorch solo CPU; ≈ minutos con el modelo medium): `D:\myapps\audio-venv\Scripts\python.exe scripts/align-lyrics.py "<letra.md>" "<wav>" youtube/<slug>/letra.srt medium` escribe `letra.srt` (+ `.json`) con un subtítulo por renglón, en UTF-8 **con BOM** (sin BOM Camtasia lo lee como ANSI y rompe á, é, ñ). Sobre la mezcla completa los versos salen bien; en estribillos repetidos o con interludios los tiempos de cada renglón no son fiables (un renglón puede ocupar 30 s): ahí usar las secciones de `audio-sections.py`. Construir la tabla con la columna «qué dice la letra» y cortar cada imagen donde empieza su frase, ajustado al pulso. Con la voz aislada (stems) la alineación mejora.
- Fotogramas para aprobación: `P:\Canciones\audio\wav\love\assets\fotogramas\<slug>\`. Portada y miniatura finales: `P:\Canciones\audio\wav\love\assets\youtube\<slug>\`. Trabajo: `youtube/<slug>/`.

### 1. Concepto (puerta 1: aprobar antes de generar)
1. Leer la letra completa y dividirla en secciones (verso, coro, puente...). Una escena (o dos) por sección; el coro regresa al motivo central con variación, como la letra.
2. Traducir cada sustantivo clave a una descripción visual inequívoca y **comprobar cada elemento contra una frase de la letra** (clima, estación, quién espera a quién, objetos). Personajes **sin rostro nítido** (de espaldas, silueta, manos), con edad, rasgos y atributos fijos (vestuario) repetidos en todos los prompts.
3. Temas sensibles (autolesión, muerte): no ilustrarlos ni sugerirlos; esperanza realista.
4. Elegir estilo y paleta propios de la canción, con arco de color si la letra tiene arco (p. ej. sequía ocre → lluvia esmeralda), distintos de las demás canciones del álbum.
5. Presentar al usuario: interpretación, lista de escenas (qué se ve, encuadre), paleta y estilo, qué se evita. **Esperar su aprobación.** No arrancar ComfyUI antes.
6. El primer borrador de prompts puede hacerlo un modelo local (`mistral:7b` o `gemma4`) con el prefijo de estilo fijo; Claude solo lo revisa.

### 2. Generar (solo imágenes)
- `scenes.json` como en el piloto: `{"style": "<prefijo común>", "width": 1280, "height": 720, "scenes": [{"id": "01_nombre", "seed": N, "prompt": "..."}]}`. Cada prompt: paleta + sujeto + encuadre ("horizon one third down", "lower third calm, little detail") + negaciones ("no text", "face not visible").
- Ejecutar: `python skills/spotify-canvas/scripts/gen_scenes.py youtube/<slug>/scenes.json youtube/<slug>/imgs youtube/<slug>/metrics.csv`. Solo genera lo que falta; para repetir una escena, mover su PNG a `v_prev/`. Usa ComfyUI en `http://127.0.0.1:8188` (variable `COMFY_API` para otro puerto).
- Tiempo: ≈ 65 s por imagen en la RTX 3050 de 6 GB con `--lowvram`; 17 imágenes ≈ 19 min. 0 tokens de Claude mientras se generan.
- **Entorno ComfyUI:** `D:\ComfyUI`, arranque con `.venv\Scripts\python.exe main.py --listen 127.0.0.1 --port 8188 --lowvram`.
  - Antes de arrancar, comprobar que el puerto 8188 esté libre. Si otro ComfyUI lo ocupa, no matarlo sin permiso del usuario: arrancar el propio en 8189 (`COMFY_API=http://127.0.0.1:8189`). Dos servidores a la vez saturan la GPU (10 min por imagen).
  - Si las imágenes salen como ruido de colores que ignora el prompt (misma imagen para la misma semilla), la GPU o el entorno están en mal estado: **reiniciar el PC** lo arregló.

### 3. Revisión (puerta 2: autorrevisión + aprobación del usuario)
- a) **Autorrevisión de Claude con UNA hoja de contacto** (cuadrícula con PIL; no abrir 17 imágenes sueltas, es lo que ahorra tokens). Abrir sueltas solo las dudosas. Lista por imagen:
  - elementos de la letra presentes y bien interpretados;
  - atributos fijos del personaje (vestuario, edad);
  - objetos de otra escena colados (el prefijo de estilo no debe llevar objetos de una escena);
  - sin texto, cables, troncos ni artefactos de IA;
  - zona inferior calmada;
  - **lo prometido al usuario se cumple** (p. ej. figura lejos de bordes).
  Lo que falle: mover el PNG a `v_prev/`, corregir el prompt (con negaciones) y regenerar solo esa escena. Un lote corrupto se ve de un vistazo.
- b) **Canal principal de revisión = la carpeta, no el chat:** copiar los PNG aprobados por la autorrevisión y `hoja.jpg` a `P:\...\fotogramas\<slug>\` y decirle la ruta al usuario, para que revise con independencia de la interfaz de la IA. Esperar su visto bueno: **no pasar al montaje sin él**.

### 4. Portada y miniatura
`python youtube/cover.py <imagen.png> "<Título>" <carpeta_salida> [--author JPMarichal]` genera `portada_1920x1080.png` y `miniatura_1280x720.png`. Zonas seguras: 12 % superior y 22 % inferior libres, márgenes laterales ≥ 8 %, título centrado al 58 %. Elegir una escena **oscura o con el sujeto fuera del centro**: el título se dibuja centrado y tapa lo que haya ahí, y el nombre del autor no se lee sobre fondos claros (en "Yo siento amor infinito por ti" el amanecer fallaba y la escena nocturna funcionó). Revisar siempre portada y miniatura a la vista. Miniatura con ≤ 3–5 palabras. El usuario aprueba antes de publicar.

### 5. Montaje (fuera de este skill; ver `youtube/CAMTASIA.md`)
- Proyecto 1920×1080 a 24 fps; importar el **WAV maestro**. Cada imagen a 1920×1080 con zoom máximo ≈ 110 %, alternando zoom-in, zoom-out y panorámica izquierda/derecha (no repetir el mismo movimiento en planos consecutivos).
- 10–18 s por imagen, con los cambios en el inicio de cada sección y al pulso. **Primeros 15 s con movimiento visible** desde el cuadro 0 (nada de negro ni título largo).
- Transiciones: disolvencia larga (≈ 1–1,5 s) por defecto y 2–3 variantes elegidas por el paso narrativo (cortina suave, empuje, zoom cruzado), como en `skills/spotify-canvas/SKILL.md` apartado 2b. Sin destellos ni cortes bruscos. Pantalla final de 15–20 s con un plano calmado y sin texto.
- Letra: subtítulos `.srt` generados en el paso 0 con `scripts/align-lyrics.py` (no quemada). En Camtasia se importan al panel Subtítulos; el `.srt` debe ir en UTF-8 **con BOM** o los acentos salen rotos. Probado con "Yo siento amor infinito por ti": el usuario confirmó que los tiempos encajan con el audio sobre la mezcla completa, sin aislar la voz. Camtasia inserta entradas «Subtítulo en blanco» en los silencios: es normal.
- Exportar MP4 H.264 High, 4:2:0, `+faststart`, BT.709, ≥ 8 Mbps a 1080p (24–30 fps); audio AAC-LC 48 kHz a 384 kbps. Verificar con `ffprobe`. Los nombres de transiciones y ajustes de exportación de Camtasia hay que **confirmarlos en el propio programa**: la investigación no los verificó.

### 6. Metadatos y publicación
Título "Canción – Artista"; descripción con párrafo inicial, letra completa, créditos (sin nombres de herramientas) y aviso de IA; plantillas en `youtube/METADATOS-v2.md`. La etiqueta de "contenido alterado o sintético" normalmente no se exige para ilustración y música original, pero verificar el texto oficial al subir. Medir en YouTube Studio la retención a los 30 s y la duración media de visualización: es la única forma de saber qué formato funciona.

## Métricas de referencia (piloto "Trae contigo la lluvia")
17 imágenes de 1280×720 en ≈ 19 min (60–70 s cada una), registradas en `youtube/trae-contigo-la-lluvia/metrics.csv`.

## Pendientes conocidos
- Confirmar duración real y secciones de "Trae contigo la lluvia" con el audio.
- Decidir con el usuario "con letra" o "sin letra" para la siguiente canción y comparar en Studio.
- El resto del repertorio se publica por etapas; cada canción nueva repite este flujo con un estilo distinto.

## Prueba del flujo: "Yo siento amor infinito por ti" (2026-10-30)
Primera canción hecha con este skill, de forma autónoma por ausencia del usuario (puertas 1 y 2 diferidas: concepto autoaprobado, fotogramas guardados para su revisión). Resultado en `youtube/yo-siento-amor-infinito/`: `PLAN.md` (tabla de cortes alineada con la letra, movimientos, transiciones, metadatos borrador), `letra.srt`, `scenes.json`, `imgs/` (14 escenas), `hoja.jpg`, `cover/`. Estilo propio de la canción: diorama de papel recortado en capas, arco de color verde/oro → plata → ocre → rosa/lavanda → índigo, motivo del almendro en flor. La autorrevisión con hojas de contacto de 6 imágenes detectó 2 fallos (flor ausente, árbol con rosas que rompía el motivo) que se regeneraron antes de guardar. 14 imágenes + 2 regeneradas ≈ 16 min.

Resultado confirmado por el usuario: la letra alineada encaja y la tabla de cortes rehecha con ella es la base del montaje. Lección: el primer plan repartió las 14 escenas en partes iguales y el usuario comprobó en Camtasia que no era realista (imágenes desfasadas de su significado). Se rehízo con `letra.srt`.

## Prueba 2: "Mentira que te mentí" (2026-10-31)
Segunda canción hecha de forma autónoma con el flujo completo (alineación incluida). Resultado en `youtube/mentira-que-te-menti/` (PLAN.md, scenes.json, imgs/, letra.srt, hoja.jpg, cover/, cover_alterna/), con copia en `P:\Canciones\audio\wav\love\assets\fotogramas\mentira-que-te-menti\` (17 PNG + hoja.jpg + `letra.srt`) y en `P:\Canciones\audio\wav\love\assets\youtube\mentira-que-te-menti\` (portada y miniatura). Estilo propio: cartel mexicano serigrafiado, coral/turquesa/mostaza/índigo, motivo del clavel. Lecciones:
- **El `.srt` va en la carpeta de fotogramas**, junto a las imágenes (petición del usuario).
- **Variaciones del estribillo:** con la alineación real, los estribillos repetidos ocupan mucho tiempo. Generar de entrada una variante de la escena del estribillo por cada repetición (misma composición, luz y actitud distintas: mediodía, tarde, crepúsculo, noche) en vez de repetir una imagen o dejar una 40 s; aquí 4 escenas de estribillo para 6 repeticiones y 3 variantes extra.
- **Detalles que la autorrevisión debe buscar:** reflejos (espejos, vidrios) que dibujan una cara; cintas, carteles o libros que generan «letras» sin sentido (poner «no letters, no writing, no symbols» en el prompt); pareja en abrazo que muestra los dos perfiles; mechones de pelo que cambian el género de un personaje.
- **Carrera al regenerar:** si hay un lote corriendo, no mover PNG a `v_prev/` ni editar prompts hasta que termine; el generador regenera lo que falta con el prompt que leyó al inicio y la imagen vuelve idéntica. Esperar el fin del lote, mover, y lanzar uno nuevo.
- **Portada:** el título centrado tapa el sujeto aunque se elija una escena con la pareja abajo; revisar siempre y, si no convence, componer a mano o elegir una escena con el centro vacío.
- Tiempos: 17 imágenes + 7 regeneraciones ≈ 25 min; alineación (CPU, medium) ≈ 4 min para 3:18 de audio.

### Corrección de la prueba 2 (2026-10-31): el estilo debe salir de la música
La primera versión de "Mentira que te mentí" (cartel mexicano serigrafiado, 17 imágenes) se descartó: el estilo se eligió solo con la letra y la canción no es regional. Archivada en `youtube/mentira-que-te-menti/v1_mexicana/` y en `v1-descartada/` de la carpeta de fotogramas. Reglas nuevas:
- **Antes del concepto, pedir al usuario el prompt de estilo de la canción (género, instrumentos, voz, ambiente) y leerlo junto al análisis de audio.** Letra sola no basta para decidir el estilo visual. Si no hay prompt, preguntar; no suponer (ni lo regional).
- **Tempo con hemiola:** `audio-sections.py` puede dar 117,5 BPM; mirar la autocorrelación del onset (picos a 172, 117 y 86 BPM = groove de drum and bass a medio tiempo con 3 contra 4). No concluir 6/8 sin comprobarlo.
- **Cuando la letra tiene muchos símbolos/metáforas** (más de ≈ 10), usar estilo onírico/surrealista (imágenes no razonables, lógica de sueño) y **más imágenes: ≈ 30** para ≈ 3 min (una por pareja de versos; mínimo ≈ 5 s por imagen). El estilo puede no ser ilustración: aquí fue fotografía cinematográfica de sueño.
- **Un motivo recurrente que cambia de papel en cada escena** (aquí, una cinta magnética ámbar con media torsión: trenza, escalera, humo, voz, lazo) ordena el exceso de símbolos. Proponerlo al usuario; descartó el primero (una gota) y aprobó el segundo.
- **Recurso estructural con la idea de la canción:** la mentira como glitch. `youtube/glitch.py` aplica por código, con un nivel 0–5 por escena (`"glitch"` en `scenes.json`), copia fantasma, color separado, franjas corridas, líneas de barrido, grano y viñeta; el nivel baja a lo largo de la canción y la última imagen queda alineada. Entrega: `final/` (con glitch) e `imgs/` (limpias). Ventaja: las variantes de estribillo salen de la misma base con otro nivel.
- **Rostros:** en el estilo fotográfico fallan más (parejas abrazadas, manos tras un cristal). Pedir en el prompt "only seen from behind / only hands visible, no faces" y revisar siempre.
- **Flujo seguido:** concepto → lista de 30 con tiempos y glitch → aprobación → generar → autorrevisión con hojas de 12 (4×3) → regenerar fallos → `glitch.py` → portada (el título centrado cabe si el sujeto queda arriba y abajo) → copia a la carpeta de fotogramas (imágenes finales + `limpias/` + `hoja.jpg` + `letra.srt`).


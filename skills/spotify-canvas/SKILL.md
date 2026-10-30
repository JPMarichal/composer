---
name: spotify-canvas
description: Crear el Canvas de Spotify (video vertical en loop de ~8 s) de una canción a partir de su letra: imaginar la escena, generar una ilustración limpia con modelos locales (ComfyUI + z_image_turbo), animarla en código (luz, cámara, partículas) con loop matemáticamente perfecto y validar los requisitos de Spotify. Activar cuando se pida "canvas", "canvas de Spotify", "video loop para la canción" o un clip vertical corto para una canción del catálogo. Escrito para que cualquier agente (Claude, GPT, Gemini, local) lo ejecute con solo shell y lectura de archivos.
---

# Spotify Canvas desde la letra

Resultado: un MP4 vertical, H.264, sin audio, en bucle, atractivo y aceptado por Spotify.
Caso de referencia: "Los postes de la calle central" (`examples/`). El método final (sección 3) salió de un intento fallido (sección 7); no repetirlo.

## 1. Requisitos de Spotify (qué es oficial y qué no)

| Dato | Valor | Fuente |
|---|---|---|
| Aspecto | 9:16 vertical | Oficial |
| Duración | 3–8 s | Oficial |
| Formato | MP4 (o JPG) | Oficial |
| Alto | "720–1080 px" | Oficial pero ambiguo |
| Tamaño en MB | **No publicado** | Terceros dicen 8–200 MB, sin respaldo |

Decisiones y por qué:
- **1080×1920.** El texto oficial leído literal daría 576×1024, pero los creadores reportan que 720×1280 (mínimo) y 1080×1920 (recomendado) suben bien. Manda la práctica.
- **7,958 s (191 frames a 24 fps), nunca 8,000 exactos.** Dos fuentes independientes reportan rechazo con 8,00 s.
- **Tamaño ≤ 15 MB** (margen propio, no oficial; el caso de referencia pesó 3 MB). Hubo un reporte de 17,4 MB rechazado sin motivo claro.
- **Sin pista de audio** (quitarla, no silenciarla), `yuv420p`, `+faststart`.
- Si la subida web falla, probar la app móvil de Spotify for Artists. Los loops solo funcionan en las apps móviles.

Política de contenido (si no, lo retiran): la imagen es el foco; sin ventas ni promoción; sin enlaces ni "síguenos"; sin logo de Spotify ni marcas; sin título ni nombre de artista (ya salen en Now Playing); sin voz cantada, cortes rápidos ni destellos.

Fuentes: support.spotify.com (Canvas guidelines, content policy, fix-spotify-canvas-upload-error), artists.spotify.com/blog (10 tips, canvas-metrics-guide), artist.tools, makecanvas.me, calvinwest.com, renderforest.com.

## 2. Qué hace atractivo un Canvas (aplicar siempre)

- **Una idea visual, un movimiento principal, un reinicio intencional** (Renderforest).
- **Arco completo, aunque sea de 8 s** (Spotify): un principio y un final, no una sola acción repetida. Un joven tallando un poste durante 8 s fue "aburridísimo".
- **Movimiento suave**; sin cortes rápidos ni destellos. Funcionan: luz que se desplaza, empuje lento de cámara, partículas, humo, agua.
- **Zona segura:** lo importante en la mitad superior y al centro; los controles tapan la mitad inferior y algunos teléfonos recortan los bordes.
- **Sin texto.** El texto generado por IA se deforma.
- **Rebote (adelante y atrás) solo si el movimiento se ve bien al revés.** Con luz y cámara sí; con manos, humo o personas no.
- Coherencia con la portada y el perfil del artista; puede actualizarse con el tiempo.
- Cifras de impacto de Spotify (>4× en guardados/añadidos a listas; "hasta 120 % más streams") son internas y máximas, no promesas.

## 3. Método: IA para la ilustración fija, código para el movimiento

**Por qué:** el video generativo de 5B en una GPU de 6 GB produce saltos y artefactos (cables que aparecen y desaparecen, manos deformes). Animar en código da bucle perfecto y cero artefactos, y tarda 1,5 min en vez de 10.

### Paso 0 — Ubicaciones fijas (no buscar en el disco)
**Servidor ComfyUI:** antes de arrancarlo, comprobar si el puerto 8188 ya está en uso (`curl http://127.0.0.1:8188/system_stats`). Un servidor ajeno o saturado de RAM produjo imágenes corruptas (bandas y ruido); si ocurre, no tocarlo: arrancar el propio en otro puerto (`--port 8189`) y exportar `COMFY_API=http://127.0.0.1:8189`. Si incluso un servidor único y limpio genera ruido de colores que ignora el prompt (misma imagen para la misma semilla), la GPU/entorno está en mal estado: **reiniciar el PC** lo arregló. Un lote corrupto se detecta de un vistazo en la hoja de contacto: descartarlo entero y regenerar.
Las letras están en el vault de Obsidian; **no hacer búsquedas recursivas en el disco**. Ruta directa:
`C:\Users\jpmar\OneDrive\Documents\Obsidian Vault\Canciones\<Título>.md` (el nombre del archivo es el título exacto; si no coincide, listar solo ese directorio y filtrar por parte del título).
Salidas fijas:
- Video final: `P:\Canciones\audio\wav\love\assets\canvas\<Título>.mp4` (consecutivo " 2", " 3" si el usuario conserva una versión previa).
- Fotogramas para aprobación: `P:\Canciones\audio\wav\love\assets\fotogramas\<slug>\` (puerta 2, ver 3b.5b).
Carpeta de trabajo: `canvas/work_<slug>/`.

### Paso 1 — Leer la letra y extraer fielmente la imagen
1. Leer la letra completa desde la ruta del paso 0.
2. **Interpretar cada palabra clave en su sentido de la letra, no el más común.** Error real: "postes" son "los pilares de una construcción" (la letra lo dice), no postes de luz; y el nombre se **graba**, no se cuelga como etiqueta. Si hay duda, preguntar al usuario.
3. Elegir una imagen con arco: p. ej. una obra de pilares al anochecer que se ilumina uno a uno, hasta reiniciarse.
4. Personajes: edad y rasgos explícitos ("about 20 years old, thick wavy dark hair", "bare-headed") y pequeños en cuadro (silueta de espaldas); evitar rostros y manos en primer plano.
5. Guardar concepto y prompts en `canvas/<slug>.md`.

### Paso 2 — Ilustración limpia
Requisitos del encuadre (se descubrieron a base de fallos):
- Vertical 9:16, estilo ilustración plana/gouache, **sin cables, sin texto, sin detalle fino** que luego no se pueda animar.
- Perspectiva de un punto con el motivo principal (los pilares) en la parte media-alta: indicar en el prompt "horizon line one third down from the top, tall pillars rising to the top edge, wide ground in the lower two thirds". Sin esa instrucción, el modelo puso la acción en el tercio inferior (tapado por los controles).
- Generar con `scripts/gen.py image --width 720 --height 1280 --prompt "..." --seed N`; **mirar la imagen** y repetir con otra `--seed` hasta que sea correcta (en el ejemplo, la 2.ª).

### Paso 3 — Marcar las zonas a animar
Mirar la imagen y anotar, para cada elemento (pilar), un rectángulo `[x0, x1, y0, y1]` en píxeles, **de cerca a lejos**, agrupado por lados. Crear `config.json` (ver `examples/postes.cfg.json` y el docstring de `scripts/animate_light.py`). Dibujar los rectángulos sobre la imagen con Pillow y revisarlos antes de renderizar; la máscara de gris los ajusta al elemento.

### Paso 4 — Renderizar
```
D:\ComfyUI\.venv\Scripts\python.exe skills\spotify-canvas\scripts\animate_light.py config.json salida.mp4
```
(cualquier Python con numpy, Pillow y scipy; ffmpeg en el PATH). Genera 191 frames a 1080×1920 con: ola de luz ámbar que recorre los elementos de lejos a cerca (el "arco"), empuje de cámara que vuelve al inicio, respiración del horizonte, estrellas que titilan y brasas ascendentes. **Todo es periódico en el número de frames**, así que el último enlaza con el primero. Los trucos: fases enteras (`sin(2π·m·u)`), y partículas con alfa 0 en el punto de reinicio.

### Paso 5 — Verificar
- Hoja de contacto: `ffmpeg -i v.mp4 -vf "select='eq(n,0)+eq(n,50)+eq(n,100)+eq(n,150)',scale=360:640,tile=4x1" -frames:v 1 sheet.png` (los mosaicos se ven pegados; no confundir con el contenido). Mirar también un fotograma a tamaño completo.
- Bucle: comparar la diferencia media entre el frame 190 y el 0 con la mediana entre frames consecutivos; deben ser del mismo orden (en el ejemplo, 0,77 vs 0,59).
- `ffprobe`: 1080×1920, `h264`, `yuv420p`, 191 frames, 7,958 s, sin stream de audio, tamaño ≤ 15 MB.

### Paso 6 — Entregar
Enviar el MP4 al usuario para que lo vea. **Pedir confirmación antes de sobrescribir** un archivo existente en `P:\Canciones\audio\wav\love\assets\canvas\<Título>.mp4` (nombre = título de la canción).

## 3b. Variante multiescena (onírica, para más engagement)

Cuando se pida "multiescena" o se quiera más ritmo que un solo plano. Caso: "Los postes de la calle central" v2 (`examples/multiescena.*`).

0. **Puerta 1: aprobar el concepto visual, antes de generar nada.** Presentar al usuario en texto: qué dice la letra (interpretación de las palabras clave), el arco, la lista de planos (qué se ve, encuadre, personaje y atributos fijos como vestuario), paleta/estilo y qué se evita explícitamente. Esperar su aprobación o correcciones; no arrancar ComfyUI ni generar imágenes hasta tenerla.
1. **Imaginar 4–5 planos que cuenten la letra**, de lo general a lo íntimo y de vuelta: calle (plano general) → acción clave en primer plano (grabar el pilar) → rostro → manos enlazadas → sonrisa → vuelve a la calle. Cada plano ≥ 1,5 s.
2. **Disolvencias largas (≈16 frames) en vez de cortes**: son más oníricas y evitan lo que Spotify desaconseja (cortes rápidos, destellos). Spotify solo avala el corte duro; la disolvencia no está confirmada oficialmente y no se encontró ningún tutorial multiescena. Si el usuario quiere el camino seguro, usar menos planos y más largos.
2b. **Variar las transiciones** (obligatorio para un álbum: en serie, la misma disolvencia en todos los videos resulta monótona). `animate_scenes.py` acepta por plano `"transition"` (cómo pasa AL SIGUIENTE; el último pasa al primero) y a nivel global `"transitions": "auto"` / `"transition_default"`. Tipos: `dissolve`, `zoom` (zoom cruzado), `blur` (sale de foco / se enfoca), `light` (swell suave de luz cálida, nunca destello), `wipe_right|wipe_left|wipe_up` (cortina de borde suave), `push_up|push_left` (el siguiente empuja al anterior). **Elegir según el paso narrativo, no al azar:**
   - plano general → detalle o rostro: `zoom`; detalle → plano general: `dissolve`.
   - recuerdo, sueño, algo que se pierde o se disuelve: `blur`.
   - paso del tiempo, noche → día, revelación, esperanza: `light` o `wipe_up` (hacia arriba = ascenso).
   - llegada, regreso, movimiento en una dirección (camino, viaje): `wipe_right` o `push_left` en la dirección del movimiento.
   - continuar una acción vertical (caída, lluvia, humo que sube): `push_up`.
   - Dentro de un video no repetir la misma transición en uniones consecutivas ni usar más de 3 tipos; entre los videos de un álbum, variar la combinación (`"transitions": "auto"` arranca en un punto distinto según `seed`). Mantener la duración (≈ 16 frames) y evitar `light` y `push` en más de una unión por video. Spotify solo avala el corte duro: todas son criterio propio; verificarlas mirando los fotogramas a mitad de cada unión.
3. **Capas continuas que unan los planos**: bokeh y brasas flotantes, velo cálido y bloom constantes en todo el clip. Son periódicas, así que la costura del bucle (último plano → primero) no se nota.
4. **Mantener coherencia visual** con un prefijo de estilo común en todos los prompts (`style` en `scenes.json`), paleta cálida y la misma descripción del personaje.
5. Pipeline: `scenes.json` (prompts, semillas) → `python scripts/gen_scenes.py scenes.json <carpeta> metrics.csv` (solo genera lo que falta; para repetir una escena, borrar su PNG) → **puerta de revisión (ver abajo)** → `render.json` (zoom, pan y halo por plano) → `python scripts/animate_scenes.py render.json salida.mp4` (~2,5 min).
5b. **Puerta de revisión antes de renderizar (obligatoria).** Dos pasos, en este orden, y no se renderiza hasta completarlos:
   - **a) Autorrevisión de la IA:** abrir cada PNG y contrastarlo con una lista por escena: (1) cada elemento clave de la letra aparece y está bien interpretado; (2) el vestuario/atributos fijos del personaje (corbata, sin sombrero, edad, barba) están visibles; (3) **no hay objetos de otra escena** (p. ej. un farol que solo corresponde al plano del barco, colado en el plano de la sirena; el estilo común puede arrastrarlos: no meter objetos de una escena en el `style`); (4) sin texto, cables, troncos u otros artefactos de IA; (5) lo importante en la mitad superior. Si algo falla, borrar ese PNG, corregir el prompt (con negaciones) y regenerar solo esa escena.
   - **Canal principal de revisión = la carpeta, no el chat:** tras la autorrevisión, guardar SIEMPRE los fotogramas en la carpeta de `fotogramas` (más una hoja de contacto `hoja.jpg`) y decir la ruta al usuario, para que pueda revisarlos con independencia de la interfaz de la IA. El envío por chat es solo un extra.
   - **b) Puerta 2: aprobación del usuario de los fotogramas.** Copiar los PNG que pasaron la autorrevisión a `P:\Canciones\audio\wav\love\assets\fotogramas\<slug>\` (respaldo y lugar donde el usuario los ve; nombres `<id>.png`), mostrarlos (p. ej. con `SendUserFile`) y esperar su visto bueno. Solo entonces ejecutar `animate_scenes.py`. Renderizar antes cuesta ≈ 2,5 min por cada error que el usuario detecte después.
6. Cada imagen: lo importante en la mitad superior. Los planos cerrados (rostro, manos, labios) funcionan bien con ilustración pintada; los labios salen más fotográficos, el bloom y el velo cálido unifican el conjunto.
7. **Verificar el bucle** comparando la diferencia en la costura con la de las demás disolvencias (deben ser del mismo orden; en el ejemplo, 4,2 vs 4–5). La diferencia mediana entre frames es mayor que en un plano único (1,6 vs 0,6) porque las disolvencias cambian toda la imagen.
8. **Métricas:** registrar un `epoch,etapa` por hito (`gen_scenes.py` lo hace para las imágenes) y resumirlo en `canvas/metrics/`. Referencia: 11,3 min (postes v2, con una corrección) y 8,9 min (Canto de sirena, 5 imágenes de ≈ 65 s + 170 s de render). Cada regeneración de una imagen más su re-render cuesta ≈ 4 min.

Lecciones de la v2/sirena (errores de IA que el usuario detectó tras el render): en el plano 3 de "postes" el rostro salió sin corbata (hay que pedir "necktie knotted at the neck and hanging down the shirt front" y encuadrar pecho) y en el plano 3 de "Canto de sirena" apareció un farol flotante heredado del `style` ("warm amber lantern accents"). Ambos se habrían evitado con la puerta 5b.

Lección de temas sensibles ("También estuve a punto"): si la letra alude a autolesión ("a punto de tirarme yo"), **no ilustrarlo ni sugerirlo**: sin acantilados con la figura en el borde, sin caídas; la figura va lejos de cualquier borde, en terreno firme, y el cierre es de esperanza realista. Un lote salió con la figura al borde de un risco aunque el prompt decía "far back from the edge": la autorrevisión debe comprobar lo que se prometió al usuario, no solo la letra. Estilo: cuando se pide "triste pero no sombrío", usar carbón + acuarela suave con paleta rosa/azul-verdoso/ocre y el color creciendo hacia el amanecer; el carbón casi monocromo resultó demasiado sombrío.

Lección de coherencia con la letra (caso "Ya no te dejaré", álbum compartido con "Trae contigo la lluvia"): (1) **no inventar clima ni estación que la letra contradiga**: "en enero, cuando no haya hielo" no admite nieve ni hielo; se rehizo todo sin invierno (cielo que se abre, brote, luz de mañana). Antes de aprobar el concepto, comprobar cada elemento del escenario contra una frase concreta de la letra. (2) **Quién espera a quién** lo fija la letra (ahí ella espera a él; en la otra, él a ella): el personaje que espera va solo en el plano de espera. (3) **Canciones de un mismo álbum deben tener entornos y paletas claramente distintos**; no copiar el escenario de una a otra (río, valle, etc.) salvo que la letra lo diga. (4) Personajes sin rostro nítido: de espaldas, siluetas o rostros ocultos por el pelo.

Lección de fidelidad: la palabra **"postes"** de esta letra son "los pilares de una construcción" **en la calle**, no troncos cortados ni postes de luz. La escena debe mostrar pilares estructurales de madera (de suelo a viga) sosteniendo un edificio en obra, sobre la banqueta de la calle central. Un tocón o tronco cortado, o un poste de luz, es un error. Lo mismo con el vestuario: "disfrazado de traje y corbata" exige la **corbata visible en todos los planos donde aparezca el personaje**. En la v2 del Canvas el plano de grabado salió sin corbata porque el prompt solo decía "hand and forearm"; en planos cerrados de manos o torso, nombrar la prenda explícitamente (p. ej. "dark suit sleeve with a white cuff, a dark tie hanging into frame") y revisarla al mirar cada imagen. Antes de generar, traducir cada sustantivo clave de la letra a una descripción visual inequívoca y repetirla en los prompts (incluidas las negaciones: "not a tree stump, not a cut log").

## 4. Requisitos del entorno (una sola vez)

- GPU NVIDIA con CUDA (probado en RTX 3050 6 GB). ffmpeg/ffprobe y Python 3.
- ComfyUI en `D:\ComfyUI` con `.venv` de uv; modelos enlazados desde `D:\myapps\ai-models\comfyui-models`: `diffusion_models/z_image_turbo_nvfp4.safetensors`, `text_encoders/qwen_3_4b_fp8_mixed.safetensors`, `vae/ae.safetensors`.
- Arrancar el servidor y esperar a que responda; **detenerlo al terminar** para liberar la GPU:
  ```
  cd D:\ComfyUI && .venv\Scripts\python.exe main.py --listen 127.0.0.1 --port 8188 --lowvram
  ```
  (`--lowvram` es obligatorio con 6 GB; tras un reinicio del equipo el servidor hay que relanzarlo.) Tiempo de la ilustración: ~4 min a 720×1280.
- Solo para la vía opcional del video generativo (sección 6): nodo ComfyUI-GGUF (`git clone https://github.com/city96/ComfyUI-GGUF` en `custom_nodes` + `uv pip install --python <python del venv> gguf`; el venv no trae pip), `unet/Wan2.2-TI2V-5B-Q4_K_M.gguf`, `text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors`, `vae/Wan2.2_VAE.pth`. Es código de terceros: pedir autorización antes de instalarlo.

## 5. Checklist final

- [ ] La escena respeta el sentido real de la letra (palabras clave bien interpretadas)
- [ ] Tiene arco (principio → cambio → reinicio), un movimiento principal
- [ ] 9:16, 1080×1920; 3–7,96 s (nunca 8,000 exactos); H.264 `yuv420p`; sin audio; ≤ 15 MB
- [ ] Sin texto, logos ni promoción; lo importante arriba/centro
- [ ] Bucle sin salto (diferencia del seam similar a la de frames consecutivos)
- [ ] Concepto visual aprobado por el usuario antes de generar (puerta 1); fotogramas respaldados en `P:\...ssetsotogramas\<slug>\`
- [ ] Imágenes autorrevisadas por el agente (lista del paso 5b) **y aprobadas por el usuario antes de renderizar**
- [ ] Revisado visualmente por el agente y aprobado por el usuario antes de sobrescribir nada

## 6. Vía opcional: video generativo (solo para movimiento sutil)

`scripts/gen.py video --image <png en ComfyUI/input> --prompt "..."` (Wan2.2 TI2V 5B, 97 frames a 448×800, ~9,5 min) y `scripts/make-canvas.ps1 -Clip <clip.mp4>` (rebote + 1080×1920 + 191 frames + validación). Usar solo para escenas con poco detalle y movimiento reversible (humo, agua, tela). **No** para personas ni escenas con cables, manos o texturas finas.

## 7. Lecciones del intento fallido (v1)

Un joven tallando un poste con navaja, animado con Wan2.2 y rebote, fue rechazado por el usuario: aburrido (una acción repetida, sin arco), con saltos y cables que aparecían y desaparecían, y además infiel a la letra (postes de luz y etiquetas en vez de pilares con el nombre grabado). Cambios: ilustración limpia sin cables, método de animación en código, arco de luz y lectura literal de la letra.

## 8. Notas para el agente

- Independiente del agente: solo hace falta shell y leer archivos; si el agente no es multimodal, pedir al usuario que apruebe la ilustración.
- Efectos fuera del repositorio (instalar un nodo de terceros, escribir o sobrescribir en `P:`) requieren autorización del usuario.
- Los límites de Spotify cambian: reconfirmar en `support.spotify.com/artists` (Canvas guidelines) antes de fijar cifras nuevas.

# YouTube: estrategia de video musical (investigación 2026-10-29)

Prueba piloto: "Trae contigo la lluvia". Publicación manual, sin distribuidora. Edición auxiliar: Camtasia.

## Nivel de evidencia (leer primero)
No existe un estudio público serio que compare formatos (letra / loop / video completo) ni retención de los primeros 30 s en música. Casi todo lo encontrado son blogs de vendedores de herramientas. Lo que sigue es criterio razonado, no datos. **La única forma de saberlo es medir en YouTube Studio con nuestras propias canciones** (retención a los 30 s, duración media de visualización).

## Qué dicen las fuentes (con reservas)
- Visualizador sencillo o audio-reactivo da la mejor relación esfuerzo/interacción; la imagen estática da la menor interacción (dynamoi.com).
- Los videos con letra ganan en búsqueda y "cantar a coro"; el video completo se reserva para sencillos clave (violetrecording, orphiq, freebeat).
- Un visualizador con bucle "retiene igual que un rodaje" es afirmación sin medición.
- Ritmo de imágenes: 3–5 s por imagen como punto de partida; cortar al pulso; alternar zoom-in/zoom-out; no dar el mismo tiempo a todas (foros y blogs; sin dato de retención). Con ilustración de movimiento lento se puede ir más largo (10–15 s).
- Retención: YouTube mide el porcentaje que sigue a los 30 s; referencia de blog ≈ 60 %. Intros largas o negras son causa típica de abandono.
- Empaque: miniatura, título y descripción pesan más que las etiquetas. Miniatura de alto contraste y ≤ 3–5 palabras. Título "Canción – Artista (Official Video)". Letra completa en la descripción (la cifra "+40–60 % de búsqueda" no está verificada).
- Capítulos: solo útiles en videos largos o de varias canciones; no para una canción.

## Datos oficiales (YouTube Help, página de codificación)
MP4, H.264 High, GOP cerrado de medio segundo, 4:2:0, `+faststart`, BT.709. Mantener la tasa de cuadros de la fuente. 1080p: 8 Mbps (24/25/30 fps), 12 Mbps (48–60). 4K: 35–45 Mbps. Audio AAC-LC 48 kHz, 384 kbps estéreo. (La página dice que aplica a socios de Content Manager; en la práctica es la referencia.)
Camtasia: no encontré documentación verificable de ajustes de exportación; usar un perfil MP4 1080p con esos valores y comprobar con `ffprobe`.

## Políticas que nos tocan (verificar en el texto oficial al subir)
- IA: la etiqueta "contenido alterado o sintético" es para lo realista (rostros/voces clonados, hechos que parecen reales). Ilustración gouache y música original de Suno sin clonar a nadie normalmente no la requieren; YouTube la está haciendo más visible desde mayo de 2026 y puede etiquetar por su cuenta.
- Monetización: la política de "contenido no auténtico" castiga producción masiva y plantillada. Mitigación que ya tenemos: estilo, paleta y transiciones distintos por canción, letra de autoría humana con changelog.
- Sin distribuidora: no hay Content ID ni canal "Tema" automático. Umbral de monetización estándar: 1.000 suscriptores y 4.000 h (una fuente menciona un cambio en 2027; sin confirmar).

## Las cuatro opciones
| Opción | Coste | Qué dicen las fuentes | Veredicto |
|---|---|---|---|
| A. Fondo estático | mínimo | menor interacción | Solo como versión de reserva o "audio" |
| B. Loop de varias escenas | bajo | funciona para visualizadores; riesgo de monotonía en 3–4 min; el bucle de 8 s del Canvas no se traslada | Aceptable solo si es largo (≥ 30 s) y con deriva lenta |
| C. Dramatización completa | muy alto | para sencillos clave | **Descartada** con la GPU actual: Wan 2.2 en 6 GB ≈ 5 min por segundo según un workflow comunitario → 4 min de canción son días, y sin consistencia de personaje |
| D. Escenas secuenciales sin loop | medio | es el punto dulce ilustración + ritmo | **Recomendada** |

## Recomendación para el piloto: D con refuerzos baratos
1. **Estructura**: una escena por sección de la letra, con motivo que vuelve. El arco ya existe (sequía ocre → lluvia esmeralda). Unas 12–16 escenas de 10–18 s; los coros regresan al motivo central con variación (como los coros de la letra).
2. **Primeros 15 s**: movimiento visible desde el cuadro 0 (nada de negro ni título largo). Un título discreto 3–4 s.
3. **Movimiento**: deriva lenta (zoom/pan alternando sentido), partículas de lluvia/polvo, disolvencias largas; variar 3 tipos de transición como en el skill. Sin video generativo salvo, opcional, 1–2 momentos clave de 3 s.
4. **Texto**: no quemar la letra completa (rompe la ilustración y compite con la voz). Título al inicio y, opcionalmente, 2–4 versos del coro en tipografía sobria. La letra va en **subtítulos .srt** subidos a YouTube (búsqueda, accesibilidad, gratis) y en la descripción. Probar "con letra" en la siguiente canción para comparar.
5. **Formato**: 16:9, 1920×1080, 24 fps (los frames ya están a 24), H.264 ≥ 8 Mbps, AAC 384 kbps desde el WAV maestro.
6. **Miniatura**: la mejor escena recortada, alto contraste, ≤ 3 palabras.

## Ahorro de tokens: qué delegar
| Tarea | Quién | Nota |
|---|---|---|
| Alinear letra con audio → SRT | local: `stable-ts` (forced alignment) con la letra conocida | Separar voz primero si hay mucha instrumentación (probado sin separar: encaja); guardar el .srt en UTF-8 con BOM para Camtasia (`scripts/align-lyrics.py`) |
| Cortes al pulso / mapa de secciones | local: librosa (ya está `just audio-analyze`) | Dar a Claude solo la tabla de tiempos |
| Primer borrador de prompts por escena | local: `mistral:7b` o `gemma4` con el prefijo de estilo fijo | Claude solo revisa el resultado (puerta 1) |
| Imágenes | local: ComfyUI z_image_turbo ≈ 65 s c/u → 16 imágenes ≈ 17 min | 0 tokens de Claude |
| Revisión de imágenes | Claude, **una hoja de contacto** en vez de 16 imágenes sueltas | Mantener puerta 2 del usuario |
| Movimiento + transiciones + montaje | Camtasia o ffmpeg `zoompan`/`xfade` | Ver aviso de tiempo |
| Metadatos (título, descripción, etiquetas) | local o plantilla | |

Aviso de tiempo: el renderizador en Python del skill tarda ≈ 0,8 s por fotograma; una canción de 4 min a 24 fps son ≈ 5.800 fotogramas → **≈ 75 min** (estimación). Para el video largo conviene que el movimiento lo haga Camtasia (zoom/pan y transiciones nativos) o ffmpeg con NVENC, y reservar el código propio para capas (lluvia, brasas) renderizadas una sola vez como clip en bucle y reutilizadas.

## Pendientes antes de producir
- Confirmar duración real y secciones de "Trae contigo la lluvia" (la letra está en el vault de Obsidian; no está en `canciones/`).
- Reutilizar `canvas/work_lluvia/` (5 imágenes ya aprobadas) como base de las escenas clave.
- Puerta 1 (concepto) y puerta 2 (fotogramas) siguen vigentes.

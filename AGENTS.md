# Composer — Instrucciones del Proyecto

Sistema RAG de composición musical con Ollama local.

## Composición de canciones

Cuando el usuario solicite una canción:

0. **Regla de Oro** — "Si un hablante nativo en un bar no diría esa frase, no la pongas."
1. **Explorar conocimiento primero** — leer `specs/002-anti-ai-isms.md` (completo), luego corpus/ (teoría, estructuras, retórica, fonética).
2. **Auditoría Léxica Previa** — antes de escribir, lista cada sustantivo abstracto y adjetivo; verifica que no esté en listado prohibido (§1.3, §2.5) y que pase la regla del bar.
3. **Regla del Sustantivo Concreto** — por cada abstracto (amor, dolor, soledad), en el mismo verso debe haber un objeto físico específico (una taza, un grifo, una persiana).
4. **Regla de Especificidad** — prohibido usar genéricos: no "la ciudad" sino "Carabanchel"; no "un coche" sino "un Renault 4"; no "una flor" sino "una buganvilia".
5. **Planificar** — elegir género (requerido, no opcional), BPM, compás, tonalidad, progresión, estructura, esquema de rima y meta-tags.
6. **Aplicar checklist anti-AI** de `specs/002-anti-ai-isms.md` — los 21 safeguards cuantificables del compositor. Cada estrofa debe pasar todos los ítems; si 3+ fallan, rehacer la canción desde cero.
7. **Verificación Fonética** — aplicar la lista de verificación fonética de `corpus/007-fonetica-acustica.md §5`: filtro de clímax (vocales abiertas en notas agudas), filtro de legato (consonantes sonoras en pasajes suaves), filtro rítmico (oclusivas alineadas con la base rítmica) y la prueba del susurro.
8. **Usar meta-tags `[ ]`** en la letra para marcar secciones (Intro, Verse, Chorus, Bridge, Outro, etc.), transiciones (Pre-Chorus, Build, Drop) y voces ([spoken word], [rap verse], [whisper]).
8b. **Paréntesis `( )` vs corchetes `[ ]`** — regla crítica de sintaxis Suno: los corchetes `[ ]` son instrucciones que NO se cantan; los paréntesis `( )` son contenido que SÍ se canta (ad-libs, eco, backing vocals). La IA comete el error frecuente de poner instrucciones de producción entre paréntesis, resultando en que Suno las canta como letra. Ver `specs/004-suno-syntax.md`. Ejemplo documentado de este error: `canciones/dorian-frente-al-cuadro.md` (instrucciones de producción en paréntesis en lugar de corchetes). Toda canción nueva debe pasar el checklist de sintaxis Suno (§Checklist del spec 004).
9. Para recuperar contexto del RAG, usar `just query "requisitos"`. Para indexar cambios, usar `just ingest` (incremental — solo re-procesa archivos modificados). Usar `just reset` + `just ingest` solo cuando se cambie la estructura del chunking o se añadan/eliminen directorios completos.
10. Para canciones complejas o largas, se puede invocar al subagente `compositor` con el task tool.
    10b. **Regla moral** — las letras promueven principios edificantes: responsabilidad, templanza, respeto, integridad familiar, esperanza realista. Cero promoción de alcohol, tabaco, drogas, café como desahogo, ni sexo prematrimonial/extramatrimonial como deseable. Ver §7 del spec.
11. **Template obligatorio** — toda canción nueva debe seguir `specs/003-file-template.md`. Usar `just template "Título" "Género"` para generar el esqueleto. La descripción debe seguir el formato de 5 partes del spec §Descripción: hook (género/instrumentación/momento), tesis, simbolismo explícito, conexión («Si alguna vez has...»), cierre. Máximo 2 párrafos.
12. **Sincronización con Notion** — los campos de `### Notion DB` en el archivo deben coincidir exactamente con los valores enviados a la base de datos "Canciones de JPMarichal". El nombre del archivo en kebab-case debe coincidir con el título.
13. **Guardar en `canciones/`** — toda canción se escribe como archivo `.md` en `canciones/`, sin mensajes adicionales en el chat. El archivo incluye metadatos (según spec 003), prompt de estilo Suno, letra completa con meta-tags, armonía, y checklist anti-AI verificado.
14. **Ciclo Escribir → Escuchar → Ajustar** — ninguna canción se da por terminada sin ser escuchada. La primera escucha revela problemas invisibles en el papel (tono, edad percibida, conexión emocional). Iterar hasta que el autor quede satisfecho.
15. **Variación de Coros** — los coros idénticos empobrecen. Cada coro debe tener al menos una variación semántica (progresión en L1, L3 o L4) para que el agua/tesis evolucione a lo largo de la canción.
16. **Suspenso por Capas** — la verdad de la canción se revela gradualmente (V1 descriptivo → Chorus tesis → V2 conflicto → Bridge revelación → Outro resolución). El oyente debe poder descubrir algo nuevo en cada escucha.
17. **Style Prompt limitado a 1000 chars** — usar la **Fórmula de 6 componentes** por orden de prioridad: (1) Género + Era, (2) Tempo/BPM, (3) Instrumentación y riffs, (4) Tratamiento vocal (personaje), (5) Ambiente y tonalidad, (6) Mezcla. Suno pesa más las primeras palabras. Incluir acordes (I-V-vi-IV), estructura, arpegios y referencia sonora. No usar nombres de artistas reales. Ver guía detallada en `specs/003-file-template.md §Style Prompt`.
18. **Changelog de Autoría** — cada canción incluye un changelog que registra todas las decisiones del autor humano vs. sugerencias del asistente. Esto protege la autoría en caso de controversia legal.
19. **Enfocarse en composición original** — poesía existente (Neruda, Machado, Benedetti) y experimentos instrumentales (Rare Metals) son experimentales/secundarios. El mérito real del autor está en la composición lírica original de su autoría. Cualquier análisis (genérico, temático, de frecuencia) debe priorizar las canciones con letra original sobre adaptaciones o piezas instrumentales.
20. **Género obligatorio al crear** — toda canción nueva debe tener género asignado en el campo `- **Género:**` del template. Canciones sin género distorsionan el análisis del catálogo.
21. **Los géneros del autor por volumen (canciones líricas, 134 archivos, ver `specs/012-identity-and-genre-analysis.md`):**
    - **Pop (33%)** — base ancha. Pop + Pop rock + Latin pop = 44 tags.
    - **Indie (33%)** — firma de autor. Indie + Spanish indie pop + Indie pop + Indie folk + Dream pop = 44 tags. "Spanish indie pop" es la sub-marca distintiva (6%).
    - **Folk (22%)** — anclaje emocional. Folk + Folk pop + Folk-pop + Indie folk = 30 tags.
    - **Chamber pop / Orquestal (14%)** — identidad culta. Chamber pop + Orchestral pop = 19 tags.
    - **Balada (12%)** — núcleo melancólico. 16 tags.
    - **Electrónica con letra (13%)** — segundo polo experimental. Electrónica + Synthwave + Synth-pop + Electropop = 17 tags.
    - **Rock (15%)** — contrapeso enérgetico. Rock + Pop rock + Soft rock + Acoustic rock = 20 tags.
    - **Statement of identity real:** Pop indie folk chamber en español, con balada como sub-modo melancólico y experimentación electrónica como segundo polo. NO proyectar "balada folk" ni "indie pop español" como identidad única — son subsets. Ver `specs/012-identity-and-genre-analysis.md` §5.
    - **Rare Metals (24 instrumentales electrónicos)** — serie experimental aparte. No compite con la obra letrista por mercado ni SEO.

## Registro de canciones existentes

Cuando el usuario entregue canciones ya compuestas (letra + metadatos) para añadir al repositorio, seguir el workflow en `skills/add-song/SKILL.md`.

## Songcase Analysis (canciones externas)

Cuando el usuario pida analizar una canción existente (no del catálogo propio), activar el skill `songcase-analysis`. Los análisis se guardan en `inspiration/<artista>-<cancion>.md` siguiendo `inspiration/SONG-TEMPLATE.md`. El directorio `inspiration/` se indexa automáticamente con `just ingest` para consultas RAG sobre armonía, estructura y producción de cualquier canción analizada.

## Herramientas del sistema

- Usar **ripgrep (`rg`)** en lugar de `grep` para búsquedas en contenido local — es más rápido y soporta regex completo.

## Comandos útiles

- `just ingest` — indexar corpus/ specs/ docs/ en el vector store
- `just query "pregunta"` — consulta RAG con mistral:7b
- `just query-fast "pregunta"` — consulta rápida con llama3.2:3b
- `just query-pro "pregunta"` — consulta profunda con gemma4
- `just reset` — limpiar índice vectorial
- `just import-from-notion` — importar canciones desde Notion al directorio local
- `just template "Título" "Género"` — generar esqueleto de canción
- `just notion-sync "canciones/canción.md"` — sincronizar archivo local → Notion
- `just reset` + `just ingest` — reindexar vector store tras cambios
- `just suno-index` — indexar todo el catálogo de Suno localmente (~1,500 clips). **Actualiza** project_name de clips existentes, no solo añade nuevos. Ejecutar después de mover clips entre proyectos.
- **Buscar en cuenta propia primero** — al recuperar canciones de Suno, usar `suno-account_list_songs` antes de buscar en público (`suno-account_search_songs`). Las canciones del usuario pueden ser privadas y no aparecer en búsquedas públicas.
- `just suno-search "término"` — buscar canciones en el índice local por título
- `just suno-stats` — resumen del catálogo por proyecto
- `just suno-list-projects` — lista todos los proyectos con su clip count
- `just suno-move-clips "Singles" "Mamá" "si vuelvo"` — mueve clips al proyecto indicado (busca por título en el índice local)
- `just suno-move-clips-from "Fronteras" "Singles" "Mamá" "si vuelvo"` — mueve clips desde un proyecto específico a otro
- `just deezer "canción" "artista"` — consultar BPM, ISRC, gain vía Deezer
- `just lookup "canción" "artista"` — Deezer + preview + análisis librosa
- `just audio-analyze "archivo.mp3"` — analizar archivo local con librosa
- `just songcase "artista" "canción"` — crear un songcase desde el template

## Playlist Promotion (Spotify)

Cuando el usuario pida crear una playlist promocional para una canción:

1. **Leer `specs/008-playlist-curation-rules.md`** — reglas completas, tiers, hallazgos de procedimiento
2. **Cargar skill** `playlist-promotion` (`.claude/skills/playlist-promotion/SKILL.md`) — workflow de 4 fases
3. **Usar script** `scripts/spotify-playlist.ps1` para operaciones API
4. **SEO del título — basado en investigación (no asumir género=primario)**: Investigar ANTES de proponer nombre. El término con **mayor search volume** va primero — puede ser actividad, mood, era o género (no siempre es el género). Estructura validada: `[Primary high-volume] : [Secondary mood/activity], [Tema]`. Las 4 dimensiones: **actividad** (workout, study, focus, sleep, driving), **mood** (chill, sad, nostalgic, energetic, melancholic), **género/subgénero** (lofi, indie folk, phonk, bedroom pop), **era/contexto** (2000s, late night, throwback). NO poético/abstracto — debe ser leíble como query de búsqueda real.
    4b. **SEO de descripción**: La descripción TAMBIÉN es SEO (Spotify la indexa). Fórmula: genre + mood + actividad + 3-5 artistas comparables (nombres buscables, >100k ML) + propuesta de valor + "Actualizada semanalmente". Máx 100 chars por frase. Ver `specs/008-playlist-curation-rules.md §Descripción SEO`.
    4c. **Patrón "Research-Once-Use-Many"** (objetivo: 2-3 min por playlist, no 15-20): Mantener un **keyword pool cacheado** en `kw-pool/` con datos de Google Trends + Spotify Search ya capturados. Por playlist, pick de la piscina + 30s de verificación en Spotify Autocomplete. Refresco mensual del pool (15 min) en lugar de re-investigar cada vez.
    4d. **Workflow de naming** (per-playlist, 2-3 min): (1) Listar 5-8 términos candidatos de `kw-pool/` cubriendo las 4 dimensiones para el género/mercado. (2) **30s check en Spotify Autocomplete** manual — escribir el candidato principal en Spotify y ver si aparece en sugerencias. (3) Si hay duda entre 2-3 candidatos, correr `just kw-spotify "termino" "ES"` para ver señales de demanda (cuántas playlists, qué títulos, qué followers). (4) Elegir primary (mayor search volume / más resultados / más popular en autocomplete). (5) Componer título y documentar en changelog de la playlist.
    4e. **Herramientas gratuitas validadas (sin coste)**:
       - **Spotify Search API** (nuestra app `playlister` ya configurada) — `GET /v1/search?type=playlist&q=<termino>` retorna top 10-50 playlists. **Los títulos de esas playlists = proxy directo de lo que la gente busca**. Funciona en español. Sin coste, sin rate limit raro. Usar `just kw-spotify "termino" "ES"`.
       - **trendspyg** (`flack0x/trendspyg`, Python, sin API key) — Google Trends RSS-based, 125 países (incluye ES, MX, AR, CL, CO), 20 categorías, sin 429 errors, 0.2s response, 5min cache built-in. Usar `just kw-trends "termino" "ES"`.
       - **trendsmcp MCP** (free tier 100 req/día, sin tarjeta) — alternativa MCP-integrada con Claude/Cursor si prefieres no usar Python.
       - ~~pytrends~~ — **NO USAR**, archivado desde 2023, 429 constantes, requiere proxies.
       - ~~artist.tools~~ — solo útil con plan de pago (Industry Access). Free tier muy limitado.
    4e. **Construir el pool inicial** (one-time, 1-2 horas): Para cada combinación (género principal × mercado meta), poblar `kw-pool/<genero>-<mercado>.json` con 30-50 keywords + interest_over_time + related_queries + Spotify playlist matches. Mercados meta iniciales: ES, MX, AR (cubren 90% del público hispano). Géneros del catálogo: balada, pop, indie/folk, indie pop, folk latino. Documentar en `kw-pool/README.md` los criterios de inclusión.
5. **Aplicar código moral §7** — filtrar artistas que promuevan alcohol, tabaco, drogas, café, violencia, abuso, malas palabras o contenido explícito
6. **Proporciones**: A=4, B=~16, C=~24, D=~21, E=~15 (70/30 rule, OnesToWatch)
7. **Credenciales en `.env`**: `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, `SPOTIFY_REFRESH_TOKEN`, `SPOTIFY_USER_ID`
7b. **Redirect URI**: `http://127.0.0.1:8080/callback/` (app: playlister en Spotify Dashboard)
7c. **⚠️ Token refresh**: extraer de .env con `$line -split '=', 2 | Select-Object -Last 1`. NO usar `-replace '.*= '` (falla porque .env no tiene espacio tras el =)
7d. **Popularidad siempre null**: app playlister creada post-Feb 2026, el campo `popularity` no está disponible en API para apps nuevas en dev mode. La métrica real está en Spotify for Artists (save rate, skip rate, streams).
8. **⚠️ Limitación crítica**: No se puede modificar tracks de una playlist existente via API (DELETE /items = 400/403). Para "actualizar", crear playlist NUEVA con `POST /v1/me/playlists` (no `/users/{id}/playlists`) y eliminar la vieja con `DELETE /followers`. La URL cambia cada vez.
9. **Usar `POST /v1/me/playlists` siempre** para crear playlists — `/users/{id}/playlists` devuelve 403.

Playlist v1 (referencia): "Balada Folk Latino: Nostalgia, Raíces y Hogar" — 80 tracks, promoviendo "Mamá, si vuelvo a verte" en posición #5. Propias en #5, #25, #45, #65. URL: https://open.spotify.com/playlist/3RemCcFC1HkpdutHaATLbp
Playlist v2 (referencia): "Indie Pop Épico: Triunfo y Transformación" — 80 tracks, promoviendo "Pequeña Era" en posición #5. Propias en #5, #25, #45, #65. URL: https://open.spotify.com/playlist/3A35KIqDxtIPnmU9FrAkAH

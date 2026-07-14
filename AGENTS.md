# Composer — Instrucciones del Proyecto

Sistema RAG de composición musical con Ollama local. Node.js v22 + LangChain.js + just (PowerShell).

## Entorno

- Windows + PowerShell. No bash.
- Node: `C:\Users\Juan.Pablo.Marichal\AppData\Local\nvm\v22.20.0\node.exe`
- Ollama debe estar corriendo (`ollama serve`).
- `just` es el task runner. `npm run` también funciona via `scripts/just.ps1`.
- No hay tests en este repo.

## Credenciales

`.env` contiene secretos reales (Notion, Suno, Spotify, MySQL). No commitear. Cargar con `dotenv`.

## RAG

- Vector store propio (`LocalVectorStore`) con persistencia en `.chroma/` + manifest por hash SHA256.
- Ingest incremental: solo re-procesa archivos modificados. `just reset` + `just ingest` solo al cambiar estructura de chunking o directorios.
- Modelos por defecto en `src/config.js`:
  - Embeddings: `nomic-embed-text`
  - Query: `mistral:7b`
  - Query-fast: `tinyllama` (hardcodeado en `src/index.js:62`, no usar el default de config)
  - Query-pro: `gemma4`

## MCP

`opencode.json` define 6 MCP locales. Activar con `just mcp-activate-local` antes de usar en VS Code.

- **notion** — `node src/notion-mcp.js`
- **notebooklm** — `npx -y notebooklm-mcp@latest`
- **suno-thirdparty** — Python server con API key de sunoapi.org
- **suno-account** — `suno_mcp` con cookie de sesión Suno
- **suno-browser** — Node `suno-mcp` apuntando a CDP `localhost:9100`
- **mysql** — `node tools/mysql-mcp-wrapper.js`

## Composición de canciones

Reglas no negociables. Incumplir cualquiera = canción rechazada.

0. **Regla de Oro** — "Si un hablante nativo en un bar no diría esa frase, no la pongas."
1. **Explorar primero** — leer `specs/002-anti-ai-isms.md` completo, luego `corpus/` (teoría, estructuras, retórica, fonética).
2. **Auditoría Léxica Previa** — listar cada sustantivo abstracto y adjetivo antes de escribir; verificar listado prohibido (§1.3, §2.5) + regla del bar.
3. **Sustantivo Concreto** — por cada abstracto (amor, dolor, soledad), en el mismo verso debe haber un objeto físico específico (una taza, un grifo, una persiana).
4. **Especificidad** — prohibido genéricos: no "la ciudad" sino "Carabanchel"; no "un coche" sino "un Renault 4"; no "una flor" sino "una buganvilia".
5. **Planificar** — género (requerido), BPM, compás, tonalidad, progresión, estructura, esquema de rima, meta-tags.
6. **Checklist anti-AI** — 21 safeguards de `specs/002-anti-ai-isms.md`. Cada estrofa debe pasar todos. Si 3+ fallan, rehacer desde cero.
7. **Verificación Fonética** — 4 filtros de `corpus/007-fonetica-acustica.md §5`: clímax (vocales abiertas en agudas), legato (consonantes sonoras en suaves), rítmico (oclusivas con base), prueba del susurro.
8. **Meta-tags `[ ]`** — marcan secciones (Intro, Verse, Chorus, Bridge, Outro) y voces ([spoken word], [rap verse], [whisper]).
9. **Sintaxis Suno crítica** — `[ ]` = instrucciones que NO se cantan; `( )` = contenido que SÍ se canta. Error frecuente: poner producción en `( )` y Suno lo canta como letra. Ver `specs/004-suno-syntax.md`. Ejemplo: `canciones/dorian-frente-al-cuadro.md`.
10. **Regla moral** — principios edificantes: responsabilidad, templanza, respeto, integridad familiar, esperanza realista. Cero alcohol, tabaco, drogas, café como desahogo, ni sexo prematrimonial/extramatrimonial como deseable. Ver §7 del spec.
11. **Template obligatorio** — `specs/003-file-template.md`. Generar con `just template "Título" "Género"`. Descripción: formato 5-partes (hook, tesis, simbolismo, conexión «Si alguna vez has...», cierre). Máx 2 párrafos.
12. **Género obligatorio** — toda canción debe tener `- **Género:**` poblado. Sin género distorsiona el análisis del catálogo.
13. **Variación de Coros** — cada coro debe tener al menos una variación semántica (progresión en L1, L3 o L4).
14. **Suspenso por Capas** — V1 descriptivo → Chorus tesis → V2 conflicto → Bridge revelación → Outro resolución.
15. **Style Prompt ≤1000 chars** — Fórmula 6 componentes: (1) Género + Era, (2) Tempo/BPM, (3) Instrumentación, (4) Tratamiento vocal, (5) Ambiente y tonalidad, (6) Mezcla. Incluir acordes (I-V-vi-IV). No nombres de artistas reales.
16. **Changelog de Autoría** — registrar decisiones humano vs. asistente.
17. **Ciclo Escribir → Escuchar → Ajustar** — ninguna canción se da por terminada sin escucharla.
18. **Géneros del catálogo** — Pop (33%), Indie (33%), Folk (22%), Chamber pop/Orquestal (14%), Balada (12%), Electrónica con letra (13%), Rock (15%). Ver `specs/012-identity-and-genre-analysis.md` §5. Identity real: Pop indie folk chamber en español.
19. **Rare Metals** — 24 instrumentales electrónicos, serie experimental aparte.
20. **Inspiración externa** — usar skill `songcase-analysis` para canciones no del catálogo. Guardar en `inspiration/<artista>-<cancion>.md`.

## Skills

- `skills/add-song/SKILL.md` — registrar canciones ya compuestas (letra + metadatos).
- `.claude/skills/playlist-promotion/SKILL.md` — crear playlists promocionales Spotify.
- `.claude/skills/playlist-outreach/SKILL.md` — generar DMs de outreach.
- `.claude/skills/songcase-analysis/SKILL.md` — analizar canciones externas.
- `.claude/skills/voice-analysis/SKILL.md` — análisis de rango vocal.
- `.claude/skills/suno-thumbs/SKILL.md` — descargar thumbnails de Suno.

## Comandos

```powershell
just ingest                  # Indexar corpus/, specs/, docs/, inspiration/, bio/
just query "pregunta"        # RAG con mistral:7b
just query-fast "pregunta"   # RAG rápido con tinyllama (streaming)
just query-pro "pregunta"    # RAG profundo con gemma4
just reset                   # Borrar índice (.chroma/)
just template "T" "G"        # Generar esqueleto de canción
just publish-song "ruta.md" "msg"  # Notion sync → ingest → commit → push (obligatorio al registrar)
just notion-sync "ruta.md"   # Sincronizar archivo local → Notion
just import-from-notion      # Importar canciones desde Notion
just songcase "a" "c"        # Crear songcase desde template
just suno-index              # Indexar catálogo Suno local (~1,500 clips)
just suno-search "término"   # Buscar en índice local por título
just suno-stats              # Resumen catálogo por proyecto
just suno-list-projects      # Listar proyectos con clip count
just suno-move-clips "target" "título"  # Mover clips entre proyectos
just deezer "c" "a"          # Metadata vía Deezer
just audio-analyze "archivo" # Analizar audio local con librosa
just kw-spotify "t" "ES"     # Verificar demanda de keyword en Spotify
just kw-trends "t" "ES"      # Verificar tendencia en Google Trends
```

## Flujo de publicación de canción

1. Crear archivo en `canciones/` siguiendo template.
2. `just publish-song "canciones/<titulo>.md" "mensaje"` — sincroniza a Notion, indexa, commitea y pushea.
3. Si hay múltiples canciones, ejecutar `publish-song` por cada una.

## Archivos clave

- `src/index.js` — entrypoint CLI (ingest/query)
- `src/config.js` — config RAG (modelos, Chroma, directorios)
- `src/ingest.js` — pipeline de ingest con hash incremental
- `src/query.js` — consulta RAG con búsqueda híbrida + reranking
- `opencode.json` — definición de MCPs del proyecto
- `.opencode/project-mcp-state.json` — estado de MCPs activos
- `.env` — credenciales (no commitear)

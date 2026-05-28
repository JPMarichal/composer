# Composer — Instrucciones del Proyecto

Sistema RAG de composición musical con Ollama local.

## Composición de canciones

Cuando el usuario solicite una canción:

0. **Regla de Oro** — "Si un hablante nativo en un bar no diría esa frase, no la pongas."
1. **Explorar conocimiento primero** — leer `specs/002-anti-ai-isms.md` (completo), luego corpus/ (teoría, estructuras, retórica).
2. **Auditoría Léxica Previa** — antes de escribir, lista cada sustantivo abstracto y adjetivo; verifica que no esté en listado prohibido (§1.3, §2.5) y que pase la regla del bar.
3. **Regla del Sustantivo Concreto** — por cada abstracto (amor, dolor, soledad), en el mismo verso debe haber un objeto físico específico (una taza, un grifo, una persiana).
4. **Regla de Especificidad** — prohibido usar genéricos: no "la ciudad" sino "Carabanchel"; no "un coche" sino "un Renault 4"; no "una flor" sino "una buganvilia".
5. **Planificar** — elegir género, BPM, compás, tonalidad, progresión, estructura, esquema de rima y meta-tags.
6. **Aplicar checklist anti-AI** de `specs/002-anti-ai-isms.md` — los 21 safeguards cuantificables del compositor. Cada estrofa debe pasar todos los ítems; si 3+ fallan, rehacer la canción desde cero.
7. **Usar meta-tags `[ ]`** en la letra para marcar secciones (Intro, Verse, Chorus, Bridge, Outro, etc.), transiciones (Pre-Chorus, Build, Drop) y voces ([spoken word], [rap verse], [whisper]).
8. Si es necesario, usar `just ingest` y `just query "requisitos"` para recuperar contexto del RAG.
9. Para canciones complejas o largas, se puede invocar al subagente `compositor` con el task tool.
10. **Guardar en `canciones/`** — toda canción se escribe como archivo `.md` en `canciones/`, sin mensajes adicionales en el chat. El archivo incluye metadatos y prompt de estilo Suno en el encabezado, y la letra completa con meta-tags en el cuerpo.
11. La canción debe entregarse con: título, género/BPM/compás, estructura, progresión, prompt de estilo Suno, letra completa con meta-tags, y checklist anti-AI verificado.

## Comandos útiles

- `just ingest` — indexar corpus/ specs/ docs/ en el vector store
- `just query "pregunta"` — consulta RAG con mistral:7b
- `just query-fast "pregunta"` — consulta rápida con llama3.2:3b
- `just query-pro "pregunta"` — consulta profunda con gemma4
- `just reset` — limpiar índice vectorial

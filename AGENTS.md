# Composer — Instrucciones del Proyecto

Sistema RAG de composición musical con Ollama local.

## Composición de canciones

Cuando el usuario solicite una canción:

1. **Explorar conocimiento primero** — leer corpus/ (teoría, estructuras, retórica) y specs/ (anti-AI) antes de escribir.
2. **Planificar** — elegir género, BPM, compás, tonalidad, progresión, estructura, esquema de rima y meta-tags.
3. **Aplicar checklist anti-AI** de `specs/002-anti-ai-isms.md` — cada estrofa debe pasar los 9 safeguards cuantificables.
4. **Usar meta-tags `[ ]`** en la letra para marcar secciones (Intro, Verse, Chorus, Bridge, Outro, etc.), transiciones (Pre-Chorus, Build, Drop) y voces ([spoken word], [rap verse], [whisper]).
5. Si es necesario, usar `just ingest` y `just query "requisitos"` para recuperar contexto del RAG.
6. Para canciones complejas o largas, se puede invocar al subagente `compositor` con el task tool.
7. **Guardar en `canciones/`** — toda canción se escribe como archivo `.md` en `canciones/`, sin mensajes adicionales en el chat. El archivo incluye metadatos y prompt de estilo Suno en el encabezado, y la letra completa con meta-tags en el cuerpo.
8. La canción debe entregarse con: título, género/BPM/compás, estructura, progresión, prompt de estilo Suno, letra completa con meta-tags, y checklist anti-AI verificado.

## Comandos útiles

- `just ingest` — indexar corpus/ specs/ docs/ en el vector store
- `just query "pregunta"` — consulta RAG con mistral:7b
- `just query-fast "pregunta"` — consulta rápida con llama3.2:3b
- `just query-pro "pregunta"` — consulta profunda con gemma4
- `just reset` — limpiar índice vectorial

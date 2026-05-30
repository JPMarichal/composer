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
21. **Los géneros primarios del autor son Pop y Balada** — estos representan el núcleo de su producción lírica original, no Indie/Folk como podría sugerir un análisis superficial.

## Registro de canciones existentes

Cuando el usuario entregue canciones ya compuestas (letra + metadatos) para añadir al repositorio, seguir el workflow en `skills/add-song/SKILL.md`.

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

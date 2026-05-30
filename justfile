# ─── Composer ───
# Profesional song composer with RAG over specs, docs and corpus

app := "composer"
embed_model := "nomic-embed-text"
llm_model := "gemma4"

# Windows: usa PowerShell como shell por defecto
set shell := ["powershell.exe", "-NoLogo", "-Command"]

# Node.js wrapper: usa la v22 de nvm4w sin tocar el default del sistema
node := "&'C:\\Users\\Juan.Pablo.Marichal\\AppData\\Local\\nvm\\v22.20.0\\node.exe'"

# ─── Ingest ────────────────────────────────────────────────

# Indexa docs/, specs/ y corpus/ en el vector store
ingest:
    {{node}} src/index.js ingest

# ─── Query ─────────────────────────────────────────────────

# Consulta RAG completa: just query "pregunta" (usa el modelo por defecto)
query q:
    {{node}} src/index.js query "{{q}}"

# Consulta rápida con tinyllama (streaming): just query-fast "pregunta"
query-fast q:
    {{node}} src/index.js query-fast "{{q}}"

# Consulta completa con gemma4: just query-pro "pregunta"
query-pro q:
    {{node}} src/index.js query-pro "{{q}}"

# ─── Ollama ────────────────────────────────────────────────

# Lista los modelos disponibles en Ollama
list-models:
    ollama list

# Trae los modelos necesarios para el proyecto
pull-models:
    ollama pull {{embed_model}}
    ollama pull {{llm_model}}

# ─── Mantenimiento ─────────────────────────────────────────

# Limpia el índice vectorial (requiere re-ingest)
reset:
    Remove-Item -LiteralPath ".chroma" -Recurse -Force -ErrorAction SilentlyContinue; Write-Host "Índice borrado. Ejecuta 'just ingest' para reindexar."

# Empuja cambios a git
git-push msg:
    git add -A; if ($?) { git status }; if ($?) { git commit -m "{{msg}}" }; if ($?) { git push }

# ─── Template ──────────────────────────────────────────────

# Genera un template de canción: just template "Mi canción" "Indie Folk"
template title genre:
    {{node}} src/template.js "{{title}}" "{{genre}}"

# Importa canciones desde Notion: just import-from-notion
import-from-notion:
    {{node}} src/import-from-notion.js

# Sincroniza un archivo local a Notion: just notion-sync canciones/mi-cancion.md
notion-sync path:
    {{node}} src/notion-sync.js "{{path}}"

# Sincroniza a Notion, indexa y hace push: just publish-song "canciones/canción.md" "mensaje commit"
publish-song path msg:
    {{node}} src/notion-sync.js "{{path}}"; if ($?) { {{node}} src/index.js ingest }; if ($?) { git add -A }; if ($?) { git commit -m "{{msg}}" }; if ($?) { git push }

# ─── Ayuda ─────────────────────────────────────────────────

default:
    @just --list

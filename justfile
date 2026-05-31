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

# ─── Suno Index ────────────────────────────────────────────

# Ruta del Python del venv de Suno MCP
sunopy := "C:\\Users\\JUANPA~1.MAR\\AppData\\Local\\Temp\\opencode\\suno-ai-mcp\\.venv\\Scripts\\python.exe"

# Indexa todo el catálogo de Suno localmente: just suno-index
suno-index:
    {{sunopy}} scripts/suno-index.py

# Busca en el índice local de Suno: just suno-search "término"
suno-search term:
    {{sunopy}} scripts/suno-search.py "{{term}}"

# Muestra resumen del catálogo Suno: just suno-stats
suno-stats:
    {{sunopy}} scripts/suno-stats.py

# Mueve clips entre proyectos de Suno: just suno-move-clips <target> <title> [<title>...]
suno-move-clips target *titles:
    {{sunopy}} scripts/suno-move-clips.py "{{target}}" {{titles}}

# Mueve clips desde un proyecto específico: just suno-move-clips-from <source> <target> <title> [...]
suno-move-clips-from source target *titles:
    {{sunopy}} scripts/suno-move-clips.py --from "{{source}}" "{{target}}" {{titles}}

# Lista proyectos de Suno con su clip count
suno-list-projects:
    {{sunopy}} -c "import asyncio,json,os; os.environ['SSL_VERIFY']='0'; from suno_mcp.suno_client import SunoClient; async def main(): \
        async with SunoClient(open(r'$(pwd)/.env').read().split('SUNO_COOKIE=')[1].split('\n')[0].strip().strip('\"').strip(\"'\")) as c: \
            projs=(await c._api('GET','/api/project/me')).json().get('projects',[]); \
            [print(f\"  {p['name']:35s} {p['clip_count']:4d} clips ({p['id'][:8]}...)\") for p in sorted(projs,key=lambda x:-x['clip_count'])]; \
        asyncio.run(main())"

# Descarga thumbnails de Suno para canciones distribuidas: just suno-thumbs
# (sin args) busca distribuidor OffStep. --distributor "X" busca otro.
suno-thumbs *args:
    {{sunopy}} scripts/suno-thumbs.py {{args}}

# ─── Ayuda ─────────────────────────────────────────────────

default:
    @just --list

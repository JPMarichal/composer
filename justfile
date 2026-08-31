# ─── Composer ───
# Profesional song composer with RAG over specs, docs and corpus

app := "composer"
embed_model := "nomic-embed-text"
llm_model := "gemma4"

# Windows: usa PowerShell como shell por defecto
set shell := ["powershell.exe", "-NoLogo", "-Command"]

# Node.js wrapper: usa la v22 de nvm4w sin tocar el default del sistema
node := "&'C:\\Users\\Juan.Pablo.Marichal\\AppData\\Local\\nvm\\v22.20.0\\node.exe'"

# PowerShell runner reutilizable para scripts del repo
pwsh := "pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass -File"

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

# Activa los MCP locales del proyecto en la config MCP activa de VS Code
mcp-activate-local:
    {{pwsh}} scripts/project-mcp.ps1 activate

# Desactiva los MCP locales del proyecto previamente activados
mcp-deactivate-local:
    {{pwsh}} scripts/project-mcp.ps1 deactivate

# Muestra qué MCP locales del proyecto están activos en VS Code
mcp-status-local:
    {{pwsh}} scripts/project-mcp.ps1 status

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

# ─── Suno WAV Download ───────────────────────────────────────

# Container name for the Suno Manager with WAV support
suno_container := "suno-manager-wav"

# Sincroniza la base de datos local al container: just wav-sync-in
wav-sync-in:
    podman cp "canciones\audio\bksuno\_downloads.sqlite" {{suno_container}}:/app/data/_downloads.sqlite

# Sincroniza la base de datos del container a disco local: just wav-sync-out
wav-sync-out:
    podman cp {{suno_container}}:/app/data/_downloads.sqlite "canciones\audio\bksuno\_downloads.sqlite"

# Muestra estadísticas del backlog WAV: just wav-stats
wav-stats:
    {{pwsh}} -c "podman cp canciones\audio\bksuno\_downloads.sqlite {{suno_container}}:/app/data/_tmp.sqlite 2>nul; podman exec {{suno_container}} sh -c 'WAV_DB_PATH=/app/data/_tmp.sqlite python3 /app/suno-wav-manager.py stats'; podman exec {{suno_container}} rm -f /app/data/_tmp.sqlite"

# Lista clips del backlog WAV: just wav-list [filter]
# Filtros: all pending queued downloaded skipped errors <project>
wav-list filter="all":
    {{pwsh}} -c "podman cp canciones\audio\bksuno\_downloads.sqlite {{suno_container}}:/app/data/_tmp.sqlite 2>nul; podman exec {{suno_container}} sh -c 'WAV_DB_PATH=/app/data/_tmp.sqlite python3 /app/suno-wav-manager.py list {{filter}}'; podman exec {{suno_container}} rm -f /app/data/_tmp.sqlite"

# Marca clips para descarga WAV: just wav-queue <project> <n> | wav-queue-all [n]
wav-queue project count:
    {{pwsh}} -c "podman cp canciones\audio\bksuno\_downloads.sqlite {{suno_container}}:/app/data/_tmp.sqlite 2>nul; podman exec {{suno_container}} sh -c 'WAV_DB_PATH=/app/data/_tmp.sqlite python3 /app/suno-wav-manager.py queue \"{{project}}\" {{count}}'; podman cp {{suno_container}}:/app/data/_tmp.sqlite canciones\audio\bksuno\_downloads.sqlite; podman exec {{suno_container}} rm -f /app/data/_tmp.sqlite"

# Cola todos los clips completos: just wav-queue-all [n]
wav-queue-all count="all":
    {{pwsh}} -c "podman cp canciones\audio\bksuno\_downloads.sqlite {{suno_container}}:/app/data/_tmp.sqlite 2>nul; podman exec {{suno_container}} sh -c 'WAV_DB_PATH=/app/data/_tmp.sqlite python3 /app/suno-wav-manager.py queue {{count}}'; podman cp {{suno_container}}:/app/data/_tmp.sqlite canciones\audio\bksuno\_downloads.sqlite; podman exec {{suno_container}} rm -f /app/data/_tmp.sqlite"

# Marca un clip como omitido: just wav-skip <clip_id[:8]> <reason>
# Razon: experimental low_quality short duplicate instrumental not_interesting other
wav-skip clip_id reason:
    {{pwsh}} -c "podman cp canciones\audio\bksuno\_downloads.sqlite {{suno_container}}:/app/data/_tmp.sqlite 2>nul; podman exec {{suno_container}} sh -c 'WAV_DB_PATH=/app/data/_tmp.sqlite python3 /app/suno-wav-manager.py skip {{clip_id}} {{reason}}'; podman cp {{suno_container}}:/app/data/_tmp.sqlite canciones\audio\bksuno\_downloads.sqlite; podman exec {{suno_container}} rm -f /app/data/_tmp.sqlite"

# Establece prioridad: just wav-priority <clip_id[:8]> <level(-2..+2)>
wav-priority clip_id level:
    {{pwsh}} -c "podman cp canciones\audio\bksuno\_downloads.sqlite {{suno_container}}:/app/data/_tmp.sqlite 2>nul; podman exec {{suno_container}} sh -c 'WAV_DB_PATH=/app/data/_tmp.sqlite python3 /app/suno-wav-manager.py priority {{clip_id}} {{level}}'; podman cp {{suno_container}}:/app/data/_tmp.sqlite canciones\audio\bksuno\_downloads.sqlite; podman exec {{suno_container}} rm -f /app/data/_tmp.sqlite"

# Descarga WAV por lotes (usa BD del container): just wav-download [n]
# Primero ejecuta wav-sync-in, luego este comando, luego wav-sync-out
wav-download count="all":
    podman cp scripts/suno-wav-manager.py {{suno_container}}:/app/suno-wav-manager.py
    podman exec {{suno_container}} sh -c 'WAV_DB_PATH=/app/data/_downloads.sqlite python3 /app/suno-wav-manager.py queue {{count}}'
    podman exec -i {{suno_container}} python3 /app/batch_wav.py

# Descarga WAVs para un proyecto específico: just wav-project "Nombre del proyecto"
# Resultado en /app/downloads/<project>_wavs/ (container) — sincroniza después con wav-sync-out
wav-project project:
    podman cp scripts/suno-download-wav.py {{suno_container}}:/app/project_wav.py
    podman exec {{suno_container}} sh -c 'WAV_DB_PATH=/app/data/_downloads.sqlite python3 /app/project_wav.py "{{project}}"'

# ─── Songcase Analysis ─────────────────────────────────────

# Crea un archivo songcase desde el template: just songcase "artista" "cancion"
songcase artist song:
	$p = "inspiration/{{artist}}-{{song}}.md".ToLower() -replace ' ','-'; if (!(Test-Path $p)) { Copy-Item "inspiration/SONG-TEMPLATE.md" $p; Write-Host "Creado: $p" } else { Write-Host "Ya existe: $p" }

# ─── Audio Metadata ─────────────────────────────────────────

# Python para audio-meta (usa el Python del sistema con librosa instalado)
pyaudio := "python"

# Busca metadata de una canción via Deezer: just deezer "Blinding Lights" "The Weeknd"
deezer song artist="":
    {{pyaudio}} scripts/audio-meta.py deezer "{{song}}" "{{artist}}"

# Analiza un archivo de audio local con librosa: just audio-analyze mp3/cancion.wav
audio-analyze path:
    {{pyaudio}} scripts/audio-meta.py analyze "{{path}}"

# Busca en Deezer + descarga preview + analiza con librosa: just lookup "Bohemian Rhapsody" "Queen"
lookup song artist="":
    {{pyaudio}} scripts/audio-meta.py lookup "{{song}}" "{{artist}}"

# Lista los campos disponibles de audio-meta.py
audio-fields:
    {{pyaudio}} scripts/audio-meta.py fields

# ─── Spotify Playlist Promotion ────────────────────────────

# Genera una plantilla editable para redactar un pitch editorial de Spotify
# Uso: just spotify-pitch-template "Título de la canción" [ruta_salida]
# Salida por defecto: canciones/pitches/pitch-editorial-<slug>.md
spotify-pitch-template title output="":
    if ("{{output}}" -eq "") { {{pwsh}} scripts/spotify-pitch-template.ps1 -Title "{{title}}" } else { {{pwsh}} scripts/spotify-pitch-template.ps1 -Title "{{title}}" -OutputPath "{{output}}" }

# Crea una playlist: just playlist-create "Título" "Descripción" true/false
playlist-create title desc ispublic:
    pwsh -NoLogo -File scripts/spotify-playlist.ps1 create "{{title}}" "{{desc}}" "{{ispublic}}"

# Añade tracks a una playlist: just playlist-add <id> <uri1> <uri2> ...
playlist-add id *uris:
    pwsh -NoLogo -File scripts/spotify-playlist.ps1 add "{{id}}" {{uris}}

# Elimina una playlist (unfollow): just playlist-delete <id>
playlist-delete id:
    pwsh -NoLogo -File scripts/spotify-playlist.ps1 delete "{{id}}"

# Busca en Spotify: just playlist-search "término" track|artist|playlist
playlist-search term type="track":
    pwsh -NoLogo -File scripts/spotify-playlist.ps1 search "{{term}}" "{{type}}"

# Lista tracks de una playlist: just playlist-tracks <id>
playlist-tracks id:
    pwsh -NoLogo -File scripts/spotify-playlist.ps1 tracks "{{id}}"

# Crea playlist NUEVA con tracks, elimina la vieja: just playlist-upload <oldId> "Título" "Descripción" true/false --file <uriFile>
# El uriFile contiene un URI por línea (spotify:track:...). La URL cambia cada vez.
playlist-upload id title desc ispublic *uris:
    pwsh -NoLogo -File scripts/spotify-playlist.ps1 upload "{{id}}" "{{title}}" "{{desc}}" "{{ispublic}}" {{uris}}

# ─── Playlist Outreach ─────────────────────────────────────

# Genera documento de DMs desde el CSV: just outreach-generate
outreach-generate:
    pwsh -NoLogo -File .claude/skills/playlist-outreach/scripts/generate-dms.ps1

# Marca un artista como contacted|replied|no_reply|skipped en el CSV
# Uso: just outreach-mark "Alex Ferreira" contacted
outreach-mark artist status:
    $csv=Import-Csv "contacts/playlist-artists.csv"; $c=0; $csv|ForEach-Object {if($_.Artist -eq "{{artist}}"){$_.Status="{{status}}";$c++}}; if($c-eq0){Write-Host "No encontrado: {{artist}}";exit 1}; $csv|Export-Csv "contacts/playlist-artists.csv" -NoTypeInformation -Encoding UTF8; Write-Host "OK {{artist}} -> {{status}} ($c registros)"

# Muestra estado del outreach: just outreach-status
outreach-status:
    $csv=Import-Csv "contacts/playlist-artists.csv"; $u=$csv|Sort-Object Artist -Unique; Write-Host "Total: $(($u|Measure-Object).Count)  Pending: $(($u|Where-Object Status -eq 'pending'|Measure-Object).Count)  Contacted: $(($u|Where-Object Status -eq 'contacted'|Measure-Object).Count)  Replied: $(($u|Where-Object Status -eq 'replied'|Measure-Object).Count)  No_reply: $(($u|Where-Object Status -eq 'no_reply'|Measure-Object).Count)"

# Voice analysis: just voice-analysis "<PREFIX><RANGE> <ARTIST>"
# PREFIX: F or M + voice type acronym (S, MS, A, C, T, BT, B)
# RANGE: vocal range e.g. E2-G6 (use # if needed)
# ARTIST: acronym of artist name omitting vowels, all caps
# Output file: voces/<PREFIX>_<RANGE>_<ARTIST>.md
voice-analysis prefix range artist:
    @if (!(Test-Path "voces")) { mkdir voces }
    $prefix=$(echo "{{prefix}}" | tr -d '\n')
    $range=$(echo "{{range}}" | tr -d '\n')
    $artist=$(echo "{{artist}}" | tr -d '\n')
    $filename=$(printf "%s_%s_%s.md" "$prefix" "$range" "$artist" | tr ' ' '_' | tr '[:lower:]' '[:upper:]')
    {{node}} src/voice-analysis.js "{{prefix}}" "{{range}}" "{{artist}}" > voces/$filename

# ─── Ayuda ─────────────────────────────────────────────────

default:
    @just --list

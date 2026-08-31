# Suno Backup — Documentación

## Resumen

Sistema de descarga masiva de clips de Suno a formato local (MP3 + m4a-opus), organizado por proyecto, con persistencia de progreso y base de datos SQLite con metadata completa.

## Archivos creados/modificados

| Archivo | Descripción |
|---------|-------------|
| `scripts/suno-index.py` | Indexa 2319 clips con metadata completa vía API de Suno |
| `scripts/suno-db-sync.py` | Sincroniza index JSON a base de datos SQLite |
| `scripts/download_all_suno.py` | Descarga MP3 + m4a-opus con checkpoint y retry |
| `canciones/audio/bksuno/_downloads.sqlite` | Base de datos con metadata (37 columnas) |
| `canciones/audio/bksuno/` | Estructura de archivos por proyecto |

## API de Suno

### Autenticación

- **Endpoint**: `https://studio-api.prod.suno.com`
- **Auth**: `Authorization: Bearer {jwt_from__session_cookie}`
- **Endpoint de feed**: `GET /api/feed/v2?page=N&page_size=50`
- **Endpoint por IDs**: `GET /api/feed/v2?ids=id1,id2,...` (incluye `media_urls`)

### URLs de audio (construidas directamente)

El endpoint `/api/feed/v2?page=N` **no incluye** `media_urls` ni `audio_url`. Las URLs se construyen así:

| Formato | URL |
|---------|-----|
| MP3 | `https://cdn1.suno.ai/{id}.mp3` |
| m4a-opus | `https://d2lwuy8qc234o3.cloudfront.net/1/clip/{id}.m4a` |

### Campos disponibles en metadata

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `metadata.prompt` | string | **Lyrics** (vacío para instrumentales) |
| `metadata.tags` | string | **Style prompt** (equivalente a `gpt_description_prompt`) |
| `metadata.duration` | float | Duración en segundos |
| `metadata.can_remix` | bool | `false` = instrumental |
| `metadata.make_instrumental` | bool | Flag de generación (siempre `false`) |
| `metadata.has_stem` | bool | Stems disponibles |
| `display_tags` | string | Tags auto-generados |
| `major_model_version` | string | Versión del modelo (ej: `v5.5`) |

### Instrumental vs Vocal

- **Primary**: `metadata.prompt` vacío = instrumental
- **Secondary**: `metadata.can_remix === false` = instrumental

### WAV — Disponible (2026-08-15, verificado en vivo)

**CORRECCIÓN:** El endpoint WAV SÍ existe. La documentación previa era incorrecta.

Flujo de descarga WAV (procesado server-side, requiere Suno Pro):

| Paso | Endpoint | Método | Descripción |
|---|---|---|---|
| 1 | `/api/gen/{clip_id}/convert_wav/` | POST | Dispara conversión server-side a WAV |
| 2 | `/api/gen/{clip_id}/wav_file/` | GET | Poll hasta obtener `wav_file_url` (máx 60s) |
| 3 | `{wav_file_url}` | GET | Download directo del CDN (`cdn1.suno.ai`) |

URLs de audio (construidas directamente o desde API):
- **WAV**: convertido server-side, URL: `https://cdn1.suno.ai/{id}.wav` (~45 MB, 24-bit/48kHz)
- **MP3**: `https://cdn1.suno.ai/{id}.mp3`
- **m4a-opus**: `https://d2lwuy8qc234o3.cloudfront.net/1/clip/{id}.m4a`

La conversión WAV no consume créditos (operación server-side sobre clips ya generados).

## Estructura de directorios

```
canciones/audio/bksuno/
├── _downloads.sqlite          # Base de datos con metadata
├── .suno-download-checkpoint.json  # Estado de descarga
├── My_Workspace/              # 939 clips (Unassigned en Suno)
│   ├── song1.mp3
│   └── song1.m4a
├── Instrumental_1/            # 468 clips
├── Lab/                       # 187 clips
├── Historic/                  # 161 clips
├── Otros90s/                  # 113 clips
├── Recordings/                # 63 clips
├── Finished/                  # 54 clips
├── De_poetas_y_sapoetas/      # 52 clips
├── Voices/                    # 43 clips
├── Church/                    # 30 clips
├── _La_oficina_de_objetos_perdidos/  # 30 clips
├── _Rare Metals/              # 27 clips
├── _Arrendajo_de_invierno/    # 26 clips
├── Al_encuentro_del_amor/     # 23 clips
├── Sonidos/                   # 23 clips
├── Karaoke/                   # 18 clips
├── _Singles/                  # 14 clips
├── De_buen_humor/             # 12 clips
├── _TVO_en_la_TV/             # 10 clips
├── De_caballeros_y_dragones/  # 8 clips
├── Protegidas/                # 6 clips
├── Lo_imposible/              # 5 clips
├── Demos/                     # 4 clips
├── Cymatics/                  # 1 clip
├── Fronteras/                 # 1 clip
├── Seeds/                     # 1 clip
└── sam/                       # 1 clip
```

## Esquema SQLite

```sql
CREATE TABLE clips (
    id TEXT PRIMARY KEY,
    title TEXT,
    status TEXT,
    created_at TEXT,
    model_name TEXT,
    major_model_version TEXT,
    project_id TEXT,
    project_name TEXT,
    project_description TEXT,
    duration REAL,
    mp3_url TEXT,
    m4a_url TEXT,
    image_url TEXT,
    image_large_url TEXT,
    lyrics TEXT,
    style_prompt TEXT,
    display_tags TEXT,
    is_instrumental BOOLEAN,
    can_remix BOOLEAN,
    has_stem BOOLEAN,
    play_count INTEGER,
    upvote_count INTEGER,
    user_id TEXT,
    display_name TEXT,
    handle TEXT,
    is_public BOOLEAN,
    is_hidden BOOLEAN,
    is_trashed BOOLEAN,
    explicit BOOLEAN,
    has_hook BOOLEAN,
    batch_index INTEGER,
    created_by TEXT,
    downloaded INTEGER DEFAULT 0,
    local_path TEXT,
    mp3_local_path TEXT,
    m4a_local_path TEXT,
    downloaded_at TEXT
);

CREATE INDEX idx_project ON clips(project_name);
CREATE INDEX idx_instrumental ON clips(is_instrumental);
CREATE INDEX idx_downloaded ON clips(downloaded);
```

## Uso

### 1. Actualizar index

```powershell
python scripts/suno-index.py
```

Requiere `SUNO_COOKIE` en `.env` con cookie fresca de Suno (el JWT expira).

Obtener cookie fresca:
1. Abrir Suno en navegador
2. F12 → Console → `document.cookie`
3. Copiar valores de `__client`, `__session`, `__session_Jnxw-muT`
4. Reemplazar `SUNO_COOKIE=` en `.env`

### 2. Sincronizar a SQLite

```powershell
python scripts/suno-db-sync.py
```

Crea el `SQLite` y subdirectorios por proyecto.

### 3. Descargar

```powershell
python scripts/download_all_suno.py
```

- Descarga MP3 + m4a-opus
- Organiza por proyecto (`bksuno/{project_name}/`)
- Resume desde checkpoint (`.suno-download-checkpoint.json`)
- Retry con backoff exponencial (5 intentos)
- Actualiza SQLite con `downloaded=1` y paths

### 4. Limpiar y reintentar

```powershell
# Borrar checkpoint y archivos parciales
del .suno-download-checkpoint.json
del /s /q canciones\audio\bksuno\*.tmp

# Re-ejecutar
python scripts/download_all_suno.py
```

## Estadísticas finales

| Métrica | Valor |
|---------|-------|
| Total clips en index | 2,328 |
| Clips en DB | 2,319 |
| Descargados | 2,319 |
| Proyectos | 23 |
| Instrumentales detectados | ~400+ |
| Formato MP3 | `cdn1.suno.ai/{id}.mp3` |
| Formato m4a-opus | `d2lwuy8qc234o3.cloudfront.net/1/clip/{id}.m4a` |
| Formato WAV | `cdn1.suno.ai/{id}.wav` (requiere conversión server-side, Suno Pro) |
| WAV consume créditos | **No** — conversión es server-side sobre clips ya generados (verificado 2026-08-15) |

## Descarga de WAVs (2026-08-15, via Suno Manager en Podman)

**IMPORTANTE:** La conversión WAV no consume créditos. Se puede descargar toda la biblioteca sin afectar el balance.

**Flujo:** POST `/api/gen/{clip_id}/convert_wav/` → poll GET `/api/gen/{clip_id}/wav_file/` → download CDN

- Cada WAV ≈ 19-45 MB (16-bit/48kHz/estéreo, server-side conversion)
- Conversión server-side toma ~60s (poll cada 2-4s)
- Descarga adicional ~30s por clip
- **2000 clips ≈ 30-40 horas** (procesamiento secuencial)
- Usar `suno-manager-wav` container en Podman (`podman exec` para scripts)

## Problemas encontrados y soluciones

| Problema | Causa | Solución |
|----------|-------|----------|
| `Auth expired (401)` | JWT expira (~1h) | Renovar `SUNO_COOKIE` en `.env` |
| URLs vacías en DB | `/api/feed/v2?page=N` no incluye `media_urls` | Construir URLs directamente con `{id}` |
| `WinError 183` (file exists) | Archivos `.tmp` pendientes | `clean_tmp_files()` al inicio |
| `WinError 32` (file in use) | Archivo bloqueado por otro proceso | Esperar/renovar |
| `UnicodeEncodeError` | Caracteres Unicode (✓ ✗) en Python 3.7 | Reemplazar por `[OK]` / `[FAIL]` |
| Index no actualiza | Endpoints cambian, cookies expiran | Regenerar index con cookie fresca |

## Notas

- El proyecto "Unassigned" en Suno se mapea a `My_Workspace` en disco
- Los títulos se sanitizan: espacios→`_`, caracteres especiales eliminados, máx 200 chars
- El script descarga **solo lo que falta** (si MP3 existe, solo baja m4a)
- El checkpoint guarda IDs completados y intentos fallidos (max 5 retries)

# 007 — Spotify API & Playlist Management

## Authorization Code Flow

### 1. Redirect URI — Restricciones (desde Nov 2025)

- `localhost` **no está permitido**
- Solo loopback IP literal: `http://127.0.0.1:PORT` o `http://[::1]:PORT`
- HTTP solo permitido para loopback; cualquier otro debe ser HTTPS
- El trailing slash `/` debe coincidir EXACTAMENTE entre lo registrado y la request
- Registrar en Spotify Developer Dashboard → app → Settings → Redirect URIs

**App: playlister (client_id: a71a05d01e87436e863eb717b975a421)**
**Redirect URI registrada: `http://127.0.0.1:8080/callback/`**

### 2. Scopes necesarios

| Propósito | Scopes |
|-----------|--------|
| Leer playlists propias y seguidas | `playlist-read-private playlist-read-collaborative` |
| Modificar/eliminar/crear playlists | `playlist-modify-private playlist-modify-public` |

### 3. Authorization URL

```
GET https://accounts.spotify.com/authorize
  ?client_id={CLIENT_ID}
  &response_type=code
  &redirect_uri={REDIRECT_URI}
  &scope={SCOPES}
```

### 4. Token Exchange

```
POST https://accounts.spotify.com/api/token
  Content-Type: application/x-www-form-urlencoded
  Authorization: Basic {base64(client_id:client_secret)}

  grant_type=authorization_code
  code={CODE}
  redirect_uri={EXACT_REDIRECT_URI}
```

- `redirect_uri` debe coincidir EXACTAMENTE con el usado en la autorización (incluyendo trailing slash)
- Responsel: `access_token` (1h), `refresh_token`

### 5. Callback Server (TcpListener)

Usar `System.Net.Sockets.TcpListener` en lugar de `System.Net.HttpListener` porque HttpListener requiere trailing slash en el prefix pero Spotify puede redirigir con o sin él.

## API Endpoints

### Lectura

| Endpoint | Uso | Notas |
|----------|-----|-------|
| `GET /v1/me` | Perfil del usuario (`id`, `display_name`, `followers.total`) | |
| `GET /v1/me/playlists?limit=50&offset=N` | Listar playlists propias y seguidas | Paginar hasta `total` |
| `POST /v1/me/playlists` | Crear playlist | Body JSON: `{name, public, description}` |
| `GET /v1/playlists/{id}` | Detalle de playlist | Incluye `followers.total` y `items.items[]` con tracks |

### Modificación

| Endpoint | Uso | Notas |
|----------|-----|-------|
| `DELETE /v1/playlists/{id}/followers` | Eliminar/unfollow playlist propia | Requiere `playlist-modify-public/private` |

### Endpoints deprecados / no funcionales

| Endpoint | Problema |
|----------|----------|
| `GET /v1/playlists/{id}/tracks` | Retorna 403 (deprecado) |
| `POST /v1/users/{user_id}/playlists` | Retorna 403 (usar `/v1/me/playlists`) |

## Estructura de datos

### Playlist Object (GET /v1/me/playlists)

```json
{
  "id": "5RluBtdtrbvE41bBuuG41R",
  "name": "Major Tom Biographical History",
  "description": "Tracking the story of Major Tom through time",
  "public": true,
  "collaborative": false,
  "owner": { "id": "12141566464", "display_name": "Juan Pablo Marichal" },
  "items": { "total": 35 },           // ← track count (NO "tracks")
  "followers": { "total": 0 },        // ← solo disponible en detalle
  "external_urls": { "spotify": "..." },
  "snapshot_id": "...",
  "images": [ ... ]
}
```

Nota: el campo es `items.total` para tracks, no `tracks.total` (que puede ser null).

### Playlist Item (track dentro de playlist)

```json
{
  "added_at": "2026-06-01T02:20:22Z",
  "added_by": { "id": "12141566464" },
  "item": {                          // ← NO es "track", es "item"
    "id": "6XhccyJwqQwbzLO29ooyKw",
    "name": "Que Das la Vida para Dar Vida",
    "artists": [{ "name": "JPMarichal" }],
    "album": { "name": "..." }
  }
}
```

## Métricas disponibles vs no disponibles

### Desde API pública
- `followers.total` — cuántos siguen la playlist
- `items.total` — cantidad de tracks
- `public`, `collaborative`
- `name`, `description`, `images`, `snapshot_id`
- Contenido de tracks (artista, álbum, id)

### Solo desde Spotify for Artists (NO via API)
- Veces que se guardó/reprodujo una playlist
- Tasa de skip/save por track
- Crecimiento histórico de seguidores
- "Discovered On" source
- Demografía de oyentes
- Source of Streams split

## Estrategia de gestión de playlists

### Playlists valiosas para promoción propia
- **Canciones de JPMarichal Playlist** — catálogo propio (27 tracks de JPMarichal)
- **Major Tom Biographical History** — curada manualmente, 35 tracks
- Cualquier playlist con seguidores (>0) tiene alcance orgánico

### Playlists contraproducentes
- Playlists generadas por Chosic / herramientas masivas (~100-102 tracks idénticos, descripciones vacías o repetitivas)
- Playlists que nadie sigue (0 seguidores) y no tienen un propósito curatorial claro
- Estas consumen espacio en el perfil sin aportar engagement

### Cómo identificar Chosic
- Descripción: `"Created with Playlist Generator from chosic.com"`
- Track count sospechosamente exacto (100-105)
- Descripciones repetitivas entre playlists
- Nombres genéricos sin propósito específico

## Notas técnicas

### PowerShell
- Usar `@{Authorization = "Bearer $token"}` para headers
- Para ordenar por múltiples columnas: `Sort-Object @{e="Col1"; d=$true}, @{e="Col2"; d=$true}`
- Variables con `:` después requieren `${variable}` en strings
- `Invoke-RestMethod` no expone `$_.Exception.Response.GetResponseStream()` en PS Core — usar try/catch con `$_.Exception.Message`

### Rate Limiting
- Sin delay agresivo: ~200-300ms entre calls es seguro
- Playlist detail rate: ~1 call/250ms para ~50 playlists funciona
- Para batches grandes (>100), espaciar más

### Token Refresh
- Access token expira en 3600s (1h)
- El refresh token no expira (a menos que se revoque)
- Para refrescar: `POST /api/token` con `grant_type=refresh_token` y `refresh_token={REFRESH_TOKEN}` (mismo Basic auth)

**⚠️ Error común — extraer refresh token de `.env`:**
```powershell
# ❌ INCORRECTO: el regex espera espacio después de =
$refresh = $line -replace '.*= ', ''

# ✅ CORRECTO: split por primer =
$refresh = ($line -split '=', 2 | Select-Object -Last 1).Trim()
```

El archivo `.env` usa formato `CLAVE=valor` sin espacio alrededor de `=`. La regex `'.*= '` (con espacio tras el =) no coincide y devuelve la línea completa, causando `invalid_grant`.

### Popularidad — limitación post-Feb 2026
Desde febrero 2026, Spotify restringió el campo `popularity` en la Web API para apps creadas después del 6-Feb-2026 en modo development. Nuestra app `playlister` fue creada después, por lo tanto:
- `GET /v1/tracks/{id}` → `popularity: null`
- `GET /v1/artists/{id}` → `popularity: null`
- `GET /v1/search` → `popularity: null`

Esto **no es un error** — es la nueva política de Spotify. La `popularity` (0-100) es el único proxy de "streams" disponible en la Web API, y no está disponible para apps nuevas en dev mode.

**Alternativa real**: usar **Spotify for Artists** (dashboard web, no API) que sí muestra:
- Streams por canción
- Save rate (saves ÷ streams)
- Skip rate
- Fuente de streams (playlists editoriales, algorítmicas, biblioteca propia)
- Crecimiento de monthly listeners
- Playlist placements actuales

El save rate (>3-4% es saludable) es la métrica de engagement más confiable.

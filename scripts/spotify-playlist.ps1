#!/usr/bin/env pwsh
# Spotify Playlist Manager
# Operaciones mecánicas de playlists vía API de Spotify
# Lee SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REFRESH_TOKEN del .env
#
# Uso:
#   .\scripts\spotify-playlist.ps1 create "Título" "Descripción" true/false
#   .\scripts\spotify-playlist.ps1 add <playlistId> <uri1> <uri2> ...
#   .\scripts\spotify-playlist.ps1 delete <playlistId>
#   .\scripts\spotify-playlist.ps1 search "término" type (track|artist|playlist)
#   .\scripts\spotify-playlist.ps1 tracks <playlistId>
#   .\scripts\spotify-playlist.ps1 upload <playlistId> "Título" "Descripción" true/false <uri1> <uri2> ...
#
# NOTA IMPORTANTE: No se puede eliminar tracks de una playlist via API
# (DELETE /items devuelve 400/403). El comando 'upload' crea una playlist
# NUEVA y elimina (unfollow) la vieja. La URL cambia cada vez.

param(
    [string]$Action,
    [string]$Arg1,
    [string]$Arg2,
    [string]$Arg3
)

# ─── Cargar .env ─────────────────────────────────────────────
$envPath = Join-Path (Split-Path -Parent $PSScriptRoot) ".env"
if (Test-Path $envPath) {
    Get-Content $envPath | ForEach-Object {
        if ($_ -match '^\s*([^#=]+)\s*=\s*(.+)\s*$') {
            $k = $matches[1].Trim()
            $v = $matches[2].Trim().Trim('"', "'")
            Set-Item -Path "env:$k" -Value $v
        }
    }
}
$clientId = $env:SPOTIFY_CLIENT_ID
$clientSecret = $env:SPOTIFY_CLIENT_SECRET
$refreshToken = $env:SPOTIFY_REFRESH_TOKEN

if (-not $clientId -or -not $clientSecret -or -not $refreshToken) {
    Write-Error "Faltan credenciales en .env: SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REFRESH_TOKEN"
    exit 1
}

# ─── Helpers ─────────────────────────────────────────────────
function Get-AccessToken {
    $body = @{ grant_type = "refresh_token"; refresh_token = $refreshToken }
    $cred = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes("${clientId}:${clientSecret}"))
    $tokens = Invoke-RestMethod -Uri "https://accounts.spotify.com/api/token" -Method Post -Body $body `
        -Headers @{Authorization = "Basic $cred"} -ContentType "application/x-www-form-urlencoded"
    return $tokens.access_token
}

function Invoke-Spotify {
    param([string]$Method, [string]$Path, $Body)
    $token = Get-AccessToken
    $headers = @{Authorization = "Bearer $token"; "Content-Type" = "application/json"}
    $uri = "https://api.spotify.com/v1/$Path"
    $params = @{Uri = $uri; Method = $Method; Headers = $headers}
    if ($Body) { $params["Body"] = ($Body | ConvertTo-Json -Compress -Depth 10) }
    try {
        return Invoke-RestMethod @params
    } catch {
        $err = $_.Exception.Response
        $reader = New-Object System.IO.StreamReader($err.GetResponseStream())
        Write-Error "API Error: $($reader.ReadToEnd())"
        exit 1
    }
}

# ─── Actions ─────────────────────────────────────────────────
switch ($Action) {

    "create" {
        # create "Título" "Descripción" true/false
        # Usa POST /me/playlists — NO /users/{id}/playlists (devuelve 403)
        $name = $Arg1; $desc = $Arg2; $isPublic = $Arg3 -eq "true"
        $body = @{name = $name; description = $desc; public = $isPublic}
        $r = Invoke-Spotify -Method Post -Path "me/playlists" -Body $body
        Write-Output "Creada: $($r.name)"
        Write-Output "ID: $($r.id)"
        Write-Output "URL: $($r.external_urls.spotify)"
        return @{id = $r.id; url = $r.external_urls.spotify}
    }

    "add" {
        # add <playlistId> <uri1> <uri2> ...
        # Usa POST /playlists/{id}/items
        $playlistId = $Arg1; $uris = @($Arg2, $Arg3) + $args | Where-Object { $_ }
        if ($uris.Count -eq 0) { Write-Error "Faltan URIs"; exit 1 }
        $body = @{uris = @($uris)}
        $r = Invoke-Spotify -Method Post -Path "playlists/$playlistId/items" -Body $body
        Write-Output "Añadidas $($uris.Count) tracks"
    }

    "update" {
        # update <playlistId> "Nuevo Nombre" "Nueva Descripción"
        $playlistId = $Arg1; $name = $Arg2; $desc = $Arg3
        $body = @{}
        if ($name) { $body["name"] = $name }
        if ($desc) { $body["description"] = $desc }
        $r = Invoke-Spotify -Method Put -Path "playlists/$playlistId" -Body $body
        Write-Output "Actualizada: $($r.name)"
    }

    "delete" {
        # delete <playlistId>
        # DELETE /playlists/{id}/followers — unfollow (elimina de tu biblioteca)
        $playlistId = $Arg1
        $r = Invoke-Spotify -Method Delete -Path "playlists/$playlistId/followers"
        Write-Output "Playlist $playlistId eliminada"
    }

    "search" {
        # search "término" type (track|artist|playlist)
        $q = $Arg1; $type = if ($Arg2) { $Arg2 } else { "track" }
        $r = Invoke-Spotify -Method Get -Path "search?q=$([System.Uri]::EscapeDataString($q))&type=$type&limit=10"
        $items = $r.tracks ?? $r.artists ?? $r.playlists
        if (-not $items) { Write-Output "Sin resultados"; return }
        $c = 1
        $items.items | ForEach-Object {
            if ($type -eq "track") {
                Write-Output "${c}. $($_.name) — $($_.artists[0].name) | $($_.uri)"
            } elseif ($type -eq "artist") {
                Write-Output "${c}. $($_.name) | followers: $($_.followers.total) | $($_.uri)"
            } else {
                Write-Output "${c}. $($_.name) | $($_.owner.display_name) | $($_.uri)"
            }
            $c++
        }
    }

    "tracks" {
        # tracks <playlistId>
        $playlistId = $Arg1
        $r = Invoke-Spotify -Method Get -Path "playlists/$playlistId"
        Write-Output "Playlist: $($r.name) — $($r.items.total) tracks"
        Write-Output "URL: $($r.external_urls.spotify)"
        Write-Output ""
        $c = 1
        $r.items.items | ForEach-Object {
            $t = $_.item
            if ($t -and $t.name) {
                Write-Output "${c}. $($t.name) — $($t.artists[0].name) | $($t.uri)"
                $c++
            }
        }
    }

    "upload" {
        # upload <oldPlaylistId> "Título" "Descripción" true|false --file <uriFile>
        #
        # IMPORTANTE: La API NO permite eliminar tracks de una playlist existente
        # (DELETE /items devuelve 400/403). Esta función:
        #   1. Crea una playlist NUEVA
        #   2. Añade todos los tracks
        #   3. Elimina (unfollow) la playlist vieja
        # La URL CAMBIA cada vez.
        $oldId = $Arg1
        $name = $Arg2; $desc = $Arg3; $isPublic = $false
        # $args = overflow args after param captures: [isPublic] [--file path] or [isPublic] [uri1 uri2...]
        if ($args.Count -ge 1) {
            $isPublic = $args[0] -eq "true"
        }
        $uris = @()
        if ($args.Count -ge 3 -and $args[1] -eq "--file") {
            $uris = @(Get-Content $args[2] | Where-Object { $_ -match '^spotify:track:' })
        } elseif ($args.Count -ge 2) {
            $uris = @($args[1..($args.Count - 1)]) | Where-Object { $_ -match '^spotify:track:' }
        }
        Write-Output "  Upload: $($uris.Count) URIs, isPublic=$isPublic"

        # 1. Create new playlist
        Write-Output "Creando nueva playlist..."
        $newPl = Invoke-Spotify -Method Post -Path "me/playlists" -Body @{
            name = $name; description = $desc; public = $isPublic
        }
        Write-Output "  Creada: $($newPl.id)"

        # 2. Add tracks in batches of 100
        Write-Output "Añadiendo $($uris.Count) tracks..."
        $batchSize = 100
        for ($i = 0; $i -lt $uris.Count; $i += $batchSize) {
            $batch = $uris[$i..([Math]::Min($i + $batchSize - 1, $uris.Count - 1))]
            Invoke-Spotify -Method Post -Path "playlists/$($newPl.id)/items" -Body @{uris = @($batch)} | Out-Null
        }
        Write-Output "  $($uris.Count) tracks añadidas"

        # 3. Delete old playlist (unfollow)
        Write-Output "Eliminando playlist vieja..."
        try {
            Invoke-Spotify -Method Delete -Path "playlists/$oldId/followers" | Out-Null
            Write-Output "  Playlist vieja eliminada"
        } catch {
            Write-Output "  No se pudo eliminar (ignorado)"
        }

        Write-Output "`nCompletado."
        Write-Output "Nueva URL: $($newPl.external_urls.spotify)"
        return @{id = $newPl.id; url = $newPl.external_urls.spotify}
    }

    default {
        Write-Output @"
Spotify Playlist Manager
Uso:
  create "Título" "Descripción" true|false   — Crear playlist (nueva cada vez)
  add <id> <uri1> [uri2...]                   — Añadir tracks a playlist existente
  delete <id>                                  — Eliminar playlist (unfollow)
  search "término" [type]                      — Buscar tracks/artists/playlists
  tracks <id>                                  — Listar tracks de una playlist
  upload <id> "Título" "Descripción" true|false <uri1> [uri2...] — Crea nueva + elimina vieja

NOTA: No se puede modificar tracks de una playlist existente via API.
upload crea una playlist NUEVA y elimina la anterior. La URL cambia.
"@
    }
}

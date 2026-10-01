# Playlist Outreach — DM Generator

Genera mensajes listos para copiar y pegar a artistas de las playlists.

## Flujo

1. **El CSV** `contacts/playlist-artists.csv` contiene todos los artistas contactables con su estado.
   - `Status = pending` → no contactado aún
   - `Status = contacted` → DM enviado
   - `Status = replied` → respondió
   - `Status = no_reply` → sin respuesta tras 7 días
   - `Status = skipped` → no contactar (ej: ya contactado antes)

2. **Generar DMs**: `just outreach-generate`
   - Lee el CSV, filtra `pending`
   - Agrupa por artista (un DM por artista, aunque esté en varias playlists)
   - Genera `contacts/outreach/dms-pl1-pl2.md`

3. **Enviar DMs**: abrir `contacts/outreach/dms-pl1-pl2.md`, copiar cada bloque y pegarlo en Instagram.

4. **Registrar envío**: tras enviar un DM, ejecutar:
   ```
   just outreach-mark "Alex Ferreira" contacted
   just outreach-mark "Ases Falsos" contacted
   ```

5. **Seguimiento**: tras 7 días, marcar como `no_reply` los que no respondieron.

## Reglas

- **Nunca contactar al mismo artista más de una vez**, aunque aparezca en playlists nuevas.
- Solo artistas **B (<10k ML)** y **C (10k-100k ML)** — los D ni responden.
- El CSV ya tiene el filtro aplicado (solo contactables).
- Si un artista responde, actualizar Status a `replied` en el CSV.

## Template DM

```
Hola @artista, soy curador de "[Playlist_Name]" en Spotify.
Acabo de incluir "[Track]" porque encaja perfecto con el mood de la playlist.
Si te gusta el proyecto, agradecería un share en stories. ¡Un abrazo!

🎵 [Playlist_URL]
```

Para artistas en dos playlists:

```
Hola @artista, soy curador de dos playlists en Spotify que incluyen tu música.
- "[Track1]" en "[Playlist1]"
- "[Track2]" en "[Playlist2]"
Si te gusta el proyecto, agradecería un share en stories. ¡Un abrazo!

🎵 [Playlist1_URL]
🎵 [Playlist2_URL]
```

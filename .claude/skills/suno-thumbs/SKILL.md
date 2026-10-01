---
name: suno-thumbs
description: >
  Descarga thumbnails (cover art) de Suno AI para las canciones del catálogo.
  Busca en el índice local de Suno (suno-index.json) los clips que coinciden
  con cada canción, obtiene la image_url vía API de Suno, y guarda las imágenes
  en canciones/thumbs/. Soporta filtrado por distribuidor (OffStep por defecto)
  o descarga para una canción específica.
---

## Qué hace

- Escanea `canciones/*.md` en busca del campo `**Distribuidor:**`
- Filtra por distribuidor (OffStep por defecto)
- Busca clips coincidentes en `suno-index.json` por fuzzy matching de título
- Obtiene `image_url` vía API de Suno (`get_songs_by_ids`)
- Descarga los thumbnails a `canciones/thumbs/`
- Omite archivos ya descargados (idempotente)

## Cómo usarlo

### Todas las canciones de OffStep
```
just suno-thumbs
```

### Canciones de otro distribuidor
```
just suno-thumbs --distributor "DistroXYZ"
```

### Canción específica (por slug o parte del nombre)
```
just suno-thumbs "farolas-sin-luz"
just suno-thumbs "amor"
```

## Requisitos

- `suno-index.json` actualizado (`just suno-index`)
- `.env` con `SUNO_COOKIE` configurada
- Conexión a Internet (descarga de imágenes desde CDN de Suno)

## Output

Las imágenes se guardan en `canciones/thumbs/` con nombre:
```
{slug}_{clip_id[:8]}_{sanitized_title}.jpg
```

## Songs renamed after Suno generation

If a song was generated in Suno under one name but later renamed for distribution,
add a `**Título Suno:**` field in the song's metadata block pointing to the
original Suno title. The script will use this as a fallback when slug matching
fails.

Example (farolas-sin-luz.md):
```markdown
- **Generador:** SUNO
- **Título Suno:** Angel nocturno
```

## Notas

- Idempotente: no redescarga si el archivo ya existe
- Las canciones sin clips en el índice local se saltan con un aviso
- Usa fuzzy matching para emparejar títulos de canciones (slugs kebab-case contra títulos Unicode de Suno)
- Estrategia de búsqueda: 1) slug del filename → 2) `Título Suno` si existe → 3) título de canción completo

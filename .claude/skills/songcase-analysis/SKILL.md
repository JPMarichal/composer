---
name: songcase-analysis
description: >
  Análisis exhaustivo de canciones existentes (no del catálogo propio) para
  crear casos de estudio en inspiration/. Combina metadata de APIs (Spotify,
  Deezer), progresiones armónicas de CifraClub/Hooktheory/Songsterr, análisis
  local con librosa, y análisis lírico-estructural. Cada songcase se indexa
  en el RAG para consulta posterior.
---

# Songcase Analysis

## Cuándo activarlo

Cuando el usuario pida:
- "Analiza esta canción" / "Haz un análisis de X"
- "Investiga la progresión de X"
- "Cómo es la estructura de X"
- "Qué acordes usa X"
- "Dame un songcase de X"
- "Documenta X como caso de estudio"
- "Busca covers/versiones de X"
- Cualquier request de investigación musical externa

## Fuentes de datos

| Fuente | Qué obtener | Cómo |
|--------|-------------|------|
| **Spotify API** | BPM, key, mode, energy, danceability, valence, acousticness, loudness, time signature | `suno-account_get_songs_by_ids` (si se tiene URL) o websearch con `site:open.spotify.com/track/ "<canción>" "<artista>"` para obtener track ID, luego inferir de la documentación pública |
| **Deezer API** | BPM, gain, ISRC, rank, release date, preview URL | `just deezer "<canción>" "<artista>"` |
| **CifraClub** | Acordes, progresión, tonalidad | Websearch con `site:cifraclub.com "<canción>" "<artista>"` |
| **Hooktheory** | Análisis armónico, función de acordes | Websearch con `site:hooktheory.com/theorytab "<canción>" "<artista>"` |
| **Songsterr / Ultimate Guitar** | Tabs, acordes alternativos | Websearch |
| **MusicBrainz** | Créditos, ISRC, discogs release data | Websearch con `site:musicbrainz.org "<canción>" "<artista>"` |
| **Wikipedia** | Contexto, historia, recepción | Websearch |
| **Songfacts** | Significado, historia, entrevistas | Websearch con `site:songfacts.com "<canción>" "<artista>"` |
| **YouTube** | Análisis visual, tutoriales | Websearch |
| **Análisis local (librosa)** | BPM real, key real, energía, danceability, valence, spectral features | Si se tiene el archivo MP3/WAV: `just audio-analyze "<path>"` |

## Workflow

### Paso 1: Recopilar metadata básica

```
1. Buscar en Spotify el track ID → https://open.spotify.com/track/{id}
2. Buscar en Deezer → just deezer "<canción>" "<artista>"
3. Buscar en MusicBrainz para créditos y discografía exacta
4. Buscar compositores, productores, año, sello
```

### Paso 2: Obtener progresión armónica

```
1. Buscar en CifraClub → websearch site:cifraclub.com "<canción>" "<artista>"
2. Buscar en Hooktheory para análisis funcional
3. Buscar en Songsterr / Ultimate Guitar para verificar
4. Transcribir acordes por sección en formato | Sección | Acordes |
```

### Paso 3: Analizar estructura

```
1. Identificar secciones (Intro, Verse, Chorus, Bridge, Outro...)
2. Mapear duraciones y compases aproximados
3. Identificar la forma general (AABA, verse-chorus, strophic, etc.)
```

### Paso 4: Analizar letra

```
1. Obtener letra completa de Spotify/LyricFind o websearch
2. Identificar tema central, recursos literarios, figuras retóricas
3. Esquema de rima
4. Conexiones intertextuales
```

### Paso 5: Analizar producción

```
1. Instrumentación por sección
2. Tratamiento vocal (registro, textura, entrega)
3. Mezcla (si hay información disponible)
```

### Paso 6: Escribir el songcase

```
1. Usar el template: inspiration/SONG-TEMPLATE.md
2. Nombre del archivo: inspiration/<artista>-<cancion-kebab-case>.md
   Ejemplo: inspiration/sheryl-crow-mrs-major-tom.md
3. Rellenar todas las secciones posibles
4. Marcar como "—" lo que no se pudo verificar
```

### Paso 7: Indexar (opcional)

```
just ingest
```

Esto incluirá `inspiration/` en el RAG, permitiendo consultas como:
"qué progresiones usa el pop de los 2000s" o "cómo se estructura una balada electrónica"

## Formato del archivo

Cada songcase sigue `inspiration/SONG-TEMPLATE.md` con estas secciones obligatorias:

1. **Identificación** — metadatos básicos de la canción
2. **Audio Features** — Spotify, Deezer, librosa
3. **Armonía** — tonalidad, progresión base, acordes por sección
4. **Estructura** — mapa de secciones, forma general
5. **Letra** — texto completo
6. **Esquema de rima**
7. **Análisis lírico** — tema, recursos, figuras, intertextualidad, contexto
8. **Producción** — instrumentación, vocal, mezcla
9. **Versiones y diferencias**
10. **Fuentes** — todas las URLs consultadas

## Reglas

1. No adivinar acordes ni progresiones — si no hay fuente fiable, dejar como `—`
2. Distinguir siempre entre versión original y covers analizados
3. Si Spotify/Deezer no tienen la canción, anotarlo — no inventar valores
4. Las fuentes deben ser verificables: incluir URLs
5. Letra completa siempre; si copyright es restrictivo, poner la estructura (no el texto completo)
6. El archivo debe nombrarse `<artista>-<cancion>.md` en kebab-case
7. Los songcases son para canciones **existentes** (no del catálogo propio) — las del catálogo van en `canciones/`

## Comandos útiles

```bash
# Consultar Deezer (BPM, ISRC, gain)
just deezer "Blinding Lights" "The Weeknd"

# Búsqueda completa Deezer + preview + análisis librosa
just lookup "Bohemian Rhapsody" "Queen"

# Analizar archivo local con librosa
just audio-analyze "path/to/song.mp3"

# Reindexar todo incluyendo inspiration/
just ingest
```

## Ejemplos de aplicación

**Input del usuario:** "Analiza Mrs. Major Tom de Sheryl Crow"
**Output esperado:** Archivo `inspiration/sheryl-crow-mrs-major-tom.md` con:
- Metadata: álbum Seeking Major Tom, 2011, 5:47
- Audio Features: ~118 BPM, key D major (o G major), 4/4
- Acordes: D-G-D-D7-G en verso, D-C-G en puente
- Letra completa con meta-tags
- Análisis intertextual: respuesta a Space Oddity/Ashes to Ashes
- 3 versiones documentadas: K.I.A. 2003, Sheryl Crow 2011, K.I.A. 2026

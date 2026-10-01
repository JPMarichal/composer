# Song Case — <Título> — <Artista>

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | |
| **Artista** | |
| **Versión analizada** | original / cover / remix / en vivo |
| **Álbum** | |
| **Año** | |
| **Duración** | |
| **ISRC** | |
| **Género(s)** | | <!-- Principal(es); ej. Pop, Rock, Balada, Tango -->
| **Compositor(es)** | |
| **Productor(es)** | |
| **Sello** | |
| **País** | |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — valores aproximados (pueden variar según el cliente).

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | | |
| **Key** | | (0=C, 1=C#/Db…) |
| **Mode** | major / minor | |
| **Camelot** | | |
| **Danceability** | 0–1 | |
| **Energy** | 0–1 | |
| **Valence** | 0–1 | (positividad musical) |
| **Acousticness** | 0–1 | |
| **Instrumentalness** | 0–1 | |
| **Speechiness** | 0–1 | |
| **Liveness** | 0–1 | |
| **Loudness** | dB | |
| **Time Signature** | | |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/{id}`

| Feature | Valor |
|---------|-------|
| **BPM** | |
| **Gain** | dB |
| **Rank** | |
| **Explicit** | sí / no |
| **Release Date** | |
| **Preview URL** | |

### 2.3 Análisis local (librosa) — opcional

> Cuando se disponga del archivo de audio.

| Feature | Valor |
|---------|-------|
| **BPM (librosa)** | |
| **Key (librosa)** | |
| **Mode** | |
| **Energy** | |
| **Danceability** | |
| **Valence** | |
| **Spectral Centroid** | Hz |
| **Onset Density** | ataques/s |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| | major / minor | |

### 3.2 Progresión base

```
I   ii   iii   IV   V   vi   vii°
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | | | |
| Verse | | | |
| Pre-Chorus | | | |
| Chorus | | | |
| Bridge | | | |
| Outro | | | |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro]         → [Verse 1]       → [Chorus]       → [Verse 2] ...
 I              vi  IV  V         I  IV  V  IV      vi  IV  I  V
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

### 4.2 Forma general

```
[Intro] [V1] [C] [V2] [C] [Puente] [C] [Outro]
```

---

## 5. Letra

```
[Sección]
...
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | | |
| Chorus | | |
| Verse 2 | | |
| Bridge | | |

---

## 7. Análisis lírico

### 7.1 Tema central

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| | | |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| | |

### 7.4 Conexión intertextual

> Referencias a otras canciones, obras, o cultura.

### 7.5 Contexto de composición

> Historia detrás de la canción, declaraciones del artista, recepción crítica.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| | | |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | |
| Textura | |
| Entrega | |
| Capas | (armonías, doublings, ad-libs) |

### 8.3 Mezcla y dinámica

- **Rango dinámico:**
- **Panning:**
- **Efectos destacados:**
- **Producción general:**

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original | |
| Cover 1 | |
| Cover 2 | |

---

## 10. Fuentes

- **Spotify:** `<url>`
- **Deezer:** `<url>`
- **CifraClub:** `<url>`
- **Hooktheory:** `<url>`
- **Songsterr / Ultimate Guitar:** `<url>`
- **Wikipedia / MusicBrainz:** `<url>`
- **Entrevistas / artículo:** `<url>`

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | |
| **Fecha del análisis** | |
| **Modelo RAG asociado** | |
| **Tags** | |
| **Pendientes** | (cosas por verificar) |

# Song Case — Perfect — Ed Sheeran

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Perfect |
| **Artista** | Ed Sheeran |
| **Versión analizada** | original |
| **Álbum** | ÷ (Divide) |
| **Año** | 2017 |
| **Duración** | 4:23 |
| **ISRC** | GBAHS1700024 |
| **Género(s)** | Pop, Soft Rock, Balada romántica, Adult Contemporary |
| **Compositor(es)** | Ed Sheeran |
| **Productor(es)** | Ed Sheeran, Will Hicks |
| **Sello** | Asylum Records / Atlantic |
| **País** | Reino Unido |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — valores aproximados (pueden variar según el cliente).

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 95 | 12/8 feel; alternativamente 63 BPM en 3/4 (getsongbpm) |
| **Key** | 8 | 8 = A♭ |
| **Mode** | major | |
| **Camelot** | 4B | |
| **Danceability** | 0.48 | |
| **Energy** | 0.38 | |
| **Valence** | 0.17 | (baja para ser canción de amor — énfasis en ternura más que euforia) |
| **Acousticness** | 0.68 | |
| **Instrumentalness** | 0.00 | |
| **Speechiness** | 0.03 | |
| **Liveness** | 0.11 | |
| **Loudness** | −8.5 dB | |
| **Time Signature** | 4 | 4/4 con subdivisión ternaria (12/8) |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/{id}`

| Feature | Valor |
|---------|-------|
| **BPM** | 95 |
| **Gain** | −10 dB |
| **Rank** | — |
| **Explicit** | no |
| **Release Date** | 2017-03-03 |
| **Preview URL** | — |

### 2.3 Análisis local (librosa) — opcional

> Cuando se disponga del archivo de audio.

| Feature | Valor |
|---------|-------|
| **BPM (librosa)** | — |
| **Key (librosa)** | — |
| **Mode** | — |
| **Energy** | — |
| **Danceability** | — |
| **Valence** | — |
| **Spectral Centroid** | — |
| **Onset Density** | — |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| A♭ | major | alta — 5 fuentes independientes |

### 3.2 Progresión base

Grados: I   ii   iii   IV   V   vi   vii°
         A♭  B♭m  Cm   D♭   E♭  Fm   Gm

Progresión principal: **I — vi — IV — V** (A♭ — Fm — D♭ — E♭)

En G (con capo traste 1, tono de ejecución común): **G — Em — C — D**

### 3.3 Acordes por sección

| Sección | Acordes (en A♭) | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | A♭ | I | Voz sola, entrada a capella |
| Verse | A♭ — Fm — D♭ — E♭ | I — vi — IV — V | Dos ciclos por verse |
| Pre-Chorus | A♭ — Fm — D♭ — E♭ | I — vi — IV — V | Misma progresión, varía melodía y dinámica |
| Chorus | Fm — D♭ — A♭ — E♭ → ... → D♭ — E♭ | vi — IV — I — V → ... → IV — V | Orden alterado: empieza en vi, resuelve a IV–V |
| Bridge | Fm — D♭ — A♭ — E♭ (x4) → A♭ — E♭ — Fm — E♭ — D♭ — E♭ | vi — IV — I — V → I — V — vi — V — IV — V | Subdivisión rítmica más densa |
| Outro | A♭ — Fm — D♭ — E♭ | I — vi — IV — V | Fade out con fingerpicking |

### 3.4 Diagrama de la progresión

```
[Intro]       → [Verse 1]        → [Pre-Chorus]     → [Chorus]           → [Verse 2]
 I              I  vi  IV  V        I  vi  IV  V        vi  IV  I  V         I  vi  IV  V

→ [Pre-Chorus] → [Chorus]          → [Bridge]                          → [Chorus] → [Outro]
   I  vi  IV  V    vi  IV  I  V       vi  IV  I  V (x4) → I  V  vi  V  IV  V   vi  IV  I  V   I  vi  IV  V
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00 | ~8 | 2 | A♭ | A capella, voz sola |
| 2 | Verse 1 | 0:08 | ~24 | 8 | A♭—Fm—D♭—E♭ x2 | Fingerpicking acústico |
| 3 | Pre-Chorus | 0:32 | ~16 | 4 | A♭—Fm—D♭—E♭ | Entra piano/bajo |
| 4 | Chorus | 0:48 | ~32 | 8 | Fm—D♭—A♭—E♭ x2 | Entra batería |
| 5 | Verse 2 | 1:20 | ~24 | 8 | A♭—Fm—D♭—E♭ x2 | Letra nueva, misma base |
| 6 | Pre-Chorus | 1:44 | ~16 | 4 | A♭—Fm—D♭—E♭ | Mayor intensidad vocal |
| 7 | Chorus | 2:00 | ~32 | 8 | Fm—D♭—A♭—E♭ x2 | Textura completa |
| 8 | Bridge | 2:32 | ~48 | 12 | vi—IV—I—V x4 → I—V—vi—V—IV—V | Clímax, falsete, breakdown |
| 9 | Chorus | 3:20 | ~40 | 10 | Fm—D♭—A♭—E♭ | Sube tonal? — No, mismo tono |
| 10 | Outro | 4:00 | ~23 | 8 | A♭—Fm—D♭—E♭ | Fade con fingerpicking |

### 4.2 Forma general

```
[Intro a capella] [V1] [Pre-C] [C] [V2] [Pre-C] [C] [Bridge] [C] [Outro]
```

Duración total: ~4:23. Sin intro instrumental — arranque a capella es la marca distintiva.

---

## 5. Letra

```
[Intro]
I found a love for me

[Verse 1]
I found a love for me
Darling, just dive right in and follow my lead
Well, I found a girl, beautiful and sweet
I never knew you were the someone waiting for me

[Pre-Chorus]
'Cause we were just kids when we fell in love
Not knowing what it was
I will not give you up this time
But darling, just kiss me slow, your heart is all I own
And in your eyes, you're holding mine

[Chorus]
Baby, I'm dancing in the dark, with you between my arms
Barefoot on the grass, listening to our favorite song
When you said you looked a mess, I whispered underneath my breath
But you heard it, darling, you look perfect tonight

[Verse 2]
Well, I found a woman, stronger than anyone I know
She shares my dreams, I hope that someday I'll share her home
I found a love, to carry more than just my secrets
To carry love, to carry children of our own

[Pre-Chorus]
We are still kids, but we're so in love
Fighting against all odds
I know we'll be alright this time
Darling, just hold my hand, be my girl, I'll be your man
I see my future in your eyes

[Chorus]
Baby, I'm dancing in the dark, with you between my arms
Barefoot on the grass, listening to our favorite song
When I saw you in that dress, looking so beautiful
I don't deserve this, darling, you look perfect tonight

[Bridge]
Baby, I'm dancing in the dark, with you between my arms
Barefoot on the grass, listening to our favorite song
I have faith in what I see, now I know I have met an angel
In person, and she looks perfect tonight

[Chorus]
Baby, I'm dancing in the dark, with you between my arms
Barefoot on the grass, listening to our favorite song
When you said you looked a mess, I whispered underneath my breath
But you heard it, darling, you look perfect tonight

[Outro]
Perfect tonight
You look perfect tonight
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABB | me/lead, sweet/me |
| Pre-Chorus 1 | AAB BCCB | love/was, time → slow/own/mine |
| Chorus | ABCB DEDE | dark/arms/grass/song; mess/breath/darling/tonight |
| Verse 2 | AABB CDCD | know/home, secrets/love → own/tonight — menos rígido |
| Pre-Chorus 2 | AAB BBCB | love/odds → time, hand/man/eyes |
| Bridge | AABB CCDD | dark/arms, grass/song; see/angel → person/tonight |

Esquema general: verso pareado (AABB) con estribillo de rima alterna (ABCB). La rima se flexibiliza en secciones de mayor carga emocional (Bridge).

---

## 7. Análisis lírico

### 7.1 Tema central

Amor idealizado que trasciende la apariencia física. Celebración de la pareja como destino inevitable (amigos de infancia → amantes → familia). Narrativa de compromiso total: "I will not give you up this time."

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Metáfora | "dancing in the dark" | Intimidad sin artificios; lo público vs. lo privado |
| Hipérbole | "stronger than anyone I know" | Idealización de la pareja |
| Anáfora | "I found a love… I found a girl… I found a love… I found a woman" | Acumulación progresiva: love → girl → love → woman |
| Imagen sensorial | "barefoot on the grass, listening to our favorite song" | Escena táctil-auditiva, anclaje concreto (regla de sustantivo concreto) |
| Ironía dramática | "when you said you looked a mess, I whispered… but you heard it" | Lo que el oyente sabe que ella sí escuchó |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Apóstrofe | "darling…" (interpelación directa permanente) |
| Pleonasmo | "to carry love, to carry children of our own" |
| Asíndeton | "barefoot on the grass, listening to our favorite song" (sin conectores) |
| Epífora | "tonight" al final de cada línea del chorus y del final |
| Progresión semántica | kids → girl → woman → love → children → angel |

### 7.4 Conexión intertextual

- El artista declaró explícitamente querer "superar a 'Thinking Out Loud'" como legado. Ambas comparten: waltz/12/8, dedicatoria amorosa, progresión I–vi–IV–V.
- La inspiración del chorus viene de bailar "March Madness" de Future en el jardín de James Blunt en Ibiza — contraste maximalista (trap/hardcore → balada acústica).
- El video homenajea a East 17 "Stay Another Day" (nieve sin referencia navideña en la letra).

### 7.5 Contexto de composición

Escrita para Cherry Seaborn, amiga de la infancia (colegio en Suffolk, luego se reencontraron en 2015). Sheeran la grabó y se la envió estando ella en Nueva York. Grabación en solitario con un ingeniero. Producida por Sheeran con asistencia de Will Hicks. El hermano Matthew Sheeran (compositor clásico) arreglaría cuerdas para la versión Bocelli.

Recepción: UK #1, US #1, 52 semanas en Billboard Hot 100, 3.99 billones de impresiones radiofónicas en 2018. Canción más sonada de la radio estadounidense en 2018.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Guitarra acústica | Intro, Verses, Outro | Fingerpicking, patrón de arpegio constante |
| Piano | Pre-Chorus → Chorus | Acompaña el build, dobla melodía en Chorus |
| Bajo | Chorus, Bridge | Entrada discreta en Chorus |
| Batería | Chorus, Bridge | Patrón mínimo: bombo en 1 y 3, hi-hat |
| Cuerdas | Bridge, Chorus final | Swell en el bridge, textura orquestal |
| Pads sintéticos | Chorus | Capa atmosférica apenas audible |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Medio (G3–G#4) — rango contenido, sin aspirar al agudo extremo |
| Textura | Voz natural, pocos efectos; ligero reverb de sala |
| Entrega | Conversacional en verso, expandida en chorus, falsete en bridge |
| Capas | Doubling en chorus final; armónicas a 3as en "tonight" |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Medio (~10 dB entre intro y clímax)
- **Panning:** Guitarra centrada, cuerdas ligeramente a L/R en bridge
- **Efectos destacados:** Reverb de sala (no hall); compresión suave en voz; fade-out natural sin corte brusco
- **Producción general:** Minimalismo orgánico — la producción no compite con la voz. La balada crece por acumulación instrumental, no por cambios de tonalidad.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (single, 2017) | Producción acústica, voz solista, fade-out |
| Perfect Duet (con Beyoncé, 2017) | Re-grabada en NY; Beyoncé canta segunda voz (estrofa propia + armonías); piano más prominente; sin fade-out (final sostenido) |
| Perfect Symphony (con Andrea Bocelli, 2017) | Orquestación completa de Matthew Sheeran; Bocelli canta en italiano (estrofa dedicada); cuerdas reales; coro operístico; video con Sheeran aprendiendo italiano |
| En vivo (gira 2018–2019) | Tono transportado a G major (sin capo); a menudo solo voz + guitarra loop; audiencia como coro |

---

## 10. Fuentes

- **Spotify:** `https://open.spotify.com/track/0tgVpDi06FyKpA1z0VMD4v`
- **Deezer:** `https://www.deezer.com/track/137267574`
- **CifraClub:** `https://www.cifraclub.com/ed-sheeran/perfect/`
- **Hooktheory:** `https://www.hooktheory.com/theorytab/view/ed-sheeran/perfect`
- **Songsterr / Ultimate Guitar:** — (no verificada)
- **Wikipedia / MusicBrainz:** `https://en.wikipedia.org/wiki/Perfect_(Ed_Sheeran_song)`
- **Entrevistas / artículo:** Songfacts — `https://www.songfacts.com/facts/ed-sheeran/perfect`

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | JPMarichal + opencode |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | — |
| **Tags** | pop, balada, waltz, 2017, ÷, wedding-song, love-song, acoustic |
| **Pendientes** | Verificar audio features exactos de Spotify (valores aproximados); verificar compás (12/8 vs 3/4) con análisis librosa; añadir cifra completa de CifraClub |

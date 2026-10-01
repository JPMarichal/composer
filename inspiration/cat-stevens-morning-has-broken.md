# Song Case — Morning Has Broken — Cat Stevens

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Morning Has Broken |
| **Artista** | Cat Stevens (Yusuf Islam) |
| **Versión analizada** | original — remasterizada 2021 |
| **Álbum** | Teaser and the Firecat |
| **Año** | 1971 (álbum) / 7 enero 1972 (single) |
| **Duración** | 3:20 (200 s) |
| **ISRC** | GBUM72104758 |
| **Género(s)** | Folk-pop, Christian hymn |
| **Compositor(es)** | Eleanor Farjeon (letra, 1931), melodía tradicional escocesa «Bunessan». Arreglo: Cat Stevens. Piano adicional: Rick Wakeman |
| **Productor(es)** | Paul Samwell-Smith |
| **Sello** | Island Records |
| **País** | Reino Unido |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — valores aproximados (pueden variar según el cliente). Track original 1971.

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 129–132 | 3/4, vals lento |
| **Key** | C / D | Versos 1,2,4 en C; intro, v3 y outro en D |
| **Mode** | major | |
| **Camelot** | 8B (C) / 10B (D) | |
| **Danceability** | 0.25 | Himno, no bailable |
| **Energy** | 0.20 | Íntimo, acústico |
| **Valence** | 0.30 | Contemplativo-serena |
| **Acousticness** | 0.95 | Predominantemente acústico |
| **Instrumentalness** | 0.0001 | Voz clara y presente |
| **Speechiness** | 0.03 | Cantado, no hablado |
| **Liveness** | 0.10 | Estudio |
| **Loudness** | −15.0 dB | Dinámica suave |
| **Time Signature** | 3/4 | Vals; notado en 9/4 en himnarios |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/1550811202`

| Feature | Valor |
|---------|-------|
| **BPM** | 0 (no detectado por Deezer) |
| **Gain** | −12.4 dB |
| **Rank** | 654,789 |
| **Explicit** | no |
| **Release Date** | 2021-11-19 (remasterizada) |
| **Preview URL** | [Deezer preview](https://cdnt-preview.dzcdn.net/api/1/1/e/c/b/0/ecb3d12cb1f74a6a6b7862cef0127f4d.mp3) |

### 2.3 Análisis local (librosa) — opcional

> Sin archivo de audio local disponible para este análisis.

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| C Major / D Major | major | Alta — cambios de tonalidad intencionales entre secciones |

### 3.2 Progresión base

```
I   ii   iii   IV   V   vi   vii°
C   Dm   Em    F    G   Am   B°
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | D — G — A — F# — Bm — G7 — C — F — C | D: I-IV-V-#IV(b5)-vi-IV7 → modula a C: IV-I | Puente pianístico de Wakeman, tomado de «Catherine Howard» |
| Verse 1 (C) | C Dm G F C \| Em Am D G \| C F C Am D \| G C F G7 C | I-ii-V-IV-I \| iii-vi-II-V \| I-IV-I-vi-II \| V-I-IV-V7-I | D7 actúa como V/V |
| Interludio 1 | F G E Am G C G7sus4 | IV-V-III-vi-V-I-V7sus4 | Breve cita instrumental |
| Verse 2 (C) | idem V1 | | |
| Interludio 2 | F G E Am F# Bm G D A7 D | IV-V-III-vi → modula a D: #IV(b5)-vi-IV-I-V7-I | El F# es pivote: bVI en C → #IV(b5) en D; el pasaje Bm-G-D-A7-D establece D mayor |
| Verse 3 (D) | D Em A G D \| F# Bm E7 A \| D G D Bm E \| A D G A D | I-ii-V-IV-I \| #iii-vi-III7-V \| I-IV-I-vi-III \| V-I-IV-V-I | Tonalidad más alta, clímax lírico-armónico |
| Interludio 3 | G A F# Bm G7 C F C | IV-V-#IV(b5)-vi-IV7 → modula a C: IV-I | Retorno a C |
| Verse 4 (C) | idem V1 | | Reafirmación |
| Outro | F G E Am F# Bm G D A7 D | IV-V-III-vi-#IV(b5)-vi-IV-I-V7-I | Cierre en D, sin resolver a C |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro: D]      → [V1: C]   → [Interludio]  → [V2: C]   → [Interludio]
D-G-A-F#-Bm-G7    I-ii-V-IV    IV-V-III-vi      I-ii-V-IV    IV-V-III-vi → modula a D
  C-F-C           iii-ii-V     I-V-I-V7sus4     iii-ii-V     #IV(b5)-vi

→ [V3: D]       → [Interludio] → [V4: C]   → [Outro: D]
  I-ii-V-IV        IV-V-#IV(b5)   I-ii-V-IV    IV-V-III-vi-#IV(b5)-vi
  #iii-vi-III7-V   vi-IV7-IV-I    iii-ii-V     IV-I-V7-I
  I-IV-I-vi-III                     I-IV-I-V7-I
  V-I-IV-V-I
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:13 | ~13 | 2 × 4 compases | D G A F# Bm G7 C F C | Piano solo, arpegios de Wakeman |
| 2 | Verse 1 | 0:13–0:44 | ~31 | 8 compases | I-ii-V-IV / iii-vi-II-V / I-IV-I-vi-II / V-I-IV-V7-I | 4 frases de 2 compases c/u |
| 3 | Interludio 1 | 0:44–0:52 | ~8 | ~2 compases | F G E Am G C G7sus4 | Puente breve |
| 4 | Verse 2 | 0:52–1:23 | ~31 | 8 compases | idem V1 | |
| 5 | Interludio 2 | 1:23–1:34 | ~11 | ~4 compases | F G E Am F# Bm G D A7 D | Modulación a D |
| 6 | Verse 3 | 1:34–2:05 | ~31 | 8 compases | I-ii-V-IV / #iii-vi-III7-V / I-IV-I-vi-III / V-I-IV-V-I | Clímax en D |
| 7 | Interludio 3 | 2:05–2:16 | ~11 | ~4 compases | G A F# Bm G7 C F C | Retorno a C |
| 8 | Verse 4 | 2:16–2:47 | ~31 | 8 compases | idem V1 | Repite letra de V1 |
| 9 | Outro | 2:47–3:20 | ~33 | ~8 compases | F G E Am F# Bm G D A7 D | Cierre en D |

### 4.2 Forma general

```
[Intro] [V1] [Inst] [V2] [Inst → mod D] [V3] [Inst → mod C] [V4] [Outro]
   D       C    C      C      D maj         D      C maj        C     D
```

---

## 5. Letra

```

[Verse 1]
Morning has broken, like the first morning
Blackbird has spoken, like the first bird
Praise for the singing, praise for the morning
Praise for them springing fresh from the Word

[Verse 2]
Sweet the rain's new fall, sunlit from heaven
Like the first dew fall on the first grass
Praise for the sweetness of the wet garden
Sprung in completeness where His feet pass

[Verse 3]
Mine is the sunlight, mine is the morning
Born of the one light Eden saw play
Praise with elation, praise every morning
God's recreation of the new day

[Verse 4]
Morning has broken, like the first morning
Blackbird has spoken, like the first bird
Praise for the singing, praise for the morning
Praise for them springing fresh from the Word
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | A A B B C C D D | broken/morning — spoken/bird — singing/morning — springing/Word |
| Verse 2 | A A B B C C D D | fall/heaven — dew fall/grass — sweetness/garden — completeness/pass |
| Verse 3 | A A B B C C D D | sunlight/morning — light/play — elation/morning — recreation/day |
| Verse 4 | A A B B C C D D | Repite esquema de V1 |

**Métrica:** 5.5.5.4 D (dactílica) — cada línea tiene ~5 sílabas, patrón de himno. Cada estrofa de 8 líneas agrupadas en 4 pareados, con rima AA BB CC DD.

---

## 7. Análisis lírico

### 7.1 Tema central

Acción de gracias por el nuevo día como renovación del acto creador. Cada amanecer es una recreación del Edén — «God's recreation of the new day». Himno de alabanza matutino que conecta Génesis 1 con la experiencia cotidiana del despertar.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Símil | «like the first morning», «like the first bird», «Like the first dew fall» | Cuatro símiles que atan cada imagen presente al origen primordial |
| Metáfora | «fresh from the Word» | El amanecer brota directamente de la Palabra creadora (Logos) |
| Personificación | «Blackbird has spoken» | El mirlo adquiere voz profética |
| Sinestesia | «Sweet the rain's new fall, sunlit from heaven» | Fusión de sensaciones: dulzura táctil + luz visual + origen celestial |
| Quiasmo | «Praise for the singing, praise for the morning» | Estructura especular que enfatiza la acción de gracias |
| Aliteración | «springing / fresh from» | S fricativa que evoca el brotar de la hierba |
| Hipálage | «sunlit from heaven» | La lluvia recibe el atributo del sol |
| Anáfora | «Praise for...» / «Praise with...» | Repetición insistente que estructura cada estrofa como letanía |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Símil | «Morning has broken like the first morning» |
| Metáfora | «fresh from the Word» (Palabra = fuente de vida) |
| Sinécdoque | «where His feet pass» (los pies de Dios = Su presencia en el Edén) |
| Hipérbaton | «Sweet the rain's new fall» (inversión del orden sintáctico) |
| Pleonasmo | «God's recreation of the new day» (re- + new, refuerzo) |
| Enálage | «Sprung in completeness» (participio por adjetivo) |
| Exclamación retórica implícita | Tono de alabanza sostenido |

### 7.4 Conexión intertextual

- **Bíblica directa:** Génesis 1 (creación), Génesis 3:8 (Dios paseando en el huerto al atardecer — «where His feet pass»), Juan 1:1 (el Logos/Palabra creadora — «fresh from the Word»).
- **Himnaria:** La melodía «Bunessan» se usaba originalmente con el villancico escocés «Child in the Manger». El metro 5.5.5.4 D es inusual en himnología.
- **Literaria:** Eleanor Farjeon fue una poeta infantil reconocida. El poema fue encargado por Percy Dearmer para *Songs of Praise* (1931). La versión original en gaélico escocés fue escrita por Mary MacDonald (1789–1872).
- **Cat Stevens:** Cancelación / secuestro espiritual: Stevens descubrió el himno en una tienda de libros de segunda mano durante un período de sequía creativa. Buscaba canciones de dominio público. La transformación de un himno de 45 segundos a una canción de 3:20 con modulaciones es un caso de estudio de arreglo pop.

### 7.5 Contexto de composición

> «Morning Has Broken» es un himno cristiano de 1931 con letra de Eleanor Farjeon (1881–1965) sobre una melodía tradicional escocesa llamada «Bunessan» (de la isla de Mull). Farjeon fue comisionada por el editor Percy Dearmer para escribir una canción de gratitud matutina. La letra se inspira en el pueblo de Alfriston, East Sussex.

> Cat Stevens descubrió el himno en una librería de viejo durante un bloqueo creativo mientras buscaba material para completar *Teaser and the Firecat*. La canción original duraba ~45 segundos; su productor Paul Samwell-Smith le dijo que necesitaba al menos tres minutos. Stevens escuchó a Rick Wakeman tocando un boceto de lo que sería «Catherine Howard» y le pidió adaptar el pasaje como intro, sección media y cierre. Wakeman accedió por £10 —años después Stevens le pagó y Wakeman donó el dinero a una escuela islámica.

> La canción alcanzó el #6 en el Billboard Hot 100 y #1 en Adult Contemporary. Es una rareza: un himno cristiano del siglo XX que se convierte en éxito pop masivo.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Piano acústico | Toda la canción | Rick Wakeman — arpegios tipo «Catherine Howard». Crucial para la identidad sonora |
| Guitarra acústica (steel-string) | Acompañamiento | Cat Stevens — rasgueo suave en 3/4 |
| Guitarra acústica (segunda) | Textura | Alun Davies — fingerpicking de apoyo |
| Bajo acústico / eléctrico | Base rítmica | Poco prominente en la mezcla |
| Batería | Leve, solo platillos | Gerry Conway / Harvey Burns — apenas perceptible, escobillas |
| Bouzouki | Color | Andreas Toumazis, Angelos Hatzipavli — textura folk |
| Cuerdas (sección) | Arco | Arreglos de Del Newman — refuerzo armónico sutil |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Tenor ligero (C4–G4 aprox.) |
| Textura | Voz solista principal, sin armonías dobladas |
| Entrega | Suave, casi susurrada, con calidez folk. Pronunciación británica cuidada. Sin vibrato excesivo |
| Capas | Voz única en primer plano. Sin backing vocals ni ad-libs |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Amplio para la época — el piano entra solo (pp), la voz se suma (mp), versos en mf, clímax del V3 en D (mf→f). No hay compresión excesiva.
- **Panning:** Voz centrada. Piano ligeramente a la izquierda. Guitarras acústicas derecha e izquierda. Cuerdas en campo amplio.
- **Efectos destacados:** Reverb de sala natural (Morgan Studios). Sin efectos artificiales notables. El sonido es orgánico, con la calidez del tape analógico.
- **Producción general:** Paul Samwell-Smith optó por un enfoque minimalista y respetuoso con el origen himnario. La producción es transparente —cada instrumento se escucha sin competir. La decisión más audaz fue la modulación a D para el V3, que eleva la canción emocionalmente.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (Cat Stevens, 1971) | Piano de Wakeman, guitarras acústicas, modulación C→D→C→D. Arreglo pop-himno |
| Himno tradicional (1931) | Canto congregacional, sin modulación, tempo más lento, órgano. Sin piano arpegiado |
| Rick Wakeman (2000, instrumental) | Piano solo, versión extendida. Sin voz. Énfasis en el material de «Catherine Howard» |
| Judy Collins | Voz femenina, arreglo más folk, menos piano virtuoso |
| Hayley Westenra | Voz soprano, arreglo orquestal completo, más lento, énfasis en la textura coral |
| Nana Mouskouri | Versión en alemán «Schön ist der Morgen» |
| Libera (choir) | Voz infantil, arreglo coral etéreo, tempo más lento |

---

## 10. Fuentes

- **Spotify:** `https://open.spotify.com/track/5mNBF10RzdnmoAvlzabgUO`
- **Deezer:** `https://www.deezer.com/track/1550811202`
- **CifraClub:** `https://www.cifraclub.com/cat-stevens/morning-has-broken/`
- **Hooktheory:** No disponible en Hooktheory
- **Ultimate Guitar:** `https://www.guitaretab.com/c/cat-stevens/274002.html`
- **Wikipedia:** `https://en.wikipedia.org/wiki/Morning_Has_Broken`
- **Songfacts:** `https://www.songfacts.com/facts/cat-stevens/morning-has-broken`
- **Hymnary:** `https://hymnary.org/text/morning_has_broken`
- **Bell&CoMusic:** `https://www.bellandcomusic.com/morning-has-broken-chords.html`

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | JPMarichal (asistido por opcode) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | gemma4 / mistral:7b |
| **Tags** | `cat-stevens`, `morning-has-broken`, `folk-pop`, `hymn`, `1971`, `rick-wakeman`, `eleanor-farjeon`, `songcase`, `uk`, `bunessan` |
| **Pendientes** | Verificar audio features exactos de Spotify API; análisis librosa opcional si se obtiene archivo WAV |

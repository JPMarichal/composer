# Song Case — You're So Vain — Carly Simon

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Deezer), análisis armónico de fuentes web (CifraClub, Ultimate Guitar), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | You're So Vain |
| **Artista** | Carly Simon |
| **Versión analizada** | Original (1972) |
| **Álbum** | No Secrets |
| **Año** | 1972 |
| **Duración** | 4:19 (single) / 4:18 (Deezer compilation) |
| **ISRC** | USEE19900883 |
| **Género(s)** | Soft rock, Pop |
| **Compositor(es)** | Carly Simon |
| **Productor(es)** | Richard Perry |
| **Sello** | Elektra Records |
| **País** | Estados Unidos |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 106.01 |
| **Gain** | -12.1 dB |
| **Rank** | 699,334 |
| **Explicit** | No |
| **Release Date** | 2008-01-21 (compilation) |
| **Preview URL** | Deezer track 766109 |

### 2.2 Análisis local (librosa) — preview 30s

| Feature | Valor |
|---------|-------|
| **BPM (librosa)** | 107.7 |
| **Key (librosa)** | C (C major, confianza 0.48; tercer chunk detecta F major) |
| **Mode** | Major |
| **Energy** | 0.784 |
| **Danceability** | 0.906 |
| **Valence** | 0.481 |
| **Spectral Centroid** | 2506.5 Hz |
| **Onset Density** | 4.03 ataques/s |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| C / F (ambas reportadas según fuente) | Major | Análisis ambivalente: CifraClub marca F, UG y librosa marcan C. La progresión funciona en ambas — el centro tonal se siente en F en los versos con resolución a C en coros. |

### 3.2 Progresión base (en F)

```
I   ii   iii   IV   V   vi   vii°
F   Gm   Am    Bb   C   Dm   Edim
```

### 3.3 Acordes por sección

| Sección | Acordes (en F) | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | Dm7 | vi | Línea de bajo descendente de Klaus Voormann (icónica) |
| Verse | Dm7 — Bb — F — Bb — Dm7 | vi — IV — I — IV — vi | Estructura circular que evade la tónica |
| Pre-Chorus | Bbmaj7 — C — Am7 — Dm7 — Bb — F | IV — V — iii — vi — IV — I | Tensión ascendente que prepara el coro |
| Chorus | F — Gm7 — F / F — Dm7 — Bbmaj7 — C13 — F | I — ii — I / I — vi — IV — V — I | Resolución completa con V-I en cierre |
| Guitar solo | Sobre progresión de Verse | | |
| Outro | F — Gm7 — F (repetido, fade out) | I — ii — I | |

### 3.4 Diagrama de la progresión

```
[Intro]    → [Verse 1]     → [Pre-Chorus]      → [Chorus]
Dm7         Dm7  Bb  I  IV   Bbmaj7  C  Am7      F  Gm7  F
vi          vi   IV  I  IV   IV      V  iii       I  ii   I
                                    Dm7  Bb  F    F  Dm7  Bbmaj7  C13  F
                                    vi   IV  I    I  vi   IV      V    I
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Compases | Acordes clave | Notas |
|---|---------|----------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:14 | ~8 | Dm7 | Bajo solista, entrada de batería a los 4s |
| 2 | Verse 1 | 0:14–0:42 | ~16 | Dm7 — Bb — F — Bb — Dm7 | Entrada de voz |
| 3 | Chorus | 0:42–1:00 | ~8 | F — Gm7 — F / F — Dm7 — Bbmaj7 — C13 — F | "You're so vain..." |
| 4 | Verse 2 | 1:00–1:28 | ~16 | Dm7 — Bb — F — Bb — Dm7 | "You had me several years ago..." |
| 5 | Chorus | 1:28–1:56 | ~12 | F — Gm7 — F / F — Dm7 — Bbmaj7 — C13 — F | Repite, con variación en "Don't you?" |
| 6 | Guitar solo | 1:56–2:27 | ~16 | Sobre Verse | Solo de Jimmy Ryan |
| 7 | Pre-Chorus | 2:27–2:42 | ~8 | Bbmaj7 — C — Am7 — Dm7 — Bb — F | "I had some dreams..." |
| 8 | Chorus | 2:42–3:10 | ~12 | F — Gm7 — F / F — Dm7 — Bbmaj7 — C13 — F | |
| 9 | Verse 3 | 3:10–3:38 | ~16 | Dm7 — Bb — F — Bb — Dm7 | "Well I hear you went up to Saratoga..." |
| 10 | Chorus | 3:38–4:00 | ~12 | F — Gm7 — F / F — Dm7 — Bbmaj7 — C13 — F | |
| 11 | Outro | 4:00–4:19 | ~8 | F — Gm7 — F (fade) | Repite "You're so vain" en fade |

### 4.2 Forma general

```
[Intro] [V1] [C] [V2] [C] [Solo] [Pre-C] [C] [V3] [C] [Outro]
```

---

## 5. Letra

```
[Intro]
Son of a gun

[Verse 1]
You walked into the party like you were walking onto a yacht
Your hat strategically dipped below one eye
Your scarf it was apricot
You had one eye in the mirror as you watched yourself gavotte
And all the girls dreamed that they'd be your partner
They'd be your partner and

[Chorus]
You're so vain, you probably think this song is about you
You're so vain (you're so vain)
I'll bet you think this song is about you
Don't you? Don't you?

[Verse 2]
You had me several years ago when I was still quite naive
Well, you said that we made such a pretty pair
And that you would never leave
But you gave away the things you loved and one of them was me
I had some dreams, they were clouds in my coffee
Clouds in my coffee and

[Chorus]
You're so vain, you probably think this song is about you
You're so vain (you're so vain)
I'll bet you think this song is about you
Don't you? Don't you? Don't you?

[Guitar Solo]

[Pre-Chorus]
I had some dreams, they were clouds in my coffee
Clouds in my coffee and

[Chorus]
You're so vain, you probably think this song is about you
You're so vain (you're so vain)
I'll bet you think this song is about you
Don't you? Don't you?

[Verse 3]
Well, I hear you went up to Saratoga and your horse naturally won
Then you flew your Learjet up to Nova Scotia
To see the total eclipse of the sun
Well, you're where you should be all the time
And when you're not you're with some underworld spy
Or the wife of a close friend
Wife of a close friend and

[Chorus]
You're so vain, you probably think this song is about you
You're so vain (so vain)
I'll bet you think this song is about you
Don't you? Don't you? Don't you now?

[Outro]
You're so vain, you probably think this song is about you
You're so vain, you probably think this song is about you
You're so vain, you probably think this song is about you
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABBCC | yacht/apricot — eye/gavotte — partner/partner (repetición) |
| Verse 2 | ABABCC | naive/pair — leave/me — coffee/coffee (repetición) |
| Chorus | AABCCDD | vain/about — vain about — you/you — (repetición interna) |
| Verse 3 | ABABCCDD | won/sun — time/spy — friend/friend — (repetición + rima consonante parcial) |

---

## 7. Análisis lírico

### 7.1 Tema central

Narcisismo masculino y desengaño amoroso. La narradora retrata a un ex-amante increíblemente vanidoso, construyendo un retrato en tres viñetas (una por verso) que lo muestran en su elemento: una fiesta, una relación pasada, y su vida de excesos. La genialidad del hook es que el sujeto, por su propia vanidad, nunca reconocerá que la canción habla de él — aunque la canción explícitamente diga que sí.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Metáfora | "Clouds in my coffee" | Sueños empañados, ilusiones rotas — imagen surrealista de claridad enturbiada |
| Símil | "Like you were walking onto a yacht" | Compara la entrada a una fiesta con abordar un yate, sugiriendo entitlement |
| Ironía dramática | "You probably think this song is about you" | El oyente sabe que SÍ es sobre él, pero el sujeto (por vanidad) lo interpreta como que NO |
| Léxico arcaizante | "Gavotte" | Danza francesa del s. XVIII — elección deliberada para subrayar la pretensión |
| Hipérbole | "Flew your Learjet up to Nova Scotia / To see the total eclipse of the sun" | Exceso de estilo de vida casi caricaturesco |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Anáfora | "You're so vain" repetido en cada chorus |
| Apóstrofe | Toda la canción es un "tú" directo al sujeto ausente |
| Interrogación retórica | "Don't you?" — cinco veces al final, casi como abucheo |
| Sinécdoque | "Your scarf it was apricot" — un detalle de vestimenta como símbolo de toda la persona |

### 7.4 Conexión intertextual

- La línea del eclipse solar total alude al eclipse del 7 de marzo de 1970, visible desde Nueva Escocia.
- "Son of a gun" como apertura — expresión coloquial de asombro/desdén.
- La canción ha sido sampleada/referenciada por Nine Inch Nails ("Starfuckers, Inc."), Janet Jackson ("Son of a Gun (I Betcha Think This Song Is About You)"), y Marilyn Manson (cover con Johnny Depp).
- Taylor Swift la cita como su inspiración #1 para escribir sobre ex-famosos.

### 7.5 Contexto de composición

Escrita a lo largo de un año. Originalmente titulada "Bless You, Ben". Simon concibió primero el chorus, y un año después, al ver a un hombre con bufanda entrando a una fiesta y mirándose al espejo, una amiga comentó "parece que está subiendo a un yate" — de ahí nació el verso inicial. Simon usó "gavotte" porque rimaba y porque "eso es lo que un hombre pretencioso y vanidoso haría". La línea "clouds in my coffee" surgió de su pianista Billy Mernit, que notó nubes reflejadas en su café.

Grabada en Trident Studios (Londres) en 1972. Mick Jagger (Rolling Stones) grabó coros no acreditados — se dice que estaba en el estudio grabando otra canción y se ofreció a cantar. La línea de bajo introductoria de Klaus Voormann es una de las más icónicas del rock.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Bajo eléctrico (Klaus Voormann) | Intro y throughout | Línea melódica descendente que define el groove |
| Piano acústico (Carly Simon) | Throughout | Base armónica, arreglo de cuerdas |
| Guitarra eléctrica (Jimmy Ryan) | Versos, solo | Solo en 1:56–2:27 |
| Batería (Jim Gordon) | Throughout | Groove mid-tempo, hi-hat marcado |
| Percusión (Richard Perry) | Acentos | Overdubs adicionales |
| Sección de cuerdas | Arreglo de Paul Buckmaster | Orquestación de Paul Buckmaster sobre el arreglo de Simon |
| Coros (Mick Jagger, Vicki Brown, Liza Strike) | Chorus | Jagger no acreditado — su voz se mezcla en el estribillo |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Mezzosoprano, confortable en el rango medio |
| Textura | Voz principal con capas de backing vocals en coro (incluyendo a Jagger) |
| Entrega | Conversacional en versos, expansiva en coros, con un toque de cinismo contenido |
| Capas | Al menos 3-4 voces superpuestas en el chorus: Simon lidera, Jagger y coristas refuerzan |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Moderado — la canción mantiene un volumen consistente, el clímax está en los coros con la entrada de cuerdas plenas.
- **Panning:** Voz centrada, guitarras ligeramente paneadas, cuerdas en estéreo amplio.
- **Efectos destacados:** Reverb de sala en la voz, delay slap en la guitarra solista.
- **Producción general:** Pulida para la época, con separación limpia entre la sección rítmica (bajo/batería anclados al centro) y los elementos melódicos (voz, cuerdas, guitarra solista).

---

## 9. El Misterio: ¿De quién trata la canción?

La identidad del sujeto es uno de los misterios más famosos de la música popular. Simon ha declarado que **la canción habla de tres hombres diferentes**, uno por verso. Solo ha nombrado públicamente a uno:

| Verso | Sujeto confirmado / especulado | Evidencia |
|-------|-------------------------------|-----------|
| **Verse 1** (fiesta, yate, bufanda) | **David** (apellido no revelado) | Simon susurró "David" en la versión de 2010 (*Never Been Gone*). Se especuló David Geffen (desmentido por Simon), David Bowie, David Cassidy, o David Crosby. Simon confirmó que no es Geffen. |
| **Verse 2** ("You had me several years ago…") | **Warren Beatty** (confirmado) | Simon confirmó a *People* (2015) que el segundo verso es sobre Beatty. Beatty llamó a Simon para agradecerle por "inmortalizarlo", convencido de que toda la canción era sobre él. |
| **Verse 3** (Saratoga, Learjet, eclipse) | **No revelado** (tercer hombre) | Posibles candidatos: Mick Jagger (cantó en la canción), Jack Nicholson, Kris Kristofferson, o el ex-esposo James Taylor. Simon nunca lo ha confirmado. |

En 2003, Simon subastó la respuesta completa por $50,000 — el ganador fue Dick Ebersol (ejecutivo de NBC), quien firmó un acuerdo de confidencialidad y nunca reveló el nombre. En 2015, Simon le susurró la respuesta completa a Taylor Swift después de un concierto en Boston. Swift ha declarado que nunca la revelará.

---

## 10. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (1972) | Producida por Richard Perry, coros de Mick Jagger |
| *Never Been Gone* (2010) | Versión acústica con whisper "David" en el outro |
| Janet Jackson feat. Carly Simon & Missy Elliott (2001) | "Son of a Gun (I Betcha Think This Song Is About You)" — sample + nueva letra |
| Marilyn Manson feat. Johnny Depp (2012) | Versión industrial/rock, Depp toca batería y guitarra solista |
| Taylor Swift & Carly Simon (2013, live) | Dúo en vivo en Gillette Stadium |

---

## 11. Fuentes

- **Wikipedia:** https://en.wikipedia.org/wiki/You're_So_Vain
- **Deezer:** https://www.deezer.com/track/766109
- **CifraClub:** https://www.cifraclub.com/carly-simon/youre-so-vain/
- **Ultimate Guitar:** https://tabs.ultimate-guitar.com/tab/carly-simon/youre-so-vain-chords-845483
- **Genius:** https://genius.com/Carly-simon-youre-so-vain-lyrics
- **Songfacts:** https://www.songfacts.com/facts/carly-simon/youre-so-vain
- **People (2015):** Confirmación de Warren Beatty como segundo verso
- **Yahoo/People:** Carly Simon Reveals 'You're So Vain' Is About Warren Beatty (2015)
- **Carly Simon official site:** https://www.carlysimon.com/youre-so-vain

---

## 12. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (DeepSeek V4 Flash) |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | Composer RAG |
| **Tags** | `songcase`, `carly-simon`, `soft-rock`, `1970s`, `mystery`, `warren-beatty`, `mick-jagger`, `clasico` |
| **Pendientes** | Verificar si la versión original en Spotify tiene features distintas a la compilación Deezer |

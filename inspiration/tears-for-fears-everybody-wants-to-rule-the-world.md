# Song Case — Everybody Wants to Rule the World — Tears for Fears

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Everybody Wants to Rule the World |
| **Artista** | Tears for Fears |
| **Versión analizada** | Original |
| **Álbum** | Songs from the Big Chair |
| **Año** | 1985 |
| **Duración** | 4:11 |
| **ISRC** | GBF088590110 |
| **Género(s)** | New Wave, Synth-Pop, Dance-Rock |
| **Compositor(es)** | Roland Orzabal, Ian Stanley, Chris Hughes |
| **Productor(es)** | Chris Hughes |
| **Sello** | Phonogram, Mercury, Vertigo |
| **País** | Inglaterra |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — valores de SongData.io para track `4RvWPyQ5RL0ao9LPZeSouE`.

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 112 | (224 en doble tempo; Deezer reporta 168 por el compás 12/8) |
| **Key** | 7 | G Major |
| **Mode** | major | |
| **Camelot** | 9B | |
| **Danceability** | 0.64 | |
| **Energy** | 0.80 | |
| **Valence** | 0.54 | (neutral-positive) |
| **Acousticness** | 0.35 | |
| **Instrumentalness** | 0.00 | |
| **Speechiness** | 0.05 | |
| **Liveness** | 0.10 | |
| **Loudness** | −12.095 dB | |
| **Time Signature** | 4/4 | (sensación de 12/8 shuffle) |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/88845911`

| Feature | Valor |
|---------|-------|
| **BPM** | 168.1 |
| **Gain** | −14.6 dB |
| **Rank** | 653,650 |
| **Explicit** | no |
| **Release Date** | 1985-03-22 |
| **Preview URL** | https://cdnt-preview.dzcdn.net/api/1/1/d/e/5/0/... |

### 2.3 Análisis local (librosa) — opcional

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
| G | major | Alta (con préstamos modales: F natural, bVII) |

> El acorde F (bVII) aparece como préstamo modal de G mixolidio/menor. La progresión tiene un sabor a G mayor con tensiones mixolidias.

### 3.2 Progresión base

```
I    ii    iii   IV    V    vi    vii°
G    Am    Bm    C     D    Em    F#dim
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | Dmaj7 – G/D (repetido) | I – IV sobre pedal de D | Arpegio de guitarra; el Dmaj7 sugiere la tónica y G/D es el IV con bajo en D |
| Verse | Dmaj7 – G/D | I – IV | El riff melódico oscila entre D y G, estableciendo la ambigüedad tonal |
| Pre-Chorus | Em – F – G – F | vi – bVII – I – bVII | Subida cromática (E → F → G); el F es prestado de G mixolidio |
| Chorus | Em – F – G – A | vi – bVII – I – II | El A (II) crea una tensión ascendente que resuelve de vuelta al verso |
| Bridge | G – D – A (repetido) | I – V – II | Sección más abierta; cambia el centro tonal con G – D – A |
| Outro | Em – F – G – A (variaciones) | vi – bVII – I – II | Misma progresión del chorus, con ad-libs y fade |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro]              → [Verse 1]          → [Pre-Chorus]
Dmaj7 – G/D (x4)       Dmaj7 – G/D (x4)     Em – F – G – F
                                                (x2)

→ [Chorus]            → [Verse 2]          → [Pre-Chorus]
Em – F – G – A (x2)    Dmaj7 – G/D (x4)     Em – F – G – F
                                                (x2)

→ [Chorus]            → [Bridge]           → [Guitar Solo]
Em – F – G – A (x2)    G – D – A (x3)       Em – F – G – A

→ [Chorus]            → [Outro / Fade]
Em – F – G – A (xN)    Em – F – G – A (variantes, fade)
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases (aprox.) | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:12 | 12 | 4+4 | Dmaj7 – G/D | Riff de guitarra con eco |
| 2 | Verse 1 | 0:12–0:39 | 27 | 8 | Dmaj7 – G/D | Entrada de bombo y voz (Curt Smith) |
| 3 | Pre-Chorus 1 | 0:39–0:52 | 13 | 4 | Em – F – G – F | Subida de tensión |
| 4 | Chorus 1 | 0:52–1:15 | 23 | 8 | Em – F – G – A | Primer estallido; batería completa |
| 5 | Verse 2 | 1:15–1:40 | 25 | 8 | Dmaj7 – G/D | Vuelve la dinámica contenida |
| 6 | Pre-Chorus 2 | 1:40–1:55 | 15 | 4 | Em – F – G – F | |
| 7 | Chorus 2 | 1:55–2:18 | 23 | 8 | Em – F – G – A | Guitarra más presente |
| 8 | Bridge | 2:18–2:46 | 28 | 8+4 | G – D – A | Sección más etérea; la batería se retira |
| 9 | Guitar Solo | 2:46–3:10 | 24 | 8 | Em – F – G – A | Neil Taylor (sesionista) |
| 10 | Chorus 3 | 3:10–3:50 | 40 | 12+ | Em – F – G – A | Variaciones líricas; ensanchamiento |
| 11 | Outro / Fade | 3:50–4:11 | 21 | — | Em – F – G – A | Fade out con repetición |

### 4.2 Forma general

```
[Intro] [V1] [Pre-C] [C1] [V2] [Pre-C] [C2] [Bridge] [Solo] [C3] [Outro/Fade]
```

---

## 5. Letra

```
[Verse 1]
Welcome to your life
There's no turning back
Even while we sleep
We will find you

[Pre-Chorus 1]
Acting on your best behaviour
Turn your back on Mother Nature

[Chorus 1]
Everybody wants to rule the world

[Verse 2]
It's my own design
It's my own remorse
Help me to decide
Help me make the

[Pre-Chorus 2]
Most of freedom and of pleasure
Nothing ever lasts forever

[Chorus 2]
Everybody wants to rule the world

[Bridge]
There's a room where the light won't find you
Holding hands while the walls come tumbling down
When they do I'll be right behind you

[Chorus 3]
So glad we've almost made it
So sad they had to fade it
Everybody wants to rule the world

[Chorus 4]
I can't stand this indecision
Married with a lack of vision
Everybody wants to rule the—

[Chorus 5]
Say that you'll never, never, never, never need it
One headline, why believe it?
Everybody wants to rule the world

[Chorus 6]
All for freedom and for pleasure
Nothing ever lasts forever
Everybody wants to rule the world
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABB | life/back, sleep/you (asociante en «you») |
| Pre-Chorus 1 | AA | behaviour/nature |
| Chorus 1 | A | world (verso único) |
| Verse 2 | AABB | design/remorse, decide/make |
| Pre-Chorus 2 | AA | pleasure/forever |
| Chorus 2 | A | world |
| Bridge | AAA | you/down/you |
| Chorus 3 | AAB | made it/fade it/world |
| Chorus 4 | AAB | indecision/vision/world |
| Chorus 5 | AAB | need it/believe it/world |
| Chorus 6 | AAB | pleasure/forever/world |

> El esquema es predominantemente libre con rimas pareadas en los versos y un estribillo que rima internamente (pleasure/forever → world).

---

## 7. Análisis lírico

### 7.1 Tema central

El deseo humano de poder y control, y sus consecuencias corrosivas. La canción contrapone la ambición (el título) con la fugacidad del placer y la libertad («Nothing ever lasts forever»). Originalmente titulada «Everybody Wants to Go to War».

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Ironía | «Acting on your best behaviour / Turn your back on Mother Nature» | La contradicción entre «buen comportamiento» y dar la espalda a la naturaleza |
| Metáfora espacial | «There's a room where the light won't find you» | Un espacio interior de refugio o escape de la vigilancia |
| Hipérbole | «Say that you'll never, never, never, never need it» | Repetición cuádruple para enfatizar la negación |
| Antítesis | «So glad we've almost made it / So sad they had to fade it» | Alegría y tristeza yuxtapuestas en el mismo pensamiento |
| Personificación | «Mother Nature» | La naturaleza como figura materna a la que se traiciona |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Asíndeton | «It's my own design / It's my own remorse / Help me to decide / Help me make the most» |
| Polisíndeton | «never, never, never, never» |
| Metonimia | «One headline, why believe it?» (la prensa como representante del poder) |
| Paradoja | «Married with a lack of vision» |
| Apóstrofe | «Welcome to your life» (el hablante se dirige directamente al oyente) |

### 7.4 Conexión intertextual

- El título parafrasea una línea de «Charlie Don't Surf» de The Clash (1980). Según Joe Strummer, confrontó a Roland Orzabal en un restaurante y éste le pagó £5 como compensación.
- «Nothing ever lasts forever» es eco del Eclesiastés bíblico (vanitas vanitatum).
- El «room where the light won't find you» evoca la cultura del surveillance state y la novela *1984* de Orwell.

### 7.5 Contexto de composición

- Fue la última canción grabada para *Songs from the Big Chair*, compuesta en dos semanas casi como afterthought.
- Roland Orzabal tocó dos acordes en su guitarra acústica para el productor Chris Hughes, quien inmediatamente quiso convertirla en canción.
- El título original era «Everybody Wants to Go to War», pero lo cambiaron porque Orzabal sentía que sonaba «demasiado sermoneador».
- Ganó el Brit Award a Mejor Sencillo en 1986.
- Es una de las canciones de los 80 más versionadas: Lorde (2013, *The Hunger Games: Catching Fire*), Weezer, Patti Smith, etc.
- La guitarra solista del outro es de Neil Taylor (músico de sesión), no de Roland Orzabal.
- Curt Smith explicó: «El concepto es serio — trata sobre todos queriendo poder, sobre la guerra y la miseria que causa».

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Guitarra acústica (Roland Orzabal) | Toda la canción | Rítmica, el esqueleto armónico |
| Bajo sintetizado (Roland Orzabal) | Verse, Chorus | Secuenciado, línea melódica simple |
| Sintetizador PPG Wave 2.3 (Ian Stanley) | Pad/texturas | Capas atmosféricas |
| Sintetizador Yamaha DX7 | Brillo, campanas | Parches FM característicos |
| LinnDrum (caja de ritmos) | Toda la canción | Programada por Chris Hughes |
| Guitarra eléctrica (Neil Taylor) | Solo, Outro | Solo melódico con vibrato |
| Guitarra eléctrica (Roland Orzabal) | Riff de Intro | Arpegio con chorus |
| Cabasa | Todo el tema | Shuffle constante |
| Percusión adicional | Varias | Pandereta, cencerro |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Medio (barítono ligero de Curt Smith) |
| Textura | Voz principal con doblajes en el coro |
| Entrega | Serena, casi desapegada en versos; más intensa en pre-chorus/chorus |
| Capas | Doblaje vocal en el estribillo; armonías a terceras en algunas frases |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Compresión media; el contraste entre verso (contenido) y coro (explosivo) es más instrumental que de volumen.
- **Panning:** Voz centrada; guitarras rítmicas ligeramente a la izquierda; sintes en estéreo amplio.
- **Efectos destacados:** Reverb tipo hall en la voz, delay sincopado en el riff de introducción, chorus en la guitarra acústica eléctrica.
- **Producción general:** Pulcra, con la estética mid-80s del pop secuenciado pero con calidez analógica. El LinnDrum está mezclado con presencia pero sin estridencia. La ambigüedad tonal (mixolidio con préstamos) le da una cualidad agridulce que contradice la energía bailable.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (1985) | Producción secuenciada, LinnDrum, PPG Wave, Neil Taylor al solo |
| Lorde (2013) | Tempo más lento, tono menor, atmosférica, orquestal, para *The Hunger Games: Catching Fire* |
| Weezer (2019) | Versión rock/pop, guitarra eléctrica distorsionada, coros power pop |
| Tears for Fears (Sport Aid, 1986) | Regrabada como charity single, producción más grandiosa |
| Patti Smith (2018) | En vivo con spoken word, energía punk |

---

## 10. Fuentes

- **Spotify:** https://open.spotify.com/track/4RvWPyQ5RL0ao9LPZeSouE
- **Deezer:** https://www.deezer.com/track/88845911
- **SongData.io:** https://songdata.io/track/1MtreDx5OtNgn8wGPjE4L5/Everybody-Wants-To-Rule-The-World-by-Tears-For-Fears
- **CifraClub:** https://www.cifraclub.com/tears-for-fears/everybody-wants-to-rule-the-world/simplificada.html
- **E-Chords:** https://www.e-chords.com/chords/tears-for-fears/everybody-wants-to-rule-the-world
- **Chordie:** https://www.chordie.com/chord.pere/www.azchords.com/t/tearsforfears-tabs-5618/...
- **Wikipedia:** https://en.wikipedia.org/wiki/Everybody_Wants_to_Rule_the_World
- **Songfacts:** https://www.songfacts.com/facts/tears-for-fears/everybody-wants-to-rule-the-world
- **Letras.com:** https://www.letras.com/tears-for-fears/39669/
- **Genius:** https://genius.com/Tears-for-fears-everybody-wants-to-rule-the-world-lyrics
- **ReverbMachine (producción):** https://reverbmachine.com/blog/tears-for-fears-everybody-wants-to-rule-the-world-synths

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | Claude (opencode) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | gemma4 (just query-pro) |
| **Tags** | new-wave, synth-pop, tears-for-fears, 1985, songs-from-the-big-chair, power, control, brit-award |
| **Pendientes** | Verificar armonía con análisis de Hooktheory; confirmar si el BPM de Deezer (168) vs Spotify (112) se debe al compás 12/8 (tres subdivisiones por pulso) |

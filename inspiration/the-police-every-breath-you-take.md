# Song Case — Every Breath You Take — The Police

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Ultimate Guitar), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Every Breath You Take |
| **Artista** | The Police |
| **Versión analizada** | Original |
| **Álbum** | Synchronicity |
| **Año** | 1983 |
| **Duración** | 4:13 (album) / 3:56 (single) |
| **ISRC** | GBAKW8300109 (UK) / USAM18300017 (US) |
| **Género(s)** | New Wave, Soft Rock |
| **Compositor(es)** | Sting (Gordon Sumner) |
| **Productor(es)** | The Police, Hugh Padgham |
| **Sello** | A&M (AM 117) |
| **País** | Reino Unido |

---

## 2. Audio Features

### 2.1 Spotify API

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 116–117 | Moderato |
| **Key** | 0 (C) → toca en A con afinación A=432 Hz | Sonido resultante: ~A♭ |
| **Mode** | major | |
| **Camelot** | 11B | Como suena en A♭, sería 4B |
| **Danceability** | ~0.52 | Ritmo constante, but no bailable |
| **Energy** | ~0.55 | Contenida, tensa |
| **Valence** | ~0.30 | Baja — música triste/amenazante |
| **Acousticness** | ~0.40 | |
| **Instrumentalness** | ~0.001 | Letra muy presente |
| **Speechiness** | ~0.03 | |
| **Liveness** | ~0.10 | Estudio |
| **Loudness** | −9.8 dB | |
| **Time Signature** | 4/4 | |

### 2.2 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 117 |
| **Gain** | −9.8 dB |
| **Rank** | 964.878 |
| **Explicit** | no |
| **Release Date** | 20 May 1983 |
| **Preview URL** | `https://cdns-preview-e.dzcdn.net/stream/c-e9b67765f22f76a41c2cb75c96cb53f2-3.mp3` |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| A (escrita) / A♭ (sonido real) | major | Alta — la canción se toca en A pero la cinta estaba a 432 Hz |

> La canción fue grabada con los instrumentos afinados a A=432 Hz en lugar del estándar A=440 Hz. Los acordes se tocan como en A mayor (A, F#m, D, E), pero el sonido resultante está ligeramente por debajo, aproximándose a A♭ mayor. _Cashbox_ y Wikipedia documentan esto como A♭ mayor.

### 3.2 Progresión base

```
I   ii   iii   IV   V   vi   vii°
A   Bm   C#m   D   E   F#m  G#°
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | A9 — F#m9 — D9 — E9 | I — vi — IV — V | Ciclo de 4 acordes, 2 compases c/u |
| Verse 1 | A9 — F#m9 — D9 — E9 — F#m9 | I — vi — IV — V — vi | Termina en vi (cadencia decepcionante) |
| Verse 2 | A9 — F#m9 — D9 — E9 — A9 | I — vi — IV — V — I | Termina en I (cadencia perfecta) |
| Pre-Chorus | D — D7 — A9 — B9 — E9 | IV — IV7 — I — V/V — V | D7 (blues) y B9 (dominante secundario) fueran de la tonalidad |
| Chorus | A9 — F#m9 — D9 — E9 — F#m9 | I — vi — IV — V — vi | Vuelve a la cadencia decepcionante |
| Bridge | F — G — F — G — F — G — F — A9 | ♭VI — ♭VII (en A) / IV — V (en C) | Modulación a C mayor (♭III) sin resolver; usa A como nota pivote |
| Outro | A9 — F#m9 — D9 (cíclico) | I — vi — IV (sin V) | Omite el V (E); solo cadencia plagal; sensación de bucle infinito obsesivo |

### 3.4 Diagrama de la progresión

```
[Intro]           → [Verse 1]        → [Pre-Chorus]     → [Chorus]
 I  vi  IV  V       I  vi  IV  V  vi   IV  IV7  I  V/V  V  I  vi  IV  V  vi

[Verse 2]         → [Pre-Chorus]     → [Chorus]         → [Bridge]
 I  vi  IV  V  I    IV  IV7  I  V/V  V  I  vi  IV  V  vi   bVI  bVII  (x4)  → A

[Chorus]          → [Outro]
 I  vi  IV  V  vi   I  vi  IV  (cíclico, sin V)
```

### 3.5 Notas armónicas destacadas

- **Cadencia decepcionante V→vi** en lugar de V→I: genera tensión no resuelta, refleja la obsesión del narrador.
- **D7 fuera de tonalidad**: el primer indicio musical de que esto no es una canción de amor — ese acorde de blues introduce un matiz siniestro (Skinny Devil Magazine).
- **B9 (V/V o dominante del dominante)**: acorde fuera de la escala (Bm7 sería lo diatónico; B9 es prestado de E mayor) — empuja con fuerza hacia E.
- **Modulación puente A→F (♭III)**: Sting usa el acorde A como nota pivote (nota común entre A y F: A es tónica de A y 3.ª de F). El puente alterna F y G sin resolver a C, creando suspensión armónica hasta que Sting repite el truco inverso (F → A).
- **Outro sin V**: al eliminar el acorde dominante, no hay resolución perfecta. Solo queda el ciclo I-vi-IV (cadencia plagal), un bucle sin escape — igual que el vigilante no puede dejar de observar. Análisis detallado en Deep Music Listening.
- **Afinación A=432 Hz**: contribuye a la cualidad "templada" y ligeramente hipnótica del sonido (432 Hz vs. 440 Hz estándar).

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:18 | 18 | 8 (2+2+2+2) | A — F#m — D — E | Riff de guitarra de Andy Summers |
| 2 | Verse 1 | 0:18–0:44 | 26 | 8 | A — F#m — D — E → F#m | Termina en F#m (cadencia decepcionante) |
| 3 | Pre-Chorus | 0:44–0:57 | 13 | 4 | D — D7 — A — B7 — E | Tensión creciente |
| 4 | Chorus | 0:57–1:14 | 17 | 8 | A — F#m — D — E → F#m | "I'll be watching you" |
| 5 | Verse 2 | 1:14–1:40 | 26 | 8 | A — F#m — D — E → A | Termina en A (varía del V1) |
| 6 | Pre-Chorus | 1:40–1:53 | 13 | 4 | D — D7 — A — B7 — E | |
| 7 | Chorus | 1:53–2:11 | 18 | 8 | A — F#m — D — E → F#m | |
| 8 | Bridge | 2:11–2:51 | 40 | 16 (8+8) | F — G (x8) | Modulación; Sting canta "Since you've gone" |
| 9 | Pre-Chorus | 2:51–3:04 | 13 | 4 | D — D7 — A — B7 — E | |
| 10 | Chorus | 3:04–3:22 | 18 | 8 | A — F#m — D — E → F#m | |
| 11 | Outro | 3:22–4:13 | 51 | ~24 | A — F#m — D (cíclico) | Sin V; fade out; Sting repite "I'll be watching you" |

### 4.2 Forma general

```
[Intro][V1][Pre-C][C][V2][Pre-C][C][Bridge][Pre-C][C][Outro/Fade]
   8     8    4   8   8    4   8    16     4    8     ~24 compases
```

---

## 5. Letra

```
[Intro]
(Instrumental)

[Verse 1]
Every breath you take
And every move you make
Every bond you break
Every step you take
I'll be watching you

Every single day
And every word you say
Every game you play
Every night you stay
I'll be watching you

[Pre-Chorus]
Oh, can't you see
You belong to me?
How my poor heart aches
With every step you take

[Chorus]
Every move you make
And every vow you break
Every smile you fake
Every claim you stake
I'll be watching you

[Verse 2]
Since you've gone I've been lost without a trace
I dream at night, I can only see your face
I look around, but it's you I can't replace
I feel so cold and I long for your embrace
I keep crying baby, baby, please

[Pre-Chorus]
Oh, can't you see
You belong to me?
How my poor heart aches
With every step you take

[Chorus]
Every move you make
And every vow you break
Every smile you fake
Every claim you stake
I'll be watching you

Every move you make
Every step you take
I'll be watching you

[Outro]
I'll be watching you

(Every breath you take)
(Every move you make)
(Every bond you break)
(Every step you take)
I'll be watching you

(Every single day)
(Every word you say)
(Every game you play)
(Every night you stay)
I'll be watching you

(fade out)
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AAAA B / AAAA B | 4 versos + "I'll be watching you" (no rima); dos estrofas de 5 líneas |
| Pre-Chorus | ABAB | Rima cruzada: see/me, aches/take |
| Chorus | AAAA B | Mismo patrón que el verso |
| Bridge | AAAA | 4 pares de versos monorrimos (trace/face, replace/embrace, please no rima) |
| Outro | Libre / anafórico | Repite "I'll be watching you" intercalado con "(Every ...)" |

---

## 7. Análisis lírico

### 7.1 Tema central

Control, vigilancia y obsesión tras una ruptura amorosa. El narrador es un ex-amante que no puede soltar — y no quiere. La canción se presenta con la textura sonora de una balada de amor, pero el contenido lírico describe vigilancia total (cada respiración, cada movimiento, cada palabra). Sting la escribió pensando en el _Gran Hermano_ orwelliano, no en una relación romántica.

**Trampa interpretativa:** Es la canción más malinterpretada de la historia del pop. Tocada en bodas como "canción de amor", cuando en realidad describe a un acosador.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Anáfora | "Every breath... every move... every bond... every step" | Repetición obsesiva de "every" — el narrador no puede dejar de contar, de vigilar |
| Polisíndeton | "Every single day / And every word you say" | La "y" acumulativa sugiere que la lista nunca termina |
| Hipérbole | "Every breath you take" | Vigilancia literalmente total — imposible en la realidad, posible en la obsesión |
| Posesión disfrazada de amor | "You belong to me" | La palabra "belong" revela la verdadera naturaleza de la relación |
| Gradación decreciente (Bridge) | trace → face → replace → embrace | El sujeto pierde agencia ("lost without a trace"), solo ve el rostro del otro, no puede reemplazarlo, desea su abrazo — la necesidad se intensifica |
| Ironía dramática | Estructura musical "dulce" vs. letra siniestra | El oyente cree que es una canción de amor hasta que presta atención a la letra |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Anáfora | "Every breath... every move... every bond... every step" |
| Asíndeton (estrofa final) | "Every smile you fake, every claim you stake" (sin conjunción) |
| Epífora | "I'll be watching you" (cierra cada estrofa) |
| Pregunta retórica | "Oh can't you see?" |
| Metáfora de vigilancia | "I'll be watching you" como panóptico emocional |

### 7.4 Conexión intertextual

- **"Stand By Me" (Ben E. King)**: la progresión I-vi-IV-V es la misma — Sting la usó conscientemente para dar una falsa sensación de familiaridad y confort (fuente: Skinny Devil Magazine).
- **"Every Breath I Take" (Gene Pitney)**: influencia lírica directa según el libro _Back to Mono_.
- **Big Brother (Orwell, _1984_)**: Sting ha declarado que pensaba en vigilancia estatal, no en una relación personal.
- **"I'll Be Missing You" (Puff Daddy & Faith Evans, 1997)**: sample directo, tributo a Notorious B.I.G. — cambió la interpretación pública hacia el duelo por un ser querido.
- **_Stranger Things_ (Netflix, 2017)**: escena del baile de invierno (Eleven y Mike) — reintrodujo la canción a la Generación Z.

### 7.5 Contexto de composición

Sting escribió la canción en Jamaica, en el escritorio de Ian Fleming (autor de James Bond) en la propiedad Goldeneye. Se despertó a medianoche con la línea "Every breath you take" en la cabeza, se sentó al piano y la terminó en media hora.

> "I woke up in the middle of the night with that line in my head, sat down at the piano and had written it in half an hour. The tune itself is generic, an aggregate of hundreds of others, but the words are interesting. It sounds like a comforting love song. I didn't realise at the time how sinister it is. I think I was thinking of Big Brother, surveillance and control." — Sting, 1993

Andy Summers contribuyó el riff de guitarra (inspirado en Béla Bartók) que se convirtió en el sello sonoro de la canción. En 2025-2026, Summers y Stewart Copeland demandaron a Sting por créditos de autor y regalías no pagadas; Sting pagó £600,000 en enero de 2026.

### 7.6 El engaño armónico

La canción usa la familiar progresión I-vi-IV-V (la misma de "Stand By Me") para crear una falsa sensación de seguridad. Pero introduce acordes fuera de tonalidad:

1. **D7** (en lugar de Dmaj7) — el primer destello siniestro
2. **B7** (en lugar de Bm7) — dominante secundario que fuerza la tensión
3. **Modulación a F-G (♭VI-♭VII)** en el puente — cambio abrupto que desorienta

En el outro, elimina el V (E), dejando solo I-vi-IV en bucle infinito. Sin dominante, no hay resolución. El oyente queda atrapado en el mismo ciclo obsesivo que el narrador.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Guitarra eléctrica (Andy Summers) | Toda | Riff Bartók con arpegios con retardo; grabado en una sola toma |
| Bajo (Sting) | Toda | Línea melódica simple, notas largas, pulsación constante |
| Batería (Stewart Copeland) | Toda | Bombos sobregrabados (Oberheim DMX box), snare + gong drum; grabado en el comedor |
| Piano (Sting) | Puente | Nota repetida (Re) — sugerencia de Hugh Padgham |
| Sintetizadores (Sting) | Fondo | Texturas de pad |
| Contrabajo eléctrico | Video | Usado por Sting en el video (no en la grabación) |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Tenor (medio-agudo) |
| Textura | Voz limpia, sin distorsión |
| Entrega | Fría, medida, casi clínica — contraste con la letra emocional |
| Capas | Sting canta todas las voces: lead + armonías + backing |
| Efectos | Reverb de estudio (AIR Studios Montserrat) |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Comprimido, dinámica uniforme — no hay grandes cambios de volumen entre secciones
- **Panning:** Guitarra ligeramente a la derecha, batería centrada, voz centrada
- **Efectos destacados:** Retardo digital en la guitarra — el riff de Summers usa un delay sincopado que crea el característico efecto de "arpegio fantasma"
- **Producción general:** Hugh Padgham (conocido por el "gated reverb" de Phil Collins). La producción es limpia, sin adornos — cada instrumento ocupa su espacio.

### 8.4 Datos de grabación

- **Estudio:** AIR Studios, Salem, Montserrat (propiedad de George Martin)
- **Fechas:** Diciembre 1982 – Febrero 1983
- **Ingeniero:** Hugh Padgham
- **Tensión en el estudio:** Sting y Copeland "se odiaban" verbal y físicamente. Hubo peleas. Las sesiones casi se cancelan.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Demo original | Sting solo con órgano Hammond, estilo Billy Preston — sin guitarra, muy diferente |
| Simple Version (3:56) | Editada, fade out más temprano |
| Álbum Version (4:13) | Completa con outro extendido |
| "I'll Be Missing You" (Puff Daddy, 1997) | Sample directo; cambió el significado a tributo fúnebre; premio Grammy |
| Rich Landers (1983) | Versión country; #68 Billboard Hot Country |
| Mason Dixon (1983) | Versión country; #69 Billboard Hot Country |

---

## 10. Datos curiosos y legado

1. **Canción más radiada de la historia** (BMI, 2019) — superó a "You've Lost That Lovin' Feelin'" después de 22 años.
2. **~15 millones de radiaciones** registradas por BMI hasta 2019.
3. **$2,000/día en regalías** para Sting alrededor de 2003.
4. **Único #1 de The Police en el Billboard Hot 100** (8 semanas).
5. **Grabación acelerada**: algunas versiones del máster (single) están ligeramente aceleradas respecto al álbum.
6. **Tocada en bodas** como si fuera una canción romántica — ironía máxima.
7. **Tensión creativa**: Summers contribuyó el riff que salvó la canción ("estaba yendo a la basura hasta que toqué en ella").
8. **Pleito legal 2025-2026**: Summers y Copeland demandaron a Sting; Sting pagó £600,000 en enero 2026.
9. **434 millones de streams en Spotify** (creciendo ~1.5M/día en 2026).
10. **Video >1.6 mil millones de vistas** en YouTube (feb 2026).
11. **Stranger Things efecto**: la escena S2E4 (baile de Snow Ball) reintrodujo la canción a Gen Z, causando un resurgimiento en TikTok.

---

## 11. Fuentes

- **Spotify:** `https://open.spotify.com/track/1JSTJqkT5qHq8MDJnJbRE1`
- **Deezer:** `https://www.deezer.com/track/4623229`
- **CifraClub:** `https://www.cifraclub.com.br/the-police/every-breath-you-take/`
- **Hooktheory:** `https://www.hooktheory.com/theorytab/view/the-police/every-breath-you-take`
- **Ultimate Guitar:** `https://tabs.ultimate-guitar.com/tab/the-police/every-breath-you-take-chords-1087239`
- **Chordify:** `https://chordify.net/chords/the-police-songs/every-breath-you-take-2-chords`
- **Wikipedia:** `https://en.wikipedia.org/wiki/Every_Breath_You_Take`
- **Wikipedia (song data):** `https://songdata.io/track/1JSTJqkT5qHq8MDJnJbRE1/Every-Breath-You-Take-by-The-Police`
- **Music Gateway (BPM/Key):** `https://www.musicgateway.com/song-key-bpm/the-police/every-breath-you-take`
- **Skinny Devil Magazine (armonía):** `http://www.skinnydevilmagazine.com/2021/09/sonic-sorcery-dark-arts-of-every-breath.html`
- **Deep Music Listening (outro analysis):** `https://deepmusiclistening.wordpress.com/2013/06/18/the-three-most-important-chords-in-pop-music-the-police-every-breath-you-take/`
- **eBassGuitar (estructura):** `https://ebassguitar.com/every-breath-you-take/`
- **Jon MacLennan (guitar chords):** `https://www.jonmaclennan.com/blog/every-breath-you-take-chords`
- **AZLyrics:** `https://www.azlyrics.com/lyrics/police/everybreathyoutake.html`
- **Sound on Sound (grabación):** Buskin, Richard (Mar 2004) — "Classic Tracks: The Police's 'Every Breath You Take'"
- **BBC Radio 2 (entrevista Sting):** "Song Library: Every Breath You Take"
- **BMI (canción más radiada):** `https://www.bmi.com/`

---

## 12. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (deepseek-v4-flash-free) |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | Sondeo web múltiple + Wikipedia + teoría musical |
| **Tags** | `stalker-song`, `new-wave`, `the-police`, `synchronicity`, `I-vi-IV-V`, `432hz`, `aclamada`, `BMI-most-played`, `worldwide-hit`, `most-misunderstood` |
| **Pendientes** | Verificar ISRC exacto con Deezer API; intentar `just lookup "Every Breath You Take" "The Police"` para features librosa exactos |

# Song Case — Come and Get Your Love — Redbone

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Come and Get Your Love |
| **Artista** | Redbone |
| **Versión analizada** | Single Version (1974) |
| **Álbum** | *Wovoka* |
| **Año** | 1973 (álbum) / 1974 (single) |
| **Duración** | 3:32 (single) / 5:00 (álbum) |
| **ISRC** | USSM17300653 |
| **Género(s)** | Pop rock, Swamp rock, Funk, R&B, Soul |
| **Compositor(es)** | Lolly Vegas (creditado), Pat Vegas (no acreditado) |
| **Productor(es)** | Lolly Vegas, Pat Vegas |
| **Sello** | Epic Records |
| **País** | Estados Unidos |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 107.11 |
| **Gain** | −10.6 dB |
| **Rank** | 839,435 |
| **Explicit** | no |
| **Release Date** | 2024-12-23 (reedición digital) |
| **Deezer ID** | 392284592 |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| D | major | Alta — I–vi–ii–V (D–Bm–Em–A) consistente |

### 3.2 Progresión base

```
I    ii   iii  IV   V    vi   vii°
D    Em   F#m  G    A    Bm   C#°
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | D — Bm — Em — A (cíclico) | I — vi — ii — V | Bajo D-E-D-E sobre patrón de tom-tom |
| Verse 1 | D — Bm — Em — A — D — Bm | I — vi — ii — V — I — vi | "Hail / What's the matter with your head?" |
| Verse 2 | D — Bm — Em — A — D — Bm | I — vi — ii — V — I — vi | "Hail / What's the matter with your feel right?" |
| Chorus | Em — A — D — Bm (×4) | ii — V — I — vi | "Come and get your love" repetido 4 veces |
| Bridge | Em — A — D — Bm | ii — V — I — vi | Misma progresión del coro con variaciones; "Come and get your love now" |
| Outro | Em — A — D — Bm (fade) | ii — V — I — vi | "La la la la..." con título intercalado |

### 3.4 Diagrama de la progresión

```
[Intro (bajo)] → [Verse 1]      → [Chorus]       → [Verse 2]
 I  vi  ii  V     I  vi  ii  V    ii  V  I  vi     I  vi  ii  V
 (cíclico)         I  vi           (×4)             I  vi

[Chorus]         → [Bridge]       → [Chorus]       → [Outro]
 ii  V  I  vi      ii  V  I  vi    ii  V  I  vi     ii  V  I  vi
 (×4)              (×4)            (×4)             (fade)
```

### 3.5 Notas armónicas destacadas

- **Progresión I–vi–ii–V (D–Bm–Em–A)**: variación del ciclo clásico I–vi–IV–V. El ii (Em) en lugar del IV (G) da una cualidad más soul y menos predecible.
- **La línea de bajo** (descrita por Pat Vegas como "C to D to B to E to A") conduce el groove: notas pedal con movimiento cromático en la práctica sobre la tónica y la mediante.
- **D7M en la guitarra sitar** sobre el bajo en D crea una textura brillante que contrasta con el tono terroso de la percusión.
- **Armonía estática**: toda la canción es una sola progresión que se repite sin modulación — 29 repeticiones del título en 3:30.

---

## 4. Estructura

### 4.1 Mapa de secciones (Single Version ~3:32)

| # | Sección | Tiempo (mm:ss) | Acordes clave | Notas |
|---|---------|----------------|---------------|-------|
| 1 | Intro | 0:00–0:10 | D — Bm — Em — A | Bajo + tom-tom; sin guitarra aún |
| 2 | Verse 1 | 0:10–0:35 | D — Bm — Em — A → D — Bm | "Hail / What's the matter with your head" |
| 3 | Chorus | 0:35–0:58 | Em — A — D — Bm (×4) | "Come and get your love" |
| 4 | Verse 2 | 0:58–1:23 | D — Bm — Em — A → D — Bm | "Hail / What's the matter with your feel right?" |
| 5 | Chorus | 1:23–1:46 | Em — A — D — Bm (×4) | |
| 6 | Bridge | 1:46–2:12 | Em — A — D — Bm (×4) | "Come and get your love now" |
| 7 | Chorus | 2:12–2:35 | Em — A — D — Bm (×4) | |
| 8 | Outro | 2:35–3:32 | Em — A — D — Bm (fade) | "La la la la... come and get your love" |

### 4.2 Forma general

```
[Intro] [V1] [C] [V2] [C] [Bridge] [C] [Outro/Fade]
   8      8    16   8    16    16     16    ~32 compases
```

> La versión de álbum (5:00) añade una introducción lenta con guitarra acústica y un coda extendido antes del outro.

---

## 5. Letra

```
[Intro]
(Instrumental — bajo y percusión)

[Verse 1]
Hail (hail), what's the matter with your head? Yeah
Hail (hail), what's the matter with your mind and your sign?
And-a ooh-ohh
Hail (hail), nothin's a matter with your head, baby
Find it, come on and find it
Hail, with it, baby, 'cause you're fine and you're mine
And you look so divine

[Chorus]
Come and get your love
Come and get your love
Come and get your love
Come and get your love

[Verse 2]
Hail (hail), what's the matter with your feel right?
Don't you feel right, baby?
Hail, oh yeah, get it from the main vine, alright
I said-a find it, find it, go on and love it
If you like it, yeah-eh
Hail (hail), it's your business if you want some
Take some, get it together, baby

[Chorus]
Come and get your love
Come and get your love
Come and get your love
Come and get your love

[Bridge]
Come and get your love
Come and get your love
Come and get your love now
Come and get your love
Come and get your love
Come and get your love
Come and get your love now
Come and get your love

[Chorus]
Come and get your love
Come and get your love
Come and get your love
Come and get your love

[Outro]
La la la la... come and get your love
La la la la la... come and get your love
(Repetir con fade)
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | Libre / asonante | head/yeah, mind/sign, find/mine/divine — rima asonante en "i" |
| Verse 2 | Libre / asonante | right/alright, like it/together, want some/baby — estructura suelta |
| Chorus | Monorrima | "love" × 4 — repetición literal |
| Bridge | Libre | "love" y "now" — variación rítmica |

---

## 7. Análisis lírico

### 7.1 Tema central

Afirmación de amor universal y autoaceptación. El narrador le dice a su pareja (y, por extensión, al mundo) que no hay nada malo en ella — su cabeza, su mente, su signo zodiacal, su pelo: todo está bien. El amor está disponible; solo hay que ir a buscarlo.

Pat Vegas explicó: *"Many think the song is just about a man singing to a woman. It is, but it's also about the coming together of different peoples."* La canción es tanto una declaración romántica como un manifiesto sutil de orgullo nativoamericano.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Apóstrofe | "Hail" | Llamada de atención que abre cada verso — como un saludo o invocación |
| Pregunta retórica | "What's the matter with your head?" | No espera respuesta; es una forma de afirmar que no hay problema |
| Anáfora | "Come and get your love" × 29 | Repetición obsesiva que graba el mensaje |
| Afirmación directa | "Nothin's a matter with your head, baby" | Respuesta inmediata a la pregunta retórica — estructura de call-and-response |
| Metáfora agrícola/espiritual | "Get it from the main vine" | Posible referencia a la Vid (Jesús en Juan 15) o a la conexión con la Tierra Madre |
| Hipérbole | "You look so divine" | Eleva a la amada a categoría divina |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Interrogación retórica | "What's the matter with your head?" |
| Anáfora | "Come and get your love" (29 veces) |
| Asíndeton | "you're fine and you're mine and you look so divine" |
| Epífora | "Come and get your love" (cierra cada sección) |
| Gradación | hair → head → mind → sign (ascenso de lo físico a lo espiritual) |

### 7.4 Conexión intertextual

- **"Hail"** como opening: evoca tanto un saludo hawaiano como una invocación espiritual ("Hail Mary").
- **"Main vine"**: posible eco de Juan 15:5 ("Yo soy la vid, vosotros los pámpanos") — aunque Pat Vegas lo niega explícitamente como referencia religiosa.
- **Guardians of the Galaxy (2014)**: la escena de apertura con Peter Quill bailando la canción en Morag la rescató del olvido y la convirtió en himno intergeneracional.
- **F Is for Family (Netflix, 2015–2021)**: usada como tema de apertura — la asocia con la nostalgia setentera y la disfunción familiar.
- **Redbone: The True Story of a Native American Rock Band (IDW, 2020)**: novela gráfica que documenta la historia de la banda.

### 7.5 Contexto de composición

Lolly Vegas llamó a su hermano Pat a las 3 a.m. en 1973, en Hollywood. Tenía una idea: "unos acordes simples, de C a D a B a E a A". Pat llevó su bajo y una grabadora. Trabajaron hasta la mañana siguiente.

La canción se llamaba originalmente "I Want to Give You My Love". Pat cambió el título a "Come and Get Your Love" porque quería que sonara a invitación, no a ofrecimiento. Incluyó el "Hail" inicial para darle grandeza: *"like glory to the world"*.

Grabada en el álbum *Wovoka* (1973), lanzada como single en enero de 1974. Alcanzó el #5 en el Billboard Hot 100 el 13 de abril de 1974 — la primera vez que una banda de nativos americanos llegaba al Top 5.

Epic Records se negó a lanzar "We Were All Wounded at Wounded Knee" como siguiente single en EE.UU. (sí en Europa), considerándolo demasiado controvertido. En su lugar lanzaron "Wovoka", que solo llegó al #101.

### 7.6 Significado cultural

Redbone usó su visibilidad para cambiar la imagen de los nativos americanos en la cultura pop. Pat Vegas: *"They saw us in Western movies being chased by the cowboys, and we didn't want to be a part of that. We wanted to show that we had grown and we were part of the future."*

La canción es un caballo de Troya: suena a pop feliz y despreocupado, pero cada "Hail" y cada referencia a "main vine" llevan una cosmovisión indígena de conexión con la tierra y el amor como fuerza universal.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Intérprete | Sección | Notas |
|-------------|------------|---------|-------|
| Bajo Fender Precision | Pat Vegas | Toda | Línea motora que duplica el tom-tom; nota pedal con variaciones D-E |
| Guitarra + Sitar eléctrico | Lolly Vegas | Toda | Sitar en la progresión principal; Telecaster en los leads del final del coro |
| Guitarra rítmica | Tony Bellamy | Fondo | Relleno armónico |
| Batería (tom-tom) | Pete DePoe | Toda | "Native American dance beat" — énfasis en el upbeat, patrón don don-don |
| Cuerdas | Arreglo de Gene Page | Fondo | 4 violines + 4 violas, doblados para sonido más lleno |

### 8.2 Sonidos distintivos

- **Guitarra distorsionada por Leslie**: Lolly Vegas tocó la guitarra a través de un altavoz Leslie (rotatorio, típicamente usado para órganos Hammond) para conseguir el característico sonido vibrante y áspero.
- **Sitar eléctrico**: el timbre nasal y sostenido del sitar eléctrico (no confundir con el sitar acústico indio) da a la canción su textura exótica única.
- **Batería "tom-tom"**: el ritmo de danza nativa americana (golpe recto con énfasis en el upbeat) en lugar del patrón rock convencional.

### 8.3 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Voz principal | Lolly Vegas — registro medio, timbre cálido y rasposo |
| Textura | Call-and-response con la banda ("Hail (hail)") |
| Entrega | Enérgica, suelta, casi improvisada |
| Capas | Coros doblados; grupo vocal en los "Hail" |
| Ad-libs | "Yeah-eh", "ooh-ohh", "ahhh" — ornamentación funk |

### 8.4 Mezcla y dinámica

- **Rango dinámico**: Compacto pero con espacio — el bajo y la percusión ocupan el centro, la guitarra-sitar brilla en los medios agudos.
- **Panning**: Voz centrada, sitar ligeramente a la izquierda, percusión centrada.
- **Efectos destacados**: Leslie speaker en guitarra; reverb de cámara en voz; compresión ligera en toda la mezcla.
- **Producción general**: Funk/R&B setentero con producción soul — cada instrumento tiene su lugar, pero el groove es lo primero. Gene Page (arreglista de The Jackson 5, Marvin Gaye) aportó el toque orquestal.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Álbum (Wovoka, 1973) | Introducción lenta (~1 min) con guitarra acústica; coda extendido; duración 5:00 |
| Single (1974) | Editada para radio — corta la intro lenta, va directo al groove; 3:32 |
| Re-edit DJ (1974) | Aún más corta, voz principal más prominente |
| Real McCoy (1995) | Eurodance; #19 Billboard Hot 100, #1 Dance; samplea el estribillo sobre base house |
| En vivo (Midnight Special, 1974) | Intro con danza tribal nativa americana por Tony Bellamy; duración extendida |
| Animated Music Video (2020) | Primer video oficial; animación de Brent Learned con viajero espiritual nativoamericano |

---

## 10. Datos curiosos y legado

1. **Hito histórico**: Primera banda de nativos americanos en alcanzar el Top 5 del Billboard Hot 100.
2. **29 repeticiones del título** en 3:30 — una de las canciones con más repeticiones del estribillo en la historia del pop.
3. **Disco dorado**: vendió más de 1 millón de copias (RIAA Gold, 22 abril 1974).
4. **Resurgimiento Guardianes de la Galaxia**: la escena de apertura (Peter Quill bailando) de 2014 reintrodujo la canción a una nueva generación. La banda sonora vendió 2.5 millones de copias solo en 2014.
5. **700+ millones de vistas en YouTube** (contando todas las versiones).
6. **Uso en Avengers: Endgame (2019)** y **Guardians of the Galaxy Vol. 3 (2023)**.
7. **Tema de F Is for Family** (Netflix, 2015–2021, 5 temporadas).
8. **"Hail" era el título provisional** del promocional antes de que la canción se llamara "Come and Get Your Love".
9. **Novela gráfica**: *Redbone: The True Story of a Native American Rock Band* (IDW, 2020), en colaboración con la familia Vegas.
10. **El sonido Leslie**: Lolly creó el característico sonido de guitarra pasando su Telecaster por un altavoz Leslie de órgano.
11. **Censura sutil**: "We Were All Wounded at Wounded Knee" (también en *Wovoka*) no fue lanzada como single en EE.UU. por su contenido político.
12. **Disputa de créditos**: Pat Vegas afirma haber co-escrito la canción pero permitió que Lolly llevara el crédito único para evitar conflictos.

---

## 11. Fuentes

- **Deezer:** `https://www.deezer.com/track/392284592`
- **Wikipedia:** `https://en.wikipedia.org/wiki/Come_and_Get_Your_Love`
- **American Songwriter:** `https://americansongwriter.com/the-story-and-meaning-behind-come-and-get-your-love-redbones-trailblazing-smash/`
- **NPR:** `https://www.npr.org/2024/04/16/1243733965/redbone-come-and-get-your-love-50-years`
- **Songfacts:** `https://www.songfacts.com/facts/redbone/come-and-get-your-love`
- **CifraClub (ukulele chords):** `https://www.ukecifras.com.br/redbone/come-and-get-your-love`
- **Wall Street Journal (Pat Vegas entrevista):** `https://redbone-band.com/wall-street-journal-pat-interview`
- **Best Classic Bands:** `https://bestclassicbands.com/redbone-come-and-get-your-love-video-8-3-20/`
- **Redbone Band Official:** `https://redbone-band.com/come-and-get-your-love`
- **Lyric Stories:** `https://lyricstories.com/song-meanings/come-and-get-your-love-lyrics-meaning`

---

## 12. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (deepseek-v4-flash-free) |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | Sondeo web múltiple + Wikipedia + entrevistas + cifra |
| **Tags** | `redbone`, `native-american`, `1974`, `wovoka`, `swamp-rock`, `guardians-of-the-galaxy`, `I-vi-ii-V`, `one-hit-wonder`, `funk-rock`, `feel-good`, `70s`, `resurgimiento-cinematográfico` |
| **Pendientes** | Verificar acordes exactos del álbum original (posible variación en la intro lenta); analizar con `just lookup` si hay preview disponible |

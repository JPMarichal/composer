# Song Case — Hallelujah — Leonard Cohen

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Hallelujah |
| **Artista** | Leonard Cohen |
| **Versión analizada** | Original (álbum *Various Positions*, 1984) |
| **Álbum** | *Various Positions* |
| **Año** | 1984 |
| **Duración** | 4:39 |
| **ISRC** | USSM10026643 |
| **Género(s)** | Folk, Gospel, Rock |
| **Compositor(es)** | Leonard Cohen |
| **Productor(es)** | John Lissauer |
| **Sello** | Columbia (rechazado en EE.UU.) / PVC (lanzamiento estadounidense) |
| **País** | Canadá |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 170.8 (12/8 compuesto) |
| **Gain** | −11.4 dB |
| **Rank** | 631,518 |
| **Explicit** | no |
| **Release Date** | 2002-10-22 (reedición *The Essential Leonard Cohen*) |
| **Deezer ID** | 15218949 |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| C | major | Alta — I–IV–V–vi con E7 como dominante secundario |

**Compás:** 12/8 (swing ternario — 4 pulsos de corchea con puntillo por compás)

### 3.2 Acordes por sección

| Sección | Acordes (en C) | Función armónica | Notas |
|---------|---------|---------|-------|
| Intro | C — Am — C — Am — F — G — C — G | I — vi — I — vi — IV — V — I — V | Arpegio fingerpicking |
| Verso (parte A) | C — Am — C — Am — F — G — C — G | I — vi — I — vi — IV — V — I — V | "I heard there was a secret chord" |
| Verso (parte B) | C — F — G — Am — F — G — E7 — Am | I — IV — V — vi — IV — V — III7 — vi | E7 es V/vi; aquí canta "the fourth, the fifth, the minor fall, the major lift" |
| Refrán | F — F — Am — Am — F — F — C — G — C | IV — IV — vi — vi — IV — IV — I — V — I | "Hallelujah" repetido; patrón que evoca el coral |

### 3.3 Meta-armonía

La canción describe su propia construcción armónica en la letra de la parte B del verso:

> *"It goes like this, the fourth, the fifth, the minor fall, the major lift"*

| Letra | Acorde | Grado | Explicación |
|-------|--------|-------|-------------|
| "the fourth" | F | IV | Acorde de subdominante |
| "the fifth" | G | V | Acorde de dominante |
| "the minor fall" | Am | vi | Tríada menor — la "caída" del modo mayor al relativo menor |
| "the major lift" | F | IV | Vuelta a la tríada mayor — el "ascenso" desde el menor |

Es un caso raro de **meta-música**: la letra explica literalmente los acordes que se están tocando.

### 3.4 Notas armónicas destacadas

- **E7 (III7)**: dominante secundario que funciona como V/vi (prepara Am). Añade tensión cromática en medio de una progresión diatónica.
- **Progresión I–IV–V–vi**: el corazón de la canción. La vuelta a vi en lugar de I (cadencia engañosa V–vi en parte B) mantiene la sensación de suspensión emocional.
- **El refrán (IV–vi–I–V–I)**: repite F y Am — el subdominante y el relativo menor — para crear un mantra hipnótico sobre la palabra "Hallelujah".
- **12/8**: el compás ternario evoca tanto el gospel como el rock and roll temprano, y da a la canción su balanceo característico.

---

## 4. Estructura

### 4.1 Forma general

```
[Intro] [Verse 1] [Refrain] [Verse 2] [Refrain] [Verse 3] [Refrain] [Outro]
   4       16         8          16         8         16         8        ~4
```

Cohen grabó 4 versos en estudio; en vivo usaba 5–7 versos distintos combinados de su archivo de ~80 borradores. La versión canónica más difundida (Buckley/Wainwright) usa los versos 1, 2, 4 y 5 de los drafts originales.

---

## 5. Letra

```
[Verse 1]
Now I've heard there was a secret chord
That David played, and it pleased the Lord
But you don't really care for music, do you?
It goes like this: the fourth, the fifth
The minor fall, the major lift
The baffled king composing Hallelujah

[Refrain]
Hallelujah, Hallelujah
Hallelujah, Hallelujah

[Verse 2]
Your faith was strong but you needed proof
You saw her bathing on the roof
Her beauty and the moonlight overthrew you
She tied you to a kitchen chair
She broke your throne, and she cut your hair
And from your lips she drew the Hallelujah

[Refrain]
Hallelujah, Hallelujah
Hallelujah, Hallelujah

[Verse 3]
You say I took the name in vain
I don't even know the name
But if I did, well really, what's it to you?
There's a blaze of light in every word
It doesn't matter which you heard
The holy or the broken Hallelujah

[Refrain]
Hallelujah, Hallelujah
Hallelujah, Hallelujah

[Verse 4 — solo en la grabación original de Cohen]
I did my best, it wasn't much
I couldn't feel, so I learned to touch
I've told the truth, I didn't come to fool you
And even though it all went wrong
I'll stand before the Lord of Song
With nothing on my tongue but Hallelujah

[Refrain]
Hallelujah, Hallelujah
Hallelujah, Hallelujah
```

> **Nota sobre las versiones:** Cohen usó diferentes combinaciones de versos en vivo. La versión de Jeff Buckley (la más famosa) omite el V4 y añade un verso que Buckley tomó de una actuación en vivo de Cohen:
> *"Well, maybe there's a God above / As for me, all I've ever learned from love / Is how to shoot at someone who outdrew ya..."*
> La versión de Rufus Wainwright (popularizada por *Shrek*) combina los versos de Buckley con algunos propios.

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABCCB | chord/Lord/you; fifth/lift/Hallelujah |
| Verse 2 | AABCCB | proof/roof/you; chair/hair/Hallelujah |
| Verse 3 | AABCCB | vain/name/you; word/heard/Hallelujah |
| Verse 4 | AABCCB | much/touch/you; wrong/song/Hallelujah |
| Refrán | AAAA | Hallelujah × 4 |

El esquema es idéntico en cada verso: dos pareados (A–A, C–C) con un tercer verso que rima con el sexto (B–B). La palabra "Hallelujah" cierra cada verso como rima terminal.

---

## 7. Análisis lírico

### 7.1 Tema central

La canción no es un himno religioso, sino una meditación sobre la multiplicidad del éxtasis y el dolor humanos. Cohen explora diferentes tipos de "Hallelujah": el del rey David componiendo, el de Sansón traicionado, el del amante roto, el del poeta ante su dios. Todos válidos. Como dijo el propio Cohen: *"All the perfect and broken hallelujahs have equal value."*

### 7.2 Referencias bíblicas

| Referencia | Texto bíblico | En la canción |
|------------|---------------|---------------|
| David tocando para Saúl | 1 Samuel 16:23 | "a secret chord that David played and it pleased the Lord" |
| Betsabé bañándose | 2 Samuel 11:2 | "You saw her bathing on the roof" |
| Sansón y Dalila | Jueces 16:4–21 | "She tied you to a kitchen chair / She broke your throne and she cut your hair" |

### 7.3 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Meta-música | "It goes like this: the fourth, the fifth, the minor fall, the major lift" | La letra describe literalmente los acordes que suenan |
| Ironía | "But you don't really care for music, do you?" | El oyente está escuchando música mientras le dicen que no le importa |
| Antítesis | "The holy or the broken Hallelujah" | Lo sagrado y lo profano unidos en la misma palabra |
| Imagen | "She tied you to a kitchen chair" | Domesticación de la tragedia bíblica — Sansón atado a una silla de cocina |
| Acumulación | "the fourth, the fifth, the minor fall, the major lift" | Gradación musical ascendente |
| Paradoja | "The baffled king composing Hallelujah" | Un rey confundido alabando a Dios — la fe nace de la duda |

### 7.4 Contexto de composición

Cohen tardó 4–5 años en escribir "Hallelujah". Llenó dos cuadernos con aproximadamente 80 versos, descartando la mayoría. En una famosa anécdota, cuenta que estaba en el Hotel Royalton de Nueva York, en calzoncillos, golpeándose la cabeza contra el suelo.

> *"I filled two notebooks and I remember being in New York, with my underwear on the carpet, banging my head on the floor, saying 'I can't finish this song.'"*

Columbia Records rechazó el álbum *Various Positions*. El presidente Walter Yetnikoff dijo: *"What is this? This isn't pop music. We're not releasing it. This is a disaster."* El álbum fue lanzado en EE.UU. por el sello independiente PVC.

La grabación original presenta a Cohen a los 50 años, con su característico barítono grave. El productor John Lissauer creó un arreglo con teclados, coros femeninos y guitarra acústica. La canción pasó desapercibida hasta que John Cale (ex Velvet Underground) la grabó para un tributo en 1991.

### 7.5 El fenómeno Buckley

Jeff Buckley escuchó la versión de Cale en el tributo y comenzó a tocarla en vivo. La grabó para *Grace* (1994) en una sola toma vocal. Su muerte por ahogamiento en 1997 (a los 30 años) impulsó la canción al estatus de himno. La versión de Buckley cambió la percepción de la canción: su voz de tenor etéreo, el crescendo dramático y la selección de versos (omitó el último verso de Cohen, añadiendo el "maybe there's a God above") la convirtieron en algo más sensual y desesperado que la resignación serena de Cohen.

---

## 8. Producción

### 8.1 Instrumentación (versión original de Cohen)

| Instrumento | Notas |
|-------------|-------|
| Guitarra acústica | Fingerpicking en patrón de arpegio |
| Teclados / Sintetizadores | Pads suaves, textura atmosférica |
| Coros femeninos | Jennifer Warnes y otras — respuesta angelical a la voz grave de Cohen |
| Bajo eléctrico | Línea simple, notas largas |
| Batería | Sutil, casi ausente — platillos y caja mínimos |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Barítono profundo (basso profundo a los 50 años) |
| Textura | Voz grave, serena, casi hablada |
| Entrega | Resignada, sabia, sin artificio |
| Capas | Voz principal centrada, coros femeninos en el refrán |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Amplio — del fingerpicking íntimo al crescendo del refrán con coros.
- **Efectos destacados:** Reverb de sala en la voz; delay sutil en guitarra.
- **Producción general:** John Lissauer creó un sonido de medidos ochenta — teclados y sintetizadores que datan la grabación, pero la voz y la guitarra son atemporales.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| **Leonard Cohen** (1984) | Barítono grave, teclados ochenteros, coros femeninos; 4 versos + V4 final "I'll stand before the Lord of Song" |
| **John Cale** (1991) | Solo piano y voz; omitió teclados; seleccionó versos distintos (sin V4); usó el "maybe there's a God above" |
| **Jeff Buckley** (1994) | La versión definitiva para el público masivo. Voz de tenor, guitarra eléctrica con sustain, crescendo dramático, una sola toma vocal. Omitió el V4 de Cohen, usó el verso de Cale. |
| **Rufus Wainwright** (2001) | Para *Shrek*; piano y orquesta; combinó versos de Buckley y Cohen; presentó la canción a toda una generación infantil |
| **k.d. lang** (2004) | Versión en los Juno Awards — considerada por muchos la mejor interpretación vocal de la canción; recibió ovación de pie |
| **Pentatonix** (2016) | A capella; arreglo vocal complejo; ~130 millones de reproducciones |
| **Cohen (Live in London, 2009)** | A los 75 años, voz aún más grave; 6 versos combinados; orquesta; versión definitiva del autor |

> Se han registrado **más de 300 versiones** oficiales, lo que la convierte en una de las canciones más versionadas de la historia.

---

## 10. Datos curiosos y legado

1. **La canción que Columbia odiaba**: rechazada por la discográfica, hoy es considerada una de las mejores canciones de todos los tiempos.
2. **80 versos escritos**: Cohen pasó años reduciendo el material a 4 versos de estudio.
3. **Múltiples "biblias" de versos**: cada versión (Cale, Buckley, Wainwright, Cohen en vivo) usa una combinación distinta.
4. **Meta-composición**: la letra explica la armonía — posiblemente el ejemplo más famoso de meta-música en la canción popular.
5. **Shrek factor**: la versión de Rufus Wainwright introdujo la canción a niños de todo el mundo; muchos padres reportaron que sus hijos pedían "la canción del Hallelujah".
6. **Uso político**: cantada en funerales de Estado, manifestaciones y homenajes — desde Ottawa (tiroteo 2014) hasta el funeral de Fidel Castro.
7. **#1 en Reino Unido (2008)**: la versión de Alexandra Burke (ganadora de *X Factor*) llegó a #1 y fue el sencillo más vendido del año; Cohen donó sus regalías (£500,000) a su fundación.
8. **La versión prohibida de Buckley**: Buckley usó el verso "I remember when I moved in you / And the holy dove was moving too" — explícitamente sexual — que fue censurado en radios.
9. **Inducción**: Canadian Songwriters Hall of Fame (2006).
10. **Cohen sobre la canción**: *"There is a religious hallelujah, but there are many other ones. When one looks at the world, there's only one thing to say, and it's hallelujah. That's the way it is."*

---

## 11. Fuentes

- **Deezer:** `https://www.deezer.com/track/15218949`
- **Wikipedia:** `https://en.wikipedia.org/wiki/Hallelujah_(Leonard_Cohen_song)`
- **Pitchfork (historia):** `https://pitchfork.com/thepitch/1360-leonard-cohens-hallelujah-musics-greatest-work-in-progress/`
- **The Conversation (armonía):** `https://theconversation.com/hallelujah-how-an-ignored-leonard-cohen-song-became-a-modern-legend-68704`
- **American Songwriter:** `https://americansongwriter.com/behind-the-meaning-of-hallelujah-by-leonard-cohen/`
- **Songfacts:** `https://www.songfacts.com/facts/leonard-cohen/hallelujah`
- **Canadian Encyclopedia:** `https://www.thecanadianencyclopedia.ca/en/article/hallelujah`
- **Lexicon of Song (análisis lírico):** `https://www.lexiconofsong.org/hallelujah.html`
- **CifraClub:** `https://www.cifraclub.com/leonard-cohen/hallelujah/`
- **Hooktheory:** `https://www.hooktheory.com/theorytab/view/leonard-cohen/hallelujah`
- **Grammy (historia):** `https://www.grammy.com/news/leonard-cohens-holy-standard/`
- **The Holy or the Broken (Alan Light, 2013):** libro completo sobre la historia de la canción

---

## 12. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (deepseek-v4-flash-free) |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | Sondeo web múltiple + Wikipedia + teoría musical + fuentes biográficas |
| **Tags** | `leonard-cohen`, `hallelujah`, `1984`, `various-positions`, `folk-rock`, `C-major`, `I-IV-V-vi`, `meta-music`, `most-covered`, `biblical-imagery`, `jeff-buckley`, `canadian-songwriter` |
| **Pendientes** | Verificar count exacto de versos en el archivo de Cohen; analizar con `just lookup` si hay preview disponible |

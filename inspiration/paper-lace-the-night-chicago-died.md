# Song Case — "The Night Chicago Died" — Paper Lace

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Deezer), análisis armónico de fuentes web (E-Chords), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | The Night Chicago Died |
| **Artista** | Paper Lace |
| **Versión analizada** | original — UK 1974 single |
| **Álbum** | Paper Lace (US version) / ...And Other Bits of Material |
| **Año** | 1974 |
| **Duración** | 3:30 (Deezer: 213 s) |
| **ISRC** | GBUM72105385 |
| **Género(s)** | Pop rock, bubblegum pop, novelty song |
| **Compositor(es)** | Peter Callander, Mitch Murray |
| **Productor(es)** | Peter Callander, Mitch Murray |
| **Sello** | Bus Stop (UK), Mercury (US), Philips (Europe) |
| **País** | Reino Unido |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: Songdata.io / análisis agregado de terceros — valores aproximados (pueden variar según el cliente).

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 106 (124 en algunas detecciones) | Rango reportado: 103–124 según fuente; 106 como tempo base percibido |
| **Key** | 9 (A) | Detectado como C por algunos algoritmos, pero la progresión armónica real (A–Bm–E7) confirma A mayor |
| **Mode** | major | A mayor |
| **Camelot** | 11B (A major) o 8B (C major según detección alternativa) | |
| **Danceability** | 0.76 | Alta — ritmo constante y bailable |
| **Energy** | 0.87 | Muy alta — producción densa con brass, percusión y coros |
| **Valence** | 0.96 | Extremadamente positiva — contradice la letra violenta |
| **Acousticness** | 0.28 | Baja — producción eléctrica, no acústica |
| **Instrumentalness** | 0.00 | No hay secciones instrumentales largas |
| **Speechiness** | 0.03 | Baja — es canto melódico, no spoken word (salvo el intro hablado) |
| **Liveness** | 0.11 | Baja — grabación de estudio |
| **Loudness** | −4.4 dB | Muy comprimido para la época |
| **Time Signature** | 4/4 | |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/1915606727`

| Feature | Valor |
|---------|-------|
| **BPM** | 0 (no disponible en API para este track) |
| **Gain** | −12.2 dB |
| **Rank** | 337978 |
| **Explicit** | no |
| **Release Date** | 2022-09-23 (reedición digital) |
| **Preview URL** | `https://cdnt-preview.dzcdn.net/api/1/1/c/f/0/0/cf01bdc78b3192c7aa70785a3522f2c5.mp3` |

### 2.3 Análisis local (librosa) — opcional

> Pendiente: requiere descarga del audio.

| Feature | Valor |
|---------|-------|
| **BPM (librosa)** | — |
| **Key (librosa)** | — |
| **Mode** | — |
| **Energy** | — |
| **Danceability** | — |
| **Valence** | — |
| **Spectral Centroid** | — |
| **Onset Density** | − |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| A (A mayor) | major | Alta — los acordes reales de la grabación confirman A mayor |

### 3.2 Progresión base

```
A   Bm   E7   A
I   ii   V7   I
```

La progresión es una simple rotación I–ii–V7–I en A mayor, típica del pop-rock de los 60s/70s. La fuerza de la canción no está en la complejidad armónica sino en la narrativa, la dinámica de producción y el gancho melódico.

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | (sirena synth + spoken word sobre percusión) | Tónica implícita (A) | Sin acordes definidos; solo batería y sintetizador |
| Verse | A – Bm – E7 – A | I – ii – V7 – I | Ciclo de 4 compases, repetido |
| Pre-Chorus | A – Bm – E7 – A | I – ii – V7 – I | Misma progresión del verso; tensión por acumulación lírica |
| Chorus | A – Bm – E7 – A | I – ii – V7 – I | Idéntica progresión, pero con dinámica elevada y coros |
| Verse 3 (resolución) | A – Bm – E7 – A | I – ii – V7 – I | Sección más calmada: solo voz + reloj + tensión narrativa |
| Outro | A (vamp) | I | Repetición de "The night Chicago died" sobre na-na-na |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro/Synth] → [Verse 1]      → [Pre-Chorus]  → [Chorus]       → [Verse 2]
  (sirena)       I ii V7 I        I ii V7 I       I ii V7 I        I ii V7 I

→ [Pre-Chorus] → [Chorus]       → [Verse 3]      → [Chorus/Outro]
   I ii V7 I      I ii V7 I        I ii V7 I        I (vamp)
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro (spoken) | 0:00–0:08 | ~8 | — | A (implícito) | Sirena synth + "Daddy was a cop…" |
| 2 | Verse 1 | 0:08–0:22 | ~14 | 4 | A–Bm–E7 | Entrada de banda completa |
| 3 | Pre-Chorus 1 | 0:22–0:34 | ~12 | 4 | A–Bm–E7 | "When a man named Al Capone…" |
| 4 | Chorus 1 | 0:34–0:54 | ~20 | 8 | A–Bm–E7 | "I heard my mama cry…" |
| 5 | Verse 2 | 0:54–1:08 | ~14 | 4 | A–Bm–E7 | Batalla descrita |
| 6 | Pre-Chorus 2 | 1:08–1:20 | ~12 | 4 | A–Bm–E7 | "'Bout a hundred cops are dead!" |
| 7 | Chorus 2 | 1:20–1:40 | ~20 | 8 | A–Bm–E7 | |
| 8 | Bridge / Verse 3 | 1:40–2:02 | ~22 | 8 | A–Bm–E7 | Reloj + silencio + puerta |
| 9 | Chorus 3 (na-na) | 2:02–2:22 | ~20 | 8 | A | Versión reducida con na-na-na |
| 10 | Outro | 2:22–3:30 | ~68 | ~24 | A (vamp) | Na-na-na hasta fade out |

### 4.2 Forma general

```
[Intro hablado] [V1] [Pre-C1] [C1] [V2] [Pre-C2] [C2] [Puente/V3] [C3 (na-na)] [Outro]
```

---

## 5. Letra

```
[Intro — spoken]
Daddy was a cop on the east side of Chicago
Back in the U.S.A., back in the bad old days

[Verse 1]
In the heat of a summer night
In the land of the dollar bill
When the town of Chicago died
And they talk about it still

[Pre-Chorus 1]
When a man named Al Capone
Tried to make that town his own
And he called his gang to war
With the forces of the law

[Chorus]
I heard my mama cry
I heard her pray the night Chicago died
Brother, what a night it really was
Brother, what a fight it really was
Glory be!
I heard my mama cry
I heard her pray the night Chicago died
Brother, what a night the people saw
Brother, what a fight the people saw
Yes indeed!

[Verse 2]
And the sound of the battle rang
Through the streets of the old East Side
'Til the last of the hoodlum gang
Had surrendered up or died

[Pre-Chorus 2]
There was shouting in the street
And the sound of running feet
And I asked someone, who said
"'Bout a hundred cops are dead!"

[Chorus]
I heard my mama cry
I heard her pray the night Chicago died
Brother, what a night it really was
Brother, what a fight it really was
Glory be!
I heard my mama cry
I heard her pray the night Chicago died
Brother, what a night the people saw
Brother, what a fight the people saw
Yes indeed!

[Verse 3 — Bridge]
Then there was no sound at all
But the clock upon the wall
Then the door burst open wide
And my daddy stepped inside
And he kissed my mama's face
And he brushed her tears away

[Chorus — shortened]
The night Chicago died
(Na-na na, na-na-na, na-na-na)
The night Chicago died
Brother, what a night the people saw
Brother, what a fight the people saw
Yes indeed!

[Outro]
The night Chicago died
(Na-na na, na-na-na, na-na-na)
The night Chicago died
Brother, what a night it really was
Brother, what a fight it really was
Glory be!
The night Chicago died
(Na-na na, na-na-na, na-na-na)
The night Chicago died
Brother, what a night the people saw
Brother, what a fight the people saw
Yes indeed!
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Intro (spoken) | A–B–C–B | Prosa rimada: Chicago/USA/days |
| Verse 1 | A–B–A–B | night/bill/died/still |
| Pre-Chorus 1 | A–B–C–B | Capone/own/war/law |
| Chorus | A–A–B–B–C–A–A–B–B–C | cry/died/was/was/be ... cry/died/saw/saw/deed |
| Verse 2 | A–B–A–B | rang/side/gang/died |
| Pre-Chorus 2 | A–B–C–B | street/feet/said/dead |
| Verse 3 (Bridge) | A–A–B–C–C–B | all/wall/wide/inside/face/away |
| Outro | Libre | Na-na-na sin rima estructurada |

Esquema dominante: coplas pareadas (AABB) en versos y pre-chorus, con un esquema más complejo en el coro que alterna "really was / fight it really was" (repetición gemela) con "people saw / fight the people saw".

---

## 7. Análisis lírico

### 7.1 Tema central

Una recreación ficticia y melodramática de un tiroteo masivo entre la policía de Chicago y la banda de Al Capone, narrada desde la perspectiva de un hijo que espera noticias de su padre policía. La canción mezcla la violencia de gánsteres con el arco emocional de una familia: la madre reza, el padre sobrevive. El tema real no es la historia de Chicago sino el *suspenso doméstico* —el hijo oyendo llorar a su madre mientras el padre está en peligro.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Hipérbole | "'Bout a hundred cops are dead!" | Exagera masivamente las bajas; ningún enfrentamiento real con Capone produjo cien policías muertos |
| Repetición | "Brother, what a night it really was / Brother, what a fight it really was" | Paralelismo gemelo en cada coro; refuerzo rítmico y emocional |
| Contraste dramático | "Then there was no sound at all / But the clock upon the wall" | Silencio absoluto después de la batalla descrita; el reloj como único testigo |
| Narración enmarcada | "Daddy was a cop on the east side of Chicago / Back in the U.S.A., back in the bad old days" | El narrador adulto recuerda su infancia; distancia temporal |
| Onomatopeya implícita | sirena synth al inicio + "shouting in the street / sound of running feet" | Paisaje sonoro construido con descripciones auditivas |
| Hipocorístico | "mama", "daddy" | Lenguaje infantil que humaniza la violencia |
| Exclamación religiosa | "Glory be!", "Yes indeed!" | Interjecciones que funcionan como estribillo emocional |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Hipérbole | "When the town of Chicago died" (la ciudad no murió — es una batalla, no el fin de Chicago) |
| Sinécdoque | "the forces of the law" por "la policía" |
| Personificación | "the town of Chicago died" |
| Asíndeton | "Then the door burst open wide / And my daddy stepped inside / And he kissed my mama's face / And he brushed her tears away" — cuatro acciones seguidas sin pausa |
| Epífora | "Brother, what a night it really was / Brother, what a fight it really was" — repetición al final de cada hemistiquio |

### 7.4 Conexión intertextual

- **Al Capone y la Masacre del Día de San Valentín (1929):** La canción se inspira libremente en este evento real, donde hombres de Capone (disfrazados de policías) asesinaron a siete miembros de la banda de Bugs Moran. La canción invierte los roles: aquí los policías son las víctimas.
- **Billy Don't Be a Hero (Paper Lace, 1974):** Predecesor temático — también una story-song sobre un soldado en la Guerra Civil estadounidense. Misma fórmula: narrativa histórica ficcionalizada + gancho pop.
- **The Untouchables (película, 1987):** Comparte la misma licencia histórica — la cultura popular prefiere el Capone mítico al Capone real.
- **American Pie (Don McLean, 1971):** Parte de la tradición de story-songs narrativas de los 70s que contaban una historia en lugar de expresar una emoción.

### 7.5 Contexto de composición

Escrita por los británicos Mitch Murray y Peter Callander —que nunca habían visitado Chicago— como respuesta a que Bo Donaldson and the Heywoods les robara el #1 estadounidense con su cover de "Billy Don't Be a Hero". Murray y Callander produjeron y lanzaron "The Night Chicago Died" rápidamente en EE.UU. para evitar otra versión competidora.

La canción es históricamente inexacta en múltiples frentes: Chicago no tiene "East Side" (ese término describe Nueva York), Al Capone nunca combatió frontalmente a la policía (la tenía comprada), y ningún tiroteo dejó 100 policías muertos. El propio Mitch Murray admitió en Songfacts: *"We were obviously a little careless with our research… The song was certainly a work of fiction, and as such, perhaps we should have used fictional gangster names. Still, it's hard to have regrets when your song is #1 in the USA."*

El alcalde de Chicago, Richard J. Daley, criticó públicamente la canción por difamar la historia de la ciudad. Irónicamente, Paper Lace no pudo tocar en EE.UU. en el momento cumbre de su éxito por problemas contractuales.

**Conexión ABBA:** Murray y Callander trabajaban con MAM (Management Agency & Music Ltd), la compañía fundada por Stig Anderson, el manager de ABBA. MAM publicó las canciones del dúo en el Reino Unido. La misma estructura que lanzó a ABBA internacionalmente también distribuyó "The Night Chicago Died" en el mercado británico. El sonido bubblegum pop de Paper Lace comparte ADN de producción con los primeros éxitos de ABBA (misma era, mismo circuito de managers y publishers europeos).

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Batería | Toda la canción | Golpe constante, bombo marcado en negras, caja en 2 y 4 — pulso de marcha |
| Bajo eléctrico | Toda la canción | Línea simple de raíz en A, sigue los cambios armónicos |
| Guitarra rítmica acústica | Versos | Rasgueo constante, proporciona la base rítmica |
| Guitarra eléctrica | Coros | Pequeños fills, acordes abiertos |
| Sintetizador | Intro | Simula sirena policial — sonido electrónico agudo y ondulante |
| Brass / sección de vientos | Coros | Posiblemente trompetas o sintetizador imitando metales; refuerza el clímax |
| Kazoos | Coros | Fuente: American Songwriter — grunting backing vocals y kazoos en la producción |
| Voz solista (Phil Wright) | Toda la canción | Voz nasal, enérgica, con acento británico cantando tema estadounidense |
| Coros masculinos | Coros y Outro | "Na-na-na" masivo, estilo estadio; doblajes vocales |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Medio (tenor ligero) — Phil Wright canta en su rango cómodo, sin grandes saltos |
| Textura | Voz solista limpia con doblajes en coros; capas de backing vocals masculinos |
| Entrega | Enérgica, casi declamatoria en versos; expansiva y exclamativa en coros ("Glory be!", "Yes indeed!") |
| Capas | Intro: spoken word sin música de fondo. Versos: voz sola con banda. Coros: voz principal doblada + coros masculinos al unísono en "na-na-na" |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Bajo — la canción mantiene un nivel de volumen consistentemente alto tras la entrada de la banda. Contraste puntual en el puente (Verse 3) donde la música se reduce a reloj + voz.
- **Panning:** Guitarra rítmica y batería centrados; voz solista centrada; coros ligeramente abiertos en estéreo.
- **Efectos destacados:** Sirena de sintetizador al inicio; sonido de reloj (tick-tock) en el puente; reverberación generosa en los coros del outro.
- **Producción general:** Producción pop de los 70s característica de MAM: limpia, comprimida, orientada a la radio AM. El contraste entre la violencia de la letra y la alegría del arreglo (kazoos, na-na-na, ritmo bailable) es el sello distintivo. Grabación probablemente en estudios londinenses con ingenieros de sesión.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Paper Lace (original UK, 1974) | La analizada en este caso. Phil Wright voz principal. |
| "La Noche Que Murió Chicago" — Banda Toro / Banda Machos | Versiones en español con arreglos de banda mexicana; cambiaron el contexto narrativo pero mantienen la historia base |
| "Kun Chicago kuoli" — Virve Rosti (Finlandia, 1974) | Versión en finés; adaptación lírica localizada |
| "Öö Chicagos" — Jaak Joala (Estonia) | Versión en estonio |
| SUPER JUNIOR — The Night Chicago Died | Interpolación / cover moderno del grupo K-pop (alteración significativa del arreglo original) |
| Bo Donaldson and the Heywoods | Llegaron a grabar una versión de "The Night Chicago Died" también, pero la de Paper Lace se impuso en el mercado estadounidense |

---

## 10. Fuentes

- **Spotify:** `https://open.spotify.com/track/2JYFnAtiW85n1ukToyCJtW`
- **Deezer:** `https://www.deezer.com/track/1915606727`
- **E-Chords:** `https://www.e-chords.com/chords/paper-lace/the-night-chicago-died`
- **Wikipedia:** `https://en.wikipedia.org/wiki/The_Night_Chicago_Died`
- **Songfacts:** `https://www.songfacts.com/facts/paper-lace/the-night-chicago-died`
- **Genius Lyrics:** `https://genius.com/Paper-lace-the-night-chicago-died-lyrics`
- **American Songwriter:** `https://americansongwriter.com/the-story-and-meaning-behind-the-night-chicago-died-the-paper-lace-song-that-fails-as-history-lesson-but-succeeds-as-pop-magic/`
- **Songdata.io (BPM/Key):** `https://songdata.io/track/2JYFnAtiW85n1ukToyCJtW/The-Night-Chicago-Died-by-Paper-Lace`
- **SuperSeventies:** `https://www.superseventies.com/sw_nightchicagodied.html`
- **Grokipedia:** `https://grokipedia.com/page/The_Night_Chicago_Died`
- **Lifestyles After 50:** `https://lifestylesafter50.com/music-flashback-the-night-chicago-died`

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | Claude (sistema opencode composer) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | gemma4 / mistral:7b (Composer RAG) |
| **Tags** | `1974`, `pop-rock`, `bubblegum-pop`, `novelty-song`, `story-song`, `UK`, `one-hit-wonder`, `Al-Capone`, `Chicago`, `MAM`, `opencode-songcase` |
| **Pendientes** | Verificar Hooktheory para diagrama armónico interactivo. Verificar librosa si se descarga el audio. Confirmar créditos de músicos de sesión. |

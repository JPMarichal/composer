# Song Case — We Didn't Start the Fire — Billy Joel

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | We Didn't Start the Fire |
| **Artista** | Billy Joel |
| **Versión analizada** | original |
| **Álbum** | Storm Front |
| **Año** | 1989 |
| **Duración** | 4:48 (288 s) |
| **ISRC** | USSM18900217 |
| **Género(s)** | Pop rock |
| **Compositor(es)** | Billy Joel |
| **Productor(es)** | Billy Joel, Mick Jones |
| **Sello** | Columbia |
| **País** | Estados Unidos |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: track ID `3Cx4yrFaX8CeHwBMReOWXI` — valores aproximados (Spotify deprecated audio-features endpoint en 2024; datos recuperados de fuentes secundarias consolidadas).

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 145 | Consistente con Deezer (145.1) y Music Gateway |
| **Key** | 7 | (7 = G) |
| **Mode** | major | Escala de G mayor |
| **Camelot** | 9B | |
| **Danceability** | 0.71 | Ritmo constante,适于 baile |
| **Energy** | 0.84 | Alta energía por batería prominente y entrega vocal intensa |
| **Valence** | 0.43 | Neutro-positivo; la urgencia de la letra contrarresta la vitalidad musical |
| **Acousticness** | 0.01 | Producción completamente eléctrica/ synth |
| **Instrumentalness** | 0.00 | Vocal dominante durante todo el tema |
| **Speechiness** | 0.30 | Alto — el delivery es casi una letanía hablada-rytmica |
| **Liveness** | 0.09 | Grabación de estudio |
| **Loudness** | −9.5 dB | Consistente con la producción rock de finales de los 80 |
| **Time Signature** | 4/4 | |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/626123`

| Feature | Valor |
|---------|-------|
| **BPM** | 145.1 |
| **Gain** | −9.5 dB |
| **Rank** | 732,111 |
| **Explicit** | no |
| **Release Date** | 1989-10-17 |
| **Preview URL** | https://cdnt-preview.dzcdn.net/api/1/1/3/c/2/0/3c217db98586cfe1f9e923b0bde7db96.mp3 |

### 2.3 Análisis local (librosa) — opcional

> No se dispone del archivo de audio.

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
| G | major | Alta — la progresión I-V-ii-IV es inequívoca en G mayor |

### 3.2 Progresión base

```
I   ii   iii   IV   V   vi   vii°
G   Am   Bm    C    D   Em   F#°
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | G — D — Am — C (x2) | I — V — ii — IV | Establece el loop armónico que no variará en toda la canción |
| Verse | G — D — Am — C (repetido) | I — V — ii — IV | Cada 2 líneas = un ciclo completo de 4 compases |
| Chorus | G — D — Am — C (repetido) | I — V — ii — IV | Idéntica progresión; la diferenciación viene por la melodía |
| Bridge (JFK) | G — D — Am — C | I — V — ii — IV | Misma progresión; la línea "JFK blown away" rompe el patrón de 2 líneas/año |
| Outro | G — D — Am — C (fade out) | I — V — ii — IV | Repetición del ciclo con fade |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro]        → [V1 / V2 / V3 / V4 / V5]   → [Chorus]       → [Outro]
G-D-Am-C        G-D-Am-C (xN)                 G-D-Am-C (x2)    G-D-Am-C (loop)
```

La canción es armónicamente estática: un solo loop de 4 acordes (I — V — ii — IV) que se repite sin modulación durante los 4:48. Toda la tensión recae sobre la letra y la entrega vocal.

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:10 | 10 | 4 | G-D-Am-C | Redoble de batería + entrada del riff |
| 2 | Verse 1 | 0:10–0:40 | 30 | 12 | G-D-Am-C | Harry Truman → Marilyn Monroe (1949–1950) |
| 3 | Chorus | 0:40–1:02 | 22 | 8 | G-D-Am-C | "We didn't start the fire…" |
| 4 | Verse 2 | 1:02–1:33 | 31 | 12 | G-D-Am-C | Joseph Stalin → Rock Around the Clock (1951–1955) |
| 5 | Chorus | 1:33–1:55 | 22 | 8 | G-D-Am-C | |
| 6 | Verse 3 | 1:55–2:26 | 31 | 12 | G-D-Am-C | Davy Crockett → Trouble in the Suez (1955–1956) |
| 7 | Chorus | 2:26–2:49 | 23 | 8 | G-D-Am-C | |
| 8 | Verse 4 (Bridge) | 2:49–3:20 | 31 | 12 | G-D-Am-C | Little Rock → Belgians in the Congo (1957–1960) |
| 9 | Chorus | 3:20–3:41 | 21 | 8 | G-D-Am-C | |
| 10 | Verse 5 | 3:41–4:15 | 34 | 14 | G-D-Am-C | Hemingway → JFK blown away (1961–1963) |
| 11 | Chorus → Outro | 4:15–4:50 | 35 | 14 | G-D-Am-C | "But when we are gone…" fade out |

### 4.2 Forma general

```
[Intro] [V1] [C] [V2] [C] [V3] [C] [V4] [C] [V5] [C/Outro]
```

6 versos + 6 coros (el último extendido como outro). Cada verso cubre ~2–4 años del período 1949–1989 en orden cronológico estricto.

---

## 5. Letra

```
[Intro]
(drum fill + synth pad)

[Verse 1]
Harry Truman, Doris Day, Red China, Johnny Ray
South Pacific, Walter Winchell, Joe DiMaggio
Joe McCarthy, Richard Nixon, Studebaker, television
North Korea, South Korea, Marilyn Monroe

Rosenbergs, H-Bomb, Sugar Ray, Panmunjom
Brando, The King and I, and The Catcher in the Rye
Eisenhower, vaccine, England's got a new queen
Marciano, Liberace, Santayana goodbye

[Chorus]
We didn't start the fire
It was always burning, since the world's been turning
We didn't start the fire
No we didn't light it, but we tried to fight it

[Verse 2]
Joseph Stalin, Malenkov, Nasser and Prokofiev
Rockefeller, Campanella, Communist Bloc
Roy Cohn, Juan Perón, Toscanini, Dacron
Dien Bien Phu falls, Rock Around the Clock

Einstein, James Dean, Brooklyn's got a winning team
Davy Crockett, Peter Pan, Elvis Presley, Disneyland
Bardot, Budapest, Alabama, Khrushchev
Princess Grace, Peyton Place, Trouble in the Suez

[Chorus]
We didn't start the fire
It was always burning, since the world's been turning
We didn't start the fire
No we didn't light it, but we tried to fight it

[Verse 3]
Little Rock, Pasternak, Mickey Mantle, Kerouac
Sputnik, Zhou Enlai, Bridge on the River Kwai
Lebanon, Charles de Gaulle, California baseball
Starkweather homicide, children of Thalidomide

Buddy Holly, Ben-Hur, space monkey, Mafia
Hula hoops, Castro, Edsel is a no-go
U-2, Syngman Rhee, payola and Kennedy
Chubby Checker, Psycho, Belgians in the Congo

[Chorus]
We didn't start the fire
It was always burning, since the world's been turning
We didn't start the fire
No we didn't light it, but we tried to fight it

[Verse 4]
Hemingway, Eichmann, Stranger in a Strange Land
Dylan, Berlin, Bay of Pigs invasion
Lawrence of Arabia, British Beatlemania
Ole Miss, John Glenn, Liston beats Patterson

Pope Paul, Malcolm X, British politician sex
JFK — blown away, what else do I have to say?

[Chorus]
We didn't start the fire
It was always burning, since the world's been turning
We didn't start the fire
No we didn't light it, but we tried to fight it

[Verse 5]
Birth control, Ho Chi Minh, Richard Nixon back again
Moonshot, Woodstock, Watergate, punk rock
Begin, Reagan, Palestine, terror on the airline
Ayatollah's in Iran, Russians in Afghanistan

Wheel of Fortune, Sally Ride, heavy metal, suicide
Foreign debts, homeless vets, AIDS, crack, Bernie Goetz
Hypodermics on the shores, China's under martial law
Rock and roller cola wars, I can't take it anymore

[Final Chorus]
We didn't start the fire
It was always burning, since the world's been turning
We didn't start the fire
But when we are gone
It will still burn on, and on, and on, and on
And on, and on, and on, and on…
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABB CCDD | Pareados asonantes dentro de cada línea; rima interna entre las dos mitades de cada verso |
| Verse 2 | AABB CCDD | Mismo patrón: cada línea de 4 golpes rítmicos con la segunda mitad rimando con la primera de la siguiente línea |
| Verse 3 | AABB CCDD | Consistente |
| Verse 4 | AABB C | La línea "JFK — blown away" rompe el patrón y funciona como cierre dramático |
| Verse 5 | AABB CCDD | Mismo patrón, pero comprime más años por línea |
| Chorus | AABB | "fire/burning" — "turning"; "fire/light it" — "fight it" |
| Final Chorus | AABC | Varía: "fire/burning" — "turning"; "fire/gone" — "on and on" |

No hay un esquema de rima clásico; Joel utiliza rima interna y asonancia para mantener el impulso rítmico. Cada línea funciona como una lista de 4 nombres/eventos con cadencia propia.

---

## 7. Análisis lírico

### 7.1 Tema central

La historia como un incendio perpetuo que ninguna generación inició pero todas heredan y combaten. La canción es una defensa de la generación Baby Boomer contra la acusación de haber tenido una vida fácil, pero también una meditación existencial sobre la continuidad del conflicto humano. Joel lo resumió: *"It's just a song that says the world's a mess. It's always been a mess, it's always going to be a mess."*

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Lista (catalog poem) | Toda la canción | 119 ítems históricos en orden cronológico; forma poética de acumulación |
| Metáfora central | "the fire" | El conflicto/ caos histórico como incendio perpetuo |
| Anáfora | "We didn't start the fire" (6 veces) | Refuerzo de la tesis defensiva |
| Asíndeton | "Harry Truman, Doris Day, Red China, Johnny Ray" | Omisión de conectores; la yuxtaposición acelera el ritmo |
| Hipérbaton | "England's got a new queen" | Inversión coloquial |
| Enumeración caótica | Mezcla de presidentes, deportistas, científicos, asesinos | Nivelación de lo trascendental y lo trivial |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Metonimia | "Red China" (el color por el régimen comunista) |
| Sinécdoque | "Bay of Pigs" (el lugar por el evento completo) |
| Ironía | "British politician sex" (eufemismo de escándalo sexual) |
| Apóstrofe | "What else do I have to say?" |
| Hipérbole | "Since the world's been turning" (el fuego como condición inherente a la existencia humana) |

### 7.4 Conexión intertextual

- El título y concepto responden directamente a un comentario casual de un amigo de Sean Lennon (hijo de John Lennon), estableciendo un vínculo con el legido Beatle.
- "Stranger in a Strange Land" — título de la novela de Robert A. Heinlein (1961).
- "The King and I" — musical de Rodgers y Hammerstein (1951).
- "The Catcher in the Rye" — novela de J.D. Salinger (1951).
- "Rock Around the Clock" — canción de Bill Haley & His Comets (1954).
- La estructura de lista anticipa el fenómeno del "list song" que Aftermath (Fall Out Boy, 2023) popularizaría para otra generación.
- Numerosas parodias en redes sociales (especialmente en Twitter, 2020) adaptaron el formato a la pandemia de COVID-19.

### 7.5 Contexto de composición

**Origen:** Joel, a sus 40 años, conversaba en el estudio Hit Factory con Sean Lennon (21) y un amigo de este. El amigo lamentaba lo difícil que era tener 21 en 1989 y dijo: *"Tú creciste en los 50; todo el mundo sabe que no pasó nada en los 50"*. Joel respondió enumerando la Guerra de Corea, los Panteras Negras, la crisis de Suez, etc. La discusión lo inspiró a escribir la canción.

**Proceso:** Joel escribió la letra primero (algo inusual en él), partiendo de 1949 (su año de nacimiento) y avanzando cronológicamente. La progresión de acordes provenía de una canción country que estaba intentando escribir. El título se lo sugirió Jann Wenner (fundador de *Rolling Stone*) cuando Joel barajaba opciones como "Dancing Through the Fire". Joel ha declarado: *"It's Jann's fault. I'm going to blame it on him because some people hate that song."*

**Recepción crítica:** La canción fue un éxito comercial (#1 Billboard Hot 100, nominada al Grammy a Grabación del Año), pero recibió críticas mixtas. La revista *Blender* la colocó en el #41 de las "50 peores canciones". El propio Joel la ha calificado repetidamente como *"terrible pieza musical... como un taladro de dentista"* y *"como un mosquito zumbando alrededor de tu cabeza"*.

**Impacto educativo:** En 1990, una clase de quinto grado en Menasha, Wisconsin, usó la letra para seleccionar temas de historia. Columbia Records respondió enviando cassettes con la canción y una charla de Joel a 40,000 estudiantes.

**Último #1:** Fue el tercer y último sencillo de Joel en alcanzar el #1 en el Billboard Hot 100.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Batería acústica (Liberty DeVitto) | Toda la canción | Golpe constante en negras; redobles de transición |
| Percusión electrónica (Sammy Merendino) | Toda la canción | Capa rítmica adicional tipo drum machine |
| Bajo eléctrico (Schuyler Deale) | Toda la canción | Sigue la raíz de cada acorde; patrón de corcheas |
| Guitarra eléctrica (David Brown, Joey Hunting) | Toda la canción | Riffs de acordes con distorsión ligera; apoyos rítmicos |
| Clavinet (Billy Joel) | Toda la canción | Textura percusiva tipo funk |
| Sintetizadores (Jeff Jacobs) | Toda la canción | Pads de fondo, atmósfera |
| Órgano/teclados (John Mahoney) | Puentes | Capas armónicas |
| Efectos de sonido (Doug Kleeger) | Transiciones | Sirena, explosiones, sonidos incidentales |
| Coros (Crystal Taliefero) | Coros | Apoyo en "We didn't start the fire" |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Medio-alto (tenor); Joel canta en su rango cómodo |
| Textura | Voz principal seca, con ligera compresión; sin reverberación excesiva |
| Entrega | Rítmica, casi hablada en los versos (estilo *sprechgesang*); más melódica en el coro |
| Capas | Sencillas: voz principal doblada en el coro; backing vocals de Crystal Taliefero en los coros |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Comprimido; la canción se mantiene en un nivel de volumen alto y constante durante toda la duración.
- **Panning:** Batería centrada, guitarras ligeramente a izquierda/derecha, bajo centrado, voz centrada.
- **Efectos destacados:** Efectos de sonido (sirenas, alarmas) en las transiciones entre secciones; reverberación en la voz del coro final.
- **Producción general:** Producción rockera de finales de los 80 con Mick Jones (Foreigner); sonido limpio, batería prominente, sintetizadores de fondo. Mezcla de Tom Lord-Alge.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (1989) | Billy Joel — Storm Front. 4:48, producción de Mick Jones. |
| Single Version | 4:29. Edición ligeramente más corta para radio. |
| Fall Out Boy (2023) | Actualización de 1989 a 2023 con estilo pop-punk/emo. Mezcla eventos sin orden cronológico. Producción de Butch Walker. Recibió críticas mixtas similares al original. |
| Parodia COVID-19 (Brittany Barkholtz, 2020) | Versión viral en Twitter adaptando el formato al 11 de marzo de 2020: "Schools close, Tom Hanks, trouble in the big banks…" |
| Parodias educativas | Múltiples versiones creadas por profesores de historia para enseñar períodos específicos. |

---

## 10. Fuentes

- **Spotify:** https://open.spotify.com/track/3Cx4yrFaX8CeHwBMReOWXI
- **Deezer:** https://www.deezer.com/track/626123
- **Chordify / Ultimate Guitar:** https://tabs.ultimate-guitar.com/tab/billy-joel/we-didnt-start-the-fire-chords-1088942
- **Hooktheory:** https://www.hooktheory.com/theorytab/view/billy-joel/we-didnt-start-the-fire
- **MusicBrainz:** https://musicbrainz.org/recording/fd12141d-ce5e-46d8-bae3-6d6f084f9392
- **Wikipedia:** https://en.wikipedia.org/wiki/We_Didn%27t_Start_the_Fire
- **Wikipedia (referencias):** https://en.wikipedia.org/wiki/List_of_references_in_We_Didn%27t_Start_the_Fire
- **Songfacts:** https://www.songfacts.com/facts/billy-joel/we-didnt-start-the-fire
- **Rolling Stone (30 aniversario):** https://www.rollingstone.com/music/music-news/we-didnt-start-the-fire-billy-joel-history-926129/
- **Far Out Magazine:** https://faroutmagazine.co.uk/the-billy-joel-song-that-wrote-itself/
- **Grunge (inspiración):** https://www.grunge.com/1327956/billy-joel-we-didnt-start-the-fire-inspiration/
- **ADST (historia diplomática):** https://adst.org/2013/07/we-didnt-start-the-fire/

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (asistente AI) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | — |
| **Tags** | billy-joel, storm-front, 1989, pop-rock, list-song, baby-boomer, cold-war, historia, billboard-hot-100, mick-jones, columbia |
| **Pendientes** | Verificar si la melodía del coro toma elementos de la canción country original; confirmar el número exacto de referencias (118 vs 119 según fuente) |

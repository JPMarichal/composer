# Song Case — La Noche Que Murió Chicago (La Noche de Chicago) — Mirla Castellanos / Paper Lace

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.
>
> **Nota sobre versiones:** Este análisis cubre principalmente la versión original de Paper Lace (1974) y la primera adaptación al español por Mirla Castellanos (1974). Existen otras versiones en español: Banda Macho / La Super Banda Macho (1974), Banda Toro (1994) y Banda Machos (2004), con letras muy diferentes.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | La Noche Que Murió Chicago (The Night Chicago Died) |
| **Artista** | Paper Lace (original) / Mirla Castellanos (versión en español, 1974) |
| **Versión analizada** | Original en inglés (Paper Lace) + versión español (Mirla Castellanos, primaria) |
| **Álbum** | …And Other Bits of Material (Paper Lace) / Mirla (Mirla Castellanos) |
| **Año** | 1974 (ambas versiones) |
| **Duración** | 3:30 (Paper Lace) / 3:33 (Mirla Castellanos) |
| **ISRC** | GBUM72105385 (Paper Lace) / US6R21328158 (Mirla Castellanos) |
| **Género(s)** | Pop rock, bubblegum pop (Paper Lace); Pop latino, balada (Mirla Castellanos) |
| **Compositor(es)** | Mitch Murray, Peter Callander |
| **Productor(es)** | Mitch Murray, Peter Callander |
| **Sello** | Philips / Mercury (Paper Lace); Discos Yare / Suramericana del Disco (Mirla) |
| **País** | Reino Unido (Paper Lace); Venezuela (Mirla Castellanos) |

### 1.1 Historial de versiones en español

| Versión | Artista | Año | País | Notas |
|---------|---------|-----|------|-------|
| **La Noche de Chicago** | **Mirla Castellanos** | **1974** | **Venezuela** | **Primera versión en español. Traducción de Miguel Ángel Landa y Raúl Zenteno. Álbum *Mirla*.** |
| La Noche Que Murió Chicago | La Super Banda Macho | 1974 | México | Letra muy diferente a la de Mirla. Sello Caytronics. |
| La Noche Que Chicago Se Murió | Banda Toro | 1994 | México | Misma letra que Banda Macho, en estilo banda sinaloense. |
| La Noche Que Chicago Murió | Banda Machos | 2004 | México | Álbum *Pura Pasión*. Versión similar a Banda Macho. |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: Estimaciones basadas en análisis de la grabación original.

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | ~115 | Original Paper Lace; Mirla: 104 |
| **Key** | 0 (C) | C Major |
| **Mode** | major | |
| **Camelot** | 8B | |
| **Danceability** | ~0.55 | Ritmo bailable, pero narrativa densa |
| **Energy** | ~0.70 | Pop rock enérgico, batería prominente |
| **Valence** | ~0.50 | Tensión narrativa contrarresta melodía alegre |
| **Acousticness** | ~0.20 | Sintetizador (sirena) + banda completa |
| **Instrumentalness** | ~0.0 | Muy vocal |
| **Speechiness** | ~0.05 | Intro hablada, resto cantado |
| **Liveness** | ~0.10 | Grabación de estudio |
| **Loudness** | ~-10 dB | |
| **Time Signature** | 4/4 | |

### 2.2 Deezer API

#### Paper Lace — Original

| Feature | Valor |
|---------|-------|
| **BPM** | 0 (no disponible) |
| **Gain** | -12.2 dB |
| **Rank** | 337,978 |
| **Explicit** | no |
| **Release Date** | 2022-09-23 (reedición) |
| **Preview URL** | https://www.deezer.com/track/1915606727 |
| **Deezer ID** | 1915606727 |

#### Mirla Castellanos — Versión en español (1974)

| Feature | Valor |
|---------|-------|
| **BPM** | 103.6 |
| **Gain** | -11.0 dB |
| **Rank** | 78,428 |
| **Explicit** | no |
| **Release Date** | 2015-02-19 (reedición) |
| **Preview URL** | https://www.deezer.com/track/66219783 |
| **Deezer ID** | 66219783 |

#### La Super Banda Macho — Versión mexicana (1974)

| Feature | Valor |
|---------|-------|
| **BPM** | 111.1 |
| **Gain** | -12.8 dB |
| **Rank** | 21,657 |
| **Explicit** | no |
| **Release Date** | 2006-06-30 (recopilatorio) |
| **Preview URL** | https://www.deezer.com/track/13323119 |
| **Deezer ID** | 13323119 |
| **ISRC** | MXF147400121 |

### 2.3 Análisis local (librosa) — opcional

> Pendiente — requiere descarga del audio.

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
| C (Do Mayor) | major | Alta |

### 3.2 Progresión base

```
I   ii   iii   IV   V   vi   vii°
C   Dm   Em    F    G   Am   B°
```

### 3.3 Acordes por sección — Paper Lace original (C Major)

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | C — E — C — F — E — Cm — Bb | I — III — I — IV — III — iii♭ — ♭VII | Sirena de sintetizador + acordes de tensión |
| Verse (estrofa) | C — Dm — G — C | I — ii — V — I | Progresión clásica pop, movimiento por cuartas |
| Verse 2 (transición) | Dm — G — C | ii — V — I | Leading al chorus |
| Chorus | C — Dm — G — C | I — ii — V — I | Misma progresión, máxima energía |
| Bridge (batalla) | Dm — G — C | ii — V — I | Tensión mantenida |
| Bridge (cien policías) | D — G — C | II — V — I | borrowed II (tensión mayor) |
| Outro / Resolución | Dm — G — C — Em — Dm — G — C | ii — V — I — iii — ii — V — I | Padre regresa, resolución emocional |

### 3.4 Diagrama de la progresión

```
[Intro]        → [Verse 1]      → [Chorus]          → [Verse 2]
C E C F E Cm Bb   C Dm G C        C Dm G C           Dm G C

[Chorus]         → [Bridge/batalla] → [Chorus]       → [Bridge/resolución]
C Dm G C           Dm G C           C Dm G C           Dm G C
                    D G C (peak)

[Outro]
C Em Dm G C  (x2)
```

---

## 4. Estructura

### 4.1 Mapa de secciones — Paper Lace original

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:13 | ~13 | 4+4 | C—E—C—F—E—Cm—Bb | Sirena sintética + spoken word |
| 2 | Verse 1 | 0:13–0:31 | ~18 | 8 | C—Dm—G—C | "Daddy was a cop…" |
| 3 | Chorus | 0:31–0:48 | ~17 | 8 | C—Dm—G—C | "I heard my momma cry…" |
| 4 | Verse 2 | 0:48–1:06 | ~18 | 8 | C—Dm—G—C | "And the sound of the battle rang…" |
| 5 | Chorus | 1:06–1:23 | ~17 | 8 | C—Dm—G—C | |
| 6 | Bridge | 1:23–1:41 | ~18 | 8 | Dm—G—C—D—G—C | "Then there was no sound at all…" (tensión con D) |
| 7 | Chorus (variado) | 1:41–1:58 | ~17 | 8 | C—Dm—G—C | |
| 8 | Outro | 1:58–3:30 | ~92 | — | C—Em—Dm—G—C | Padre regresa, nana-nana, fade out |

### 4.2 Forma general

```
[Intro spoken/sirena] [V1] [C] [V2] [C] [Bridge (batalla)] [C] [Outro (resolución)] [Fade]
```

---

## 5. Letra

### Versión original — Paper Lace (1974)

```
[Spoken Intro]
Daddy was a cop on the East Side of Chicago
Back in the USA, back in the bad old days

[Verse 1]
In the heat of a summer night
In the land of the dollar bill
When the town of Chicago died
And they talk about it still

When a man named Al Capone
Tried to make that town his own
And he called his gang to war
With the forces of the law

[Chorus]
I heard my momma cry
I heard her pray the night Chicago died
Brother, what a night it really was
Brother, what a fight it really was
Glory be

I heard my momma cry
I heard her pray the night Chicago died
Brother, what a night the people saw
Brother, what a fight the people saw
Yes, indeed

[Verse 2]
And the sound of the battle rang
Through the streets of the old East Side
Till the last of the hoodlum gang
Had surrendered up or died

There was shouting in the street
And the sound of running feet
And I asked someone who said
'Bout a hundred cops are dead

[Chorus]
I heard my momma cry
I heard her pray the night Chicago died
Brother, what a night it really was
Brother, what a fight it really was
Glory be

I heard my momma cry
I heard her pray the night Chicago died
Brother, what a night the people saw
Brother, what a fight the people saw
Yes, indeed

[Bridge]
Then there was no sound at all
But the clock upon the wall
Then the door burst open wide
And my daddy stepped inside

And he kissed my momma's face
And he brushed her tears away

[Outro]
The night Chicago died (no, no, no)
The night Chicago died
Brother, what a night the people saw
Brother, what a fight the people saw
Yes, indeed

The night Chicago died
The night Chicago died
Brother, what a night it really was
Brother, what a fight it really was
Glory be
```

### Versión — Mirla Castellanos (1974)

```
[Intro hablado / Spoken]
En los años 20 sucedió en Chicago
El F.B.I. está aquí
Nadie se podrá escapar

[Verse 1]
Fue una noche de verano, cuando la ciudad murió
Me contaron que fue en vano, lo que el hampa resistió
Al Capone se llamó, al que la ley se enfrentó
Y esa noche decidió terminar con el control

[Chorus]
Y vi a mamá llorar, la oí rezar cuando papá salió
Fue la noche que el mundo tembló
La noche que la ciudad murió — y fue así

Y vi a mamá llorar, la oí rezar cuando papá salió
Fue la noche que el mundo tembló
La noche que la ciudad murió — y fue así

[Verse 2]
Y los gangster disparaban, sin pedir ni dar cuartel
Uno a uno van cayendo, y los muertos son ya cien
Y lloraban las mujeres, y los hombres maldecían
Pero solo era el lamento del Chicago que moría

[Chorus]
Y vi a mamá llorar, la oí rezar cuando papá salió
Fue la noche que el mundo tembló
La noche que la ciudad murió — y fue así

Y vi a mamá llorar, la oí rezar cuando papá salió
Fue la noche que el mundo tembló
La noche que la ciudad murió — y fue así

[Bridge / Resolución]
Y quedó todo en silencio, la batalla terminó
Y se impuso al fin la ley, sobre el hampa que era rey
Y mi padre se marchó, el Chicago así murió

[Outro]
Chicago ya murió
Fue la noche que el mundo tembló
La noche que la ciudad murió — y fue así

Na na na na na na na na na na na
Fue la noche que el mundo tembló
La noche que la ciudad murió — y fue así

Y vi a mamá llorar
Na na na na na na na na na na na

Chicago ya murió
Fue la noche que el mundo tembló
La noche que la ciudad murió — y fue así
```

### Versión — La Super Banda Macho / Banda Toro (1974 / 1994)

```
[Verse 1]
Papá trabajaba, cuando vivía en Chicago
Siempre policía él fue, siempre al lado de la ley
Una noche de verano, en la tierra del dólar fue
Donde todo Chicago vio, déjenme explicarles que

Cuando el señor Al Capone, de la ciudad se adueñó
A su pandilla llamó, por las fuerzas del señor

[Chorus]
Mi madre oí llorar, la noche en que Chicago se murió
Hermano, qué noche mandó Dios
Hermano, qué guerra tan atroz — gloria y paz

Mi madre oí llorar, la noche en que Chicago se murió
Hermano, qué noche mandó Dios
Esa guerra todo el mundo vio — yo la vi

[Verse 2]
El sonar de las calles fue, por el sur de la gran ciudad
Una guerra sin cuartel, hasta que todo acabó
Se escuchó alguien que gritó, entre la gente correr
En las calles se murieron, policías más de cien

[Chorus]

[Bridge]
Y después nada sonó, solo el reloj se escuchó
Hasta que la puerta se abrió, y mi padre apareció
A mi madre la besó, y sus lágrimas secó

[Outro]
La noche en que murió, Chicago se murió
Hermano, qué noche mandó Dios
Hermano, qué guerra tan atroz — gloria y paz

La noche en que murió, Chicago se murió
Hermano, qué noche mandó Dios
Esa guerra todo el mundo vio — yo la vi
```

---

## 6. Esquema de rima

### Paper Lace original

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABB CCDD | Pareados asonantes |
| Chorus | EEF GGHF | Estribillo con estructura libre, variación en L4 |
| Verse 2 | IIJJ KKLL | Mismo patrón que V1 |
| Bridge | MMNN OOPP | Pareados, transición al desenlace |

### Mirla Castellanos

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | ABAB CDCD | Rima asonante más libre que el original |
| Chorus | EFG EFG | Repetición del hook "y fue así" |
| Verse 2 | ABAB CDCD | |
| Bridge | AABB CCDD | |

### Banda Macho / Banda Toro

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABB CCDD | Rima consonante más estricta |
| Chorus | EEF GGHF | Similar al original, con "gloria y paz" |

---

## 7. Análisis lírico

### 7.1 Tema central

La canción narra un tiroteo ficticio entre la policía de Chicago y la mafia de Al Capone, visto a través de los ojos de un niño cuyo padre es policía. El tema central es la angustia familiar en medio de la violencia urbana: la madre reza, el padre sale a una batalla que no eligió, y la ciudad muere simbólicamente. El final es agridulce: el padre sobrevive, pero Chicago ha cambiado para siempre.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Narración en primera persona | "I heard my momma cry" / "Y vi a mamá llorar" | El narrador es testigo infantil, no protagonista |
| Hipérbole | "About a hundred cops are dead" / "Los muertos son ya cien" | Exageración histórica del conflicto |
| Personificación | "When the town of Chicago died" / "La noche que la ciudad murió" | Chicago es tratada como un ser vivo que muere |
| Simbolismo del reloj | "But the clock upon the wall" / "Solo el reloj se escuchó" | El silencio después de la batalla, la espera |
| Ironía dramática | "Brother, what a fight it really was" | El oyente sabe que la batalla es ficción histórica |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Anáfora | "Brother, what a night… Brother, what a fight…" |
| Asíndeton | "Na na na na na na na na na na na" — vacío lírico que sugiere lo indecible |
| Epífora | "The night Chicago died" repetido al final de cada estrofa |
| Hipérbaton | "Of the old East Side" / "Del Chicago que moría" |

### 7.4 Conexión intertextual

- **Matanza de San Valentín (1929):** La canción se inspira en la masacre real, aunque en la realidad murieron 7 miembros de la banda de Bugs Moran a manos de hombres de Capone disfrazados de policías. No hubo cien policías muertos ni un tiroteo masivo.
- **Al Capone:** Figura histórica real, arrestado en 1932 por evasión de impuestos.
- **Género de "balada de muerte urbana":** Similar a "Billy Don't Be a Hero" (también de Paper Lace), "The Night They Drove Old Dixie Down" (The Band), "Patches" (Clarence Carter).
- **Paper Lace vs. Suno AI contexto de composición:** Esta canción es un ejemplo perfecto de cómo un compositor británico (Mitch Murray) que nunca visitó Chicago creó un éxito global basado en películas de gánsteres. Paralelo relevante para el catálogo de composición del proyecto Composer.

### 7.5 Contexto de composición

- **Origen:** Mitch Murray y Peter Callander, compositores británicos de Nottingham, nunca habían estado en Chicago. Basaron la letra en películas de gánsteres. En entrevista en *Beat Club*, Callander dijo: "There's an East Side of everywhere!" al ser confrontado con que Chicago no tiene un East Side.
- **Reacción de Chicago:** Paper Lace envió el sencillo al alcalde Richard J. Daley, quien lo detestó. Un miembro de su staff sugirió que la banda "saltara al río Chicago, metiera la cabeza bajo el agua tres veces y saliera dos. Por favor, díganos: ¿están locos?"
- **Éxito:** #1 Billboard Hot 100, #3 UK, #2 Canadá. Disco de Oro (RIAA). Paper Lace no pudo tocar en EE. UU. por problemas contractuales.
- **Versión Mirla Castellanos:** Traducida por Miguel Ángel Landa (su entonces esposo) y Raúl Zenteno. La versión de Mirla suaviza el sonido: orquestación más melódica, menos percusiva, voz mezzo-soprano en lugar de la voz masculina del original. La letra en español es más libre — no es traducción literal sino adaptación que conserva la estructura narrativa pero modifica imágenes y métrica para ajustarse al español.
- **Versión Banda Macho:** Grabada en el mismo 1974 en México por La Super Banda Macho. La letra es sustancialmente diferente: más cercana al original inglés en la narrativa del padre policía, pero con un giro religioso ("por las fuerzas del señor", "gloria y paz"). Esta versión es la que pervive en el imaginario mexicano a través de Banda Toro (1994) y Banda Machos (2004).
- **Versión Banda Toro (1994):** Se convirtió en un himno de fiestas populares en México, a pesar de su temática violenta. Irónicamente, la versión más festiva (ritmo de banda sinaloense) narra la historia más trágica.

---

## 8. Producción

### 8.1 Instrumentación — Paper Lace original

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Sintetizador analógico | Intro | Imita sirena de policía — el sonido más icónico de la canción |
| Batería acústica | Todas | Ritmo constante de pop rock, bombo en negras |
| Bajo eléctrico | Todas | Línea melódica simple, siguiendo la raíz de los acordes |
| Guitarra rítmica acústica | Verses | Rasgueo suave, apoyo armónico |
| Guitarra eléctrica | Chorus | Más presente, distorsión ligera |
| Piano / teclado | Verses, Bridge | Acentos, especialmente en la transición |
| Pandereta | Chorus | Refuerza el ritmo bailable |
| Voces masculinas (grupo) | Intro | Spoken word, casi susurrado |
| Coros | Chorus | Armonías vocales en "Brother, what a night…" |

### 8.2 Tratamiento vocal — Mirla Castellanos

| Característica | Descripción |
|----------------|-------------|
| Registro | Mezzo-soprano, brillante y proyectada |
| Textura | Voz solista con coros de acompañamiento |
| Entrega | Dramática, casi teatral — acorde con el estilo de diva latina de los 70 |
| Capas | Armonías en el estribillo, ad-libs en el outro |

### 8.3 Mezcla y dinámica — Paper Lace

- **Rango dinámico:** Medio. La canción mantiene un volumen relativamente constante con pequeñas variaciones entre verso y estribillo.
- **Panning:** Guitarra acústica centrada, batería con stereo estándar (hi-hat L, ride R), coros ligeramente paneados.
- **Efectos destacados:** Sirena de sintetizador (intro, filtro wah), reverberación en voces del estribillo, sonido de tic-tac de reloj en el bridge (0:08 en la versión con reloj).
- **Producción general:** Típica del pop británico de 1974. Grabación limpia, mezcla centrada en la voz narrativa. El spoken intro y la sirena le dan un carácter de "radio-teatro musical".

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| **Paper Lace (original, 1974)** | Pop rock británico. Voz masculina. Spoken intro con sirena sintética. Letra en inglés. BPM ~115. |
| **Mirla Castellanos (1974)** | Balada pop latino. Voz femenina (mezzo-soprano). Orquestación más suave. Letra adaptada al español (no traducción literal). BPM 104. Más melódica, menos percusiva. |
| **La Super Banda Macho (1974)** | Estilo banda mexicana temprana. Letra diferente con giro religioso ("gloria y paz"). ISRC MXF147400121. BPM 111. |
| **Banda Toro (1994)** | Banda sinaloense. Ritmo bailable (contraste irónico con la letra violenta). Misma letra que Banda Macho. La versión más popular en México. |
| **Banda Machos (2004)** | Estilo banda actualizado. Misma letra que Banda Macho. Álbum *Pura Pasión*. |
| **Vicky Rosti (Finlandia, 1975)** | Versión en finlandés "Kun Chicago kuoli". Traducción casi literal. #1 en Finlandia. |
| **Super Junior-K.R.Y. (Corea, 2006)** | Versión en coreano para drama *Hyena*. Misma melodía, letra completamente reescrita. |

---

## 10. Fuentes

- **Spotify (Paper Lace):** https://open.spotify.com/track/6DhENrLGgw5rZRI0AKTyiK
- **Spotify (Mirla Castellanos):** https://open.spotify.com/track/5HILgZ7by4PJnzPZnNfnLN
- **Deezer (Paper Lace):** https://www.deezer.com/track/1915606727
- **Deezer (Mirla Castellanos):** https://www.deezer.com/track/66219783
- **Deezer (Banda Macho):** https://www.deezer.com/track/13323119
- **CifraClub (Paper Lace):** https://www.cifraclub.com/paper-lace/30077/letra/translation.html
- **Ultimate Guitar (Paper Lace):** https://tabs.ultimate-guitar.com/tab/paper-lace/the-night-chicago-died-chords-803372
- **ChordU (Paper Lace):** https://chordu.com/chords-tabs-the-night-chicago-died-id_p-L0NpaErkk
- **Wikipedia (EN):** https://en.wikipedia.org/wiki/The_Night_Chicago_Died
- **Wikipedia (ES):** https://es.wikipedia.org/wiki/The_Night_Chicago_Died
- **Wikipedia (Mirla Castellanos):** https://es.wikipedia.org/wiki/Mirla_Castellanos
- **Acordes Banda Macho:** https://acordesdcanciones.com/banda-macho-la-noche-que-murio-chicago/
- **Letras.com (traducción):** https://www.letras.com/paper-lace/30077/traduccion.html
- **Frontera Collection (Banda Macho 45):** https://frontera.library.ucla.edu/es/recordings/la-noche-que-murio-chicago
- **Infobae (historia):** https://www.infobae.com/mexico/2025/02/19/la-tragica-historia-detras-de-la-cancion-la-noche-que-murio-chicago/
- **Blog Aquella Música (Mirla):** http://duquemusical.blogspot.com/2006/01/mirla-castellanos-la-noche-de-chicago.html

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | Asistente IA (OpenCode) + investigación web |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | — |
| **Tags** | Paper Lace, Mirla Castellanos, Banda Macho, Banda Toro, versión español, 1974, pop rock, balada, banda, Chicago, Al Capone, matanza San Valentín, cover, Venezuela, México |
| **Pendientes** | Verificar audio features vía Spotify API; análisis librosa local; encontrar edición original del álbum *Mirla* de 1974 (no reedición); verificar créditos exactos de traducción de Miguel Ángel Landa vs. Raúl Zenteno |

# Song Case — American Pie — Don McLean

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Deezer), análisis armónico de fuentes web, y análisis lírico-estructural. Archivo indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | American Pie |
| **Artista** | Don McLean |
| **Versión analizada** | Original (álbum, 1971) |
| **Álbum** | *American Pie* |
| **Año** | 1971 |
| **Duración** | 8:42 (LP), 8:34 (streaming), 4:11+4:31 (single edit) |
| **ISRC** | USEM38600088 |
| **Género(s)** | Folk rock, Singer-songwriter, Soft rock |
| **Compositor(es)** | Don McLean |
| **Productor(es)** | Ed Freeman |
| **Sello** | United Artists (original), Capitol/EMI (reediciones) |
| **País** | Estados Unidos |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 138.7 |
| **Gain** | −12.1 dB |
| **Rank** | 810,532 |
| **Explicit** | No |
| **Release Date** | 2003-06-12 (reedición) |
| **ISRC** | USEM38600088 |
| **Preview URL** | https://cdnt-preview.dzcdn.net/... |

### 2.2 Hooktheory

| Feature | Valor |
|---------|-------|
| **Key** | G Major |
| **Tempo** | ~78 BPM (prólogo/outro), ~138-142 BPM (versos/coros) |
| **Meter** | 4/4 |
| **Chord Complexity** | 30/100 |
| **Melodic Complexity** | 58/100 |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| G | Major | Alta — toda la canción en G mayor, con uso extenso del ♭VII (F) prestado de G mixolidio/menor paralela. |

### 3.2 Progresión base

```
G     Am    Bm    C     D     Em    F#°
I     ii    iii   IV    V     vi    vii°
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro/Prologue | G – D – Em7 – Am – C – Em – D – G | I – V – vi7 – ii – IV – vi – V – I | Piano solo, lento, rubato. |
| Verse (rápido) | G – Am – C – Am – Em – D – G – D – Em – Am7 – C – Em – A7 – D | I – ii – IV – ii – vi – V | A7 como dominante secundario (V7/ii). |
| Chorus | G – C – G – D – G – C – G – D – Em – A7 – Em – D7 – G – C – G | I – IV – I – V | La melodía enfatiza F (♭7 de G) sobre C, sonoridad mixolidia. |
| Outro/Coda | C – D7 – G – C – G (repetido, fade) | IV – V7 – I – IV – I | Piano de Paul Griffin variando jazz. |

### 3.4 Diagrama de la progresión

```
[Intro]             → [Verse]                → [Chorus]
I  V  vi7  ii  IV   I  ii  IV  ii  vi  V     I  IV  I  V  I  IV  I  V
vi  V  I                                      vi  V7/ii  vi  V7  I  IV  I
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo | Duración | Acordes clave | Notas |
|---|---------|--------|----------|---------------|-------|
| 1 | Prologue | 0:00 | ~50s | I – V – vi7 – ii – IV | Piano solo, lento. "A long, long time ago..." |
| 2 | Chorus | 0:50 | ~28s | I – IV – I – V | Tempo rápido. "Bye, bye Miss American Pie..." |
| 3 | Verse 1 | — | ~28s | I – ii – IV – ii – vi – V | "Did you write the book of love..." |
| 4 | Chorus | 1:18 | ~28s | | |
| 5 | Verse 2 | 1:46 | ~59s | | Dylan (jester), Elvis (king), Beatles (quartet). |
| 6 | Chorus | 2:45 | ~28s | | |
| 7 | Verse 3 | 3:13 | ~62s | | Manson (helter skelter), Byrds. |
| 8 | Chorus | 4:15 | ~28s | | |
| 9 | Instrumental | 4:43 | ~12s | | |
| 10 | Verse 4 | 4:55 | ~60s | | Altamont, Stones, Satan. |
| 11 | Chorus | 5:55 | ~28s | | |
| 12 | Verse 5 | 6:23 | ~62s | | Vuelve a tempo lento. Janis Joplin. |
| 13 | Verse 6 | 7:25 | ~40s | | "The three men I admire most..." |
| 14 | Outro | 8:05 | ~37s | IV – V7 – I – IV – I fade | Coro final con multi-track. |

### 4.2 Forma general

```
[Prologue] → [C] → [V1] → [C] → [V2] → [C] → [V3] → [C] →
[Instr] → [V4] → [C] → [V5] (lento) → [V6] (lento) → [Outro fade]
```

---

## 5. Letra

```
[Prologue]
A long, long time ago
I can still remember how that music used to make me smile
And I knew if I had my chance
That I could make those people dance
And maybe they'd be happy for a while
But February made me shiver
With every paper I'd deliver
Bad news on the doorstep
I couldn't take one more step
I can't remember if I cried
When I read about his widowed bride
But something touched me deep inside
The day the music died

[Chorus]
So bye, bye, Miss American Pie
Drove my Chevy to the levee but the levee was dry
And them good ole boys were drinking whiskey 'n rye
Singin' this'll be the day that I die
This'll be the day that I die

[Verse 1]
Did you write the book of love
And do you have faith in God above
If the Bible tells you so?
Now do you believe in rock and roll?
Can music save your mortal soul?
And can you teach me how to dance real slow?
Well, I know that you're in love with him
'Cause I saw you dancin' in the gym
You both kicked off your shoes
Man, I dig those rhythm and blues
I was a lonely teenage broncin' buck
With a pink carnation and a pickup truck
But I knew I was out of luck
The day the music died

[Verse 2]
Now for ten years we've been on our own
And moss grows fat on a rollin' stone
But that's not how it used to be
When the jester sang for the king and queen
In a coat he borrowed from James Dean
And a voice that came from you and me
Oh, and while the king was looking down
The jester stole his thorny crown
The courtroom was adjourned
No verdict was returned
And while Lenin read a book on Marx
The quartet practiced in the park
And we sang dirges in the dark
The day the music died

[Verse 3]
Helter skelter in a summer swelter
The birds flew off with a fallout shelter
Eight miles high and falling fast
It landed foul on the grass
The players tried for a forward pass
With the jester on the sidelines in a cast
Now the halftime air was sweet perfume
While the sergeants played a marching tune
We all got up to dance
Oh, but we never got the chance
'Cause the players tried to take the field
The marching band refused to yield
Do you recall what was revealed
The day the music died?

[Verse 4]
Oh, and there we were all in one place
A generation lost in space
With no time left to start again
So come on, Jack be nimble, Jack be quick
Jack Flash sat on a candlestick
'Cause fire is the devil's only friend
Oh, and as I watched him on the stage
My hands were clenched in fists of rage
No angel born in Hell
Could break that Satan's spell
And as the flames climbed high into the night
To light the sacrificial rite
I saw Satan laughing with delight
The day the music died

[Verse 5]
I met a girl who sang the blues
And I asked her for some happy news
But she just smiled and turned away
I went down to the sacred store
Where I'd heard the music years before
But the man there said the music wouldn't play
And in the streets the children screamed
The lovers cried and the poets dreamed
But not a word was spoken
The church bells all were broken

[Verse 6]
And the three men I admire most
The Father, Son and the Holy Ghost
They caught the last train for the coast
The day the music died

[Outro]
And they were singing bye, bye, Miss American Pie
Drove my Chevy to the levee but the levee was dry
And them good ole boys were drinking whiskey 'n rye
Singin' this'll be the day that I die
This'll be the day that I die
```

---

## 6. Esquema de rima

| Sección | Esquema | Notas |
|---------|---------|-------|
| Prologue | AABBCCDDEEFFGG | 14 versos, pareados. |
| Chorus | AABBC | 5 versos. "Pie/dry" (A), "rye" (B extiende A), "die/die" (C). |
| Verses 1-4 | AABBCCDDEEFFGG | 14 versos, pareados con variaciones. |
| Verse 5 | AABBCBDD | 10 versos, tempo lento, esquema más libre. |
| Verse 6 | AABBCC | 6 versos. Triple rima: most/Ghost/coast. |

---

## 7. Análisis lírico

### 7.1 Tema central

Elegía alegórica por la inocencia perdida de Estados Unidos narrada a través del rock and roll. Cada verso representa una etapa del declive: la inocencia de los 50 (Buddy Holly), el despertar político (Dylan, Beatles), la psicodelia y la violencia (Manson, Altamont), y la resignación de los 70.

### 7.2 Referencias clave

| Símbolo | Referencia real |
|---------|----------------|
| "February made me shiver" | Muerte de Buddy Holly (3 feb 1959) |
| "The day the music died" | Accidente aéreo que mató a Holly, Valens, Big Bopper |
| "The jester" | Bob Dylan |
| "The king" | Elvis Presley |
| "The quartet practiced in the park" | The Beatles |
| "Lenin read a book on Marx" | John Lennon (doble sentido con Vladimir Lenin) |
| "Helter skelter" | Charles Manson / The Beatles |
| "The birds flew off" | The Byrds ("Eight Miles High") |
| "The sergeants played a marching tune" | Sgt. Pepper's Lonely Hearts Club Band |
| "Jack Flash sat on a candlestick" | Rolling Stones / JFK |
| "Satan laughing with delight" | Mick Jagger / Altamont |
| "A girl who sang the blues" | Janis Joplin |
| "The three men I admire most" | Buddy Holly, Ritchie Valens, Big Bopper |

### 7.3 Recursos literarios

| Recurso | Ejemplo |
|---------|---------|
| **Alegoría extendida** | La historia del rock = la historia de EE.UU. |
| **Leitmotiv** | "The day the music died" cierra cada verso. |
| **Ironía trágica** | "This'll be the day that I die" invertido de "That'll Be the Day" de Holly. |
| **Metáfora deportiva** | V3 entero: "players", "forward pass", "halftime", "take the field". |
| **Símil religioso** | "The Father, Son and the Holy Ghost" como Buddy, Valens, Bopper. |
| **Contraste temporal** | Prólogo lento → versos rápidos → V5 lento = nostalgia → caos → resignación. |

### 7.4 Contexto de composición

- McLean tenía 13 años y repartía periódicos cuando vio la noticia del accidente.
- "It means I don't ever have to work again if I don't want to" — McLean sobre el significado de la canción.
- Manuscrito original subastado por $1.2 millones (Christie's, 2015).
- McLean deliberadamente deletreó "Lennin" para doble sentido (John Lennon / Vladimir Lenin).
- Documental *The Day the Music Died* (Paramount+, 2022) reveló nuevas interpretaciones.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Intérprete | Notas |
|-------------|------------|-------|
| Voz principal | Don McLean | Tenor folk, narrativa. |
| Guitarra acústica | Don McLean | Martin D-28, rasgueo constante. |
| Guitarra eléctrica | David Spinozza | Fills sutiles. |
| Piano | Paul Griffin + Don McLean | Griffin añadido en último minuto; definió el sonido. |
| Clavinet | Paul Griffin | Coros. |
| Bajo | Bob Rothstein | |
| Batería | Roy Markowitz | |
| Coro final | West 44th St Rhythm & Noise Choir | Supuestamente incluía a Pete Seeger, James Taylor, Carly Simon. |

### 8.2 Mezcla y dinámica

- **Rango dinámico:** Muy amplio — de piano solo susurrado a orquesta completa.
- **Innovación:** La canción comienza en mono y se expande gradualmente a estéreo durante 8:42, simbolizando el paso de la era monoaural a la estéreo.
- **Grabación:** The Record Plant, Nueva York. 26 de mayo de 1971.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (1971) | 8:42, 6 estrofas completas, prólogo lento, outro con coro. |
| Single edit | 4:11 + 4:31. Corta V5 y V6. |
| Madonna (2000) | Dance-pop, 4:33, #1 UK. McLean la elogió. |
| "Weird Al" Yankovic (1999) | "The Saga Begins" — parodia de Star Wars. McLean dio permiso. |
| Home Free (2021) | A cappella country con McLean en voz. |

---

## 10. Fuentes

- **Deezer:** https://www.deezer.com/track/3156285
- **Wikipedia:** https://en.wikipedia.org/wiki/American_Pie_(song)
- **Hooktheory:** https://www.hooktheory.com/theorytab/view/don-mclean/american-pie
- **Documental (2022):** *The Day the Music Died: The Story of Don McLean's American Pie* (Paramount+)

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | Asistente IA |
| **Fecha del análisis** | 2026-06-02 |
| **Tags** | `#DonMcLean` `#AmericanPie` `#FolkRock` `#1971` `#TheDayTheMusicDied` `#BuddyHolly` `#Songcase` |
| **Pendientes** | — |

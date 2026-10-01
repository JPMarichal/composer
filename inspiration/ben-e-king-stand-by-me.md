# Song Case — Stand by Me — Ben E. King

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Deezer), análisis armónico de fuentes web, y análisis lírico-estructural. Archivo indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Stand by Me |
| **Artista** | Ben E. King |
| **Versión analizada** | Original (1961) |
| **Álbum** | *Don't Play That Song!* (1962) |
| **Año** | 1961 |
| **Duración** | 2:57 |
| **ISRC** | USAT21205862 |
| **Género(s)** | Soul, R&B, Doo-wop |
| **Compositor(es)** | Ben E. King, Jerry Leiber, Mike Stoller (seud. Elmo Glick) |
| **Productor(es)** | Jerry Leiber, Mike Stoller |
| **Sello** | Atco (Atlantic) |
| **País** | Estados Unidos |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 119.15 |
| **Gain** | −10.3 dB |
| **Rank** | 921,926 |
| **Explicit** | No |
| **Release Date** | 2016-11-25 (reedición) |
| **ISRC** | USAT21205862 |
| **Deezer ID** | 136710424 |

### 2.2 Análisis local (librosa) — preview 30s

| Feature | Valor |
|---------|-------|
| **BPM (librosa)** | 117.5 |
| **Energy** | 0.9135 |
| **Danceability** | 0.9285 |
| **Valence** | 0.4374 |
| **Spectral Centroid** | 1657.69 Hz |
| **Onset Density** | 3.05 ataques/s |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| A | Major | Alta — unánime en todas las transcripciones. También se toca en G con capo 2. |

### 3.2 Progresión base (los "Stand by Me changes")

```
I    ii    iii   IV    V     vi    vii°
A    Bm    C#m   D     E     F#m   G#°
```

La progresión I–vi–IV–V–I es conocida en teoría musical como **"the Stand by Me changes"**.

### 3.3 Acordes por sección

Toda la canción usa la misma progresión: **A – F#m – D – E – A** (I – vi – IV – V – I).

| Sección | Acordes | Notas |
|---------|---------|-------|
| Intro | A (pedal) | Bajo solo + triángulo + cepillo |
| Versos | A – F#m – D – E – A | Se repite 2× por verso |
| Coros | A – F#m – D – E – A | Misma progresión, énfasis vocal |
| Instrumental | A – F#m – D – E – A (×2) | Solo de cuerdas |
| Outro | A – F#m – D – E – A (fade) | |

**Observación:** No hay cambio armónico entre verso y coro. La diferenciación se logra por instrumentación, intensidad vocal y rango melódico.

### 3.4 La línea de bajo icónica (Lloyd Trotman)

Walking bass en negras que delinea cada acorde:

```
A:    A – E – F# – G#     (raíz, 5ª, 6ª, 7ª M → A)
F#m:  F# – C# – D – E     (raíz, 5ª, 6ª, 7ª m → F#)
D:    D – A – B – C#      (raíz, 5ª, 6ª, 7ª M → D)
E:    E – B – C# – D       (raíz, 5ª, 6ª, 7ª m → E)
```

### 3.5 Diagrama de la progresión

```
[Intro]   → [Verse 1]   → [Chorus 1] → [Verse 2]   → [Chorus 2]
A pedal     I vi IV V I   I vi IV V I  I vi IV V I    I vi IV V I

[Instr]     → [Chorus 3] → [Outro fade]
I vi IV V I   I vi IV V I  I vi IV V I
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo | Duración | Compases | Acordes | Notas |
|---|---------|--------|----------|----------|---------|-------|
| 1 | Intro | 0:00 | ~14s | 4 | A pedal | Bajo + triángulo + cepillo |
| 2 | Verse 1 | 0:14 | ~29s | 8 | I–vi–IV–V–I | Entra voz |
| 3 | Chorus 1 | 0:43 | ~17s | 4 | I–vi–IV–V–I | Entran cuerdas |
| 4 | Verse 2 | 1:00 | ~30s | 8 | I–vi–IV–V–I | |
| 5 | Chorus 2 | 1:30 | ~18s | 4 | I–vi–IV–V–I | "Stand now" |
| 6 | Instrumental | 1:48 | ~32s | 8 | I–vi–IV–V–I (×2) | Solo orquestal |
| 7 | Chorus 3 | 2:20 | ~18s | 4 | I–vi–IV–V–I | |
| 8 | Outro | 2:38 | ~19s | 4+ | I–vi–IV–V–I fade | |

### 4.2 Forma general

```
[Intro] → [V1] → [C1] → [V2] → [C2] → [Instr] → [C3] → [Outro fade]
   4c      8c     4c     8c     4c       8c        4c      4c+
```

---

## 5. Letra

```
[Verse 1]
When the night has come
And the land is dark
And the moon is the only light we'll see
No, I won't be afraid
Oh, I won't be afraid
Just as long as you stand, stand by me

[Chorus 1]
So darlin', darlin', stand by me
Oh, stand by me
Oh, stand
Stand by me, stand by me

[Verse 2]
If the sky that we look upon
Should tumble and fall
Or the mountain should crumble to the sea
I won't cry, I won't cry
No, I won't shed a tear
Just as long as you stand, stand by me

[Chorus 2]
And darlin', darlin', stand by me
Oh, stand by me
Whoa, stand now
Stand by me, stand by me

[Chorus 3]
Darlin', darlin', stand by me
Oh, stand by me
Oh, stand now
Stand by me, stand by me

[Outro]
Whenever you're in trouble, won't you stand by me?
Oh, stand by me
Whoa, just stand now
Oh, stand, stand by me
(fade)
```

---

## 6. Esquema de rima

| Sección | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | ABCBDC | dark/see (asonante), afraid/afraid (repetición), me/me |
| Chorus | AAAB | Repetición de "me" |
| Verse 2 | ABDCEC | fall/sea (consonante), cry/tear (libre), me/me |
| Outro | AAAB | Mismo patrón |

---

## 7. Análisis lírico

### 7.1 Tema central

Amor incondicional y apoyo inquebrantable. El narrador promete que no importa la catástrofe, no sentirá miedo mientras su ser querido esté a su lado.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| **Hipérbole apocalíptica** | "If the sky should tumble and fall" | Catástrofe cósmica para contrastar con la fuerza del vínculo |
| **Anáfora** | "No, I won't be afraid / Oh, I won't be afraid" | Énfasis en la determinación |
| **Antítesis** | Noche/luz, miedo/valentía, caída/permanencia | Caos exterior vs calma interior |
| **Epífora** | "stand by me" al final de estrofas y coros | Refuerzo de la petición central |
| **Apóstrofe** | "So darlin', darlin'" | Dirección directa al amado |

### 7.3 Conexión intertextual

- **Salmo 46:1-3**: "God is our refuge and strength... Therefore we will not fear, though the earth give way and the mountains fall into the heart of the sea."
- **"Stand by Me Father"** (gospel de Sam Cooke): Inspiración directa para King.
- **Himno original de Charles Albert Tindley (1905)**: "Stand by Me" registrado por un ministro de Filadelfia.
- **Película *Stand by Me* (1986)**: Rob Reiner adaptó el cuento de Stephen King "The Body".

### 7.4 Contexto de composición

- King acababa de dejar The Drifters (1960). Llevó un esbozo a Leiber & Stoller basado en el gospel que escuchó de adolescente.
- King cantó a cappella: "When the night has come..." y dijo "That's all I wrote". Leiber respondió: "That's pretty good. You want me to finish it?"
- La canción fue rechazada cuando King aún estaba en The Drifters (manager George Treadwell no la quiso).
- Grabación: 27 oct 1960, Atlantic Studios, NYC. Sesión rápida.
- #4 Billboard Hot 100 (1961), #1 R&B, #1 UK (1962). ~3 millones de copias.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Intérprete | Notas |
|-------------|------------|-------|
| Voz principal | Ben E. King | Tenor con entrega gospel |
| Contrabajo | Lloyd Trotman | La línea de bajo más icónica del soul |
| Guitarra | Al Caiola | Rasgueo en contratiempo |
| Piano | Ernie Hayes | Refuerzo armónico sutil |
| Batería | Gary Chester | Cepillo en tarola |
| Triángulo | Phil Kraus | "Ting" característico del intro |
| Cuerdas | Orquesta (arr. Stanley Applebaum) | Entran en coro 1 |
| Vientos | Romeo Penque | Pequeños fills |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Tenor / barítono ligero |
| Textura | Voz principal doblada sutilmente |
| Entrega | Íntima en versos, expansiva en coros. Melismas gospel ("li-i-ight") |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Amplio — intro mínimo, coros con orquesta completa.
- **Grabación original:** Mono. Reverb de cámara de Atlantic Studios.
- **Producción:** Leiber & Stoller buscaron sonido "seco pero profundo". Tom Dowd (ingeniero) — leyenda de Atlantic.

### 8.4 El ritmo "shave-and-a-haircut"

La percusión inicial imita el ritmo clásico de dos cortas-dos largas. Stoller lo llamó "baion modificado", basado en bossa nova simplificado.

---

## 9. Versiones y diferencias

| Versión | Año | Diferencias clave |
|---------|-----|-------------------|
| Ben E. King original | 1961 | A major, contrabajo acústico, 119 BPM, 2:57 |
| John Lennon | 1975 | Más lento, rock, voz rasposa, #20 US |
| Otis Redding | 1964 | En vivo, más rápido, más groove |
| Mickey Gilley | 1980 | Country, #1 country charts |
| Florence + The Machine | 2015 | Orquestal/etérea, para Final Fantasy XV |
| 4 The Cause | 1998 | Dance-pop, #1 UK |
| Prince Royce | 2010 | Bachata, éxito latino |
| Kingdom Choir | 2018 | Gospel, boda real Harry y Meghan |
| Playing for Change | ~2009 | Global, músicos de todo el mundo |

---

## 10. Impacto cultural

- **BMI Top 100 Songs of 20th Century:** #4 (más de 7 millones de interpretaciones hasta 1999)
- **Rolling Stone 500 Greatest:** #122
- **Library of Congress National Recording Registry:** Inducted 2014
- **>500 versiones documentadas**
- **~1,500 millones de streams en Spotify (2025)**
- **Relanzamiento 1986** tras la película *Stand by Me* de Rob Reiner: #9 Billboard
- **$22.8 millones en regalías** hasta 2012 (6ª canción más lucrativa de su era)

---

## 11. Trivia

- Inspirada en Salmo 46:1-3.
- Escrita justo después de "Spanish Harlem" (con Phil Spector).
- Casi fue de The Drifters — su manager la rechazó.
- Leiber & Stoller usaron el pseudónimo Elmo Glick.
- El bajo lo tocó Lloyd Trotman, no el bajista habitual de la banda.
- Cassius Clay (Muhammad Ali) grabó una versión spoken word en 1963.
- King no era considerado compositor por Leiber, pero insistieron en darle crédito.
- Atlantic dudó en publicarla por sonar "demasiado gospel".

---

## 12. Fuentes

- **Deezer:** https://www.deezer.com/track/136710424
- **Wikipedia:** https://en.wikipedia.org/wiki/Stand_by_Me_(Ben_E._King_song)
- **Ultimate Guitar:** https://tabs.ultimate-guitar.com/tab/ben-e-king/stand-by-me-chords-73005
- **Library of Congress essay:** https://www.loc.gov/static/programs/national-recording-preservation-board/documents/StandByMe.pdf
- **BMI:** http://www.bmi.com/news/entry/232893
- **Songfacts:** https://www.songfacts.com/facts/ben-e-king/stand-by-me

---

## 13. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | Asistente IA |
| **Fecha del análisis** | 2026-06-02 |
| **Tags** | `#BenEKing` `#StandByMe` `#Soul` `#RB` `#1961` `#LeiberStoller` `#I-vi-IV-V-I` `#Songcase` `#Atlantic` `#LloydTrotman` |
| **Pendientes** | Verificar si el bajo fue Lloyd Trotman o Wendell Marshall (algunas fuentes citan a Marshall). |

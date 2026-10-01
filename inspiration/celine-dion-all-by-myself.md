# Song Case — All by Myself — Celine Dion

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | All by Myself |
| **Artista** | Celine Dion |
| **Versión analizada** | Cover (1996) |
| **Álbum** | Falling into You |
| **Año** | 1996 |
| **Duración** | 5:12 |
| **ISRC** | CAC229800162 |
| **Género(s)** | Power ballad, soft rock, adult contemporary |
| **Compositor(es)** | Eric Carmen, Sergei Rachmaninoff (melodía del verso basada en Concierto para Piano n.º 2, Op. 18) |
| **Productor(es)** | David Foster |
| **Sello** | Epic / Columbia |
| **País** | Canadá / EE. UU. |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 119.8 |
| **Gain** | −12.0 dB |
| **Rank** | 777,551 |
| **Explicit** | no |
| **Release Date** | 1996-03-11 |
| **Preview URL** | https://www.deezer.com/track/714269242 |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| Bm | minor | Alta |

### 3.2 Progresión base

```
i   bVII   bVI   V    (Bm   A   G   F#)
```

Armonía altamente cromática con acordes prestados, disminuidos, dominantes secundarios y semi-disminuidos.

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | Bm — A — G — F# | i — bVII — bVI — V | Tema descendente de Rachmaninoff |
| Verse | A — Dm6 — A — Em7 — F — F# — Bm — Dm — A — Dm — E | I — iv6 — I — v7 — bVI — VI — iii — iv — I — iv — V | En área de A mayor (relativo mayor) |
| Pre-Chorus | A — Dm6 — A — Em7 — F — F# — Bm — Dm — A | I — iv6 — I — v7 — bVI — VI — iii — iv — I | "Livin' alone..." |
| Chorus | A — C#m — Em — F — F# — Bm — E | I — iii — v — bVI — VI — iv — VII | Resuelve E7 — A (V7 — I en A) |
| Interludio | Em — D — G — Am — Bsus — B | i — bVII — III — iv — Vsus — V | En 3/4, tema de Rachmaninoff |
| Key Change | Db — Fm — Gb — Bb7 — Ebm — Gb/Ab — Ab | I — iii — IV — bVII — vi — IV/V — V | Modulación a Db mayor |
| Final Chorus | Db — Fm — Abm7/B — Bb7 — Ebm — Gbm7/Ab — Ab | I — iii — v7 — bVII7 — vi — IV/v — V | |

### 3.4 Diagrama de la progresión

```
[Intro]     → [Verse 1]    → [Chorus]    → [Verse 2]
 i bVII bVI V  I iv6 I v7     I iii v bVI   I iv6 I v7
               bVI VI iv VII   VI iv VII
```

---

## 4. Estructura

### 4.1 Forma general

```
[Intro] [V1] [C] [V2] [C] [C var.] [Interludio] [Key Change] [C Final] [Outro]
```

### 4.2 Secciones

| # | Sección | Tiempo | Acordes clave | Notas |
|---|---------|--------|---------------|-------|
| 1 | Intro (instrumental) | 0:00 | Bm — A — G — F# | Piano solo, tema Rachmaninoff |
| 2 | Verse 1 | 0:30 | A — Dm6 — A — Em7 | "When I was young..." |
| 3 | Chorus | 1:00 | A — C#m — Em — F — F# — Bm — E | "All by myself..." |
| 4 | Verse 2 | 1:30 | A — Dm6 — A — Em7 | "Hard to be sure..." |
| 5 | Chorus | 2:00 | A — C#m — Em — F — F# — Bm — E | |
| 6 | Chorus (variación) | 2:30 | misma | "Don't wanna live..." |
| 7 | Interludio instrumental | 3:00 | Em — D — G — Am — Bsus — B | Tema Rachmaninoff en 3/4 |
| 8 | Key Change | 3:30 | Db — Fm — Gb — Bb7 — Ebm | Modulación + F5 |
| 9 | Final Chorus | 3:40 | Db — Fm — Gb — Bb7 — Ebm | |
| 10 | Outro/Coda | 4:00 | — | "I never, never, never needed anyone" |

---

## 5. Letra

```
[Verse 1]
When I was young
I never needed anyone
And making love was just for fun
Those days are gone

[Pre-Chorus]
Livin' alone
I think of all the friends I've known
When I dial the telephone
Nobody's home

[Chorus]
All by myself
Don't wanna be
All by myself
Anymore

[Verse 2]
Hard to be sure
Sometimes I feel so insecure
And loves so distant and obscure
Remains the cure

[Chorus]
All by myself
Don't wanna be
All by myself
Anymore

[Chorus Variation]
All by myself
Don't wanna live
All by myself
Anymore

[Interlude - instrumental]

[Key Change — Chorus]
All by myself
Don't wanna be
All by myself
Anymore

[Outro]
All by myself
Don't wanna live
Oh
Don't wanna live
By myself, by myself
Anymore
By myself
Anymore
Oh
All by myself
Don't wanna live
I never, never, never
Needed anyone
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABB | young/fun — anyone/gone |
| Pre-Chorus | AABB | alone/known — telephone/home |
| Chorus | AAAB | myself/be/myself/anymore |
| Verse 2 | AABB | sure/insecure — obscure/cure |
| Outro | Libre | prosa rítmica |

---

## 7. Análisis lírico

### 7.1 Tema central

La soledad existencial y el anhelo de conexión humana. Arco emocional desde la independencia juvenil ("never needed anyone") hasta el aislamiento adulto ("nobody's home").

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Contraste temporal | "When I was young / Those days are gone" | Pasado de autosuficiencia vs. presente de dependencia |
| Imagen concreta | "When I dial the telephone / Nobody's home" | Metáfora tangible del aislamiento |
| Litotes | "Don't wanna be / All by myself / Anymore" | Negación como afirmación emocional |
| Repetición | "All by myself" (x17 en total) | Obsesión temática, mantra de soledad |
| Regresión al final | "I never, never, never needed anyone" | Vuelta a la actitud juvenil, ciclo sin resolver |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Hipérbaton | "And loves so distant and obscure / Remains the cure" |
| Anáfora | "All by myself" en cascada en el outro |
| Asíndeton | "By myself, by myself / Anymore / By myself / Anymore" |

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Piano (David Foster) | Toda la canción | Base armónica y melódica |
| Cuerdas | Toda | Arreglo orquestal masivo |
| Batería | Coros en adelante | Entra en el primer chorus |
| Bajo | Coros en adelante | |
| Guitarras | Versos y coros | |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Contralto a soprano (F5 en clímax) |
| Textura | Versos íntimos (close miking) → coros expansivos (room ambience) |
| Entrega | Crescendo dramático: susurro → grito desesperado |
| Capas | Una toma principal; armónicas sutiles en el coro final |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Muy amplio — del piano solo al tutti orquestal
- **Key Change:** Subida de un semitono (A → Db) para el clímax final — retenido del original de Carmen
- **Nota F5:** Nota aguda improvisada de ~8 segundos sostenidos antes del key change — David Foster la sorprendió en el estudio
- **Producción general:** Wall of Sound de David Foster — arreglo cinematográfico con crescendos orquestales

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Eric Carmen (1975) | Original; slide guitar, 7:10 de duración, BPM ~128 |
| Celine Dion (1996) | Más lenta (119 BPM), orquestación masiva, F5 añadida, key change mantenido |
| Sola Otra Vez (1996) | Versión en español de Celine, #1 Latin Pop Airplay |

---

## 10. Datos clave

- La melodía del verso está tomada del **Concierto para Piano n.º 2 en Do menor, Op. 18 de Rachmaninoff** (1900-1901), segundo movimiento (Adagio sostenuto)
- La herencia de Rachmaninoff recibe **12% de regalías**
- Carmen también usó el mismo origen para su siguiente sencillo "Never Gonna Fall in Love Again"
- #4 Billboard Hot 100, #1 Adult Contemporary (3 semanas)
- El álbum *Falling into You* ganó el Grammy a Álbum del Año 1997
- La nota F5 no estaba planeada — David Foster la puso como reto durante la grabación

---

## 11. Fuentes

- **Deezer:** https://www.deezer.com/track/714269242
- **Wikipedia:** All by Myself song
- **Songfacts:** All by Myself
- **Genius:** Celine Dion — All by Myself
- **Hooktheory:** All by Myself
- **MusicNotes:** Partitura publicada

---

## 12. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | Claude + exploración web |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | mistral:7b |
| **Tags** | power ballad, adult contemporary, Rachmaninoff, David Foster, key change, F5 |
| **Pendientes** | Verificar progresión exacta del interludio con Hooktheory |

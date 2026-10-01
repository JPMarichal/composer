# Song Case — Mamma Mia — ABBA

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Mamma Mia |
| **Artista** | ABBA |
| **Versión analizada** | Original |
| **Álbum** | ABBA |
| **Año** | 1975 |
| **Duración** | 3:35 |
| **ISRC** | SEAYD7501010 |
| **Género(s)** | Pop, glam pop, europop |
| **Compositor(es)** | Benny Andersson, Björn Ulvaeus, Stig Anderson (título) |
| **Productor(es)** | Benny Andersson, Björn Ulvaeus |
| **Sello** | Polar Music |
| **País** | Suecia |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 137.3 |
| **Gain** | −9.9 dB |
| **Rank** | 839,630 |
| **Explicit** | no |
| **Release Date** | 2008-06-02 |
| **Preview URL** | https://www.deezer.com/track/884030 |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| D | major | Alta |

### 3.2 Acordes por sección

| Sección | Acordes | Función armónica |
|---------|---------|-----------------|
| Intro | D5 — Daug — D5 — Daug (x4) | I — Iaug — I — Iaug |
| Verse (1.ª mitad) | D — D — G(G6) — G(Gmaj7) | I — I — IV(IV6) — IV(IVmaj7) |
| Verse (2.ª mitad) | D — D — Daug — Daug — G — G — A — A — G — D/F# | I — I — Iaug — Iaug — IV — IV — V — V — IV — I(3.ª) |
| Pre-Chorus | A — G — D/F# — A5 (x2) | V — IV — I(3.ª) — V |
| Chorus | D5 — D5(G/D) — G/D — G/D (alterna I con IV pedal) | I — I(IV pedal) — IV — IV |
| Middle 8 | D — A/C# — Bm — A — C/G — G — Em — A | I — V(3.ª) — vi — V — bVII — IV — ii — V |
| Middle 8 (fin) | D — Bm — C/G — G — Em7 — A | I — vi — bVII — IV — ii7 — V |

Nota: El acorde D aumentado (D — F# — A#) crea tensión armónica inmediata — un sello de ABBA.

---

## 4. Estructura

```
[Intro marimba] [V1] [Pre-C] [C] [Middle 8] [V2] [Pre-C] [C] [Middle 8 var.] [C] [Outro]
```

---

## 5. Letra

```
[Verse 1]
I've been cheated by you since I don't know when
So I made up my mind, it must come to an end
Look at me now, will I ever learn?
I don't know how, but I suddenly lose control
There's a fire within my soul

[Pre-Chorus]
Just one look and I can hear a bell ring
One more look and I forget everything, whoa

[Chorus]
Mamma mia, here I go again
My my, how can I resist you?
Mamma mia, does it show again?
My my, just how much I've missed you

[Middle 8]
Yes, I've been broken-hearted
Blue since the day we parted
Why, why did I ever let you go?
Mamma mia, now I really know
My my, I could never let you go

[Verse 2]
I've been angry and sad about things that you do
I can't count all the times that I've told you we're through
And when you go, when you slam the door
I think you know that you won't be away too long
You know that I'm not that strong

[Middle 8 - variation]
Mamma mia, even if I say
Bye-bye, leave me now or never
Mamma mia, it's a game we play
Bye-bye doesn't mean forever
```

---

## 6. Análisis lírico

### 6.1 Tema central

La trampa de una relación intermitente: sabe que debería irse ("I made up my mind, it must come to an end") pero no puede resistir ("how can I resist you?"). La genialidad lírica es el tira y afloja: desafío alternando con vulnerabilidad.

### 6.2 Contexto

- No estaba prevista como sencillo — se lanzó por demanda abrumadora desde Australia
- 10 semanas #1 en Australia (sigue siendo récord para un artista internacional)
- Primer #1 en Reino Unido desde "Waterloo" (1974), rompiendo 18 meses de sequía
- Fue ofrecida a Brotherhood of Man, que la rechazó
- Única actuación de ABBA en vivo en *Top of the Pops* (por regla del sindicato de músicos)
- La marimba fue un añadido de último minuto (Benny la encontró en un rincón del estudio)
- La canción dio nombre al musical *Mamma Mia!* y la franquicia cinematográfica
- Stig Anderson contribuyó el título (exclamación italiana "madre mía")
- El partido danés de extrema derecha intentó usarla en 2010; ABBA demandó y ganó

### 6.3 Producción

- Ostinato de marimba (D5 — Daug) define todo el tema — el sonido más icónico de la canción
- El acorde D aumentado crea tensión inmediata y curiosidad armónica
- Oboe en los versos — toque barroco deliberadamente incongruente
- El coro es la sección más silenciosa — contraste textural intencional tras el poderoso pre-coro
- Arreglo de cuerdas de Sven-Olof Walldoff
- La producción cambia drásticamente entre secciones: intro de marimba → verso completo → pre-coro potente → coro limpio → middle 8 orquestal

---

## 7. Fuentes

- **Deezer:** https://www.deezer.com/track/884030
- **Wikipedia:** Mamma Mia (song)
- **Songfacts:** Mamma Mia
- **Genius:** ABBA — Mamma Mia
- **ABBA Omnibus:** Ficha de grabación
- **SpyTunes:** Análisis armónico detallado

---

## 8. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | Claude + exploración web |
| **Fecha del análisis** | 2026-06-02 |
| **Tags** | ABBA, Mamma Mia, marimba, augmented chord, Australia, Stig Anderson, 1975 |

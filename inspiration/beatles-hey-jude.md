# Song Case — Hey Jude — The Beatles

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Deezer), análisis armónico de fuentes web, y análisis lírico-estructural. Archivo indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Hey Jude |
| **Artista** | The Beatles |
| **Versión analizada** | Original (single, 1968) |
| **Álbum** | Non-album single; compilado en *Hey Jude* (US 1970), *1967–1970* (UK 1973), *Past Masters Vol. 2* (1988), *1* (2000) |
| **Año** | 1968 |
| **Duración** | 7:11 |
| **ISRC** | GBUM71505902 (remaster 2015) |
| **Género(s)** | Rock, Pop rock, Soft rock |
| **Compositor(es)** | Lennon–McCartney (principalmente Paul McCartney) |
| **Productor(es)** | George Martin |
| **Sello** | Apple Records |
| **País** | Reino Unido |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 147.66 |
| **Gain** | −11.2 dB |
| **Rank** | 839,332 |
| **Explicit** | No |
| **Release Date** | 2015-12-24 (remaster) |
| **ISRC** | GBUM71505902 |
| **Preview URL** | https://cdnt-preview.dzcdn.net/... |

Nota: BPM 147.66 corresponde a la remasterización. El tempo original es ~72 BPM (negra en 4/4), ~144 contando corcheas.

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| F | Major | Alta — canción completa en F mayor. No hay modulación, aunque la coda reemplaza V (C) por ♭VII (E♭) para una sonoridad mixolidia. |

### 3.2 Progresión base

```
F     G     Am    Bb    C     Dm    E°
I     ii    iii   IV    V     vi    vii°
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | F – C – B♭ – F | I – V – IV – I | Piano solo, McCartney a capella sobre acordes. |
| Verse | F – C – B♭ – F (×2) | I – V – IV – I | "Hey Jude, don't make it bad..." |
| Bridge | B♭ – F – C7 – F – F7 – B♭ – F – B♭ – F – C7 – F | IV – I – V7 – I – I7 | El F7 aparece en "pain" — séptima de dominante sobre la tónica para tensión armónica. |
| Coda | F – E♭ – B♭ – F (×19) | I – ♭VII – IV – I | Doble cadencia plagal. Ausencia de dominante (C), carácter modal hipnótico. |

### 3.4 Diagrama de la progresión

```
[Intro]         → [Verse 1]     → [Bridge]        → [Coda/Outro]
I  V  IV  I     I  V  IV  I     IV  I  V7  I  I7   I  ♭VII  IV  I
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo | Duración | Acordes clave | Notas |
|---|---------|--------|----------|---------------|-------|
| 1 | Intro | 0:00 | ~26s | F – C – B♭ – F | Piano + voz, sin batería ni bajo. |
| 2 | Verse 1 | 0:26 | ~42s | I – V – IV – I | "Hey Jude, don't make it bad..." |
| 3 | Chorus/Refrán | 1:08 | ~19s | I – V – IV – I | "Na na na..." |
| 4 | Verse 2 | 1:27 | ~47s | I – V – IV – I | Entran guitarra acústica (John) y pandereta (Ringo). |
| 5 | Chorus | 2:14 | ~19s | I – V – IV – I | |
| 6 | Bridge 1 | 2:33 | ~17s | IV – I – V7 – I – I7 | Entra batería. F7 en "pain". |
| 7 | Verse 3 | 2:50 | ~38s | I – V – IV – I | Guitarra eléctrica (George). Mayor densidad. |
| 8 | Chorus | 3:28 | ~10s | I – V – IV – I | |
| 9 | Bridge 2 | 3:38 | ~10s | IV – I – V7 – I | |
| 10 | Coda/Outro | 3:48 | ~3:23 | I – ♭VII – IV – I | ~19 repeticiones, fade out. Orquesta de 36 músicos. |

### 4.2 Forma general

```
[Intro] [V1] [Refr] [V2] [Refr] [Puente1] [V3] [Refr] [Puente2] [Coda/Outro fade]
```

---

## 5. Letra

```
[Intro]
Hey Jude, don't make it bad
Take a sad song and make it better
Remember to let her into your heart
Then you can start to make it better

[Verse 1]
Hey Jude, don't be afraid
You were made to go out and get her
The minute you let her under your skin
Then you begin to make it better

[Bridge 1]
And anytime you feel the pain
Hey Jude, refrain
Don't carry the world upon your shoulders
For well you know that it's a fool
Who plays it cool
By making his world a little colder

[Verse 2]
Hey Jude, don't let me down
You have found her, now go and get her
Remember to let her into your heart
Then you can start to make it better

[Bridge 2]
So let it out and let it in
Hey Jude, begin
You're waiting for someone to perform with
And don't you know that it's just you
Hey Jude, you'll do
The movement you need is on your shoulder

[Outro/Coda]
Na na na na-na-na-na, hey Jude...
(repeated ~19 times with fade)
```

---

## 6. Esquema de rima

| Sección | Esquema | Notas |
|---------|---------|-------|
| Verses | ABCB | better/better riman. bad/heart no. |
| Bridge 1 | AABCCD | pain/refrain (pareado), fool/cool (pareado), shoulders/colder (asonante). |
| Bridge 2 | AABCCD | in/begin, you/do, shoulder (mismo patrón). |
| Coda | — | Sin rima, repetición cíclica con ad-libs. |

---

## 7. Análisis lírico

### 7.1 Tema central

Consuelo y resiliencia ante la adversidad. McCartney escribió la canción para Julian Lennon (5 años) durante el divorcio de John y Cynthia. La canción evoluciona de un consuelo íntimo a una celebración colectiva y catártica.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| **Apostrofe** | "Hey Jude" | Invocación directa al destinatario toda la canción. |
| **Metáfora musical** | "Take a sad song and make it better" | Música como vehículo de sanación. |
| **Antítesis** | "Don't carry the world… / a fool who plays it cool" | Carga vs liberación. |
| **Repetición anafórica** | "Na na na" | Mantra de afirmación colectiva. |
| **Sinécdoque** | "Let her into your heart / under your skin" | La parte por el todo. |
| **Paradoja** | "The movement you need is on your shoulder" | La fuerza está dentro. John la llamó la mejor línea. |

### 7.3 Contexto de composición

- Escrita por McCartney conduciendo a Kenwood para visitar a Julian y Cynthia Lennon en mayo de 1968.
- Título original: "Hey Jules" — cambiado por fonética.
- John siempre sintió que la canción era para él, no para Julian.
- John la llamó "una de las obras maestras de Paul".
- Primera composición de McCartney como lado A sin coautoría sustancial de Lennon.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Intérprete | Sección | Notas |
|-------------|------------|---------|-------|
| Voz principal | Paul McCartney | Toda | |
| Piano | Paul McCartney | Toda | |
| Guitarra acústica | John Lennon | Verse 2+ | |
| Guitarra eléctrica | George Harrison | Verse 3+ | |
| Batería | Ringo Starr | Bridge+ | Entra en el puente. |
| Bajo | Paul McCartney | Bridge+ | |
| Pandereta | Ringo Starr | Verse 2+ | |
| Orquesta (36 músicos) | Sesión | Coda | 10 violines, 3 violas, 3 cellos, 2 contrabajos, 2 flautas, 2 clarinetes, 1 clarinete bajo, 1 fagot, 1 contrafagot, 4 trompetas, 2 cornos, 4 trombones, percusión. |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Tenor (McCartney), rango amplio. |
| Textura | Voz principal + doblaje ocasional + coros de John y George. |
| Entrega | Evoluciona de íntima (intro) a desgarrada (coda, con gritos y ad-libs). |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Extremo — del piano solo susurrado a la orquesta completa a pleno volumen.
- **Efectos destacados:** El famoso grito "Fucking hell!" de John (o Paul según McCartney en *The Lyrics*, 2021) audible en ~2:58.
- **Producción general:** Primera grabación de los Beatles en 8 pistas (Trident Studios). Primera fuera de EMI. George Martin escribió el arreglo orquestal. 35 de 36 músicos de orquesta aplaudieron y cantaron en la coda (pago doble). McCartney subido al piano de cola dirigiendo.
- **Grabación:** 31 jul – 1 ago 1968, Trident Studios, Londres.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (1968) | 7:11, fade out completo. |
| Edición radial | Coda acortada a ~4–5 min (no oficial). |
| *Love* (2006) | Remix de George y Giles Martin para Cirque du Soleil. |
| McCartney en vivo | Sube un semitono (F#) en la coda; divide al público en secciones. |
| Wilson Pickett (1968) | Grabada en FAME Studios, Muscle Shoals. Duane Allman en guitarra (primer solo reconocido). #23 Hot 100, #13 R&B. |
| Elvis Presley (1972) | Memphis Sessions con Chips Moman. |

---

## 10. Fuentes

- **Deezer:** `api.deezer.com/track/116348632`
- **Wikipedia:** https://en.wikipedia.org/wiki/Hey_Jude
- **Análisis Alan Pollack:** https://www.icce.rug.nl/~soundscapes/DATABASES/AWP/hj.shtml
- **Hooktheory:** https://www.hooktheory.com/theorytab/view/the-beatles/hey-jude

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | Asistente IA |
| **Fecha del análisis** | 2026-06-02 |
| **Tags** | `#TheBeatles` `#HeyJude` `#PaulMcCartney` `#1968` `#ClassicRock` `#Songcase` |
| **Pendientes** | — |

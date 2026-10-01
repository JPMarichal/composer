# Song Case — Hey Bulldog — The Beatles

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Hey Bulldog |
| **Artista** | The Beatles |
| **Versión analizada** | Original (álbum *Yellow Submarine*) |
| **Álbum** | *Yellow Submarine* |
| **Año** | 1969 |
| **Duración** | 3:09 |
| **ISRC** | GBAYE0601680 |
| **Género(s)** | Hard rock, Blues rock, Rock psicodélico |
| **Compositor(es)** | Lennon–McCartney (compuesta principalmente por John Lennon) |
| **Productor(es)** | George Martin |
| **Sello** | Apple Records |
| **País** | Reino Unido |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 100.11 |
| **Gain** | −11.4 dB |
| **Rank** | 399,705 |
| **Explicit** | no |
| **Release Date** | 2015-12-24 (remaster) |
| **Deezer ID** | 116348730 |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| C mayor / Mixolidio / C menor | shifting — modal shifting constante | Alta — Pollack y Hooktheory confirman |

La canción cambia de modo repetidamente: las estrofas están en C mayor con inflexión mixolidia (Bb natural), el estribillo cambia a C menor, y la sección de piano riff usa ambas.

### 3.2 Progresión base

```
C:    I     ii    iii   IV    V     vi    vii°
      C     Dm    Em    F     G     Am    B°

Con Bb (♭VII) prestado del modo Mixolidio.
Con Gm (v) prestado del modo menor paralelo.
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Riff intro | C — Gm — C — Gm — Bb — Gm — F — Bb — Gm — C | I — v — I — v — ♭VII — v — IV — ♭VII — v — I | Riff de piano en octavas doblado por guitarra y bajo |
| Verse | C — Gm — C — Gm — Bb — Gm — F — Bb — Gm — C | I — v — I — v — ♭VII — v — IV — ♭VII — v — I | Misma progresión; 8 compases |
| Verse 2 | C — Gm — C — Gm — Bb — Gm — F — Bb — Gm — C | I — v — I — v — ♭VII — v — IV — ♭VII — v — I | |
| Refrain | Am — G — F — C — F — C — D — G | vi — V — IV — I — IV — I — II — V | "You can talk to me" — 5 compases irregulares |
| Solo verse | C — Gm — C — Gm — Bb — Gm — F — Bb — Gm — C | I — v — I — v — ♭VII — v — IV — ♭VII — v — I | Solo de guitarra de George Harrison sobre la progresión base |
| Outro | C — Gm — alternando + spoken word | I — v | 25 compases de jam con ladridos y diálogo |

### 3.4 Diagrama de la progresión

```
[Riff intro] → [Verse 1]  → [Verse 2]  → [Refrain] → [Riff]
 I  v  I  v    I  v  I  v  I  v  I  v   vi  V  IV   I  v
 ♭VII  v  IV   ♭VII  v  I  ♭VII  v  I  I  IV  I  ...
 ♭VII  v  I

[Guitar solo] → [Verse 3] → [Refrain] → [Outro / Jam]
 I  v  ...        I  v  ...   vi  V ...   I  v (cíclico con spoken word)
```

### 3.5 Notas armónicas destacadas

- **Gm menor (v) en lugar de G mayor (V)**: en el modo Mayor esperarías G (V) — pero Lennon usa Gm (v) prestado del C menor paralelo. Esto debilita la sensación de tónica y es la marca armónica más característica de la canción.
- **Bb (♭VII) mixolidio**: el acorde de Si bemol mayor (♭VII) viene del modo Mixolidio de C. Crea una sensación de ambigüedad modal — ¿estamos en C mayor, C mixolidio o C menor?
- **Ausencia de dominante G**: la canción evita sistemáticamente el G mayor (V natural), usando Gm en su lugar. La única aparición de G mayor es en el estribillo ("you can talk to me") como V de C después de D → G (II → V).
- **Estribillo irregular**: dura 5 compases en lugar de 8 — el fraseo impar desorienta al oyente.
- **Blues y gospel**: a pesar de la complejidad modal, la canción tiene un feeling bluesero constante gracias al riff de piano y la entrega vocal.

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo | Compases | Notas |
|---|---------|--------|----------|-------|
| 1 | Riff intro | 0:00–0:14 | 6 | Piano solo en octavas → entra guitarra → entra banda completa |
| 2 | Verse 1 | 0:14–0:35 | 8 | "Sheepdog standing in the rain" |
| 3 | Verse 2 | 0:35–0:56 | 8 | "Big man walking in the park" |
| 4 | Refrain | 0:56–1:14 | 5 (irregular) | "You can talk to me" |
| 5 | Riff (transición) | 1:14–1:22 | 4 | Guitarra distorsionada |
| 6 | Solo verse | 1:22–1:44 | 8 | Solo de George Harrison |
| 7 | Verse 3 | 1:44–2:05 | 8 | "Some kind of solitude" |
| 8 | Refrain | 2:05–2:23 | 5 | |
| 9 | Outro / Jam | 2:23–3:09 | 29 | Ladridos, "Hey bulldog", spoken word, fade |

### 4.2 Forma general

```
[Riff(6)] [V1(8)] [V2(8)] [Ref(5)] [Riff(4)] [Solo(8)] [V3(8)] [Ref(5)] [Outro(29)]
```

---

## 5. Letra

```
[Riff instrumental]

[Verse 1]
Sheepdog, standing in the rain
Bullfrog, doing it again
Some kind of happiness is measured out in miles
What makes you think you're something special when you smile?

[Verse 2]
Childlike, no one understands
Jackknife in your sweaty hands
Some kind of innocence is measured out in years
You don't know what it's like to listen to your fears

[Refrain]
You can talk to me
You can talk to me
You can talk to me
If you're lonely, you can talk to me

[Riff instrumental]

[Guitar Solo]

[Verse 3]
Big man, walking in the park
Wigwam, frightened of the dark
Some kind of solitude is measured out in you
You think you know me but you haven't got a clue

[Refrain]
You can talk to me
You can talk to me
You can talk to me
If you're lonely, you can talk to me

[Outro — spoken word / ad-lib]
Hey bulldog!
Hey bulldog!
(Barking sounds, laughter)
"What'd you say?" "I said 'roof'!"
"Aw, you got it, that's it, man"
"Hey, don't look at me, I only have ten children"
(Laughter, barking)
Hey bulldog...
(fade)
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABB | rain/again; miles/smile |
| Verse 2 | AABB | understands/hands; years/fears |
| Verse 3 | AABB | park/dark; you/clue |
| Refrain | AAAA | me × 4 / me × 4 |

---

## 7. Análisis lírico

### 7.1 Tema central

John Lennon dijo que la letra "no significa nada" — era un ejercicio de escritura surrealista. Sin embargo, emergen temas de incomunicación ("you think you know me but you haven't got a clue") y soledad ("if you're lonely, you can talk to me") que atraviesan su obra posterior.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Imagen surrealista | "Sheepdog standing in the rain / Bullfrog doing it again" | Animales en situaciones absurdas |
| Antítesis | "Big man walking in the park / Wigwam frightened of the dark" | Poder y vulnerabilidad |
| Paradoja | "Some kind of happiness is measured out in miles" | La felicidad como distancia |
| Ironía | "You think you know me but you haven't got a clue" | Autoconciencia del artista incomprendido |

### 7.3 Contexto de composición

Grabada el 11 de febrero de 1968 en Abbey Road — una de las últimas sesiones en las que los cuatro Beatles trabajaron juntos como banda. Originalmente se llamaba "Hey Bullfrog". Paul McCartney, al oír el riff de piano de John, empezó a ladrar; John se rió, dejaron los ladridos, y cambiaron el título.

Geoff Emerick (ingeniero) la citó como uno de los últimos esfuerzos grupales genuinos de la banda — antes de que las tensiones de la India y la llegada de Yoko Ono fracturaran la dinámica.

La canción fue un "relleno" contractual para *Yellow Submarine* — United Artists pidió cuatro canciones nuevas y la banda las grabó rápido.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Notas |
|-------------|-------|
| Piano (Lennon) | Riff en octavas — base de toda la canción |
| Guitarra líder (Harrison) | Distorsión pesada; solo gemelo con bends blueseros |
| Bajo (McCartney) | Línea melódica que duplica el riff de piano — fuzz bass |
| Batería (Starr) | Ritmo recto 4/4 con fills característicos en los compases 2 y 4 del verso |
| Tamboril (McCartney) | En el riff intro |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Lennon: barítono rasgado; McCartney: armonías agudas |
| Textura | Voz doblada (Lennon) con armonías de McCartney |
| Entrega | Agresiva, casi burlona — "sneering" (David Grohl) |
| Capas | La sección hablada del outro es un precursor del rap |

### 8.3 Mezcla

- Guitarra de Harrison con distorsión saturada y alta en la mezcla.
- Efecto de spoken word en el outro: Emerick bajó los faders para destacar el diálogo.
- Producción de George Martin: equilibrada pero con la crudeza necesaria.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (1969) | Mono / estéreo; la mezcla estéreo de 2009 revela mejor el diálogo del outro |
| *Love* (2006) | Mezcla con "Lady Madonna" — transición entre ambas |
| Dave Matthews Band | Versión en vivo con improvisación extendida |
| Jeff Lynne & Dave Grohl (2014) | Tributo Grammy 50 aniversario Ed Sullivan — Grohl: "the quintessential Beatles rocker" |

---

## 10. Datos curiosos

1. **Título original "Hey Bullfrog"**: cambiado por los ladridos de Paul durante la grabación.
2. **Última sesión de grupo genuina**: Emerick la considera el último momento Beatle.
3. **Doblaje de Yellow Submarine**: la escena fue animada después de la canción — los Beatles grabaron un video promocional en el estudio.
4. **Relleno contractual**: una de las 4 canciones nuevas exigidas por United Artists para la película.
5. **Presunto sitar**: Lennon intentó tocar un sitar como un banjolele al estilo George Formby — no funcionó.
6. **"I have ten children"**: Paul dice esta frase en el outro. Nunca se ha explicado.
7. **Precursora del rap**: la sección hablada del outro es citada como ejemplo temprano de rap en el rock.

---

## 11. Fuentes

- **Deezer:** `https://www.deezer.com/track/116348730`
- **Wikipedia:** `https://en.wikipedia.org/wiki/Hey_Bulldog_(The_Beatles_song)`
- **The Beatles Bible:** `https://www.beatlesbible.com/songs/hey-bulldog/`
- **Alan W. Pollack (análisis armónico):** `https://www.icce.rug.nl/~soundscapes/DATABASES/AWP/hb.shtml`
- **Hooktheory:** `https://www.hooktheory.com/theorytab/view/the-beatles/hey-bulldog`
- **Songfacts:** `https://www.songfacts.com/facts/the-beatles/hey-bulldog`
- **Beatlesebooks (historia):** `http://www.beatlesebooks.com/hey-bulldog`

---

## 12. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (deepseek-v4-flash-free) |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | Sondeo web + Wikipedia + Pollack + Hooktheory + teoría musical |
| **Tags** | `beatles`, `hey-bulldog`, `1968`, `yellow-submarine`, `lennon`, `hard-rock`, `c-major`, `modal-shifting`, `blues-rock`, `riff-based`, `surrealismo`, `dog-barks` |
| **Pendientes** | Verificar la duración exacta de cada sección |


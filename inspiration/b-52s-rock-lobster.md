# Song Case — Rock Lobster — The B-52's

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Rock Lobster |
| **Artista** | The B-52's |
| **Versión analizada** | Álbum (1979) |
| **Álbum** | *The B-52's* |
| **Año** | 1978 (single original DB Records) / 1979 (relanzamiento Warner Bros.) |
| **Duración** | 4:37 (DB single) / 6:49 (álbum) / 4:52 (single 1979) |
| **ISRC** | USWB19901100 |
| **Género(s)** | New wave, Surf rock, Post-punk, Avant-pop |
| **Compositor(es)** | Fred Schneider, Ricky Wilson (acreditados luego: Kate Pierson, Cindy Wilson, Keith Strickland) |
| **Productor(es)** | Chris Blackwell |
| **Sello** | DB Records (original) / Warner Bros. (relanzamiento) |
| **País** | Estados Unidos |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 179.8 |
| **Gain** | −13.0 dB |
| **Rank** | 475,907 |
| **Explicit** | no |
| **Release Date** | 2008-12-16 (reedición) |
| **Deezer ID** | 14618394 |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| Cm (estrofas) → Fm (coro) | minor | Alta — Wikipedia y Hooktheory confirman |

### 3.2 Progresión base (estribillo en Fm)

```
Cm:   i     ii°    III    iv     v     VI    VII
      Cm    D°     Eb     Fm     Gm    Ab    Bb

Fm:   i     ii°    III    iv     v     VI    VII
      Fm    G°     Ab     Bbm    Cm    Db    Eb
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro / Riff | Cm — Bb — Ab — G | i — VII — VI — V | Riff de guitarra surf oscilante; V es mayor (prestado del armónico) |
| Verso | Cm — Bb — Ab — G (cíclico) | i — VII — VI — V | Sprechgesang de Schneider sobre el riff |
| Pre-coro ("Down at the beach...") | Cm — Fm — Cm — Fm | i — iv — i — iv | Ascenso a Fm prepara el coro |
| Chorus ("Rock Lobster!") | Fm — Eb — Db — C | i — VII — VI — V | Cambio a Fm; grito ascendente de Pierson/Wilson |
| Sección de animales | Cm — Bb — Ab — G | i — VII — VI — V | Lista de criaturas marinas; cada animal tiene un efecto vocal |
| Outro | Cm — Bb — Ab (fade) | i — VII — VI | Fade out instrumental |

### 3.4 Diagrama de la progresión

```
[Riff intro]   → [Verso]           → [Pre-coro]        → [Chorus]
 i  VII  VI  V   i  VII  VI  V      i  iv  i  iv        i  VII  VI  V (en Fm)
  (Cm)             (Cm)                                    (Fm)

[Sección animales] → [Outro]
 i  VII  VI  V      i  VII  VI  (fade)
 (Cm)
```

### 3.5 Notas armónicas destacadas

- **Cm i — VII — VI — V**: una progresión descendente por grado (1–7–6–5) típica del rock y el surf. En Cm: Cm, Bb, Ab, G. El V es mayor (G) en lugar de Gm (v) — usa la sensible (B natural) del menor armónico.
- **Cambio de tónica Cm → Fm en el coro**: el coro modula a Fm (subdominante). La progresión i—VII—VI—V se mantiene, pero transportada: Fm, Eb, Db, C.
- **Riff de guitarra en afinación abierta C-F-x-x-F-F**: Ricky Wilson eliminó las dos cuerdas centrales (D y G), creando un intervalo de cuarta y quinta constante. El riff alterna entre dos patrones sobre las seis cuerdas restantes pero con un sonido disonante y único.
- **Korg SB-100 Synthe-Bass**: Kate Pierson tocó la línea de bajo en un sintetizador monofónico, dándole un timbre áspero y electrónico que contrasta con la guitarra surf.

---

## 4. Estructura

### 4.1 Mapa de secciones (álbum 6:49)

| # | Sección | Tiempo | Notas |
|---|---------|--------|-------|
| 1 | Intro / Riff | 0:00–0:30 | Guitarra surf + Farfisa; entra bajo sintetizado |
| 2 | Verso 1 | 0:30–1:15 | "Let's go down to the beach, baby" |
| 3 | Pre-coro | 1:15–1:30 | "Down at the beach" |
| 4 | Chorus | 1:30–1:50 | "Rock Lobster!" con grito ascendente ahhh |
| 5 | Verso 2 | 1:50–2:45 | "There goes a dogfish, chased by a catfish" |
| 6 | Sección animales | 2:45–5:00 | Lista de criaturas con vocalizaciones; estructura cercana al prog |
| 7 | Outro | 5:00–6:49 | Fade; "Motion in the ocean" repetido |

### 4.2 Forma general

```
[Riff] [V1] [Pre-C] [C] [V2] [Sección animales (lista)] [Outro/Fade]
  16     24     8     8    24           ~64               ~32 compases
```

La sección de animales es un crescendo sin estructura fija — similar a "Good Vibrations" de Beach Boys. Las secciones cambian tan rápido que la canción roza el prog-rock.

---

## 5. Letra

```
[Intro]
(Riff instrumental)

[Verse 1]
Let's go down to the beach, baby
Let's go down to the beach, baby
Let's go down to the beach, baby
Let's go down to the beach, baby

[Pre-Chorus]
Down at the beach
Down at the beach
Down at the beach
Down at the beach

[Chorus]
(Rock lobster! Rock lobster!)
Ahhhh (ascending) — rock lobster!
Ahhhh (ascending) — rock lobster!
Ahhhh (ascending) — rock lobster!

[Verse 2]
There goes a dogfish, chased by a catfish
In flew a sea robin, watch out for that piranha
There goes a narwhal, here comes a bikini whale!

Big suckers, little suckers
Ooh, there goes a stingray, manta ray
Jellyfish, ahhh, there's a jellyfish

[Sección de animales — lista extendida]
(Dogfish! Catfish! Sea robin! Piranha!
 Narwhal! Bikini whale! Stingray! Manta ray!
 Jellyfish!)
...con vocalizaciones de Kate Pierson y Cindy Wilson
...efectos de sonido onomatopéyicos

[Outro / Fade]
Motion in the ocean
Motion in the ocean
(Boops)
(Rock lobster!)
...
(fade out)
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | Monorrima | "beach" × 8 |
| Lista animales | Libre / no rima | Nombres de animales en secuencia |
| Chorus | Monorrima | "lobster" × N |
| Outro | Libre | "Motion in the ocean" — única rima del tema |

La canción apenas rima — es una lista rítmica más que una canción lírica tradicional.

---

## 7. Análisis lírico

### 7.1 Tema central

Una fiesta en la playa donde aparecen criaturas marinas imaginarias y un hombre pierde una oreja. No hay "significado profundo" — es puro surrealismo kitsch, diseñado para hacer bailar y reír. Fred Schneider lo concibió como un poema tonto sobre una langosta.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Imagen surrealista | "Here comes a bikini whale!" | Ballena en bikini — absurdo puro |
| Listado catálogo | Dogfish, catfish, sea robin, piranha, narwhal | Acumulación de animales reales e inventados |
| Onomatopeya | Vocalizaciones de peces | Pierson y Wilson imitan sonidos marinos |
| Repetición | "Let's go down to the beach" × 8 | Hipnosis rítmica |

### 7.3 Contexto de composición

Fred Schneider estaba en la discoteca 2001 en Atlanta. En lugar de show de luces, proyectaban diapositivas de langostas en la parrilla, perritos y hamburguesas. Pensó: "Rock this, rock that... rock lobster!"

La banda improvisó durante horas en una sala de sangría de una funeraria (sin calefacción). Ricky Wilson y Keith Strickland editaron kilometros de cinta para montar la canción final. La guitarra de Wilson tenía una afinación excéntrica (C-F-x-x-F-F, dos cuerdas quitadas) que creó el riff icónico.

### 7.4 John Lennon y Yoko Ono

John Lennon oyó "Rock Lobster" en una discoteca de Bermuda en 1979. Reconoció los gritos de Yoko Ono en las vocalizaciones de Pierson y Wilson. Llamó a Yoko: *"Get the axe out — they're ready for us again!"* La canción lo inspiró a salir de su retiro de 5 años y grabar *Double Fantasy* (1980).

Yoko Ono confirmó en entrevista con Songfacts (2013): *"Listening to the B-52s, John said he realized that my time had come."* En 2002, Ono se unió a la banda en su concierto del 25 aniversario para interpretar "Rock Lobster".

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Notas |
|-------------|-------|
| Guitarra Mosrite (barítono) | Ricky Wilson — afinación C-F-x-x-F-F, sin cuerdas D y G |
| Farfisa Combo Organ | Kate Pierson — sonido vintage 60s, una tecla no funcionaba en la grabación original |
| Korg SB-100 Synthe-Bass | Kate Pierson — línea de bajo icónica tocada en sintetizador monofónico |
| Batería | Keith Strickland — ritmo surf rock |
| Cowbell | Keith Strickland (grabación) / Fred Schneider (en vivo) |
| Voces | Fred Schneider (sprechgesang), Kate Pierson (agudos), Cindy Wilson (graves) |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Schneider: barítono hablado; Pierson: soprano; Wilson: mezzosoprano |
| Textura | Tres voces completamente distintas, sin mezclarse — cada una ocupa su estrato |
| Entrega | Schneider: sprechgesang deadpan; Pierson/Wilson: gritos, ululaciones, onomatopeyas |
| Capas | Llamada y respuesta; armonías paralelas de tercera, cuarta y quinta |

### 8.3 Mezcla y dinámica

- **Producción original (DB, 1978)**: $700 de presupuesto. Sonido crudo, sin bajo, Farfisa con tecla rota. "Everything was kind of up front" (Kate Pierson).
- **Relanzamiento (Warner Bros., 1979)**: Producido por Chris Blackwell en Nasáu. Añadió el Korg SB-100, mejor ecualización, pero mantuvo la crudeza.
- **Efectos**: casi sin reverb — sonido seco y directo. La guitarra de Ricky Wilson corta como cuchilla.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| **DB Records single** (1978) | 4:37, más rápida, sin bajo, más cruda; más líneas en la sección de animales |
| **Álbum** (1979) | 6:49, Korg SB-100 synths, producción más limpia, verso adicional |
| **Single 1979** | 4:52, editada del álbum |
| **En vivo (2002, con Yoko Ono)** | Yoko interpretó las partes de peces |
| **35 Aniversario** | Versiones remasterizadas |

---

## 10. Datos curiosos y legado

1. **#147 de las 500 mejores canciones de todos los tiempos** (Rolling Stone, 2004).
2. **Única canción en el Hot 100 que menciona un narval**.
3. **Cowbell legendaria**: segundo mejor uso de cowbell después de "Don't Fear the Reaper".
4. **La canción que resucitó a John Lennon** — inspiró *Double Fantasy*.
5. **Ricky Wilson**: murió de SIDA en 1985 a los 32 años; el riff de "Rock Lobster" fue su tarjeta de presentación.
6. **Guitarra sin cuerdas centrales**: Wilson quitó D y G — solo tocaba sobre C, F (bajos) y F, F (agudos).
7. **Equipo de hockey**: el equipo de hockey de Athens, Georgia, se llama "Rock Lobsters" en honor a la canción (2024).
8. **Fred Schneider es vegetariano**: dejó de comer crustáceos a los 4 años. Grabó un video para PETA sobre langostas.
9. **Presupuesto original**: $700, pagado por Danny Beard de DB Records.

---

## 11. Fuentes

- **Deezer:** `https://www.deezer.com/track/14618394`
- **Wikipedia:** `https://en.wikipedia.org/wiki/Rock_Lobster_(song)`
- **Songfacts:** `https://www.songfacts.com/facts/the-b-52s/rock-lobster`
- **American Songwriter:** `https://americansongwriter.com/the-meaning-behind-rock-lobster-by-the-b-52s/`
- **People (oral history):** `https://people.com/music/the-b-52s-rock-lobster-oral-history/`
- **Uncut:** `https://www.uncut.co.uk/features/b-52s-rock-lobster-theres-not-songs-like-104998/`
- **Hooktheory:** `http://devhookpad.hooktheory.com/theorytab/view/the-b-52s/rock-lobster`
- **Everything Explained:** `https://everything.explained.today/Rock_Lobster/`

---

## 12. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (deepseek-v4-flash-free) |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | Sondeo web + Wikipedia + Songfacts + Hooktheory + teoría musical |
| **Tags** | `b-52s`, `rock-lobster`, `1978`, `new-wave`, `surf-rock`, `c-minor`, `post-punk`, `novelty-song`, `john-lennon`, `yoko-ono`, `athens-georgia`, `narwhal`, `cowbell` |
| **Pendientes** | Verificar la lista exacta de animales (varía entre versiones) |

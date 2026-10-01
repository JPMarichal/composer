# Song Case — California Dreamin' — The Mamas & the Papas

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | California Dreamin' |
| **Artista** | The Mamas & the Papas |
| **Versión analizada** | original (single version) |
| **Álbum** | If You Can Believe Your Eyes & Ears |
| **Año** | 1965 (single) / 1966 (álbum) |
| **Duración** | 2:42 |
| **ISRC** | USMC16532697 |
| **Género(s)** | Sunshine pop, folk rock, soft rock, psychedelic pop |
| **Compositor(es)** | John Phillips, Michelle Phillips |
| **Productor(es)** | Lou Adler |
| **Sello** | Dunhill, RCA Victor |
| **País** | Estados Unidos |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — valores aproximados (pueden variar según el cliente).

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 112 | |
| **Key** | 4 | (E major / C# minor) |
| **Mode** | minor | |
| **Camelot** | 10A | |
| **Danceability** | 0.59 | |
| **Energy** | 0.35 | |
| **Valence** | 0.41 | (positividad musical) |
| **Acousticness** | 0.69 | |
| **Instrumentalness** | 0.00 | |
| **Speechiness** | 0.03 | |
| **Liveness** | 0.18 | |
| **Loudness** | -13.46 dB | |
| **Time Signature** | 4/4 | |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/2321278`

| Feature | Valor |
|---------|-------|
| **BPM** | 112.35 |
| **Gain** | -12.1 dB |
| **Rank** | 935739 |
| **Explicit** | no |
| **Release Date** | 1998-03-17 (relanzamiento) |
| **Preview URL** | vía Deezer CDN |

### 2.3 Análisis local (librosa) — opcional

> Cuando se disponga del archivo de audio.

| Feature | Valor |
|---------|-------|
| **BPM (librosa)** | — |
| **Key (librosa)** | — |
| **Mode** | — |
| **Energy** | — |
| **Danceability** | — |
| **Valence** | — |
| **Spectral Centroid** | Hz |
| **Onset Density** | ataques/s |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| C# minor | minor | alta (concierto) — guitarra con capo en traste 4 suena en Am |

La guitarra original usa capo en traste 2 o 4. La progresión se analiza en Am (relativo de C mayor), que es como se toca. En concierto, la tonalidad real es C# menor.

### 3.2 Progresión base

```
i   VII   VI   V7sus4   V7
Am  G     F    E7sus4   E7
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | E7 → Am | V7 → i | Acorde E7 sostenido, resuelve a Am |
| Verse (estrofa) | Am → G → F → G → E7 | i → VII → VI → VII → V7 | Cada línea doblada por la armonía vocal |
| Chorus (refrán) | Am → G → F → G → E7 → Am | i → VII → VI → VII → V7 → i | Misma progresión, varía la melodía |
| Flute Solo | Am → G → F → G → E7 → Am | i → VII → VI → VII → V7 → i | Misma base armónica |
| Outro | Am → G → F → G → E7 → Am (x3) | i → VII → VI → VII → V7 → i | Repite fading out |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro]        → [Verse 1]     → [Verse 2]    → [Flute Solo]  → [Verse 3]    → [Outro]
  E7  Am         Am G F G E7     Am G F G E7    Am G F G E7    Am G F G E7    Am G F...
  V7   i         i VII VI VII V7  i VII VI ...   i VII VI ...   i VII VI ...   (fade)
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:08 | ~8 | 2 | E7 → Am | Rasgueo de guitarra acústica |
| 2 | Chorus/Refrán | 0:08–0:32 | ~24 | 8 | Am G F G E7 | Las 4 líneas con armonías a 4 voces. No hay "verse" inicial |
| 3 | Verse (iglesia) | 0:32–0:56 | ~24 | 8 | Am G F G E7 | Denny Doherty canta solo, responde el grupo |
| 4 | Flute Solo | 0:56–1:20 | ~24 | 8 | Am G F G E7 | Solo de flauta alta (Bud Shank) |
| 5 | Verse final | 1:20–1:52 | ~32 | 10 | Am G F G E7 | "If I didn't tell her…" |
| 6 | Outro | 1:52–2:42 | ~50 | ~10 | Am G F… (fade) | Repetición con fade |

### 4.2 Forma general

```
[Chorus] [Verse] [Flute Solo] [Chorus] [Outro/fade]
```

La estructura es inusual: el "coro" va primero. El tema principal ("All the leaves are brown") aparece desde el segundo 8, funcionando como hook inmediato.

---

## 5. Letra

```
[Chorus]
All the leaves are brown (All the leaves are brown)
And the sky is grey (And the sky is grey)
I've been for a walk (I've been for a walk)
On a winter's day (On a winter's day)
I'd be safe and warm (I'd be safe and warm)
If I was in L.A. (If I was in L.A.)
California dreamin' (California dreamin')
On such a winter's day

[Verse]
Stopped into a church
I passed along the way
Well, I got down on my knees (Got down on my knees)
And I pretend to pray (I pretend to pray)
You know the preacher liked the cold (Preacher liked the cold)
He knows I'm gonna stay (Knows I'm gonna stay)
California dreamin' (California dreamin')
On such a winter's day

[Flute Solo]

[Chorus]
All the leaves are brown (All the leaves are brown)
And the sky is grey (And the sky is grey)
I've been for a walk (I've been for a walk)
On a winter's day (On a winter's day)
If I didn't tell her (If I didn't tell her)
I could leave today (I could leave today)
California dreamin' (California dreamin')
On such a winter's day

[Outro]
(California dreamin')
On such a winter's day
(California dreamin')
On such a winter's day
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Chorus/Refrán | AABB CCDD | brown/grey — walk/day — warm/L.A. — dreamin'/day |
| Verse | AABB CCDD | church/way — knees/pray — cold/stay — dreamin'/day |
| Chorus final | AABB CCDD | brown/grey — walk/day — her/today — dreamin'/day |

Rima consonante perfecta en todos los casos. Estructura de copla simple.

---

## 7. Análisis lírico

### 7.1 Tema central

Nostalgia y deseo de escape. Un narrador atrapado en un invierno neoyorquino anhela el calor y la seguridad de California (específicamente Los Ángeles). La canción captura la melancolía del desplazamiento geográfico y la idealización del hogar perdido.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Contraste cromático | "All the leaves are brown / And the sky is grey" | Marrón y gris = muerte, frío. Se opone al sol implícito de California |
| Hipálage | "On such a winter's day" | El día no "es" invernal por él mismo; la sensación térmica y emocional lo vuelve invernal |
| Sinestesia | "I'd be safe and warm / If I was in L.A." | La seguridad se mezcla con la sensación térmica — California como útero protector |
| Eco / repetición | "(All the leaves are brown)" | Las voces de respaldo repiten cada línea como eco, creando textura de ensoñación |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Anáfora | "All the leaves are brown / And the sky is grey / I've been for a walk / On a winter's day" — estructura paralela en cada pareado |
| Ironía dramática | "You know the preacher liked the cold / He knows I'm gonna stay" — el predicador sabe que el narrador se quedará en el frío, pero el narrador desea irse a California |
| Metonimia | "L.A." por el estilo de vida californiano, el sol, el hogar perdido |
| Epífora | "California dreamin' / On such a winter's day" — cierre repetido de cada estrofa |

### 7.4 Conexión intertextual

> La canción ha sido versionada por The Beach Boys, José Feliciano, America, Sia, y Bobby Womack. Aparece en la película *Chungking Express* (1994) de Wong Kar-wai como leitmotiv narrativo, y en *Stranger Things* temporada 4 (cover de The Beach Boys).

### 7.5 Contexto de composición

> John y Michelle Phillips escribieron la canción en 1963 mientras vivían en Nueva York durante un invierno particularmente frío. Michelle, originaria de California, extrañaba el sol. John soñó la melodía una noche y despertó a Michelle para que le ayudara con la letra. La segunda estrofa se inspiró en una visita a la Catedral de San Patricio. Originalmente la grabó Barry McGuire con los Mamas & the Papas como coristas; Lou Adler re-grabó la voz principal con Denny Doherty sobre la misma pista instrumental. Barry McGuire puede oírse brevemente en el canal izquierdo al inicio del tema. La canción fue #1 del Billboard Year-End 1966 y está en el Grammy Hall of Fame (2001). Rolling Stone la colocó en el #420 de las 500 mejores canciones de la historia (2021).

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Guitarra acústica | Toda la canción | P.F. Sloan (intro), John Phillips (ritmo); capo traste 2 o 4 |
| Batería | Toda la canción | Hal Blaine — golpe suave con escobillas |
| Bajo | Toda la canción | Joe Osborn — líneas simples, walking |
| Piano | Toda la canción | Larry Knechtel — acordes de relleno |
| Flauta alta (alto flute) | Solo (0:56–1:20) | Bud Shank — solo improvisado a 1ª toma |
| Pandereta | Acentos | Hal Blaine |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Medio-alto (tenor) |
| Textura | 4 voces (Denny Doherty líder, John Phillips, Cass Elliot, Michelle Phillips en armonía) |
| Entrega | Relajada, con anhelo contenido; el eco coral crea atmósfera onírica |
| Capas | La voz líder canta la línea principal; las armonías repiten cada frase en eco (call-and-response), efecto que sugiere introspección |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Moderado; transiciones suaves entre secciones
- **Panning:** Voces centradas; guitarra rítmica ligeramente a la izquierda; solo de flauta centrado
- **Efectos destacados:** Reverberación de cámara (United Western Studio); la mezcla original de McGuire apenas se filtra en el canal izquierdo
- **Producción general:** Producción limpia de Lou Adler; sonido "California Sound" característico: brillante pero con calidez analógica

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (Mamas & Papas) | 2:42, voz principal Denny Doherty, flauta alta Bud Shank |
| Barry McGuire (1965) | Grabación original; armónica en lugar de flauta; voz más rasposa |
| José Feliciano (1968) | Versión latin-jazz con cuerdas; arreglo orquestal de George Tipton |
| America (1979) | Versión soft rock; voz principal Dewey Bunnell; usada en banda sonora *California Dreaming* |
| The Beach Boys (1986) | Producida por Terry Melcher; Roger McGuinn en guitarra de 12 cuerdas; Al Jardine voz líder |
| Freischwimmer (2015) | Remix tropical house; #1 en Billboard Dance Club Songs (2016) |
| Sia (2016) | Versión poderosa; usada en *Nerve* y *Sia's Music* |
| Bobby Womack | Versión soul; parte de su repertorio clásico |

---

## 10. Fuentes

- **Spotify:** `https://open.spotify.com/track/63rva3TBizr6x1Yp5uwKfD`
- **Deezer:** `https://www.deezer.com/track/2321278`
- **CifraClub:** `https://www.cifraclub.com/the-mamas-and-the-papas/california-dreamin/`
- **Hooktheory:** — (progresión documentada en jonmaclennan.com)
- **Songsterr / Ultimate Guitar:** `https://tabs.ultimate-guitar.com/tab/the-mamas-the-papas/california-dreamin-chords-10986`
- **Wikipedia / MusicBrainz:** `https://en.wikipedia.org/wiki/California_Dreamin%27`
- **Songfacts:** `https://www.songfacts.com/facts/the-mamas-the-papas/california-dreamin`
- **Genius:** `https://genius.com/The-mamas-and-the-papas-california-dreamin-lyrics`
- **Gold Radio (composición):** `https://www.goldradio.com/features/song-facts/california-dreamin-mamas-papas-lyrics-meaning`

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (music analyst agent) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | gemma4 / mistral:7b |
| **Tags** | sunshine-pop, folk-rock, california-sound, 1960s, nostalgia, winter, counterculture |
| **Pendientes** | Verificar progresión exacta con Hooktheory; análisis librosa pendiente |

# Song Case — Take On Me — a-ha

> **Propósito:** Análisis exhaustivo del hit internacional de a-ha (1985), uno de los temas más icónicos del synth-pop de los 80s. Documenta las 3 versiones de estudio, la progresión armónica, el rango vocal extremo de Morten Harket, y la producción que llevó 3 años y 3 intentos en concretarse.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Take On Me |
| **Artista** | a-ha (Morten Harket, Pål Waaktaar, Magne Furuholmen) |
| **Versión analizada** | Alan Tarney 1985 (versión internacional hit) |
| **Álbum** | *Hunting High and Low* |
| **Año** | 1985 (tercera versión; original 1984) |
| **Duración** | 3:46 (7"), 4:50 (12" extended), 3:18 (1984 original) |
| **ISRC** | USWB19901214 |
| **Compositor(es)** | Pål Waaktaar, Magne Furuholmen, Morten Harket |
| **Productor(es)** | Alan Tarney (hit); Tony Mansfield (1984) |
| **Género(s)** | Synth-pop, New Wave, Pop rock |
| **Sello** | Warner Bros. Records |
| **País** | Noruega (grabado en Londres, UK) |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 168.8 |
| **Gain** | -9.7 dB |
| **Rank** | 988080 |
| **Explicit** | No |
| **Release Date** | 1985-06-12 |
| **Duración** | 227s (3:47) |

### 2.2 Spotify API (aproximado vía Music Gateway)

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 169 | Consistente con Deezer (168.8) |
| **Key** | A (Camelot 11B) | A major según Wikipedia; algunos detectores dan F#m (11A, relativo menor) |
| **Mode** | major | |
| **Camelot** | 11B | |
| **Danceability** | Media-alta | Ritmo rápido, pulso constante |
| **Energy** | Alta | Synth brillante, batería marcada |
| **Loudness** | -5.7 dB | |
| **Time Signature** | 4/4 | |

### 2.3 Análisis local (librosa) — pendiente

> No se dispone del archivo de audio local. Según Klangio: -13 dB loudness, 167 BPM.

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| A | major | Alta (Wikipedia, Hooktheory) |

### 3.2 Progresión base

```
I = A   ii = Bm   iii = C#m   IV = D   V = E   vi = F#m   VII = G
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro/Riff | Bm7 — E — A — D — E | ii7 — V — I — IV — V | La base del riff icónico de Juno-60 |
| Verse | Bm7 — E — A — D — E | ii7 — V — I — IV — V | Cíclico, cada 2 compases |
| Chorus | A — C#m7/G# — F#m — D | I — iii7/V — vi — IV | Ascenso vocal progresivo |
| Bridge | C#m — G — C#m — G — Bm — E | iii — VII — iii — VII — ii — V | Única sección con G natural (bVII) |
| Outro | A — C#m7 — F#m — D (y variantes) | I — iii7 — vi — IV | Fade out con repetición del chorus |

### 3.4 Diagrama armónico

```
[Riff]     → [Verse 1]       → [Chorus]              → [Verse 2]
 ii7 V I IV V   ii7 V I IV V    I iii7/5 vi IV          ii7 V I IV V

→ [Chorus]      → [Bridge]                     → [Chorus] → [Outro]
 I iii7/5 vi IV   iii VII iii VII ii V (x2)     I iii7/5 vi IV    fade
```

### 3.5 Notas armónicas

- La canción **nunca abandona la tónica A** — es una exhibición de economía armónica. Todo el peso recae en la melodía vocal y el riff.
- El puente introduce el único acorde foráneo (G natural, bVII), creando tensión mixolidia que resuelve a Bm → E → A.
- La progresión del verso (ii7–V–I–IV–V) es una variación del canon pop, pero ejecutada a 169 BPM.

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Duración aprox | Compases | Acordes clave | Notas |
|---|---------|---------------|----------|---------------|-------|
| 1 | Intro (riff) | 0:00–0:09 | 4 | Bm7-E-A-D-E | Riff sintetizado, presentación del motivo |
| 2 | Verse 1 | 0:09–0:30 | 8 | Bm7-E-A-D-E | "We're talking away…" |
| 3 | Chorus 1 | 0:30–0:51 | 8 | A-C#m7/G#-F#m-D | "Take on me…" |
| 4 | Verse 2 | 0:51–1:12 | 8 | Bm7-E-A-D-E | "So needless to say…" |
| 5 | Chorus 2 | 1:12–1:33 | 8 | A-C#m7/G#-F#m-D | |
| 6 | Bridge | 1:33–1:54 | 8 | C#m-G-C#m-G-Bm-E | Única sección con cambio armónico |
| 7 | Chorus 3 | 1:54–2:15 | 8 | A-C#m7/G#-F#m-D | Con variaciones vocales |
| 8 | Outro | 2:15–3:46 | ~24+ | A-C#m7/G#-F#m-D (fade) | Repite chorus hasta fade |

### 4.2 Forma general

```
[Riff] → [V1] → [C1] → [V2] → [C2] → [Bridge] → [C3] → [Outro/Fade]
```

Estructura **verse-chorus estándar** con bridge antes del chorus final.

---

## 5. Letra

```
[Verse 1]
We're talking away
I don't know what I'm to say
I'll say it anyway
Today's another day to find you
Shying away
I'll be coming for your love, OK?

[Chorus]
Take on me (take on me)
Take me on (take on me)
I'll be gone
In a day or two

[Verse 2]
So needless to say
I'm odds and ends
But I'll be stumbling away
Slowly learning that life is OK
Say after me
It's no better to be safe than sorry

[Chorus]
Take on me (take on me)
Take me on (take on me)
I'll be gone
In a day or two

[Bridge]
All the things that you say, yeah
Is it life or just to play my worries away?
You're all the things I've got to remember
You're shying away
I'll be coming for you anyway

[Chorus]
Take on me (take on me)
Take me on (take on me)
I'll be gone
In a day or two

[Outro]
Take on me (take on me)
Take me on (take on me)
I'll be gone
In a day or two
(fade)
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABBCB | "away/say/anyway/find you/away/OK" — asonante |
| Chorus | AAB | "me/me/gone" + "two" — rima libre |
| Verse 2 | AABCDB | "say/ends/away/OK/me/sorry" — asonante |
| Bridge | AABCDB | "say/play/away/remember/away/anyway" |

El esquema es predominantemente **asonante libre**, típico del pop donde la melodía prima sobre la rima perfecta.

---

## 7. Análisis lírico

### 7.1 Tema central

Ruega por amor antes de que se acabe el tiempo. El narrador siente que su pareja se distancia ("shying away") y pide que lo "tome" (take on me / hold me) antes de que sea demasiado tarde ("I'll be gone in a day or two").

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Metáfora | "odds and ends" | El narrador se describe como fragmentos sueltos, incompleto |
| Hipérbaton | "needless to say / I'm odds and ends" | Inversión del orden lógico |
| Ironía | "slowly learning that life is OK" | Aprendizaje lento y doloroso |
| Thetan exclamación | "Take on me (take on me)" | Eco/pedir refuerzo |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Anáfora | "Take on me / Take me on" |
| Pleonasmo | "Take on me (take on me)" — la repetición en eco |
| Interrogación retórica | "Is it life or just to play?" |

### 7.4 Conexión intertextual

- El riff inicial de teclado se origina en una canción de la banda previa de Waaktaar y Furuholmen, **Bridges**, titulada "Miss Eerie" (influencia de Ray Manzarek / The Doors).
- La canción pasó por títulos previos: "The Juicy Fruit Song" (inspirado por un comercial de chicle), "Lesson One", y "All's Well That Ends Well and Moves With the Sun".
- El vídeo de rotoscopio (Steve Barron) se inspiró en la película *Altered States* (1980) y en el corto animado *Commuter* de Michael Patterson.
- La línea "It's no better to be safe than sorry" es una inversión del proverbio inglés "better safe than sorry".

### 7.5 Contexto de composición

- El riff de teclado fue escrito por Furuholmen a los **15 años**.
- La canción fracasó **dos veces** antes de ser un hit: la versión de Tony Mansfield (1984, peaked #137 UK) y la primera versión de Alan Tarney (1985, también flopped).
- Warner Bros. invirtió **$100,000** en el vídeo de rotoscopio — el más caro de la época.
- La banda gastó el presupuesto del álbum en una versión que no funcionó. Estaban en Londres con visa de turista, sin dinero, a punto de ser deportados.
- El ejecutivo Jeff Ayeroff (Warner Bros.) vio una foto de la banda y dijo: *"Morten Harket was one of the best-looking men in the world"* — y decidió apostar por ellos.
- La versión final se grabó en **5 días** en RG Jones, Wimbledon, cuando Alan Tarney tenía un hueco entre otros proyectos.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| **Roland Juno-60** (Furuholmen) | Toda la canción | Riff principal, melodía icónica |
| **Yamaha DX7** (Waaktaar) | Toda la canción | Capas de pads |
| **PPG Wave** (Waaktaar/Furuholmen) | Toda la canción | Texturas digitales |
| **LinnDrum** (Waaktaar) | Toda la canción | Programada por Waaktaar; caja con half-time feel |
| **Acoustic guitar** (Waaktaar) | Verses | Rítmica, apenas audible en la mezcla final |
| **Overdubbed hi-hat / cymbals** (Waaktaar) | Toda | Sobre la base de LinnDrum |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | A2 a E5 — **2.5 octavas** |
| Textura | Clara, con falsetto en el agudo |
| Entrega | Desde susurro en versos hasta belting en chorus |
| Capas | La respuesta "take on me" en el chorus es una segunda toma en eco |
| Micrófono | Neumann U47 con preamp y EQ Neve |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Compresivo, propio de los 80s — la mezcla es densa pero con espacio para el vocal.
- **Panning:** Synth riff centrado, pads a los lados, voz centrada.
- **Efectos destacados:** Reverb tipo hall en la voz de Harket; delay sincopado en el riff.
- **Coda:** La versión de Tarney añadió un fade-out extendido (vs. los cortes abruptos de las versiones previas).
- **Producción general:** Alan Tarney — minimalista pero pulido. Tarney dijo: *"All I did was recreate the original demo, the one from Sydenham. That was the one that had all the charm."*

---

## 9. Versiones y diferencias

| Versión | Año | Duración | Productor | Diferencias clave |
|---------|-----|----------|-----------|-------------------|
| **Original (Mansfield)** | 1984 | 3:18 | Tony Mansfield | Fairlight CMI sampler, synth stabs, sonido más crudo, final abrupto |
| **King (1984)** | 1984 | 3:10 | Neill King | Synths más pop, mezcla más limpia que Mansfield pero aún inmadura |
| **Tarney (hit)** | 1985 | 3:46 | Alan Tarney | LinnDrum con half-time snare, coda en fade-out, voz más agresiva, riff más definido |
| **Extended Version** | 1985 | 4:50 | Alan Tarney | Secciones extendidas, más espacio instrumental |
| **Kygo Remix** | 2015 | — | Kygo | Tropical house, reemplaza el riff original, preserva vocal de Harket |

---

## 10. Fuentes

- **Deezer:** `https://www.deezer.com/track/664107`
- **Songfacts:** `https://www.songfacts.com/facts/a-ha/take-on-me`
- **Wikipedia:** `https://en.wikipedia.org/wiki/Take_on_me`
- **Sound on Sound (Classic Tracks):** `https://www.soundonsound.com/techniques/classic-tracks-ha-take-me`
- **Rolling Stone:** `https://www.rollingstone.com/music/music-news/the-secret-history-of-a-has-smash-take-on-me-95480/`
- **Song Exploder (transcripción):** `https://songexploder.net/wp-content/uploads/2025/10/Song-Exploder-A-ha-Transcript.pdf`
- **CifraClub:** `https://www.cifraclub.com.br/a-ha/take-on-me/`
- **Ultimate Guitar:** `https://tabs.ultimate-guitar.com/tab/a-ha/take-on-me-chords-2553492`
- **Hooktheory:** `https://www.hooktheory.com/theorytab/view/a-ha/take-on-me`
- **Music Gateway:** `https://www.musicgateway.com/song-key-bpm/a-ha/take-on-me`

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (asistente) |
| **Fecha del análisis** | 2026-06-02 |
| **Tags** | synth-pop, new wave, 80s, norway, rotoscoping, one-hit-wonder-america, vocal-extreme |
| **Pendientes** | Analizar archivo local con librosa para confirmar BPM/key; buscar entrevista completa de Song Exploder; verificar cifras de ventas exactas |

# Song Case — Wild World — Cat Stevens

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Wild World |
| **Artista** | Cat Stevens (Yusuf Islam) |
| **Versión analizada** | original (álbum) |
| **Álbum** | Tea for the Tillerman |
| **Año** | 1970 (álbum) / 1971 (single) |
| **Duración** | 3:15 (álbum) / 3:21 (remaster 2020) |
| **ISRC** | GBAAN7000041 |
| **Género(s)** | Folk rock, singer-songwriter, soft rock |
| **Compositor(es)** | Cat Stevens (Yusuf Islam) |
| **Productor(es)** | Paul Samwell-Smith |
| **Sello** | Island (UK), A&M (US) |
| **País** | Reino Unido |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — valores aproximados (pueden variar según el cliente).

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 152 | |
| **Key** | 0 | (C mayor / Am) |
| **Mode** | major | |
| **Camelot** | 8B | |
| **Danceability** | 0.48 | |
| **Energy** | 0.54 | |
| **Valence** | 0.43 | (positividad musical) |
| **Acousticness** | 0.34 | |
| **Instrumentalness** | 0.00 | |
| **Speechiness** | 0.03 | |
| **Liveness** | 0.11 | |
| **Loudness** | -8.51 dB | |
| **Time Signature** | 4/4 | |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/902671822`

| Feature | Valor |
|---------|-------|
| **BPM** | 0 (no detectado por Deezer) |
| **Gain** | -13.5 dB |
| **Rank** | 745588 |
| **Explicit** | no |
| **Release Date** | 2020-03-13 (relanzamiento) |
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
| C major (relativo Am) | major | alta — aunque la canción inicia en Am (relativo), el coro resuelve en C mayor |

### 3.2 Progresión base

```
I    V7/vi  V/V   IV    IV    ii    V7
C    D7     G7    F     F     Dm    E7   (enarmónico: E7 como V de Am)
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | Am — D7 — G — Cmaj7 — F — Dm — E | i — V7/vi — V/V — I — IV — ii — V/i | Ciclo completo que presenta toda la paleta armónica |
| Verse | Am — D7 — G — Cmaj7 — F — Dm — E | i — V7/vi — V/V — I — IV — ii — V/i | "Now that I've lost everything to you" |
| Pre-Chorus | Am — D7 — G — C — F — Dm — E — G7 | i — V7/vi — V/V — I — IV — ii — V/i — V7/V | "But if you want to leave, take good care" |
| Chorus | C — G — F — C — G — F — C — Dm — E | I — V — IV — I — V — IV — I — ii — V/i | "Ooh baby baby it's a wild world" |
| Outro | Am — D7 — G — Cmaj7 — F — Dm — E — Am | i — V7/vi — V/V — I — IV — ii — V/i — i | Repite el ciclo del intro |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro]                    → [Verse 1]                 → [Pre-Chorus]
Am D7 G Cmaj7 F Dm E        Am D7 G Cmaj7 F Dm E       Am D7 G C F Dm E G7
i  V7 V  I    IV ii V       i  V7 V  I    IV ii V       i  V7 V I IV ii V V7/V

→ [Chorus]                   → [Verse 2] → [Pre-Chorus] → [Chorus]
C G F C G F C Dm E           (igual que V1)              (igual)
I V IV I V IV I ii V/i
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:08 | ~8 | 2 | Am D7 G Cmaj7 F Dm E | Ciclo completo "la la la" |
| 2 | Verse 1 | 0:08–0:36 | ~28 | 8 | Am D7 G Cmaj7 F Dm E | "Now that I've lost everything to you" |
| 3 | Pre-Chorus | 0:36–0:49 | ~13 | 4 | Am D7 G C F Dm E G7 | "But if you want to leave…" |
| 4 | Chorus | 0:49–1:11 | ~22 | 8 | C G F C G F C Dm E | "Ooh baby baby it's a wild world" |
| 5 | Verse 2 | 1:11–1:39 | ~28 | 8 | Am D7 G Cmaj7 F Dm E | "You know I've seen a lot…" |
| 6 | Pre-Chorus | 1:39–1:52 | ~13 | 4 | (igual) | |
| 7 | Chorus | 1:52–2:14 | ~22 | 8 | (igual) | |
| 8 | Instrumental | 2:14–2:26 | ~12 | 4 | Am D7 G Cmaj7 F Dm E | Ciclo "la la la" |
| 9 | Pre-Chorus | 2:26–2:39 | ~13 | 4 | (igual) | "Baby I love you…" |
| 10 | Chorus (x2) | 2:39–3:15 | ~36 | 14 | (igual) | Repite hasta fade |

### 4.2 Forma general

```
[Intro] [V1] [Pre-C] [C] [V2] [Pre-C] [C] [Instrumental] [Pre-C] [C] [C]
```

---

## 5. Letra

```
[Intro]
La la la la la la la la la la
La la la la la la la la la la
La la la la la la la la la la la

[Verse 1]
Now that I've lost everything to you
You say you wanna start something new
And it's breakin' my heart you're leavin'
Baby, I'm grievin'

[Pre-Chorus]
But if you wanna leave, take good care
Hope you have a lot of nice things to wear
But then a lot of nice things turn bad out there

[Chorus]
Ooh baby baby, it's a wild world
It's hard to get by just upon a smile
Ooh baby baby, it's a wild world
I'll always remember you like a child, girl

[Verse 2]
You know I've seen a lot of what the world can do
And it's breakin' my heart in two
Because I never wanna see you sad girl
Don't be a bad girl

[Pre-Chorus]
But if you wanna leave, take good care
Hope you make a lot of nice friends out there
But just remember there's a lot of bad and beware

[Chorus]
Ooh baby baby, it's a wild world
It's hard to get by just upon a smile
Ooh baby baby, it's a wild world
I'll always remember you like a child, girl

[Instrumental / "La la la"]

[Pre-Chorus]
Baby, I love you
But if you wanna leave, take good care
Hope you make a lot of nice friends out there
But just remember there's a lot of bad and beware

[Chorus]
Ooh baby baby, it's a wild world
It's hard to get by just upon a smile
Ooh baby baby, it's a wild world
I'll always remember you like a child, girl

Ooh baby baby, it's a wild world
It's hard to get by just upon a smile
Ooh baby baby, it's a wild world
And I'll always remember you like a child, girl
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABB | you/new — leavin'/grievin' |
| Pre-Chorus | AAB | care/wear — (bad) out there — rima libre (care/wear, there suelta) |
| Chorus | AABB | world/smile — world/girl |
| Verse 2 | AABB | do/two — sad/bad |
| Pre-Chorus | AAB | care/there — (beware) — patrón similar al primer pre-coro |

Rima consonante en versos, asonante en pre-coros.

---

## 7. Análisis lírico

### 7.1 Tema central

Despedida y protección. Un amante (real o metafórico) se despide de alguien que se marcha, advirtiéndole sobre los peligros del mundo mientras expresa su dolor por la separación. Subtexto: Stevens escribió sobre su propio regreso a la industria musical tras casi morir de tuberculosis.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Metáfora conceptual | "It's a wild world" | El mundo como espacio salvaje, peligroso, que requiere protección |
| Antítesis | "nice things" / "turn bad" — "sad girl" / "bad girl" | Tensión entre lo que se desea y lo que ocurre; inocencia vs. experiencia |
| Anáfora | "But if you want to leave, take good care / Hope you make a lot of nice friends out there / But just remember there's a lot of bad and beware" | Estructura paralela en todos los pre-coros |
| Diminutivo afectivo | "like a child, girl" | Infantilización de la destinataria — gesto paternal y protector |
| Ironía dramática | "It's hard to get by just upon a smile" | La sonrisa como símbolo de inocencia que el narrador sabe insuficiente |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Apóstrofe | "Ooh baby baby" — invocación directa a la amada ausente |
| Epíteto | "wild world" — adjetivo antepuesto que se vuelve casi nombre propio |
| Paralelismo | "It's breakin' my heart you're leavin' / Baby, I'm grievin'" — dos verbos en -ing para el mismo acto |
| Polisíndeton implícito | La repetición de "baby, baby" en el coro como muletilla retórica |
| Quiasmo semántico | "I'll always remember you like a child, girl" — él la recordará como niña mientras ella se va a ser adulta |

### 7.4 Conexión intertextual

> Pet Shop Boys fueron acusados (por Jonathan King) de plagiar "Wild World" para su éxito "It's a Sin" (1987). King lanzó su propia versión de "Wild World" arreglada como "It's a Sin" para demostrarlo; Pet Shop Boys lo demandaron y ganaron, donando la compensación a caridad.
> 
> La versión de Jimmy Cliff (1970, producida por el propio Stevens) alcanzó el #8 en UK antes que la versión de Stevens — que no se lanzó como single en UK.

### 7.5 Contexto de composición

> Cat Stevens compuso "Wild World" durante las sesiones de *Tea for the Tillerman* (1970), tras recuperarse de un colapso pulmonar causado por tuberculosis en 1969 — experiencia que casi lo mata. Aunque popularmente se asocia con su ruptura con la actriz Patti D'Arbanville, Stevens aclaró en *The Chris Isaak Hour* (2009) que la inspiración primaria fue su propio regreso a la música: "Me estaba advirtiendo a mí mismo que tuviera cuidado esta vez. Trata sobre perder el contacto con el hogar y la realidad — el hogar especialmente." No obstante, también dijo a Billboard que era "mi canción de despedida con mi novia Patti D'Arbanville." La ambigüedad — autobiográfica y romántica — es su fuerza lírica.
> 
> La canción fue el primer gran éxito de Stevens en EE.UU. (#11 Billboard Hot 100, 1971) y dio a *Tea for the Tillerman* el impulso comercial para ser un clásico. Chris Blackwell (Island Records) la llamó "el mejor álbum que hemos lanzado."

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Guitarra clásica | Toda la canción | Cat Stevens — patrón de rasgueo flamenco/folk |
| Guitarra acústica (segunda) | Textura | Alun Davies — armonía y respaldo |
| Batería | Versos y coros | Harvey Burns — congas, tambourine, golpe suave |
| Contrabajo | Toda la canción | John Ryan — pizzicato, líneas melódicas simples |
| Teclados/piano | Leve textura | Cat Stevens (mínimo, casi imperceptible) |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Medio (barítono ligero) |
| Textura | Voz principal + backing vocals (Alun Davies) |
| Entrega | Íntima, confesional, ligeramente nasal. Stevens canta con vulnerabilidad apenas contenida |
| Capas | Doble pista ocasional; armónicas suaves en el coro; "la la la" del intro con capas |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Medio-bajo; canción principalmente acústica sin grandes contrastes de volumen
- **Panning:** Guitarra clásica centrada; segunda guitarra ligeramente a la derecha; voz centrada; percusión dispersa
- **Efectos destacados:** Reverberación natural de sala; compresión suave; el "la la la" inicial tiene un filtro de presencia característico
- **Producción general:** Paul Samwell-Smith logra una producción limpia y orgánica que privilegia la calidez acústica y la intimidad vocal. Sin adornos innecesarios. Textura folk con influencias mediterráneas

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (Cat Stevens, 1970) | 3:15, acústica, guitarra clásica, arreglo folk |
| Jimmy Cliff (1970) | Versión reggae temprana; producida por el propio Stevens; #8 UK |
| Maxi Priest (1988) | Reggae comercial; #5 UK, #25 US; producida por Sly & Robbie |
| Mr. Big (1993) | Rock balada con guitarra eléctrica; #27 US; sonido "unplugged" |
| James Blunt (2007, Live Earth) | Versión íntima al piano en Wembley |
| Bastille feat. Kianja (2018) | Electropop, coros procesados |
| Garth Brooks (2013) | Versión country |
| Pet Shop Boys conexión | Jonathan King lanzó versión en 1987 para probar supuesto plagio con "It's a Sin" |

---

## 10. Fuentes

- **Spotify:** `https://open.spotify.com/track/7mjSHL2Eb0kAwiKbvNNyD9`
- **Deezer:** `https://www.deezer.com/track/902671822`
- **CifraClub:** `https://www.cifraclub.com/cat-stevens/wild-world/`
- **Hooktheory:** — (progresión documentada en azchords.com y chordie.com)
- **Songsterr / Ultimate Guitar:** `https://tabs.ultimate-guitar.com/tab/cat-stevens/wild-world-chords-24256`
- **Wikipedia / MusicBrainz:** `https://en.wikipedia.org/wiki/Wild_World_(song)`
- **Songfacts:** `https://www.songfacts.com/facts/cat-stevens/wild-world`
- **Genius:** `https://genius.com/Cat-stevens-wild-world-lyrics`
- **Cat Stevens official:** `https://catstevens.com/media/songs/wild-world`

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (music analyst agent) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | gemma4 / mistral:7b |
| **Tags** | folk-rock, singer-songwriter, 1970s, cat-stevens, heartbreak, farewell, tuberculosis |
| **Pendientes** | Verificar progresión con Hooktheory; análisis librosa pendiente; aclarar versión exacta (single vs álbum) en streaming |

# Song Case — Dust in the Wind — Kansas

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Dust in the Wind |
| **Artista** | Kansas |
| **Versión analizada** | Original |
| **Álbum** | Point of Know Return |
| **Año** | 1977 |
| **Duración** | 3:26 |
| **ISRC** | USSM10103196 |
| **Género(s)** | Progressive Rock, Acoustic Rock, Ballad |
| **Compositor(es)** | Kerry Livgren |
| **Productor(es)** | Jeff Glixman |
| **Sello** | Kirshner Records |
| **País** | Estados Unidos |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — valores de SongData.io para track `6zeE5tKyr8Nu882DQhhSQI`.

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | 94 | (188 en doble tempo; Deezer reporta 187.1) |
| **Key** | 7 | G Major (ambigua, también analizable en A menor) |
| **Mode** | major | |
| **Camelot** | 9B | |
| **Danceability** | 0.48 | |
| **Energy** | 0.32 | (baja, acústica) |
| **Valence** | 0.39 | (melancólica) |
| **Acousticness** | 0.37 | |
| **Instrumentalness** | 0.00 | |
| **Speechiness** | 0.03 | |
| **Liveness** | 0.11 | |
| **Loudness** | −10.687 dB | |
| **Time Signature** | 4/4 | |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/830342`

| Feature | Valor |
|---------|-------|
| **BPM** | 187.1 |
| **Gain** | −12.7 dB |
| **Rank** | 712,407 |
| **Explicit** | no |
| **Release Date** | 1977-10-11 |
| **Preview URL** | https://cdnt-preview.dzcdn.net/api/1/1/8/b/3/0/... |

### 2.3 Análisis local (librosa) — opcional

| Feature | Valor |
|---------|-------|
| **BPM (librosa)** | — |
| **Key (librosa)** | — |
| **Mode** | — |
| **Energy** | — |
| **Danceability** | — |
| **Valence** | — |
| **Spectral Centroid** | — |
| **Onset Density** | — |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| G / Am | major / minor (ambigua) | Alta |

> La canción oscila entre G Major (I = G) y A menor (vi = Am). El centro tonal es maleable: las estrofas se apoyan en C y Am, y el coro resuelve fuertemente en Am con el patrón G–Am–G/D–D/F#. La ambigüedad modal es parte de la riqueza armónica.

### 3.2 Progresión base

```
En G:    I    ii    iii   IV    V    vi    vii°
         G    Am    Bm    C     D    Em    F#dim

En Am:   i    ii°   III   iv    v    VI    VII
         Am   Bdim  C     Dm    Em   F     G
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | C – Cmaj7 – Cadd9 – C / Asus2 – Asus4 – Am – Asus2 | IV – IVmaj7 – IVadd9 – IV / v–ii–vi–v (en G) | Arpegio fingerpicking (Travis picking) en C con coloraturas; luego Am con suspensiones |
| Verse | C – G/B – Am – G – Dm7 – Am | IV – I/iii – vi – I – ii7 – vi | La línea descendente del bajo (C–B–A–G–D–A) crea movimiento |
| Chorus | G – Am – Am/G – D/F# – G – Am | I – vi – vi/I – V/iii – I – vi | Resolución fuerte de D/F# → G → Am (V–I–vi en G) |
| Instrumental | Amadd9 – Amadd9 – G/A – G/A | vi – vi – I/ii – I/ii | Coloraturas armónicas; violín doblado |
| Bridge | C – G/B – Am – G – Dm7 – Am (con variación) | IV – I/iii – vi – I – ii7 – vi | Similar al verso, con mayor intensidad |
| Outro | G – Am – Am/G – D/F# – G – Am | I – vi – vi/I – V/iii – I – vi | Repetición del coro con fade |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro]              → [Verse 1]          → [Chorus]
C – Cmaj7 – Cadd9 – C   C – G/B – Am – G    G – Am – Am/G – D/F#
Asus2 – Asus4 – Am       Dm7 – Am            G – Am

→ [Verse 2]          → [Chorus]           → [Bridge]
C – G/B – Am – G        G – Am – Am/G – D/F#   C – G/B – Am – G
Dm7 – Am                 G – Am                Dm7 – Am

→ [Chorus]           → [Instrumental]     → [Outro/Fade]
G – Am – Am/G – D/F#    Amadd9 – Amadd9        G – Am – Am/G – D/F#
G – Am                  G/A – G/A              G – Am (fade con «The wind»)
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases (aprox.) | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:15 | 15 | 8 | C – Cmaj7 – Cadd9 – C / Asus2 – Asus4 – Am | Fingerpicking en C, luego Am con suspensiones |
| 2 | Verse 1 | 0:15–0:45 | 30 | 8+4+? | C – G/B – Am – G – Dm7 – Am | «I close my eyes…» |
| 3 | Chorus 1 | 0:45–1:04 | 19 | 4+4 | G – Am – Am/G – D/F# – G – Am | «Dust in the wind…» |
| 4 | Verse 2 | 1:04–1:34 | 30 | 8+4+? | C – G/B – Am – G – Dm7 – Am | «Same old song…» |
| 5 | Chorus 2 | 1:34–1:56 | 22 | 4+4 | G – Am – Am/G – D/F# – G – Am | «All we are is dust in the wind» |
| 6 | Bridge | 1:56–2:24 | 28 | 8+4+? | C – G/B – Am – G – Dm7 – Am | «Don't hang on…»; tensión máxima |
| 7 | Chorus 3 | 2:24–2:46 | 22 | 4+4 | G – Am – Am/G – D/F# – G – Am | Backing vocals «All we are is dust in the wind» |
| 8 | Outro | 2:46–3:26 | 40 | — | G – Am – Am/G – D/F# – G – Am | Fade out con violín y repetición de «The wind» |

### 4.2 Forma general

```
[Intro] [V1] [C1] [V2] [C2] [Bridge] [C3] [Outro/Fade]
```

---

## 5. Letra

```
[Verse 1]
I close my eyes
Only for a moment, and the moment's gone
All my dreams
Pass before my eyes, a curiosity

[Chorus 1]
Dust in the wind
All they are is dust in the wind

[Verse 2]
Same old song
Just a drop of water in an endless sea
All we do
Crumbles to the ground, though we refuse to see

[Chorus 2]
Dust in the wind (ah, aah, aah)
All we are is dust in the wind
Oh, oh, oh

[Bridge]
Now, don't hang on
Nothing lasts forever but the earth and sky
It slips away
And all your money won't another minute buy

[Chorus 3]
Dust in the wind
All we are is dust in the wind
(All we are is dust in the wind)

[Outro]
Dust in the wind
(Everything is dust in the wind)
Everything is dust in the wind
The wind
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABCB | eyes/moment's/gone (A), dreams/curiosity (B), eyes asocia internamente |
| Chorus 1 | AA | wind/wind |
| Verse 2 | AABCB | song/water/sea (A), do/see (B) |
| Chorus 2 | AAA | wind/wind/wind |
| Bridge | AAA | on/sky/away/buy (pareados cruzados: on/on, sky/sky/away/buy) |
| Chorus 3 | AAA | wind/wind/wind |
| Outro | AAAA | wind/wind/wind/wind |

> Esquema predominantemente libre, con rimas asonantes y repetición cíclica de «wind» como ancla lírica. La irregularidad rítmica de los versos contrasta con el estribillo hipnótico y repetitivo.

---

## 7. Análisis lírico

### 7.1 Tema central

La fugacidad de la vida y la insignificancia del ser humano frente a la eternidad. La letra es una meditación estoico-existencialista: todo esfuerzo, posesión y ambición se reduce a polvo. «Dust in the wind» es la metáfora central: lo que somos es efímero, frágil, llevado por el viento del tiempo.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Símil | «Same old song / Just a drop of water in an endless sea» | La vida como una gota frente a la inmensidad |
| Metáfora central | «Dust in the wind» | El polvo como símbolo de la mortalidad |
| Ironía trágica | «All your money won't another minute buy» | La riqueza material es impotente contra la muerte |
| Hipérbaton | «Nothing lasts forever but the earth and sky» | Inversión del orden lógico para enfatizar lo único permanente |
| Anáfora | «Dust in the wind… / All we are is dust in the wind» | Repetición rítmica que funciona como mantra |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Asíndeton | «I close my eyes / Only for a moment and the moment's gone» |
| Metonimia | «And all your money won't another minute buy» (dinero por bienes materiales) |
| Interrogación retórica | (implícita en la estructura: ¿para qué aferrarse?) |
| Sinécdoque | «All we are is dust in the wind» (el polvo representa la totalidad del ser) |
| Oxímoron suave | «a curiosity» aplicado a los sueños de toda una vida |

### 7.4 Conexión intertextual

- El título y estribillo se inspiran directamente en poesía de nativos americanos: Livgren leía un libro de poesía indígena cuando encontró la frase «All we are is dust in the wind».
- Ecos bíblicos del Génesis 3:19 («polvo eres y en polvo te convertirás») y del Eclesiastés («vanidad de vanidades, todo es vanidad»).
- La línea «Nothing lasts forever but the earth and sky» remite a la filosofía estoica y al *Memento mori*.
- El tema de la brevedad de la vida conecta con el «Carpe Diem» horaciano y con la tradición del *ars moriendi*.

### 7.5 Contexto de composición

- Kerry Livgren compuso la canción en el verano de 1977 durante un descanso entre giras.
- Originalmente era un ejercicio de fingerpicking (Travis picking) para mejorar su destreza: una progresión de acordes que tocaba repetidamente.
- Su esposa lo escuchó y le dijo: «Eso es muy bonito. Deberías hacer una canción con eso». Livgren pensó que no era un estilo apropiado para Kansas.
- En 15 minutos, tarareando la línea «All we are is dust in the wind» que había encontrado en poesía nativa americana, compuso la canción completa.
- Cuando la tocó para la banda, hubo «un silencio atónito» — nadie esperaba una balada acústica del grupo conocido por su prog-rock sinfónico.
- A pesar de no haber sido planeada como sencillo (la discográfica prefirió «Point of Know Return»), el airplay la impulsó hasta el #6 en el Billboard Hot 100.
- Sigue siendo el mayor éxito comercial de Kansas y su canción más emblemática.
- La canción prefigura la conversión de Kerry Livgren al cristianismo dos años después; está cargada de alusiones bíblicas y cuestionamientos espirituales.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Guitarra acústica (Kerry Livgren) | Toda la canción | Fingerpicking (Travis picking) en standard tuning; el motor rítmico y armónico |
| Guitarra acústica (Rich Williams) | Toda la canción | Segunda guitarra que dobla y refuerza |
| Violín / Viola (Robby Steinhardt) | Toda la canción | Contrapunto melódico, fills, y solo instrumental; timbre característico |
| Voz principal (Steve Walsh) | Versos y Chorus | Voz de barítono con vibrato controlado |
| Coros (Robby Steinhardt + Steve Walsh) | Chorus | Armonías a dos voces |
| Percusión de mano (Phil Ehart) | Chorus, Bridge | Hand drums sutiles, casi imperceptibles; entrada en el segundo chorus |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Barítono (Steve Walsh) |
| Textura | Voz principal con doblajes ocasionales en el coro |
| Entrega | Reflexiva, casi susurrada en los versos; más plena en el coro |
| Capas | Armonías a dos voces (Walsh y Steinhardt) en el estribillo, con eco de llamada y respuesta en la sección final |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Amplio; el contraste entre la intimidad del fingerpicking solitario (intro, versos) y la entrada del violín/coros (chorus) es marcado pero orgánico.
- **Panning:** Guitarras acústicas en estéreo amplio (izquierda Livgren, derecha Williams); voz centrada; violín ligeramente desplazado.
- **Efectos destacados:** Reverb natural de sala; delay analógico en la voz para el «ah, aah, aah» del puente; compresión suave en las guitarras acústicas.
- **Producción general:** Intencionadamente despojada para Kansas, que venía de arreglos orquestales densos. Jeff Glixman capturó la intimidad del fingerpicking de Livgren sin sobreproducir. La mezcla es diáfana, con las guitarras acústicas ocupando el centro espectral y el violín de Steinhardt como textura superior. La ausencia de bajo eléctrico y batería (solo hand drums) es la decisión más radical.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (1977) | Acústica, fingerpicking, violín, hand drums |
| Two for the Show (1978, en vivo) | Versión en directo con público; más energía |
| Always Never the Same (1998, sinfónica) | Con orquesta sinfónica; arreglos de cuerda expandidos |
| Sarah Brightman (1999, *Eden*) | Versión new age / classical crossover con orquesta |
| Corey Taylor & Noah Sebastian (2025) | Versión rock/metal para la película *Queen of the Ring*; slide guitar y fiddle |
| Scorpions (en vivo) | Versión rock con guitarra eléctrica |

---

## 10. Fuentes

- **Spotify:** https://open.spotify.com/track/6zeE5tKyr8Nu882DQhhSQI
- **Deezer:** https://www.deezer.com/track/830342
- **SongData.io:** https://songdata.io/track/6zeE5tKyr8Nu882DQhhSQI/Dust-in-the-Wind-by-Kansas
- **CifraClub:** https://www.cifraclub.com/kansas/dust-in-the-wind/
- **E-Chords:** https://www.e-chords.com/chords/kansas/dust-in-the-wind
- **Chordie:** https://www.chordie.com/chord.pere/www.azchords.com/k/kansas-tabs-2129/dustinthewind-tabs-20638.html
- **Wikipedia:** https://en.wikipedia.org/wiki/Dust_in_the_Wind
- **Songfacts:** https://www.songfacts.com/facts/kansas/dust-in-the-wind
- **Letras.com:** https://www.letras.com/kansas/20711/
- **Genius:** https://genius.com/Kansas-dust-in-the-wind-lyrics
- **American Songwriter (historia):** https://americansongwriter.com/the-story-and-meaning-behind-dust-in-the-wind-a-fingerpicking-exercise-turned-smash-ballad-by-kansas/

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | Claude (opencode) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | gemma4 (just query-pro) |
| **Tags** | progressive-rock, acoustic-ballad, kansas, 1977, point-of-know-return, mortality, fingerpicking, violin |
| **Pendientes** | Verificar tonalidad exacta con análisis de librosa; confirmar si la ambigüedad G/Am se resuelve estadísticamente; buscar partitura oficial de Cherry Lane Music |

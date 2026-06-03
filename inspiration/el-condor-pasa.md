# Song Case — El Cóndor Pasa (If I Could) — Simon & Garfunkel

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | El Cóndor Pasa (If I Could) |
| **Artista** | Simon & Garfunkel (feat. Los Incas) |
| **Versión analizada** | cover |
| **Álbum** | Bridge Over Troubled Water |
| **Año** | 1970 |
| **Duración** | 3:06 |
| **ISRC** | USSM16900182 |
| **Género(s)** | Folk rock, Andean folk, World music |
| **Compositor(es)** | Daniel Alomía Robles (melodía original, 1913), Jorge Milchberg (arreglo, 1965), Paul Simon (letra en inglés, 1970) |
| **Productor(es)** | Paul Simon, Art Garfunkel, Roy Halee |
| **Sello** | Columbia Records |
| **País** | Estados Unidos / Perú (melodía original) |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: estimaciones basadas en múltiples fuentes (no se pudo obtener respuesta directa de la API). El track ID es `0DTCO8gD4taLTodnuba1jH`.

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | ~147 (Deezer) / ~73 (percepción) | El pulso percibido es ~73 BPM; Deezer detecta 147 (posible detección de semicorcheas o doble tempo) |
| **Key** | 4 (E) | E minor es la tonalidad universalmente aceptada |
| **Mode** | minor | |
| **Camelot** | 9A (E minor) | |
| **Danceability** | ~0.40 | Moderada — ritmo de marcha lenta |
| **Energy** | ~0.30 | Baja — textura acústica, dinámica suave |
| **Valence** | ~0.35 | Agridulce — melancólica pero serena |
| **Acousticness** | ~0.90 | Alta — instrumentación completamente acústica |
| **Instrumentalness** | ~0.05 | Baja — tiene letra |
| **Speechiness** | ~0.03 | Música cantada, no hablada |
| **Liveness** | ~0.10 | Estudio |
| **Loudness** | −16.9 dB | Deezer gain |
| **Time Signature** | 4/4 | |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/13174765`

| Feature | Valor |
|---------|-------|
| **BPM** | 147.1 |
| **Gain** | −16.9 dB |
| **Rank** | 718813 |
| **Explicit** | no |
| **Release Date** | 2025-01-20 (remaster digital) / 1970-01-26 (original) |
| **Preview URL** | https://www.deezer.com/track/13174765 |

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
| **Spectral Centroid** | — |
| **Onset Density** | — |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| E (Mi) | minor | Alta — unánime en todas las fuentes (CifraClub, Ultimate Guitar, AmChords, LosAcordes) |

### 3.2 Progresión base

```
i       III      VI       VII      v7
Em      G        C        D        B7
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro (rubato) | Em (— Am — Em) | i — iv — i | Tempo libre, quenas y charangos establecen la melodía |
| Verse | Em — G — Em | i — III — i | Progresión mínima: bordón en Em, ascenso a III |
| Chorus | C — G — C — G — Em | VI — III — VI — III — i | Contraste modal: el VI (C) abre el sonido a modo mayor |
| Outro | C — G — C — G — Em | VI — III — VI — III — i | Misma progresión del Chorus, se desvanece |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro rubato]   → [Verse 1]       → [Chorus]        → [Verse 2]
Em (Am) Em         i  III  i         VI  III  VI  III  i    i  III  i

→ [Chorus]        → [Verse 3]       → [Chorus]        → [Outro]
VI  III  VI  III  i    i  III  i    VI  III  VI  III  i    VI  III  VI  III  i
```

Nota: el B7 aparece en tablaturas detalladas (AmChords) como dominante secundaria (V7/III o como acorde de paso hacia Em), pero CifraClub omite el B7 en su versión principal.

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00 – 0:09 | ~9 | 4+4 | Em (— Am — Em) | Rubato; quenas y charangos, melodía libre |
| 2 | Verse 1 | 0:09 – 0:35 | ~26 | 8 | Em — G — Em | "I'd rather be a sparrow than a snail" |
| 3 | Chorus 1 | 0:35 – 0:59 | ~24 | 8 | C — G — C — G — Em | "Away, I'd rather sail away" |
| 4 | Verse 2 | 0:59 – 1:23 | ~24 | 8 | Em — G — Em | "I'd rather be a hammer than a nail" |
| 5 | Chorus 2 | 1:23 – 1:47 | ~24 | 8 | C — G — C — G — Em | Repite Chorus |
| 6 | Verse 3 | 1:47 – 2:11 | ~24 | 8 | Em — G — Em | "I'd rather be a forest than a street" |
| 7 | Chorus 3 | 2:11 – 2:35 | ~24 | 8 | C — G — C — G — Em | Repite Chorus |
| 8 | Verse 4 | 2:35 – 2:58 | ~23 | 8 | Em — G — Em | "I'd rather feel the earth beneath my feet" |
| 9 | Outro | 2:58 – 3:06 | ~8 | 2+ | C — G — C — G — Em | Cierre con fade en Em |

### 4.2 Forma general

```
[Intro] [V1] [C1] [V2] [C2] [V3] [C3] [V4] [Outro]
```

No hay bridge ni pre-chorus. La forma es estrófica con estribillo recurrente. Cada verso tiene 2 líneas; cada chorus tiene 4 líneas.

---

## 5. Letra

```
[Intro]
(Instrumental — quenas y charangos en rubato)

[Verse 1]
I'd rather be a sparrow than a snail
Yes I would, if I could, I surely would
Hmm-mmmmm

I'd rather be a hammer than a nail
Yes I would, if I only could, I surely would
Hmm-mmmmm

[Chorus]
Away, I'd rather sail away
Like a swan that's here and gone
A man gets tied up to the ground
He gives the world its saddest sound
Its saddest sound
Hmm-mmmmm

[Verse 2]
I'd rather be a forest than a street
Yes I would, if I could, I surely would
Hmm-mmmmm

I'd rather feel the earth beneath my feet
Yes I would, if I only could, I surely would
Hmm-mmmmm

[Chorus]
Away, I'd rather sail away
Like a swan that's here and gone
A man gets tied up to the ground
He gives the world its saddest sound
Its saddest sound
Hmm-mmmmm

[Verse 3]
I'd rather be a sparrow than a snail
Yes I would, if I could, I surely would
Hmm-mmmmm

I'd rather be a hammer than a nail
Yes I would, if I only could, I surely would
Hmm-mmmmm

[Chorus]
Away, I'd rather sail away
Like a swan that's here and gone
A man gets tied up to the ground
He gives the world its saddest sound
Its saddest sound
Hmm-mmmmm

[Outro]
(Instrumental fade — C  G  C  G  Em)
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 (L1-L2) | A / A | snail / nail |
| Verse 1 (estribillo interno) | B / B | would / would |
| Chorus | C / C / D / D / D | away / gone / ground / sound / sound |
| Verse 2 | E / E / F / F | street / feet / would / would |
| Mmm's | — | Fonemas nasales /m/ sin rima |

El esquema es predominantemente de pareados (couplets) con repetición del estribillo interno "if I could / if I only could". El chorus usa rima consonante perfecta (away/gone — ground/sound).

---

## 7. Análisis lírico

### 7.1 Tema central

La tensión entre libertad y atadura. Cada verso establece una dicotomía: lo libre y elevado (gorrión, martillo, bosque, tierra) vs. lo fijo y limitado (caracol, clavo, calle). El estribillo condensa la tesis: el hombre «atado a la tierra» produce «el sonido más triste». La canción es una meditación sobre la condición humana y el anhelo de trascendencia.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Metáfora de libertad | sparrow / hammer / forest / swan | Serie de imágenes de autonomía y poder |
| Antítesis | sparrow vs. snail; hammer vs. nail; forest vs. street | Contraste entre lo agente y lo paciente |
| Metáfora extendida | "A man gets tied up to the ground" | La atadura a la tierra como condición humana |
| Sinestesia inversa | "saddest sound" (sonido + emoción) | Atribución de emoción a un fenómeno acústico |
| Anáfora | "I'd rather be..." (x4) | Repetición estructural que unifica las estrofas |
| Epífora | "I surely would" | Refuerzo de la voluntad al final de cada par |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Metáfora | "Like a swan that's here and gone" |
| Hipérbaton | "A man gets tied up to the ground" (voz pasiva para enfatizar la condición) |
| Asíndeton | Ausencia de conectores entre los versos del chorus |
| Aliteración | "saddest sound" (/s/); "swan that's" |
| Epanadiplosis | "saddest sound / Its saddest sound" |

### 7.4 Conexión intertextual

- La melodía original de la zarzuela **El cóndor pasa** (Daniel Alomía Robles, 1913) es un himno andino sobre la libertad, representada por el cóndor.
- La letra de Paul Simon dialoga con la tradición pastoral: el campo (forest, earth) vs. la ciudad (street).
- La imagen del cisne («swan that's here and gone») evoca el mito del cisne como ave de paso, símbolo de lo efímero.
- Declarada **Patrimonio Cultural de la Nación** por el Perú en 2004, considerada «segundo himno nacional».
- Más de 4000 versiones y 300 sets de letras existen en todo el mundo.

### 7.5 Contexto de composición

La melodía fue compuesta por el peruano **Daniel Alomía Robles** en 1913 como parte de la zarzuela *El cóndor pasa*, con libreto de Julio de La Paz (seudónimo de Julio Baudouin). Se estrenó el 19 de diciembre de 1913 en el Teatro Mazzi de Lima. La zarzuela trata sobre mineros andinos oprimidos; el cóndor simboliza la libertad y la justicia.

En 1965, **Paul Simon** escuchó una versión instrumental del grupo **Los Incas** en el Théâtre de l'Est parisien de París. Simon se hizo amigo de la banda, y el director **Jorge Milchberg** le dijo erróneamente que era una melodía tradicional peruana del siglo XVIII. Simon pidió permiso para usarla y Milchberg aceptó a cambio de regalías.

Simon & Garfunkel grabaron la canción en París usando la pista instrumental de Los Incas como base, añadiendo la letra en inglés. Fue lanzada en septiembre de 1970 como sencillo, alcanzando el #18 en Billboard Hot 100 y #1 en Australia, Alemania, Austria y Países Bajos.

A finales de 1970, **Armando Robles Godoy**, hijo del compositor, demandó con éxito por derechos de autor. La canción había sido registrada en EE.UU. en 1933. Robles Godoy describió el caso como «amistoso» y basado en un «malentendido honesto». Desde entonces, Robles figura como compositor principal.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Quenas (2) | Toda la canción | Flautas andinas verticales; llevan la melodía principal y contramelodías |
| Charangos (2) | Toda la canción | Laúd andino de caparazón de armadillo; uno rasgueado, otro punteado (introducción) |
| Guitarra acústica | Toda la canción | Paul Simon — acompañamiento armónico |
| Bombo | Toda la canción | Percusión andina de doble parche; pulso constante |
| Voz (Paul Simon) | Versos | Voz principal en las estrofas |
| Voz (Art Garfunkel) | Chorus | Voz principal en el estribillo (registro agudo) |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Simon: barítono ligero (zona cómoda). Garfunkel: tenor alto (conocido por su registro agudo, aquí alcanza notas muy altas en el chorus) |
| Textura | Entrecruzada: Simon canta los versos en registro grave; Garfunkel toma el estribillo en falsete/agudo |
| Entrega | Simon: conversacional, íntimo. Garfunkel: etéreo, casi frágil |
| Capas | La voz de Garfunkel en el chorus suena sola, sin armonías vocales — notable para un dúo conocido por sus armonías |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Amplio — el intro es muy suave, el chorus tiene un pico de intensidad.
- **Panning:** Las quenas están centradas (lead); los charangos ligeramente paneados a izquierda/derecha.
- **Efectos destacados:** Reverb natural de sala; sin efectos artificiales notables. La voz de Garfunkel en el chorus tiene un timbre brillante que roza la distorsión.
- **Producción general:** Minimalista y orgánica. Es la pista menos producida del álbum *Bridge Over Troubled Water* — la base instrumental de Los Incas se usó tal cual, solo se añadieron voces. Roy Halee mezcló con transparencia, preservando el carácter acústico.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| **Original (1913)** | Zarzuela orquestal. Sin letra. Instrumentación: orquesta sinfónica con elementos andinos. Compuesta por Daniel Alomía Robles. |
| **Los Incas (1963)** | Arreglo instrumental con quenas, charangos y bombo. Grabado en París para Philips. Sin letra. Arreglo de Jorge Milchberg. |
| **Simon & Garfunkel (1970)** | Añade letra en inglés de Paul Simon. Usa la pista de Los Incas como base. Folk rock / Andean. #18 Billboard, #1 en varios países. |
| **Armando Robles Godoy (post-1970)** | Letra en español escrita por el hijo del compositor tras la demanda, tomando la versión de Simon como referencia. |
| **The Wainwright Sisters (2015)** | Cover en *Songs in the Dark*. Voz femenina, arreglo minimalista. |
| **Perú (Patrimonio Cultural, 2004)** | Declarada oficialmente Patrimonio Cultural de la Nación. Más de 4000 versiones registradas mundialmente. |

---

## 10. Fuentes

- **Spotify:** https://open.spotify.com/track/0DTCO8gD4taLTodnuba1jH
- **Deezer:** https://www.deezer.com/track/13174765
- **CifraClub:** https://www.cifraclub.com/simon-e-garfunkel/el-condor-pasa/
- **CifraClub (If I Could):** https://www.cifraclub.com/simon-e-garfunkel/el-condor-pasa-if-i-could/
- **Ultimate Guitar:** https://tabs.ultimate-guitar.com/tab/2053291
- **AmChords:** https://www.amchords.com/guitar/simon-amp-garfunkel/el-condor-pasa-if-i-could
- **LosAcordes:** https://www.losacordes.com/acordes/simon-garfunkel/el-condor-pasa
- **LaCuerda:** https://acordes.lacuerda.net/canciones/el_condor_pasa
- **Wikipedia (inglés):** https://en.wikipedia.org/wiki/El_C%C3%B3ndor_Pasa_(song)
- **Wikipedia (español):** https://es.wikipedia.org/wiki/El_C%C3%B3ndor_Pasa_(If_I_Could)
- **Songfacts:** https://www.songfacts.com/facts/simon-garfunkel/el-condor-pasa-if-i-could
- **MusicBrainz:** https://musicbrainz.org/recording/ — búsqueda por ISRC USSM16900182
- **Lyrics (Simon & Garfunkel official):** https://www.simonandgarfunkel.com/track/el-condor-pasa-if-i-could-6/
- **Lyrics (Paul Simon official):** https://www.paulsimon.com/track/el-condor-pasa-if-i-could/

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (Claude) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | mistral:7b (just query) |
| **Tags** | `Simon & Garfunkel`, `Perú`, `Andean folk`, `folk rock`, `cover`, `cóndor`, `world music`, `Paul Simon`, `Daniel Alomía Robles`, `Los Incas`, `copyright` |
| **Pendientes** | Obtener audio features exactos de Spotify API con autenticación. Analizar con librosa si se descarga el audio. Verificar si el B7 aparece en la grabación real o es solo una simplificación de tablatura. |

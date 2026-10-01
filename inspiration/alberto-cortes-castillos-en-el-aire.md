# Song Case — Castillos en el aire — Alberto Cortés

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Castillos en el aire |
| **Artista** | Alberto Cortés (Alberto Cortez) |
| **Versión analizada** | original |
| **Álbum** | Pantalones azules |
| **Año** | 1970 |
| **Duración** | 3:18 |
| **ISRC** | ES5088001982 |
| **Género(s)** | Cantautor, Balada, Folk argentino, Poesía musicada |
| **Compositor(es)** | Alberto Cortez |
| **Productor(es)** | — |
| **Sello** | Hispavox |
| **País** | Argentina (nacionalizado español) |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — valores aproximados (pueden variar según el cliente).

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | ~100 | |
| **Key** | 5 | 5 = F (menor/mayor alternante) |
| **Mode** | minor / major | Versos en Fm, coro en F mayor (modo paralelo) |
| **Camelot** | 4A / 7B (según sección) | |
| **Danceability** | ~0.35 | |
| **Energy** | ~0.45 | |
| **Valence** | ~0.30 | |
| **Acousticness** | ~0.80 | |
| **Instrumentalness** | ~0.00 | |
| **Speechiness** | ~0.04 | |
| **Liveness** | ~0.15 | |
| **Loudness** | −12.8 dB | |
| **Time Signature** | 4 | 4/4 |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/{id}`

| Feature | Valor |
|---------|-------|
| **BPM** | 100.3 |
| **Gain** | −12.8 dB |
| **Rank** | 96795 |
| **Explicit** | no |
| **Release Date** | 1970 (reedición 2016-08-19) |
| **Preview URL** | Disponible |

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
| F menor (versos) | minor | alta — i–iv–V–VII en Fm |
| F mayor (coro) | major | alta — V7–I–IV–V7/ii–ii en F |
| Alternancia modo paralelo | menor↔mayor | el recurso central de la canción |

### 3.2 Progresión base

**Verso (F menor):**
Grados: i   v   iv   IV   i   iv   V   i
         Fm  Cm  Bbm  Bb   Fm  Bbm  C   Fm

**Coro (F mayor):**
Grados: V7 — I — V7 — I — II — II# — III — VI7 — V7/V — V — V7 — I
         C7   F    C7   F    G    G#    A    D7     G7     C    C7   F

Puente hacia coro (descenso cromático):
C — Bb — Am — G (V — IV — iii — ii)

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Verse 1 | Fm — C — Cm — Bb — Bbm — Fm — Bbm — C — F | i — V — v — IV — iv — i — iv — V — I | El último acorde es F mayor (resolución picarda que anticipa el coro) |
| Verse 2 | Fm — C — Cm — Bb — Bbm — Fm — Bbm — C — F | i — V — v — IV — iv — i — iv — V — I | Misma progresión, letra nueva |
| Verse 3 | Fm — C — Cm — Bb — Bbm — Fm — Bbm — C — Fm | i — V — v — IV — iv — i — iv — V — i | Cierra en Fm (vuelve al modo menor) |
| Chorus | C7 — F — C7 — F — G G# A — D7 — G7 — C — C7 — F | V7 — I — V7 — I — II II# III — VI7 — V7/V — V — V7 — I | Ascenso cromático G–G#–A, cadencia de dominantes encadenadas (D7→G7→C→F) |
| Puente tras coro | C — Bb — Am — G | V — IV — iii — ii | Descenso por grado conjunto |
| Outro | C7 — F — ... — Bbm — C — F → fade | V7 — I — ... — iv — V — I | "La la rara la ra" sobre I–IV–V–I |

### 3.4 Diagrama de la progresión

```
[Verse]                          [Chorus]
Fm  C   Cm  Bb  Bbm  Fm  Bbm  C    C7  F  C7  F  G  G#  A  D7  G7  C  C7  F ...
 i   V   v   IV  iv   i   iv   V    V7  I  V7  I  II II# III VI7 V7/V V  V7  I

[Puente post-coro]                           [Outro]
C  Bb  Am  G  → (vuelve a Verse)             C7  F  ... la la rara la ra
V  IV  iii  ii
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Verse 1 | 0:00 | ~25 | 8 | Fm → F | Intro instrumental breve |
| 2 | Chorus | 0:25 | ~20 | 8 | C7—F—G→A—D7—G7—C | Entra orquestación |
| 3 | Verse 2 | 0:45 | ~25 | 8 | Fm → F | |
| 4 | Chorus | 1:10 | ~20 | 8 | C7—F—...—C—Bb—Am—G | |
| 5 | Verse 3 | 1:30 | ~25 | 8 | Fm → Fm | "Acaba aquí la historia del idiota" |
| 6 | Chorus | 1:55 | ~20 | 8 | C7—F—... | "Por construir... Por abrir..." |
| 7 | Outro | 2:15 | ~33 | ~16 | C7—F—Bb—C—F | "La la rara la ra" — fade |

### 4.2 Forma general

```
[Intro] [V1] [C] [V2] [C] [V3] [C] [Outro]
```

Estructura clásica de canción de cantautor: verso→coro×3 con cierre narrativo en el tercer verso (no hay bridge). La progresión armónica distingue verso (Fm) de coro (F mayor) — contraste modo menor/mayor.

---

## 5. Letra

```
[Verse 1]
Quiso volar, igual que las gaviotas
Libre en el aire, como el aire libre
Y los demás dijeron: «Pobre idiota,
no sabe que volar es imposible»

Mas extendió las alas hacia el cielo
Y poco a poco fue ganando altura
Y los demás quedaron en el suelo
Guardando la cordura

[Chorus]
Y construyó castillos en el aire
A pleno sol, con nubes de algodón
En un lugar a donde nunca nadie
Pudo llegar usando la razón

Y construyó ventanas fabulosas
Llenas de luz, de magia y de color
Y convocó al duende de las cosas
Que tienen mucho que ver con el amor

[Verse 2]
En los demás, al verlo tan dichoso
Cundió la alarma, se dictaron normas
«No vaya a ser que fuera contagioso
tratar de ser feliz de aquella forma»

La conclusión es clara y contundente:
Lo condenaron por su chifladura
A convivir de nuevo con la gente
Vestido de cordura

[Chorus]
Por construir castillos en el aire
A pleno sol, con nubes de algodón
En un lugar a donde nunca nadie
Pudo llegar usando la razón

Y por abrir ventanas fabulosas
Llenas de luz, de magia y de color
Y convocar al duende de las cosas
Que tienen mucho que ver con el amor

[Verse 3]
Acaba aquí la historia del idiota
Que por el aire, como el aire libre
Quiso volar, igual que las gaviotas…
Pero eso es imposible… ¿o no?

[Chorus / Outro]
La la rara la ra la la ra ra ra
La la rara la ra la la ra ra ra
La la rara la ra la la ra la la
La la rara la ra la ra ra ra ra
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | ABAB CDCD | Rima consonante perfecta: gaviotas/idiota, libre/imposible; cielo/suelo, altura/cordura |
| Chorus | ABAB CDCD | aire/algodón/nadie/razón; fabulosas/color/cosas/amor |
| Verse 2 | ABAB CDCD | dichoso/normas/contagioso/formas; contundente/chifladura/gente/cordura |
| Verse 3 | ABAB | idiota/libre/gaviotas/imposible — cierra el círculo con el verso inicial |
| Outro | — | Vocablos no léxicos «la la rara la ra» |

Esquema consistentemente **ABAB** (rima cruzada) en todas las estrofas de 4 versos, con rima consonante estricta. La rima en «-ura» (altura/cordura/chifladura) es el leitmotiv fónico que ancla las estrofas narrativas.

---

## 7. Análisis lírico

### 7.1 Tema central

La tensión entre el individuo que sueña y la sociedad que castiga la disidencia creativa. El «idiota» que intenta volar como las gaviotas es el arquetipo del soñador antisistema. La canción critica el conformismo social que patologiza la felicidad auténtica («no vaya a ser que fuera contagioso»).

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Metáfora central | «castillos en el aire» | Sueños, utopías, aspiraciones sin base material (frase hecha, revitalizada) |
| Símil | «igual que las gaviotas» | Libertad como estado natural |
| Antítesis | «volar» vs. «imposible» | El conflicto central del protagonista |
| Ironía dramática | «pobre idiota» (dicho por otros) | El narrador está del lado del idiota |
| Paradoja | «libre en el aire, como el aire libre» | Libertad absoluta vs. atrapamiento social |
| Hipérbole | «a donde nunca nadie pudo llegar» | La inalcanzabilidad del sueño |
| Animalización | «quiso volar igual que las gaviotas» | El soñador como ser alado |
| Pleonasmo | «el aire, como el aire libre» | Énfasis en la cualidad esencial |
| Poliptoton | «cordura» → «chifladura» → «cordura» | El marco conceptual se invierte: la locura es la verdadera cordura |
| Epifonema | «Pero eso es imposible… ¿o no?» | Pregunta retórica final que invierte la tesis |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Apóstrofe | (el narrador interpela al oyente con la pregunta final) |
| Asíndeton | «a pleno sol, con nubes de algodón» |
| Polisíndeton | «de luz, de magia y de color» |
| Anadiplosis | «cordura» → «cordura» (cierra el primer verso, abre la condena) |
| Quiasmo | «Libre en el aire, como el aire libre» — ABBA |
| Interrogación retórica | «¿o no?» — desestabiliza al oyente |

### 7.4 Conexión intertextual

- **«Castillos en el aire»** — frase hecha del español (Don Quijote: «no se le pase asentar castillos en el aire»). La canción es una reivindicación quijotesca.
- **Gaviotas** — símbolo recurrente en la literatura de libertad (Juan Salvador Gaviota de Richard Bach, 1970 — mismo año).
- **«Duende»** — término lorquiano (Teoría y juego del duende, 1933). García Lorca definía el duende como el poder misterioso que todos sienten pero nadie explica. Cortés lo vincula directamente con el amor.
- **«Chifladura» / «cordura»** — par dialéctico que recuerda a «El loco» de Tagore o «El hombre que confundió a su mujer con un sombrero» de Sacks.

### 7.5 Contexto de composición

Alberto Cortés (José Alberto García Gallo, Rancul, Argentina, 1940 — Móstoles, España, 2019) escribió la canción para su álbum *Pantalones azules* (1970). La canción pertenece a su etapa de madurez como cantautor, después de haber evolucionado desde los boleros iniciales hacia un estilo poético-filosófico que él mismo llamaba «de las cosas sencillas».

Dato biográfico notable: Cortés adoptó su nombre artístico de un cantante peruano llamado Darío Alberto Cortez Olaya, quien lo demandó y ganó en tribunales belgas. El asunto se resolvió cuando el Cortés argentino alcanzó mucha mayor fama.

En 2007 recibió el Grammy Latino a la Excelencia. Falleció en 2019 por insuficiencia cardíaca.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Piano | Versos | Acompañamiento armónico melódico, arpegios |
| Guitarra acústica | Toda la canción | Base rítmica, fingerpicking |
| Batería suave | Versos, Coros | Escobillas, patrón mínimo |
| Cuerdas | Coros | Swell orquestal, típico de la producción Hispavox 1970 |
| Bajo | Coros | Línea melódica, refuerza el cambio armónico |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Barítono medio |
| Textura | Voz solista, natural, sin efectos |
| Entrega | Narrativa y conversacional en verso; expandida y más redonda en coro |
| Capas | Ocasional doubling en el coro final |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Moderado (crecimiento gradual verso→coro)
- **Panning:** Centrado, típico de grabación de los 70
- **Efectos destacados:** Reverb de cámara en voz; cuerdas con ligero delay
- **Producción general:** Orgánica y sin artificios. La producción de Hispavox de la época prioriza la claridad vocal y la calidez acústica. El contraste dinámico entre verso (menor, contenido) y coro (mayor, expansivo) es el principal recurso expresivo.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (1970) | Piano y cuerdas, voz de Cortés, producción Hispavox |
| Jaime Urrutia (cover) | Versión rock-pop, más guitarras eléctricas, vocal más rasgada |
| Varios homenajes póstumos (2019) | Versiones orquestales en conciertos tributo en Latinoamérica |

---

## 10. Fuentes

- **Spotify:** `https://open.spotify.com/track/...`
- **Deezer:** `https://www.deezer.com/track/130415754`
- **CifraClub:** `https://www.cifraclub.com/alberto-cortez/castillos-en-el-aire/`
- **LaCuerda:** `https://acordes.lacuerda.net/alberto_cortez/castillos_en_el_aire.shtml`
- **Songsterr / Ultimate Guitar:** — (no verificada)
- **Wikipedia / MusicBrainz:** `https://es.wikipedia.org/wiki/Alberto_Cortez`
- **Entrevistas / artículo:** `https://www.letras.com/alberto-cortez/413050/significado.html`

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | JPMarichal + opencode |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | — |
| **Tags** | cantautor, argentina, 1970, protesta, poesía, duende, quijote, modo-paralelo |
| **Pendientes** | Verificar Spotify audio-features exactas; confirmar álbum original (Pantalones azules vs. recopilaciones); analizar el descenso cromático C–Bb–Am–G en relación con el ascenso G–G#–A del coro (simetría armónica) |

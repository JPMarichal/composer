# Song Case — Everybody Knows — Leonard Cohen

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Everybody Knows |
| **Artista** | Leonard Cohen |
| **Versión analizada** | Original (álbum *I'm Your Man*, 1988) |
| **Álbum** | *I'm Your Man* |
| **Año** | 1988 |
| **Duración** | 5:34 |
| **ISRC** | USSM10027491 |
| **Género(s)** | Synth-pop, Art rock, Protest song, Folk electrónico |
| **Compositor(es)** | Leonard Cohen, Sharon Robinson |
| **Productor(es)** | Michel Robidoux |
| **Sello** | Columbia Records |
| **País** | Canadá |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 104.1 |
| **Gain** | −15.7 dB |
| **Rank** | 479,837 |
| **Explicit** | no |
| **Release Date** | 2012-04-03 (reedición digital) |
| **Deezer ID** | 80869710 |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| Dm (D menor natural con V mayor) | minor | Alta — i–VI–iv–V–VII–III |

### 3.2 Progresión base

```
i     ii°   III   iv    v    VI   VII
Dm    E°    F     Gm    Am   Bb   C
```

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | Dm — A | i — V | Síncopa de sintetizador grave |
| Verso | Dm — Bb — Dm — Bb — Gm — A — C — Dm — Eb — A — Dm | i — VI — i — VI — iv — V — VII — i — III — V — i | La progresión se desvía hacia Eb (III) y luego V–i |
| Verso (variante) | Dm — Bb — Dm — Bb — Gm — A — C — Dm — Eb — A — Dm | i — VI — i — VI — iv — V — VII — i — III — V — i | Misma estructura, nuevas letras |
| Chorus | F — C — Dm — C — Bb — F | IV — I — i — I — VI — IV | Modulación a F mayor (relativo mayor de Dm) |
| Outro | Dm — Bb — Dm (fade) | i — VI — i | Vuelve a la tónica menor y se desvanece |

### 3.4 Diagrama de la progresión

```
[Intro]          → [Verse]               → [Chorus]          → [Verse] ...
 i  V              i  VI  i  VI  iv  V     IV  I  i  I  VI    i  VI  i  VI  iv  V
                   VII  i  III  V  i       IV                  VII  i  III  V  i

[Chorus]          → [Verse/Bridge]        → [Chorus]          → [Outro]
 IV  I  i  I  VI   i  VI  i  VI  iv  V     IV  I  i  I  VI    i  VI  i  (fade)
 IV                VII  i  III  V  i       IV
```

### 3.5 Notas armónicas destacadas

- **Tonalidad menor con V mayor (A)**: el acorde A (V) en lugar de Am (v) — la sensible (C#) crea la tensión de la dominante menor-armónica.
- **C (VII) y F (III) como acordes préstamo**: C es el VII grado (subtonica) del modo menor natural; F es el III (mediante mayor) — ambos aportan color modal.
- **Eb (III)**: el acorde de Mi bemol mayor es el III del modo menor natural. Aparece como sorpresa armónica al final de cada verso, justo antes del retorno a A–Dm.
- **Contraste menor–mayor en el Chorus**: el estribillo modula a F mayor (relativo mayor de Dm), dando un respiro momentáneo de la oscuridad del verso, pero la letra sigue siendo igual de sombría — ironía armónica.
- **Síncopa del bajo sintetizado**: la línea de bajo no sigue el patrón 4/4 recto — usa anticipaciones y retrasos que desestabilizan al oyente.

---

## 4. Estructura

### 4.1 Forma general

```
[Intro] [Verse 1] [Verse 2] [Chorus] [Verse 3] [Verse 4] [Chorus] [Verse 5] [Verse 6] [Chorus] [Outro]
   2       16        16         8        16        16        8        16        16        8       ~8
```

No hay un bridge tradicional — cada verso introduce nuevas imágenes. La estructura es acumulativa: cada verso añade una capa de desesperanza.

---

## 5. Letra

```
[Intro]
(Instrumental — sintetizador grave pulsante)

[Verse 1]
Everybody knows that the dice are loaded
Everybody rolls with their fingers crossed
Everybody knows the war is over
Everybody knows the good guys lost
Everybody knows the fight was fixed
The poor stay poor, the rich get rich
That's how it goes
Everybody knows

[Verse 2]
Everybody knows that the boat is leaking
Everybody knows the captain lied
Everybody got this broken feeling
Like their father or their dog just died
Everybody talking to their pockets
Everybody wants a box of chocolates
And a long stem rose
Everybody knows

[Chorus]
Everybody knows, everybody knows
That's how it goes
Everybody knows
Everybody knows, everybody knows
That's how it goes
Everybody knows

[Verse 3]
Everybody knows that you love me, baby
Everybody knows that you really do
Everybody knows that you've been faithful
Ah, give or take a night or two
Everybody knows you've been discreet
But there were so many people you just had to meet
Without your clothes
And everybody knows

[Verse 4]
And everybody knows that it's now or never
Everybody knows that it's me or you
And everybody knows that you live forever
When you've done a line or two
Everybody knows the deal is rotten
Old Black Joe's still picking cotton
For your ribbons and bows
And everybody knows

[Chorus]
Everybody knows, everybody knows
That's how it goes
Everybody knows
Everybody knows, everybody knows
That's how it goes
Everybody knows

[Verse 5]
Everybody knows that the plague is coming
Everybody knows that it's moving fast
Everybody knows that the naked man and woman
Are just a shining artifact of the past
Everybody knows the scene is dead
But there's gonna be a meter on your bed
That will disclose
What everybody knows

[Verse 6]
And everybody knows that you're in trouble
Everybody knows what you've been through
From the bloody cross on top of Calvary
To the beach of Malibu
Everybody knows that it's coming apart
Take one last look at this sacred heart
Before it blows
And everybody knows

[Chorus]
Everybody knows, everybody knows
That's how it goes
Everybody knows
Everybody knows, everybody knows
That's how it goes
Everybody knows

[Outro]
(Instrumental — fade)
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABBCCDD | loaded/crossed; over/lost; fixed/rich; goes/knows |
| Verse 2 | AABBCCDD | leaking/lied; feeling/died; pockets/choclates; rose/knows |
| Verse 3 | AABBCCDD | baby/do; faithful/two; discreet/meet; clothes/knows |
| Verse 4 | AABBCCDD | never/you; forever/two; rotten/cotton; bows/knows |
| Verse 5 | AABBCCDD | coming/fast; woman/past; dead/bed; disclose/knows |
| Verse 6 | AABBCCDD | trouble/through; Calvary/Malibu; apart/blows; knows |
| Chorus | AA BB A | knows/goes/knows (×2) |

Cada verso sigue estrictamente un esquema de 8 versos con rima pareada. La palabra "knows" cierra siempre.

---

## 7. Análisis lírico

### 7.1 Tema central

Catálogo de la podredumbre del mundo — desigualdad económica ("the poor stay poor, the rich get rich"), racismo sistémico ("Old Black Joe's still picking cotton"), crisis del SIDA ("the plague is coming"), guerra y corrupción ("the war is over, the good guys lost", "the captain lied"), hipocresía en las relaciones ("give or take a night or two"), y la apatía general ("everybody talking to their pockets, everybody wants a box of chocolates").

Pero el tono no es de denuncia airada, sino de **cinismo resignado y humor negro**. La repetición de "everybody knows" sugiere que estas verdades no son revelaciones — son obvias. Todos lo saben. Nadie actúa.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Anáfora | "Everybody knows" (abre casi todas las líneas) | 30+ repeticiones — martilleo hipnótico |
| Ironía | "Everybody knows that you've been faithful / Ah, give or take a night or two" | La contradicción en el mismo verso |
| Listado catálogo | Seis versos, cada uno con dominio distinto | Dinero, amor, drogas, SIDA, religión — cubre todo |
| Contraste sacro-profano | "From the bloody cross on top of Calvary / To the beach of Malibu" | El dolor de Cristo equiparado al hedonismo californiano |
| Metáfora | "The dice are loaded" | La vida está amañada |
| Hipérbole | "Everybody knows the fight was fixed" | No es literal, pero captura la sensación de injusticia |
| Sarcasmo | "Everybody wants a box of chocolates / And a long stem rose" | Consumismo como distracción del horror |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Anáfora | "Everybody knows..." (30+ ocurrencias) |
| Asíndeton | "The dice are loaded... the war is over... the good guys lost" |
| Ironía dramática | El oyente sabe que el narrador es cínico, pero se identifica |
| Sinécdoque | "talking to their pockets" (pockets = money) |
| Gradación descendente | De "everybody knows the plague is coming" a "everybody wants a box of chocolates" |
| Hipérbole | "everybody knows" — no todo el mundo lo sabe, pero debería |

### 7.4 Conexión intertextual

- **"Old Black Joe"**: referencia a la canción de Stephen Foster (1853) — Cohen recontextualiza el personaje como emblema del racismo que persiste.
- **"The Sacred Heart"**: devoción católica al Sagrado Corazón de Jesús — aquí es un corazón que va a explotar.
- **"The plague is coming"**: referencia directa a la crisis del SIDA de los 80.
- **"Pump Up the Volume" (1990)**: Christian Slater usa la canción como himno de rebeldía adolescente — la popularizó entre Gen X.
- **"Justice League" (2017)**: usada en el tráiler — nueva exposición masiva.
- **Don Juan Demarco (1995)**: versionada por Johnny Depp y Marlon Brando en la película.

### 7.5 Contexto de composición

Leonard Cohen escribió la letra y se la entregó a Sharon Robinson, su corista y futura colaboradora frecuente. Era la primera de muchas colaboraciones. Robinson cuenta:

> *"Leonard had most of the lyric done when he handed it to me. There's a profound honesty in it. He's exposing something we all know and talk about with those close to us, but not publicly."*

Robinson eligió un tono menor ("a protest song, so Leonard wanted something tough") y construyó la melodía en el piano de su casa. Cohen quería contrastes: sintetizadores duros contra su voz orgánica.

El álbum *I'm Your Man* (1988) marcó un giro radical para Cohen. Abandonó la espiritualidad lúcida de *Various Positions* por un cinismo mordaz y una instrumentación electrónica. La canción nació de lo que Cohen llamó "the fallout, the residue, the dust of some catastrophe" — el colapso de sus convicciones religiosas previas.

### 7.6 Interpretación política

A pesar de los intentos de apropiación por figuras como Alex Jones, la canción no es un manifiesto de conspiración. El "everybody knows" de Cohen no es una llamada a despertar, sino una constatación melancólica de que todos sabemos que el sistema está podrido y no hacemos nada. Sharon Robinson: *"It says we're not really in control of our destiny. There are others running things, and we go about our daily lives with that in the background."*

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Notas |
|-------------|-------|
| Sintetizador (bajo) | Línea pulsante, grave, síncopa hipnótica |
| Sintetizador (textura) | Pads oscuros, drones |
| Oud | Aporta un color oriental/mediterráneo — contraste con los sintetizadores |
| Guitarra española | Flourishes acústicos en el estribillo |
| Batería electrónica | Caja y bombo secos, sonido típico de los 80 |
| Coros | Jennifer Warnes en backing vocals |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Barítono grave — casi hablado en los versos |
| Textura | Voz grave, rasposa, "cigarette-infused snarl" |
| Entrega | Fría, sardónica, con humor seco en las pausas |
| Capas | Voz principal en el centro; ocasional doblaje en el estribillo |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Comprimido — propio del synth-pop de los 80.
- **Panning:** Sintetizadores estéreo anchos, voz centrada y seca.
- **Efectos destacados:** Reverb tipo hall en pads; la voz de Cohen está sorprendentemente seca (poca reverb), lo que la hace más íntima y amenazante.
- **Producción general:** Michel Robidoux creó un sonido deliberadamente artificial — el contraste entre la voz terrenal de Cohen y los sintetizadores fríos refuerza el tema de la deshumanización.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| **Leonard Cohen** (1988) | Original — sintetizadores, oud, Jennifer Warnes en coros; 6 versos, 5:34 |
| **Concrete Blonde** (1991) | Versión rock — guitarra eléctrica distorsionada, voz de Johnette Napolitano; incluida en *Pump Up the Volume* |
| **Rufus Wainwright** (2000) | Versión más suave, piano y cuerdas |
| **Don Juan DeMarco** (1995) | Interpretada por Johnny Depp y Marlon Brando en la película |
| **The Specials** (2021) | Versión ska/reggae en *Protest Songs 1924-2012* |
| **Ted Leo and the Pharmacists** | Versión punk rock en vivo |

---

## 10. Datos curiosos y legado

1. **Primera colaboración con Sharon Robinson**: inició una sociedad creativa que duraría hasta la muerte de Cohen. Robinson co-escribió también "Ain't No Cure for Love" y "Waiting for the Miracle".
2. **Oud en una canción synth-pop**: la inclusión del oud (laúd árabe) es un guiño a las influencias mediterráneas de Cohen, pero en un contexto electrónico.
3. **Alex Jones y la apropiación**: el locutor de conspiracy theories usó la canción repetidamente como cortina musical. No es el uso que Cohen pretendía.
4. **"Everybody Knows" ≠ "Everybody Knows"**: existen al menos dos canciones de Cohen con título similar — esta y "Everybody Knows" de *Recent Songs* (1979), que es completamente distinta.
5. **Resurgimiento cinematográfico**: usada en *Justice League* (2017), *Pump Up the Volume* (1990), y series como *The Handmaid's Tale*.
6. **#4 en votación de Rolling Stone**: quedó cuarta en la encuesta de lectores de mejores canciones de Cohen — por detrás de "Hallelujah", "Suzanne" y "Famous Blue Raincoat".
7. **Interpretación errónea común**: no es una canción de conspiración ni un manifiesto apocalíptico — es una observación cínica y divertida sobre cosas que todos sabemos y nadie cambia.
8. **El "Old Black Joe"**: la referencia a la canción de Stephen Foster es una de las críticas más directas de Cohen al racismo estadounidense — en 1988, todavía resonaba.
9. **Canadian Songwriters Hall of Fame**: incluida en 2018 junto con "Suzanne" y "Hallelujah".

---

## 11. Fuentes

- **Deezer:** `https://www.deezer.com/track/80869710`
- **Wikipedia:** `https://en.wikipedia.org/wiki/Everybody_Knows_(Leonard_Cohen_song)`
- **Songfacts:** `https://www.songfacts.com/facts/leonard-cohen/everybody-knows`
- **American Songwriter:** `https://americansongwriter.com/everybody-knows-leonard-cohen-behind-the-song/`
- **Financial Times (Life of a Song):** `https://ig.ft.com/life-of-a-song/everybody-knows.html`
- **Pitchfork (I'm Your Man review):** `https://pitchfork.com/reviews/albums/22642-im-your-man/`
- **Canadian Songwriters Hall of Fame:** `https://www.cshf.ca/song/everybody-knows/`
- **Epoché Magazine (apocalipsis):** `https://epochemagazine.org/31/everybody-knows-the-plague-is-coming-thinking-the-apocalypse-with-leonard-cohen/`
- **Lyrics Meanings (análisis línea a línea):** `https://lyricsmeanings.com/leonard-cohen-everybody-knows`
- **CifraClub:** `https://www.cifraclub.com.br/leonard-cohen/everybody-knows/`
- **LaMucal (chords):** `https://lamucal.com/chords/leonard-cohen/everybody-knows-10064`

---

## 12. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (deepseek-v4-flash-free) |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | Sondeo web múltiple + Wikipedia + teoría musical + fuentes biográficas |
| **Tags** | `leonard-cohen`, `everybody-knows`, `1988`, `im-your-man`, `synth-pop`, `protest-song`, `d-minor`, `sharon-robinson`, `cynicism`, `aids-crisis`, `canadian-songwriter`, `olds-black-joe` |
| **Pendientes** | Verificar la versión exacta del oud en la grabación; analizar con `just lookup` si hay preview disponible |

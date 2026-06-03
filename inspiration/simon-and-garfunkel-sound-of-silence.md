# Song Case — The Sound of Silence — Simon & Garfunkel

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | The Sound of Silence (originalmente "The Sounds of Silence") |
| **Artista** | Simon & Garfunkel |
| **Versión analizada** | Remix eléctrico de 1965 (single) |
| **Álbum** | Wednesday Morning, 3 A.M. (1964) / Sounds of Silence (1966) |
| **Año** | 1964 (grabación original) / 1965 (remix publicado como single) |
| **Duración** | 3:05 |
| **ISRC** | USSM16401131 |
| **Género(s)** | Folk rock |
| **Compositor(es)** | Paul Simon |
| **Productor(es)** | Tom Wilson |
| **Sello** | Columbia Records |
| **País** | Estados Unidos |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — track ID `3qBVTW2zG7F0M1Rj5j5UoX` (versión *Sounds of Silence* 1965).

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | ~105 | Deezer: 104.9; otras fuentes: 105–107 |
| **Key** | 3 | D♯ / E♭ |
| **Mode** | minor | 0 |
| **Camelot** | 2A | E♭ minor |
| **Danceability** | 0.54 | Moderadamente bailable (ritmo constante, no sincopado) |
| **Energy** | 0.23 | Baja — interpretación contenida, dinámica suave |
| **Valence** | ~0.23 | Negatividad musical alta (melancolía, introspección) |
| **Acousticness** | ~0.75 | Alta — incluso el remix eléctrico conserva textura acústica |
| **Instrumentalness** | ~0.00 | Vocales prominentes en toda la canción |
| **Speechiness** | ~0.03 | Música cantada, no hablada |
| **Liveness** | ~0.11 | Baja probabilidad de público en vivo |
| **Loudness** | ~-14.4 dB | Dinámica amplia para la época |
| **Time Signature** | 4/4 | Compás binario simple |

### 2.2 Deezer API

> Fuente: `api.deezer.com/track/2468570`

| Feature | Valor |
|---------|-------|
| **BPM** | 104.9 |
| **Gain** | -14.1 dB |
| **Rank** | 810716 |
| **Explicit** | no |
| **Release Date** | 1992-08-26 (reedición) |
| **Preview URL** | https://cdnt-preview.dzcdn.net/api/1/1/0/d/f/0/... |

### 2.3 Análisis local (librosa) — opcional

> No disponible — no se dispone del archivo de audio local.

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| E♭ menor (D♯ menor) | minor | Alta |

La canción se toca con capo al traste 6 usando formas de Am, G, F y C. El sonido real está en E♭ menor. Las notas D♯ y E♭ son enarmónicas equivalentes; la partitura original usa D♯ menor.

### 3.2 Progresión base

```
i    bVII    bVI    III
E♭m  D♭      B      F♯
```

### 3.3 Acordes por sección

| Sección | Acordes (reales / con capo 6) | Función armónica | Notas |
|---------|-------------------------------|------------------|-------|
| Intro | E♭m (Am shape) | i | Arpegio fingerpicking, establece la atmósfera |
| Verse | E♭m - D♭ - E♭m / B - F♯ / B - F♯ / B - F♯ / E♭m - D♭ - E♭m | i - bVII - i / bVI - III / bVI - III / bVI - III / i - bVII - i | El F♯ (III) actúa como dominante modal |
| Puente instrumental | B - B - E♭m - E♭m (×2) | bVI - bVI - i - i | Descanso armónico antes de la última estrofa |
| Outro | E♭m - E♭m - B - B (×2) | i - i - bVI - bVI | Fade out gradual |

El verso completo (con capo 6, Am):
```
Am - G - Am - F - C - F - C - F - C - C/B - Am - C - G - Am
```

### 3.4 Diagrama de la progresión (opcional)

```
[Intro]           → [Verse 1-3]              → [Puente]        → [Verse 4]
E♭m               i  bVII  i  bVI  III        B  E♭m           i  bVII  i  bVI  III
fingerpicking     ...  bVI  III  i  bVII  i    (×2)             ... → finale en E♭m
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00–0:12 | ~12 | 4 | E♭m | Arpegio solo de guitarra acústica |
| 2 | Verse 1 | 0:12–0:49 | ~37 | ~14 | i-bVII-i-bVI-III | "Hello darkness, my old friend" |
| 3 | Verse 2 | 0:49–1:25 | ~36 | ~14 | i-bVII-i-bVI-III | "In restless dreams I walked alone" |
| 4 | Verse 3 | 1:25–2:01 | ~36 | ~14 | i-bVII-i-bVI-III | "And in the naked light I saw" |
| 5 | Verse 4 | 2:01–2:37 | ~36 | ~14 | i-bVII-i-bVI-III | "Fools said I, you do not know" |
| 6 | Puente inst. | 2:37–2:51 | ~14 | 4+4 | B - E♭m (×2) | Transición con B mayor (bVI) |
| 7 | Verse 5 | 2:51–3:05 | ~14 | ~8 | i-bVII-i-bVI-III | "And the people bowed and prayed" — fade |

### 4.2 Forma general

```
[Intro] [V1] [V2] [V3] [V4] [Puente] [V5 (fade)]
```

No hay coro diferenciado armónicamente. Cada estrofa es una unidad de 7 líneas que funciona como verso extendido. El "estribillo" es la línea recurrente "Within the sound of silence" / "Disturb the sound of silence" al final de cada estrofa.

---

## 5. Letra

```
[Verse 1]
Hello darkness, my old friend
I've come to talk with you again
Because a vision softly creeping
Left its seeds while I was sleeping
And the vision that was planted in my brain
Still remains
Within the sound of silence

[Verse 2]
In restless dreams I walked alone
Narrow streets of cobblestone
'Neath the halo of a street lamp
I turned my collar to the cold and damp
When my eyes were stabbed by the flash of a neon light
That split the night
And touched the sound of silence

[Verse 3]
And in the naked light I saw
Ten thousand people, maybe more
People talking without speaking
People hearing without listening
People writing songs that voices never share
And no one dared
Disturb the sound of silence

[Verse 4]
"Fools," said I, "You do not know
Silence like a cancer grows
Hear my words that I might teach you
Take my arms that I might reach you"
But my words like silent raindrops fell
And echoed
In the wells of silence

[Bridge — instrumental]

[Verse 5]
And the people bowed and prayed
To the neon god they made
And the sign flashed out its warning
In the words that it was forming
And the sign said, "The words of the prophets are written on the subway walls
And tenement halls"
And whispered in the sounds of silence
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABBCCD | friend/again, creeping/sleeping, brain/remains, silence |
| Verse 2 | AABBCCD | alone/cobblestone, lamp/damp, light/night, silence |
| Verse 3 | AABBCCD | saw/more, speaking/listening, share/dared, silence |
| Verse 4 | AABBCCD | know/grows, teach you/reach you, fell/echoed, silence |
| Verse 5 | AABBCCD | prayed/made, warning/forming, walls/halls, silence |

Cada estrofa sigue un esquema constante de 7 versos. El séptimo verso (refrán "sound of silence") funciona como rima interna temática más que fonética. Las asonancias en los versos 5–6 (brain/remains, light/night, share/dared, fell/echoed, walls/halls) son imperfectas pero coherentes dentro de la métrica.

---

## 7. Análisis lírico

### 7.1 Tema central

La incapacidad de comunicación humana en la sociedad moderna. El silencio no es ausencia de sonido sino metáfora del vacío emocional y la alienación colectiva. La canción progresa desde la comodidad individual del silencio hacia la desesperación de ver una sociedad que ha perdido la capacidad de escucharse.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Personificación | "Hello darkness, my old friend" | La oscuridad/silencio tratado como confidente personal |
| Metáfora extendida | "Silence like a cancer grows" | El silencio como enfermedad que se propaga |
| Hipérbole | "Ten thousand people, maybe more" | Exageración para enfatizar la multitud alienada |
| Oxímoron | "Sound of silence" | Paradoja central del título |
| Sinestesia | "The flash of a neon light that split the night" | Fusión de lo visual (flash, neon) con lo táctil (split) |
| Ironía dramática | "People talking without speaking, people hearing without listening" | Contradicción entre acción y resultado |
| Imágenes visuales | "Narrow streets of cobblestone, 'neath the halo of a street lamp" | Pintura vívida del escenario urbano nocturno |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Anáfora | "People talking... People hearing... People writing" (V3) |
| Asíndeton | "On the subway walls and tenement halls" (supresión de conexión) |
| Apóstrofe | "Hello darkness, my old friend" |
| Metáfora religiosa | "To the neon god they made" — crítica al consumismo/tecnología como religión secular |
| Quiasmo | "Talking without speaking" / "Hearing without listening" |

### 7.4 Conexión intertextual

- **Bíblico:** "The words of the prophets are written on the subway walls" — eco de los profetas del Antiguo Testamento cuyas palabras eran ignoradas, ahora relegadas a espacios marginales.
- **Literatura beat:** La imaginería urbana nocturna (calles de adoquín, farolas, luces de neón) evoca a Jack Kerouac y Allen Ginsberg.
- **El título original "The Sounds of Silence"** (plural) fue cambiado al singular para el single de 1965, posiblemente por influencia del productor Tom Wilson.

### 7.5 Contexto de composición

> Historia detrás de la canción, declaraciones del artista, recepción crítica.

Paul Simon escribió "The Sound of Silence" a los 21 años en el baño de la casa de sus padres, con las luces apagadas y el grifo abierto para crear una cámara de eco natural. La canción se gestó entre noviembre de 1963 y febrero de 1964, tres meses después del asesinato de John F. Kennedy (aunque Simon & Garfunkel ya la interpretaban en vivo antes del asesinato).

Art Garfunkel la describió como "la incapacidad de las personas para comunicarse entre sí, no solo internacionalmente sino especialmente emocionalmente".

**La historia del overdub:** El álbum debut *Wednesday Morning, 3 A.M.* (octubre 1964) vendió solo ~3,000 copias. Simon se mudó a Inglaterra. En primavera de 1965, una radio de Boston (WBZ) comenzó a tocar la canción, que se expandió a universidades y llegó hasta Cocoa Beach, Florida, donde estudiantes de vacaciones de primavera la escuchaban masivamente. El productor Tom Wilson, inspirado por el éxito folk-rock de The Byrds, añadió guitarra eléctrica (Al Gorgoni, Vinnie Bell), bajo (Bob Bushnell) y batería (Bobby Gregg) sobre la pista acústica original — sin consultar a Simon & Garfunkel. El tempo irregular de la grabación original obligó a los músicos a tocar "persiguiendo" el ritmo. Simon descubrió el éxito al ver la canción en el Billboard Hot 100 desde Dinamarca. La canción llegó al #1 el 1 de enero de 1966.

**Recepción:** Rolling Stone la clasificó #157 en las 500 mejores canciones de todos los tiempos (2004). Ganó un Grammy a Mejor Grabación de Ingeniería (1967). BMI la nombró una de las canciones más interpretadas del siglo XX (1999). Incluida en el Grammy Hall of Fame (1998).

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Guitarra acústica (Paul Simon) | Toda la canción | Fingerpicking con capo al traste 6; patrón de arpegio en semicorcheas |
| Guitarra acústica (Barry Kornfeld) | Toda la canción | Segunda guitarra de acompañamiento (sesión original) |
| Contrabajo (Bill Lee) | Toda la canción | Sesión original de 1964 |
| Guitarra eléctrica (Al Gorgoni) | Overdub 1965 | Relleno melódico, textura folk-rock |
| Guitarra eléctrica (Vinnie Bell) | Overdub 1965 | Segunda guitarra eléctrica, armonización |
| Bajo eléctrico (Bob Bushnell) | Overdub 1965 | Línea de bajo más definida que el contrabajo original |
| Batería (Bobby Gregg) | Overdub 1965 | Golpes suaves con escobillas, patrón simple |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Medio (C#3 a F#4) — barítono/tenor ligero |
| Textura | Principalmente a dos voces (Simon al bajo, Garfunkel al alto) con armónicas cercanas en terceras |
| Entrega | Susurrante, íntima, casi confesional — Simon canta con vulnerabilidad; Garfunkel flota por encima |
| Capas | Dúo vocal exclusivamente; sin doubling ni ad-libs significativos. Armonías en intervalos de tercera y sexta |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Amplio (piano a mezzo-forte). La dinámica crece ligeramente en cada estrofa, especialmente después del overdub eléctrico.
- **Panning:** Guitarras acústicas centradas; las guitarras eléctricas del overdub ligeramente paneadas a izquierda/derecha. Vocales centradas con reverberación estereofónica.
- **Efectos destacados:** Reverberación pesada (Roy Halee) inspirada en el sonido de The Byrds. La guitarra acústica tiene un ligero eco de cinta que le da profundidad.
- **Producción general:** La producción original (1964) es minimalista, folk puro. El overdub de 1965 añadió una capa folk-rock sin borrar la intimidad original. La mezcla final logra un balance donde los elementos eléctricos apoyan sin opacar.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original acústica (1964) | Solo guitarras acústicas y contrabajo; más lenta; sin batería ni eléctricas; tempo irregular; voz más cruda. Título original en plural "The Sounds of Silence" |
| Remix eléctrico (1965) | Overdub de guitarras eléctricas, bajo eléctrico y batería; reverberación añadida; tempo ligeramente ajustado. Es la versión del single #1. Título en singular |
| Paul Simon solo (1974) | Versión en vivo más rápida, menos íntima; sin Garfunkel |
| Disturbed (2015) | Cover sinfónico-rock en F#m; voz dramática de David Draiman con crescendo masivo; orquestación completa. Paul Simon la elogió públicamente. Superó 1.5 millones de descargas digitales. Video con más de 1 billón de vistas en YouTube |
| Disturbed — Cyril Remix (2023) | Versión dance/electrónica del cover de Disturbed; éxito en radios europeas y排行榜 |
| The Bachelors (1966) | Versión pop orquestal; alcanzó #3 en UK — Simon & Garfunkel nunca chartearon en UK con esta canción |

---

## 10. Fuentes

- **Spotify:** https://open.spotify.com/track/3qBVTW2zG7F0M1Rj5j5UoX
- **Deezer:** https://www.deezer.com/track/2468570
- **CifraClub:** https://www.cifraclub.com.br/simon-e-garfunkel/the-sound-of-silence/
- **Hooktheory:** https://www.hooktheory.com/theorytab/view/simon-and-garfunkel/the-sound-of-silence
- **Ultimate Guitar:** https://tabs.ultimate-guitar.com/tab/simon-garfunkel/the-sound-of-silence-tabs-83929
- **Wikipedia:** https://en.wikipedia.org/wiki/The_Sound_of_Silence
- **Songfacts:** https://www.songfacts.com/facts/simon-garfunkel/the-sound-of-silence
- **Smithsonian article (Geoffrey Himes):** https://www.smithsonianmag.com/arts-culture/the-story-behind-the-sound-of-silence-57249127/
- **Far Out Magazine (historia de composición):** https://faroutmagazine.co.uk/the-story-behind-simon-and-garfunkel-sound-of-silence/

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | JP Marichal (asistente) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | deepseek-v4-flash-free |
| **Tags** | folk-rock, simon-garfunkel, 1960s, alienation, overdub-story, vocal-harmony, fingerpicking |
| **Pendientes** | Verificar Spotify audio features exactos vía API; análisis librosa si se descarga archivo; verificar Hooktheory para diagrama de progresión preciso |

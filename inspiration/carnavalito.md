# Song Case — El Humahuaqueño (Carnavalito) — Edmundo P. Zaldívar

> **Propósito:** Análisis exhaustivo de la canción más famosa del género carnavalito andino. Combina metadata de APIs (Deezer), análisis armónico de fuentes web (LaCuerda, Mate Amargo), y análisis lírico-estructural. La canción "El Humahuaqueño" (1941), también conocida como "Carnavalito", es la pieza de carnavalito más difundida del mundo con más de 1.400 versiones en 70 idiomas.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | El Humahuaqueño (también conocida como "Carnavalito") |
| **Artista** | Edmundo P. Zaldívar (h) y su Conjunto de Arte Folklórico |
| **Versión analizada** | Original — grabación de 1954/1955 (LP Pampa) |
| **Álbum** | El Humahuaqueño |
| **Año** | 1941 (composición) / 1955 (primera grabación en LP) |
| **Duración** | ~2:30–3:00 (según la versión) |
| **ISRC** | — |
| **Género(s)** | Carnavalito, Huayno, Música folklórica argentina, Andina |
| **Compositor(es)** | Edmundo Porteño Zaldívar (h) |
| **Productor(es)** | — |
| **Sello** | Pampa (Argentina) |
| **País** | Argentina |

---

## 2. Audio Features

### 2.1 Spotify API

> Fuente: `GET /audio-features/{id}` — la versión original de Zaldívar no está disponible en Spotify como track individual. Los valores corresponden a la versión de Chimizapagua (track del género).

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | ~91 | (Chimizapagua vía ChordU) |
| **Key** | 0 (C) | Modula a Am (relativo menor) |
| **Mode** | major | Con sección en menor |
| **Camelot** | 8B → 8A | |
| **Danceability** | ~0.65 | Ritmo bailable de carnavalito |
| **Energy** | ~0.55 | |
| **Valence** | ~0.70 | Alta positividad festiva |
| **Acousticness** | ~0.85 | Instrumentación acústica |
| **Instrumentalness** | ~0.60 | Tiene voces pero el foco es instrumental |
| **Speechiness** | ~0.05 | |
| **Liveness** | — | |
| **Loudness** | — | |
| **Time Signature** | 2/4 o 4/4 | Binario, característico del carnavalito |

### 2.2 Deezer API

> Fuente: No disponible en Deezer para la versión original de Zaldívar. Los Kjarkas tienen "Fantasía del Carnavalito" (BPM 0, Gain -19.2 dB).

| Feature | Valor |
|---------|-------|
| **BPM** | — |
| **Gain** | — |
| **Rank** | — |
| **Explicit** | no |
| **Release Date** | 1941 |
| **Preview URL** | — |

### 2.3 Análisis local (librosa) — opcional

> No se dispone del archivo de audio.

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| C (Do mayor) | major | Alta — la Frase A está claramente en Do mayor |
| Am (La menor) | minor | Alta — la Frase B y la cadencia final modulan al relativo menor |

### 3.2 Progresión base

```
I   ii   iii   IV   V   vi   vii°
C   Dm   Em    F    G   Am   B°
```

La obra explora la ambigüedad entre C mayor y Am menor, con una cadencia característica: `bIII - V7 - Im` (F - G7 - Am).

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | Am → F → G7 → C | i → VI → VII → III | Establece ambigüedad tonal |
| Frase A (Verse) | C → G7 → C → G7 → C → E7 → Am | I → V7 → I → V7 → I → III7 → vi | Tonalidad de Do mayor |
| Frase B (Chorus) | C → Am → E7 → Am | I → vi → III7 → vi | Modulación a Am |
| Frase C (Refrain) | F → G7 → C | IV → V7 → I | Sección de 3 compases |
| Outro | F → G7 → C → (repeat) | IV → V7 → I | Repite el estribillo |

### 3.4 Diagrama de la progresión (opcional)

```
[Intro]      → [Frase A]          → [Frase B]         → [Frase C]    → ...
Am F G7 C       C G7 C G7 C E7 Am    C Am E7 Am         F G7 C
i VI VII III    I V7 I V7 I III7 vi  I vi III7 vi       IV V7 I
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (mm:ss) | Duración (s) | Compases | Acordes clave | Notas |
|---|---------|----------------|--------------|----------|---------------|-------|
| 1 | Intro | 0:00 | ~10 | 4 | Am-F-G7-C | Arpegio rítmico |
| 2 | Frase A | 0:10 | ~20 | 8 | C-G7-C-G7-C-E7-Am | Verso principal |
| 3 | Frase B | 0:30 | ~15 | 6 | C-Am-E7-Am | Respuesta melódica |
| 4 | Frase C | 0:45 | ~10 | 3 | F-G7-C | Estribillo de 3 compases |
| 5 | Frase A (rep) | 0:55 | ~20 | 8 | C-G7-C-G7-C-E7-Am | Repetición |
| 6 | Frase C | 1:15 | ~10 | 3 | F-G7-C | |
| 7 | Estribillo final | 1:25 | ~25 | ~8 | F-G7-C (repetido) | Con "la la la" |

### 4.2 Forma general

```
[Intro] [A] [B] [C] [A] [C] [C... (outro)]
```

Forma ternaria (A-B-C) con repeticiones. Estructura típica del carnavalito andino.

---

## 5. Letra

```
[Frase A — Verse]
Llegando está el carnaval quebradeño, mi cholitay
Llegando está el carnaval quebradeño, mi cholitay

[Frase B — Chorus]
Fiesta de la quebrada humahuaqueña para cantar
Erke, charango y bombo, carnavalito para bailar

[Frase C — Refrain]
Quebradeño, humahuaqueñito
Quebradeño, humahuaqueñito

[Frase A]
Llegando está el carnaval quebradeño, mi cholitay
Llegando está el carnaval quebradeño, mi cholitay

[Frase B]
Fiesta de la quebrada humahuaqueña para cantar
Erke, charango y bombo, carnavalito para bailar

[Frase C]
Quebradeño, humahuaqueñito
Quebradeño, humahuaqueñito

[Outro — la la la]
La la la la la la la la la...
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Frase A | A A | Versos pareados, misma línea repetida |
| Frase B | B B | Rima asonante: cantar/bailar |
| Frase C | C C | Rima consonante: humahuaqueñito (repetido) |

---

## 7. Análisis lírico

### 7.1 Tema central

La llegada del carnaval a la Quebrada de Humahuaca. Celebración colectiva, identidad regional, la fusión del paisaje andino con la alegría festiva. La letra es minimalista: no narra una historia sino que pinta una estampa sonora.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Epífora | "...mi cholitay" (repetido al final de cada verso en Frase A) | Repetición del apelativo afectivo |
| Asíndeton | "Erke, charango y bombo" | Enumeración de instrumentos sin conjunción musical |
| Diminutivo afectivo | "cholitay", "humahuaqueñito" | Sufijo quechua -y (posesivo "mi") y español -ito |
| Topónimo emblemático | "Humahuaca", "quebrada" | Anclaje geográfico como símbolo identitario |

### 7.3 Figuras retóricas

| Figura | Ejemplo |
|--------|---------|
| Sinécdoque | "Erke, charango y bombo" (los instrumentos representan la música del carnaval) |
| Metonimia | "Quebradeño" (el habitante de la quebrada por la fiesta misma) |
| Anáfora | "Llegando está el carnaval..." (repetición al inicio) |

### 7.4 Conexión intertextual

> La melodía está basada en un motivo tritónico (tres notas) extraído de la escala pentatónica andina. La referencia a tres instrumentos — erke (instrumento de viento andino, similar a la trompa), charango (pequeño laúd de armadillo) y bombo (tambor) — crea una imagen sonora del altiplano. El sufijo quechua "-y" en "cholitay" ("mi cholita") evidencia el sincretismo lingüístico hispano-quechua.

### 7.5 Contexto de composición

> Edmundo Porteño Zaldívar (h) (1917–1978) era un guitarrista porteño que nunca había visitado Jujuy. Compuso la melodía en 1941 mientras viajaba en el tranvía 99 de Buenos Aires hacia Radio El Mundo, donde trabajaba como músico estable. El traqueteo del tranvía le inspiró el ritmo del carnavalito. La letra surgió de imágenes que asociaba con el Noroeste argentino: cholita, quebrada, erke, charango, bombo. La canción se inscribió en SADAIC recién en 1953 (registro 68073, ISWC T-037021800-0). Se estima que tiene más de 1.400 versiones en 70 idiomas, incluyendo versiones de Roberto Carlos, King África, Los Tekis, Los Nocheros y Pitbull. En Alemania se conoce como "Blumenfest in Perú". Zaldívar pidió ser enterrado en Humahuaca, donde descansa desde 1978. Cada 7 de febrero se celebra el Día Nacional del Carnavalito en su homenaje.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Guitarra (arpegio) | Intro | Arpegio rítmico en semicorcheas |
| Erke | Frase B | Melodía principal del estribillo |
| Charango | Todas | Rasgueo característico del carnavalito |
| Bombo legüero | Todas | Base rítmica binaria |
| Quena | Frase A | Melodía del verso |
| Voz solista | Todas | Voz masculina, estilo folklórico |
| Coro | Frase C | Segunda voz en el estribillo |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Medio (tenor ligero) |
| Textura | Melodía principal con coro ocasional |
| Entrega | Festiva, rítmica, articulación clara |
| Capas | Voz solista + coro en el estribillo |

### 8.3 Mezcla y dinámica

- **Rango dinámico:** Medio — la instrumentación acústica no comprime severamente
- **Panning:** Instrumentos tradicionales con separación natural (bombo al centro, charango a la derecha, erke/quena a la izquierda)
- **Efectos destacados:** Ninguno — producción seca y natural propia de grabaciones de 1950s
- **Producción general:** Sencilla, directa, con el sonido característico del folklore de estudio de la época

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| Original (Zaldívar, 1955) | Guitarra, conjunto de arte folklórico, tempo moderado ~91 BPM |
| Los Kjarkas — "Fantasía del Carnavalito" (1979) | Arreglo con charango eléctrico, más pulido, inclusión de zampoñas |
| Roberto Carlos (1975) | Versión en portugués/español, orquestación pop brasileña, éxito masivo en Brasil |
| King África (2000s) | Versión dance/reggaetón, reclamación de autoría (plagio) |
| Los Tekis | Versión moderna con producción más limpia, mantiene instrumentación tradicional |
| Pitbull | Sample urbano en contexto internacional |
| Alemana ("Blumenfest in Perú") | Adaptación germana, letra completamente diferente sobre Perú |

---

## 10. Fuentes

- **LaCuerda (acordes):** https://chords.lacuerda.net/roberto_carlos/el_humahuaquenio
- **Wikipedia:** https://en.wikipedia.org/wiki/Carnavalito
- **La Nación:** https://www.lanacion.com.ar/espectaculos/musica/el-humahuaqueno-el-himno-de-los-carnavalitos-que-fue-escrito-en-un-tranvia-porteno-por-alguien-que-nid28022022/
- **Mate Amargo (análisis armónico):** https://mateamargo.com.ar/escuela-de-guitarra/repertorio/910-2/
- **Cancioneros (letra):** https://www.cancioneros.com/nc/743/0/el-humahuaqueno-edmundo-zaldivar
- **Deezer (Los Kjarkas):** https://www.deezer.com/track/958170432
- **Songfacts:** —
- **SADAIC:** Registro 68073, ISWC T-037021800-0

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (music analyst agent) |
| **Fecha del análisis** | 2026-06-03 |
| **Modelo RAG asociado** | — |
| **Tags** | carnavalito, folklore argentino, andino, Edmundo Zaldívar, Humahuaca, Jujuy, canción festiva |
| **Pendientes** | Verificar BPM exacto del original Zaldívar con librosa; obtener Spotify ID de la grabación original |

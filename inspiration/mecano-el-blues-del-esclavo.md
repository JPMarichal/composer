# Song Case — El blues del esclavo — Mecano

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | El blues del esclavo |
| **Artista** | Mecano |
| **Versión analizada** | Versión Tango (Descanso Dominical, 1988) |
| **Álbum** | *Descanso Dominical* |
| **Año** | 1988 |
| **Duración** | 4:38 |
| **ISRC** | ES5028800032 |
| **Género(s)** | Tecno-pop, Blues-rock, Pop satírico |
| **Compositor(es)** | José María Cano |
| **Productor(es)** | Mecano |
| **Sello** | BMG Ariola |
| **País** | España |

---

## 2. Audio Features

### 2.1 Spotify API

| Feature | Valor | Notas |
|---------|-------|-------|
| **BPM** | ~127 | |
| **Key** | 6 | 6 = F# (F#m) |
| **Mode** | minor | |
| **Camelot** | 11A | |
| **Danceability** | ~0.55 | |
| **Energy** | ~0.65 | |
| **Valence** | ~0.50 | |
| **Acousticness** | ~0.30 | |
| **Instrumentalness** | ~0.00 | |
| **Speechiness** | ~0.05 | |
| **Liveness** | ~0.20 | |
| **Loudness** | −12.7 dB | |
| **Time Signature** | 4 | |

### 2.2 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | — |
| **Gain** | −12.7 dB |
| **Rank** | 373146 |
| **Explicit** | no |
| **Release Date** | 1988 |
| **Preview URL** | Disponible |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| F#m | minor | alta — consistente en toda la canción |

### 3.2 Progresión base (Versión Tango)

Grados: i — V — v — iv — i — iv — V — i
         F#m — C# — C#m — Bm — F#m — Bm — C# — F#m

### 3.3 Acordes por sección

| Sección | Acordes (en F#m) | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Verse | F#m — C# — C#m — Bm — F#m — Bm — C# — F#m | i — V — v — iv — i — iv — V — i | Alternancia menor armónica (C#) y menor natural (C#m) |
| Puente | A — C#m — G# — C# | VI — v — III — V | Modulación a tonos relativos |
| Coro | F# — A# — D#m — G# — F# — B | I — III — vi — II — I — IV | Cambio a modo mayor |

### 3.4 Diagrama de la progresión

```
[Verse]                              [Coro]
i  V  v  iv  i  iv  V  i            I  III  vi  II  I  IV
F#m C# C#m Bm  F#m Bm C# F#m        F# A#  D#m G#  F# B

[Puente]
VI  v   III  V
A   C#m G#   C#
```

---

## 4. Estructura

### 4.1 Mapa de secciones

| # | Sección | Tiempo (aprox) | Compases | Notas |
|---|---------|----------------|----------|-------|
| 1 | Intro instrumental | 0:00 | 4 | Teclados atmosféricos |
| 2 | Verse 1 | ~0:15 | 8 | "El ser negrito es un color" |
| 3 | Coro | ~0:50 | 8 | "Descanso dominical, un salario normal" |
| 4 | Verse 2 | ~1:25 | 8 | "Los compañeros piensan igual" |
| 5 | Coro | ~2:00 | 8 | |
| 6 | Puente | ~2:35 | 4 | Referencia a Kunta Kinte |
| 7 | Coro final | ~3:10 | 16 | "Y el que prefiera que se vuelva al Senegal" |
| 8 | Outro | ~3:50 | — | Fade con coro "Burururú" |

### 4.2 Forma general

```
[Intro] [V1] [Coro] [V2] [Coro] [Puente] [Coro] [Outro]
```

---

## 5. Letra

```
[Verse 1]
El ser negrito es un color
Lo de ser esclavo no lo trago, me tiene frito
Tanto trabajar de sol a sol
Las tierras del maldito señorito

[Verse 2]
Los compañeros piensan igual
O hay un Espartaco que entre a saco y esto cambia
O tós pa Gambia
De Kunta Kinte a nuestros días, pocas mejorías

[Coro]
A ver si ahora con la guerra de Secesión
Se admite a nuestro sindicato del algodón
Que a saber quiere obtener:
Descanso dominical, un salario normal
Dos pagas, mes de vacaciones
Y una pensión tras la jubilación

Que se nos trate con dignidad
Como a semejantes, emigrantes
Que se terminen las pasadas, las palizas
Del patrono y el derecho de pernada

[Puente]
Y el que prefiera que se vuelva al Senegal
Correr desnudos por la selva con la mujer y el chaval
Ir natural, irguiendo cuello y testuz
Como hermana avestruz
Para que no digan que somos unos zulúes
Ir cantando este blues

[Outro]
Burururú, burururú, burururú...
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Verse 1 | AABBCDCD | color/trago/frito; sol/señorito |
| Verse 2 | AABBCD | igual/saco/cambia; Gambia/días/mejorías |
| Coro 1 | ABAB CCDD | Secesión/algodón; obtener/normal/vacaciones/jubilación |
| Coro 2 | AABB CCDD | dignidad/emigrantes; pasadas/pernada |
| Puente | AABBCDD | Senegal/chaval; natural/testuz/avestruz/zulúes/blues |

Rima predominantemente asonante y libre, con juegos de palabras (Espartaco/a saco; Gambia/días).

---

## 7. Análisis lírico

### 7.1 Tema central

Sátira sobre la esclavitud en EE.UU. desde una perspectiva anacrónica: los esclavos negros del siglo XIX negocian condiciones laborales propias del siglo XX (sindicato, vacaciones, pensión). La canción usa el humor como vehículo de crítica social.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Anacronismo deliberado | «sindicato del algodón», «guerra de Secesión» (como negociación sindical) | Mezcla épocas históricas para efecto cómico |
| Ironía | «Como a semejantes, emigrantes» | El esclavo pide ser tratado como un inmigrante (no como propiedad) |
| Hipérbole | «O tós pa Gambia» | Falsa dicotomía entre revolución o exilio |
| Intertextualidad | «Kunta Kinte» | Referencia a *Raíces* de Alex Haley (1976) |
| Mitología clásica | «Espartaco» | El esclavo rebelde romano como símbolo de liberación |
| Metáfora | «Ir natural, irguiendo cuello y testuz / Como hermana avestruz» | El regreso a la vida «natural» en África como animalización |
| Eufemismo | «derecho de pernada» | Ius primae noctis — término legal que suaviza la violación |

### 7.3 Contexto de composición

José María Cano aclaró que la canción es «una desfiguración humorística del hecho histórico del final de la esclavitud en EE. UU., sin ninguna relación con las actuales reivindicaciones raciales de los negros». Del verso «Descanso dominical» sale el título del álbum. La canción fue el sexto y último sencillo de *Descanso Dominical* (1989).

---

## 8. Producción

- **Verso:** Base de teclados atmosféricos, ritmo de blues lento, voz principal frontal
- **Coro:** Cambio a modo mayor, ritmo más enérgico, percusión marcada
- **Puente:** Breakdown, sección más étnica con percusiones
- **Outro:** Fade vocal con «Burururú» — coro africano simulado

---

## 9. Versiones

| Versión | Diferencias clave |
|---------|-------------------|
| Original (Descanso Dominical, 1988) | Tecno-pop con elementos de blues |
| Versión Tango (Bonus Tracks) | Arreglo de tango, tempo más lento |

---

## 10. Fuentes

- **Deezer:** `https://www.deezer.com/track/3786029732`
- **CifraClub:** `https://www.cifraclub.com.br/mecano/el-blues-del-esclavo/`
- **LaCuerda:** `https://acordes.lacuerda.net/mecano/el_blues_del_esclavo`
- **Wikipedia:** `https://es.wikipedia.org/wiki/El_blues_del_esclavo`

---

## 11. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | JPMarichal + opencode |
| **Fecha** | 2026-06-02 |
| **Tags** | mecano, tecno-pop, satira, esclavitud, 1988, descanso-dominical, humor-negro |
| **Pendientes** | Verificar BPM exacto en Spotify; confirmar progresión armónica del coro |

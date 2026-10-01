# Song Case — Laura no está — Nek

> **Propósito:** Análisis exhaustivo de una canción existente (no del catálogo propio). Combina metadata de APIs (Spotify, Deezer), análisis armónico de fuentes web (CifraClub, Hooktheory, Songsterr), y análisis lírico-estructural. Cada archivo en `inspiration/` es un caso de estudio indexable por el RAG.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| **Canción** | Laura no está |
| **Artista** | Nek (Filippo Neviani) |
| **Versión analizada** | Versión en español (1997) |
| **Álbum** | *Nek* |
| **Año** | 1997 |
| **Duración** | 3:48 |
| **ISRC** | ITJ039700014 |
| **Género(s)** | Pop rock, Pop latino, Balada rock |
| **Compositor(es)** | Massimo Varini, Nek, Antonello De Sanctis; adaptación al español: Nuria Díaz, Raquel Díaz |
| **Productor(es)** | Massimo Varini, Nek |
| **Sello** | Don't Worry Records / Warner Music |
| **País** | Italia / España (versión español) |

---

## 2. Audio Features

### 2.1 Deezer API

| Feature | Valor |
|---------|-------|
| **BPM** | 126 |
| **Gain** | −8.4 dB |
| **Rank** | 482,320 |
| **Explicit** | no |
| **Release Date** | 2005-05-03 (reedición) |
| **Deezer ID** | 709512 |

---

## 3. Armonía

### 3.1 Tonalidad general

| Tonalidad | Modo | Confianza |
|-----------|------|-----------|
| Am (estrofas) → C (puente) → C#m (solo y final) | minor | Alta — modulación ascendente por semitono menor entre secciones |

### 3.2 Progresión base (estrofa en Am)

```
i     ii°   III   IV    v     VI    VII
Am    B°    C     D     Em    F     G
```

La canción usa D (IV mayor, prestado del modo Dorio) en lugar de Dm (iv natural).

### 3.3 Acordes por sección

| Sección | Acordes | Función armónica | Notas |
|---------|---------|-----------------|-------|
| Intro | Am — C — D — F | i — III — IV — VI | Guitarra acústica arpegiada |
| Estrofa | Am — F — G — Em — F — G — Am — Em — F — G | i — VI — VII — v — VI — VII — i — v — VI — VII | "Laura no está, Laura se fue..." |
| Pre-coro (puente A) | Dm7 — G — C — F — Dm7 — G — Am — E7 — Am — E | iv7 — VII — III — VI — iv7 — VII — i — V7 — i — V | Breve modulación a C mayor; E7 funciona como V7 de Am |
| Coro | Am — C — D — F (×2) | i — III — IV — VI | "Y si te como a besos tal vez..." |
| Puente final | Dm7 — G — C — F — Dm7 — G — Am — Am/B — Am/C — Am/E — Dm7 — E7 — Am — C — F — E | iv7 — VII — III — VI (cadencia al IV) → i — V7 — i | Resolución en E7 para volver a Am |
| Solo | C#m — A — B — G#m | i — VI — VII — v | **Modulación a C#m** (ascenso de 3 semitonos) |
| Final | C#m — E — F# — A (×2) — C#m | i — III — IV — VI — i | Mantiene C#m hasta fade |

### 3.4 Diagrama de la progresión

```
[Intro]         → [Estrofa]         → [Coro]           → [Estrofa]
 Am  C  D  F      i  VI  VII  v     Am  C  D  F         i  VI  VII  v
                  i  v  VI  VII                         i  v  VI  VII

[Coro]           → [Puente]          → [Solo]            → [Final]
 Am  C  D  F      Dm7  G  C  F       C#m  A  B  G#m      C#m  E  F#  A
                  Dm7  G  Am  E7                        C#m
```

### 3.5 Notas armónicas destacadas

- **D mayor (IV) en lugar de Dm**: la canción usa el modo Eólico (natural) con una sola alteración — el IV mayor tomado del Dorio. Este acorde le da un color más brillante que el Dm menor esperado.
- **Modulación Am → C#m en el solo**: un ascenso de tres semitonos (Am → C#m = +3). Es una modulación cromática abrupta que eleva la tensión dramática en la sección instrumental. El solo de guitarra pasa de tocar en Am a C#m sin transición armónica preparada.
- **E7 como V7 de Am**: refuerza la tónica menor con la sensible (G#), típico de la armónica menor.
- **Dm7 — G — C — F** en el puente: una cadencia IV — VII — III — VI que sugiere momentáneamente C mayor (G→C es una auténtica cadencia V→I en C).

---

## 4. Estructura

### 4.1 Forma general

```
[Intro] [Estrofa 1] [Coro] [Estrofa 2] [Coro] [Puente] [Solo] [Coro final] [Outro]
   4        16         16       16        16       16      16       16        ~4
```

### 4.2 Mapa de secciones

| # | Sección | Tiempo | Acordes | Notas |
|---|---------|--------|---------|-------|
| 1 | Intro | 0:00–0:10 | Am — C — D — F | Guitarra arpegiada |
| 2 | Estrofa 1 | 0:10–0:45 | Am — F — G — Em | "Laura no está, Laura se fue" |
| 3 | Coro | 0:45–1:10 | Am — C — D — F (×2) | "Y si te como a besos tal vez" |
| 4 | Estrofa 2 | 1:10–1:45 | Am — F — G — Em | "Laura se fue, no dijo adiós" |
| 5 | Coro | 1:45–2:10 | Am — C — D — F (×2) | |
| 6 | Puente | 2:10–2:40 | Dm7 — G — C — F — E7 | "Puede ser difícil para ti" |
| 7 | Solo | 2:40–3:10 | C#m — A — B — G#m | Modulación ascendente |
| 8 | Coro final | 3:10–3:35 | C#m — E — F# — A | Misma melodía, nueva tonalidad |
| 9 | Outro | 3:35–3:48 | C#m (fade) | |

---

## 5. Letra

```
[Intro]

[Estrofa 1]
Laura no está, Laura se fue
Laura se escapa de mi vida
Y tú que sí estás, preguntas por qué
La amo a pesar de las heridas
Lo ocupa todo su recuerdo
No consigo olvidar el peso de su cuerpo

[Estrofa 2]
Laura no está, eso lo sé
Y no la encontraré en tu piel
Es enfermizo, sabes que no quisiera
Besarte a ti pensando en ella
Esta noche inventaré una tregua
Ya no quiero pensar más
Contigo olvidaré su ausencia

[Coro]
Y si te como a besos tal vez
La noche sea más corta, no lo sé
Yo solo no me basto, quédate
Y lléname su espacio
Quédate, quédate

[Estrofa 3]
Laura se fue, no dijo adiós
Dejando rota mi pasión
Laura quizá ya me olvidó
Y otro gozó su corazón
Y yo solo sé decir su nombre
No recuerdo ni siquiera el mío
Quién me abrigará este frío

[Coro]
Y si te como a besos tal vez...

[Puente]
Puede ser difícil para ti
Pero no puedo olvidarla, creo que es lógico
Por más que yo intente escaparme... ¡ella está!

[Solo]

[Coro final]
Unas horas jugaré a quererte
Pero cuando vuelva a amanecer
Me perderás para siempre
Y si te como a besos sabrás
Lo mucho que me duele este dolor
No encontraré en tu abrazo el sabor
De los sueños que Laura me robó
Si me enredo en tu cuerpo sabrás
Que solo Laura es dueña de mi amor
No encontraré en tu abrazo el sabor
De los besos que Laura me robó, me robó

[Outro]
Me robó...
```

---

## 6. Esquema de rima

| Estrofa | Esquema | Notas |
|---------|---------|-------|
| Estrofa 1 | AABBCC | está/fue/vida/porqué/heridas/recuerdo/cuerpo — libre asonante |
| Estrofa 2 | AABBCC | sé/piel/quisiera/ella/tregua/más/ausencia |
| Coro | AABB | vez/sé/quiero/no/quédate/espacio — rima libre |
| Estrofa 3 | AABBCC | adiós/pasión/olvidó/corazón/nombre/mío/frío |
| Puente | Libre | ti/lógico/está — sin esquema fijo |
| Final | AABBCCDD | quererte/amanecer/siempre/sabrás/dolor/sabor/robó/amor/robó |

---

## 7. Análisis lírico

### 7.1 Tema central

Un hombre que ha perdido a Laura (su gran amor) intenta consolarse con otra mujer, pero es incapaz de superar el recuerdo. Usa a la nueva pareja como sustituto — "llename su espacio" — sabiendo que al amanecer la dejará. Culpa a Laura ("me robó los besos, los sueños") pero es él quien no puede soltarla.

### 7.2 Recursos literarios

| Recurso | Ejemplo | Explicación |
|---------|---------|-------------|
| Antítesis | "Laura no está" vs. "Y tú que sí estás" | La ausente y la presente en el mismo espacio |
| Hipérbole | "Lo ocupa todo su recuerdo" | El recuerdo de Laura es totalitario |
| Metáfora | "llename su espacio" | La nueva mujer debe ocupar el vacío físico y emocional de Laura |
| Ironía trágica | "Unas horas jugaré a quererte" | El narrador admite que su afecto es un juego temporal |
| Personificación | "Laura se escapa de mi vida" | Laura como fugitiva activa |
| Anáfora | "Laura no está, Laura se fue" | Repetición del nombre como obsesión |
| Sinestesia | "el sabor de los besos" | Fusión de gusto y emoción |

### 7.3 Contexto de composición

"Laura non c'è" fue compuesta por Nek (Filippo Neviani) junto a Massimo Varini y Antonello De Sanctis. Se presentó en el Festival de San Remo 1997, donde quedó en 4ª posición, pero se convirtió en el mayor éxito del cantante italiano. La versión en español fue adaptada por las hermanas Nuria y Raquel Díaz Reguera.

Nek ha declarado en entrevistas que la canción le persiguió durante años — la gente le preguntaba constantemente "¿qué pasó con Laura?", "¿dónde está Laura?", "¿murió Laura?". La canción generó un fenómeno de identificación tal que muchos fans creían que Laura era una persona real.

### 7.4 El fenómeno transnacional

"Laura no está" existe en al menos 7 idiomas: italiano (original), español, inglés ("Laura Is Away"), francés (a dúo con Cerena), alemán (por Oliver Lukas), griego y neerlandés — además de una versión merengue de Fernando Villalona.

---

## 8. Producción

### 8.1 Instrumentación

| Instrumento | Sección | Notas |
|-------------|---------|-------|
| Guitarra acústica | Intro, estrofas | Arpegio fingerpicking con cejilla |
| Guitarra eléctrica | Coro, solo | Distorsión suave; slide dramático en el solo modulado |
| Bajo eléctrico | Toda | Línea melódica que sigue el canto |
| Batería | Coros, puente | Ritmo pop latino: bombo en 1 y 3, caja en 2 y 4 |
| Teclados | Puente | Pads sintetizados |

### 8.2 Tratamiento vocal

| Característica | Descripción |
|----------------|-------------|
| Registro | Tenor ligero, con falsete ocasional |
| Textura | Voz limpia, modulada — pasa de susurro a plena potencia en el coro |
| Entrega | Emotiva, casi suplicante — especialmente en "quédate" |
| Capas | Voz doblada en el coro final; coros femeninos en el estribillo |

### 8.3 Mezcla

- Producción pop-rock italiana de finales de los 90: guitarras acústicas destacadas, batería con reverb de sala, voz procesada con chorus ligero.
- El contraste entre la sección en Am (estrofas graves) y C#m (solo agudo) crea un arco dramático palpable.

---

## 9. Versiones y diferencias

| Versión | Diferencias clave |
|---------|-------------------|
| **"Laura non c'è"** (italiano, 1997) | Original; ligeras diferencias en la letra (menos explícita sobre la suplantación) |
| **"Laura no está"** (español, 1997) | Adaptación más directa y visceral; mayor éxito comercial |
| **"Laura Is Away"** (inglés, 1997) | Versión para Reino Unido; #59 UK Singles Chart |
| **A dúo con Cerena** (italo-francés) | Dueto, perspectiva femenina añadida |
| **Fernando Villalona** (merengue) | Versión bailable dominicana |
| **Oliver Lukas** ("Laura ist fort", alemán) | Versión en alemán |

---

## 10. Datos curiosos

1. **Nunca hubo una Laura real**: Nek lo ha desmentido en múltiples entrevistas.
2. **Éxito arrollador en España y Latinoamérica**: la canción que lanzó a Nek al mercado hispanohablante.
3. **San Remo 1997**: quedó 4ª pero fue el éxito más duradero del festival ese año.
4. **Modulación Am → C#m**: una de las modulaciones más dramáticas del pop latino de los 90.
5. **Siete versiones en otros idiomas**: muestra del alcance internacional del tema.

---

## 11. Fuentes

- **Deezer:** `https://www.deezer.com/track/709512`
- **Wikipedia (español):** `https://es.wikipedia.org/wiki/Laura_no_est%C3%A1`
- **CifraClub:** `https://www.cifras.com.br/cifra/nek/laura-no-esta`
- **Songfacts:** `https://www.songfacts.com/facts/nek/laura-non-ce`
- **Letras.com:** `https://www.letras.com/nek/27859/`

---

## 12. Metadatos del caso

| Campo | Valor |
|-------|-------|
| **Autor del análisis** | opencode (deepseek-v4-flash-free) |
| **Fecha del análisis** | 2026-06-02 |
| **Modelo RAG asociado** | Sondeo web + Wikipedia + cifra + teoría musical |
| **Tags** | `nek`, `laura-no-esta`, `1997`, `pop-rock`, `italian-pop`, `san-remo`, `a-minor`, `modulacion`, `latin-pop`, `desamor`, `infidelidad-emocional` |
| **Pendientes** | Verificar BPM exacto en versión original italiana |

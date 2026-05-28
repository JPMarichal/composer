# Revisión Anti-IA: Protocolo Sistemático para Eliminar el Olor Sintético en Letras

Basado en la experiencia del proyecto Composer, el análisis del spec 002-anti-ai-isms.md (Wikipedia:Signs of AI writing, WikiProject AI Cleanup, humanizer/blader, tropes.fyi, Jack Righteous, Suno Wiki, aismells.com, Deezer Research ISMIR 2025, Reddit r/udiomusic), y los hallazgos de la investigación de composición y poética (corpus/004, corpus/005).

---

## 0. Diagnóstico Inicial: ¿A qué huele la IA?

### 0.1 Síntomas Inmediatos de Olor Sintético

| Síntoma | Descripción | Ejemplo |
|---------|-------------|---------|
| **Síndrome del Poeta Automático** | Demasiadas figuras retóricas apiladas sin función narrativa | "Ecos de susurros en la noche eterna" (4 AI-ismos en 1 línea) |
| **Belleza Vacía** | Suena bonito pero no dice nada concreto | "El alma se eleva en la tempestad del corazón" |
| **Falta de Creencias** | La canción no toma posición, solo describe. Sin tesis. | Describe lluvia en campo y ciudad sin concluir nada |
| **Adjetivos sin Peso** | Adjetivos decorativos que no aportan información sensorial | "profunda", "eterna", "infinita", "mágica" |
| **Neutralidad Emocional** | La canción no arriesga una emoción auténtica (miedo, rabia, vergüenza, deseo específico) | "La vida sigue, el tiempo pasa" en lugar de "Tengo miedo de que no vuelvas" |
| **Estructura Predecible** | Versos de longitud similar, rimas perfectas, sin métrica quebrada, sin sorpresas | Todas las estrofas con el mismo número de sílabas y mismo esquema ABAB |
| **Colección de Imágenes** | Imágenes bonitas sin conexión entre sí, como un collage | "La luna, el viento, las estrellas, el mar" en versos consecutivos |

### 0.2 Test de las 3 Preguntas

Para cada verso, preguntar:

1. **¿Pasaría la Regla del Bar?** — ¿Un hablante nativo diría esto en voz alta en un bar, contando algo que le pasó?
2. **¿Tiene anclaje sensorial?** — ¿Activa al menos un sentido (olfato, tacto, temperatura, textura, sonido específico)?
3. **¿Tiene tesis?** — ¿Este verso apoya la idea central de la canción o solo rellena?

Si un verso falla 2 de 3, hay que reescribirlo.

---

## 1. Protocolo de Revisión en 10 Pasos

### Paso 1: Auditoría Léxica (Superficie)

**Qué hacer:** Recorrer toda la letra palabra por palabra y marcar cualquier término que aparezca en el listado de léxico sobreuso (spec 002-anti-ai-isms.md, §1).

**Buscador de AI-ismos léxicos:**
- ecos, susurros, neón, elevarse, ascender, volar
- gracia, abrazo, jungla de concreto
- sueños rotos, noche eterna, sombras, latidos
- destellos, sendero, llama, tempestad
- vacío, abismo, puentes, muros, cicatriz
- bailar/danzar (como metáfora automática de libertad)

**Regla:** Cada palabra prohibida encontrada = reescribir la línea completa, no solo la palabra.

**Ejemplo de reescritura:**
```
❌ "La lluvia baila en el asfalto"
   (AI-ismo semántico + palabra no prohibida pero sí muy gastada: baila)
✅ "La lluvia golpea el capó del coche aparcado"
   (verbo concreto + objeto físico específico)
```

### Paso 2: Auditoría Semántica (Verbo-Sujeto)

**Qué hacer:** Para cada par verbo-sujeto en la letra, preguntar: "¿Puede realmente X hacer Y?"

**Patrón de AI-ismo semántico:** La IA elige verbos inusuales con sujetos que no los admiten semánticamente, tratando de sonar "poética" pero produciendo combinaciones que ningún hablante nativo diría.

**Ejemplos de detección:**
```
"silencio llora" → el silencio no tiene cuerdas vocales
"tiempo sangra" → el tiempo no tiene sistema circulatorio
"noche abraza" → la noche no tiene brazos
"lluvia baila" → la lluvia no tiene pies ni voluntad
"recuerdos queman" → los recuerdos no producen calor
```

**Alternativas reales:** Usar verbos de acción mundana (subir, bajar, ir, venir, dar, pasar, dejar, coger, tener, estar, hacer, caer, golpear, correr, empapar, sonar, oler, saber, pesar, doler, callar, temblar, girar).

### Paso 3: Prueba de Concretitud (Sustantivo Abstracto → Objeto)

**Qué hacer:** Identificar cada sustantivo abstracto (amor, dolor, soledad, silencio, memoria, esperanza, miedo, rabia, tiempo, vida, muerte). Para cada uno, verificar que en el mismo verso (o el inmediatamente anterior/posterior) haya **un objeto físico específico** que lo ancle.

**Regla:** 1 abstracto → mínimo 1 concreto en la misma unidad de 2 versos.

**Ejemplo:**
```
❌ "La soledad es un abismo sin fondo"
   (abstracto "soledad" + abstracto "abismo" + metáfora sobre-explicada)
✅ "La soledad es un grifo que gotea a las tres de la mañana"
   (abstracto "soledad" + concreto "grifo" + especificidad temporal "tres de la mañana")
```

### Paso 4: Prueba de Especificidad (Genérico → Específico)

**Qué hacer:** Marcar cada sustantivo genérico y reemplazarlo por algo específico.

**Sustituciones obligatorias:**
| Genérico (IA) | Específico (Humano) |
|---|---|
| la ciudad | Carabanchel, Vallecas, el barrio de la Concepción |
| el campo | las afueras de Alcalá, la vega del Henares |
| un coche | un Renault 4, un Seat Panda destartalado |
| una flor | una buganvilia, un clavel reseco |
| un pájaro | un gorrión cojo, una urraca en la antena |
| la lluvia | el calabobos de marzo, el diluvio de la semana pasada |
| el viento | el aire que se cuela por la rendija de la ventana |
| el mar | la orilla de la Concha, el puerto de Santa María |

**Excepción:** Si el genérico es intencional por razones de universalidad narrativa (ej: "la calle" porque es MI calle, la que el oyente imagina como suya), se permite SOLO si está anclado por otros detalles específicos.

### Paso 5: Prueba de Tesis (¿Qué está diciendo esta canción?)

**Qué hacer:** Escribir la tesis de la canción en UNA oración. Luego verificar que cada sección la apoya.

**Preguntas:**
- ¿El estribillo es la tesis o solo rima bonito?
- ¿Cada verso añade evidencia a la tesis o divaga?
- ¿El puente contradice la tesis para luego reforzarla, o solo está de adorno?
- ¿Sabría el oyente la tesis después de escuchar la canción una vez?

**Protocolo de reescritura si la tesis no está clara:**
1. Definir la tesis (una oración, 15 palabras máximo).
2. Reescribir el estribillo para que contenga la tesis de forma directa.
3. Revisar que cada verso aporte un detalle que la apoye.
4. El puente debe ofrecer una perspectiva que haga la tesis más verdadera.

### Paso 6: Prueba de Métrica y Ritmo

**Qué hacer:** Medir cada verso (contar sílabas con sinalefa, acento final, licencias). Verificar:

1. **¿Hay un patrón métrico consistente?** — Que no sea un accidente.
2. **¿Hay métrica quebrada?** — Al menos 1 verso con métrica diferente (intencional).
3. **¿Las sinalefas suenan naturales?** — Si una sinalefa fuerza la pronunciación, romperla con hiato.

**Para una canción en 6/8 (compás ternario):** Los versos deben poder frasease en grupos de 3 pulsos.
**Para una canción en 4/4 (compás cuaternario):** Los versos deben poder frasease en grupos de 4 pulsos.

**Ejemplo de revisión métrica en octosílabo (romance ABCB):**
```
La llu-via_en las a-fue-ras                (7+1=8) ✓
de A-calá em-pa-pa-ba_a-llá                (a-llá aguda = 7+1=8) ✓
```

### Perfil métrico (silabario)

Antes de dar una canción por terminada, construir su **silabario** — tabla de sílabas por línea y por sección:

| Sección | L1 | L2 | L3 | L4 | Diferencia |
|---------|----|----|----|----|------------|
| V1 | 12 | 12 | 11 | 12 | ±1 |
| Chorus | 11 | 12 | 12 | 12 | ±1 |
| Bridge | 10 | 10 | 10 | 10 | perfecto |

**Verificar:**
- Versos de la misma sección deben diferir en **máx 2 sílabas** entre el más largo y el más corto
- Bridges pueden ser 1-2 sílabas más cortos que versos y coros (relajación natural)
- Si una sección tiene variación >2, o un verso aislado se desvía, hay que ajustarlo

El perfil métrico ayuda a musicalizar: un guitarrista o compositor sabe de un vistazo dónde sobran o faltan sílabas.

### Paso 7: Prueba Narrativa (Arco y Propósito)

**Qué hacer:** Trazar el arco emocional de la canción.

**Para cada sección, identificar:**
- **Verso 1:** ¿Dónde empieza emocionalmente el narrador?
- **Verso 2:** ¿Qué pasó para que la situación cambie?
- **Puente:** ¿Qué verdad nueva se revela?
- **Outro:** ¿Dónde termina emocionalmente el narrador?

**Si el arco es plano** (empieza y termina en el mismo sitio), la canción necesita una reestructuración profunda.

**Arco mínimo aceptable (para canción contemplativa):**
1. Observación externa → 2. Reconocimiento interno → 3. Transformación de la mirada

---

### Paso 8: Prueba de Realidad (Precisión del Mundo Físico)

**Qué hacer:** Para cada sustantivo concreto y cada acción en la letra, verificar que se comportan en el mundo real como la canción dice. No basta con que sea poético — tiene que ser cierto.

**Descubrimiento del proyecto:** En "Donde Cae la Lluvia", el verso "la tierra espera la lluvia en la siega" es métricamente perfecto, semánticamente coherente y sensorialmente concreto. Pero es **falso**: la siega es la cosecha, que ocurre en estación seca. La tierra espera la lluvia **en la siembra**.

**Regla:** Un sustantivo concreto que es factualmente incorrecto es **peor** que un abstracto — porque el oyente que sabe del tema lo detecta al instante y pierde toda confianza en la canción.

**Ejemplos:**
```
❌ "la tierra espera la lluvia en la siega"
   (la siega = cosecha = estación seca. Falso.)
✅ "la tierra espera la lluvia en la siembra"
   (la siembra necesita lluvia. Cierto.)

❌ "el barro se seca bajo la lluvia de abril"
   (la lluvia moja, no seca. Contradicción física.)
✅ "el barro se ablanda bajo la lluvia de abril"
   (la lluvia ablanda el barro. Cierto.)
```

**Verificaciones rápidas:**
- Agricultura: ¿cuándo se siembra? ¿cuándo se siega? ¿qué hace la lluvia a cada cultivo?
- Meteorología: ¿la lluvia enfría o calienta? ¿a qué hora del día suele llover en cada estación?
- Geografía: ¿esa ciudad tiene mar? ¿esa calle existe? ¿esa estación ocurre allí?
- Física básica: ¿el objeto se comporta como debería? (el agua corre cuesta abajo, el humo sube, el metal suena al golpearse)

### Paso 9: Contador de Saturación Léxica (Muletillas y Palabras Fantasma)

**Qué hacer:** Recorrer toda la letra y contar ocurrencias de cada palabra o frase que aparezca más de una vez. No solo prohibidas — también las inocentes.

**Descubrimiento del proyecto:** "Donde Cae la Lluvia" usó "tan solo" 4 veces. Ninguna instancia es incorrecta, pero 4 repeticiones en una canción corta crean una **muletilla invisible** que solo aparece al contar sistemáticamente.

**Patrones de saturación a detectar:**

| Patrón | Ejemplo de saturación | ¿Por qué es problema? |
|--------|----------------------|----------------------|
| **Muletilla léxica** | "tan solo" × 4 | El oyente lo percibe como tic verbal |
| **Estructura paralela** | 3 versos seguidos empezando con "Y" | Anaphora no intencional |
| **Palabra comodín** | "agua" en cada estrofa de una canción sobre lluvia | Redundancia temática |
| **Idioma interno** | "allá" × 3 en el mismo verso | Auto-referencia sin progresión |

**Regla:** Ninguna palabra o frase (no estructural) debe aparecer más de **3 veces** en toda la canción. Si aparece 4+, reemplazar al menos 2 ocurrencias con sinónimos o reestructurar el verso.

**Excepciones:**
- Artículos, preposiciones, pronombres personales átonos
- La palabra que da título a la canción (máx 6 apariciones)
- Verbos copulativos ("ser", "estar", "haber")

### Paso 10: Auditoría Sensorial — Temperatura y Textura

**Qué hacer:** Recorrer la letra y verificar que la experiencia física completa está cubierta. No basta con imágenes visuales.

**Descubrimiento del proyecto:** "Donde Cae la Lluvia" es una canción sobre la lluvia. Cero menciones a frío, humedad, escalofrío, piel mojada, ropa pegada al cuerpo. La temperatura estaba **ausente** del tema que más la exige.

**Espectro sensorial obligatorio para cada canción:**

| Tema | Sentido obligatorio | Ejemplo de inclusión |
|------|---------------------|----------------------|
| Lluvia/agua | Temperatura (frío/humedad) | "la piel se me pone de gallina" / "el calabobos cala hasta los huesos" |
| Ciudad/tráfico | Olfato (gases/escape) | "huele a gasoil y a fritanga de la esquina" |
| Comida/cocina | Tacto + temperatura | "la cuchara de palo quema al remover" |
| Campo/tierra | Textura + olfato | "la tierra húmeda se pega a la alpargata" |
| Noche/oscuridad | Tacto (aire/superficies) | "el aire de la calle está más fresco" |
| Fabricio/taller | Sonido + olfato | "huele a aceite quemado y a viruta" |

**Regla:** Para cualquier canción que mencione un fenómeno atmosférico, temperatura y humedad son **obligatorios** en al menos 2 versos. Para otros temas, al menos un sentido no-visual (olfato, tacto, temperatura, textura) por estrofa.

---

## 2. Revisión Estructural Avanzada

### 2.1 Checklist de 21 Safeguards (Spec 002)

Cada canción debe pasar los 21 safeguards. Si 3 o más fallan, la canción se rehace desde cero.

Los safeguards más violados por IA en el proyecto:

| # | Safeguard | Fallo típico de IA | Cómo revisarlo |
|---|---|---|---|
| 1 | 30%+ asonantes/libres | IA prefiere consonante perfecta | Contar rimas, dividir por total |
| 4 | ≥1 coloquialismo por estrofa | IA usa registro neutro culto | Buscar "pues", "venga", "a ver", "bueno", "joder" (si aplica), contracciones |
| 5 | ≥1 verso métrica quebrada | Todos los versos miden igual | Medir todos los versos, buscar diferencias |
| 7 | Detalles sensoriales por estrofa | IA usa imágenes visuales genéricas | Marcar olor, tacto, temperatura, textura explícitos |
| 9 | 1 imagen absurda/surrealista | IA evita lo que no controla | Buscar algo que "no encaje" — un pez de cartón, una naranja en un semáforo |
| 12 | Cero verbos forzados | IA elige verbo "poético" insólito | Preguntar: ¿alguien diría esto? |
| 16 | Puente sin "Pero" | 100% de los puentes IA empiezan con "Pero" | Verificar la primera palabra del puente |
| 17 | Título no repetido 4+ veces | IA repite título en cada estribillo 4-6 veces | Contar repeticiones del título |

### 2.2 El Problema del "Sin"

La IA abusa de construcciones con "sin". Patrón detectado:

```
❌ "sin mirar atrás, sin pedir perdón, sin saber dónde voy"
   (Tríada + parallel negation + todo en "sin")
✅ "sin hacer ruido, como quien no quiere la cosa"
   (Solo 1 "sin" + coloquialismo + especificidad)
```

**Regla:** Máximo 1 verso con "sin" por estrofa.

### 2.3 El Problema del "Y"

La IA encadena versos con "y" para crear fluidez falsa.

```
❌ "Y el viento... Y el mar... Y el sol..."
   (Anaphora abuse con "y")
✅ "El viento empuja las persianas. El mar está hoy gris."
   (Sin "y" — juxtaposición directa)
```

**Regla:** Máximo 1 "y" al inicio de verso por canción.

### 2.4 El Problema del Adjetivo Decorativo

La IA añade adjetivos que no aportan información sensorial nueva.

```
❌ "el oscuro abismo profundo y frío"
   (3 adjetivos para "abismo", todos abstractos)
✅ "el pozo del patio — el agua está verde y huele a hierro"
   (2 adjetivos concretos + anclaje sensorial olfativo)
```

**Regla:** Proporción verbos/adjetivos ≥ 2:1. Cada adjetivo debe responder a "¿qué sensación física produce?".

---

## 3. Tabla de Sustituciones Rápidas

| AI-ismo | Problema | Alternativa |
|---------|----------|-------------|
| "La lluvia baila..." | Verbo forzado, personificación automática | "La lluvia golpea el toldo..." |
| "...en la noche eterna" | Hipérbole vacía | "...hasta que clarea" o "...y no hay quien pare" |
| "El silencio grita" | Oxímoron gastado | "El silencio se nota más que las palabras" |
| "Ecos de..." | Marca registrada de Suno/Udio | Eliminar "ecos" completamente |
| "Luces de neón" | Meme de la comunidad Suno | "El fluorescente de la tienda" / "La farola que parpadea" |
| "Tender puentes / derribar muros" | Metáfora constructiva automática | Decir la acción concreta: "llamarla" / "volver" |
| "El tiempo se desangra" | Metáfora médica sin justificación | "El tiempo no pasa" / "Se me hizo de noche sin darme cuenta" |
| "Camino / sendero" | Metáfora de viaje vital automática | "La carretera" / "El callejón" / "La ruta del 27" |
| "El abrazo del..." | Abuso de "abrazo" como consuelo | "Arrimarse" / "Pasar el brazo" |
| "El dolor baila" | Verbo forzado + sinsentido | "El dolor vuelve" / "Duele al respirar" |

---

## 4. Caso Práctico: Reescritura de una Estrofa con Olor a IA

### Versión Original (Estilo IA)

```
La lluvia baila en el asfalto           — verbo forzado "baila"
y susurra su canción eterna             — "susurra" prohibido, "eterna" vacío
en la ciudad que no tiene descanso      — "ciudad" genérico, "no tiene descanso" cliché
donde los sueños se hacen sombras       — "sueños" + "sombras" = doble AI-ismo
```

**Problemas detectados:** 7 violaciones en 4 versos.

### Revisión Paso a Paso

**1. Definir tesis:** La misma agua revela quién eres según dónde caiga.

**2. Reemplazar AI-ismos léxicos:** baila→golpea, susurra→(eliminar), eterna→(eliminar), ciudad→(nombrar), sueños→(eliminar), sombras→(eliminar).

**3. Buscar coloquialismo:** ninguna → añadir.

**4. Añadir especificidad:** ¿qué ciudad? ¿qué calle? ¿qué hora?

**5. Añadir sensorial:** temperatura, olor, textura.

### Versión Revisada (Humana)

```
La lluvia golpea el toldo del taller          — verbo concreto, objeto específico
a las seis de la tarde, un martes de enero     — especificidad temporal
y el asfalto huele a polvo mojado              — sensorial (olfato + textura)
como si la ciudad se lavara por dentro         — tesis implícita (transformación)
```

**Safeguards cumplidos:** 8/8 en esta estrofa.

---

## 5. Checkpoints de Calidad

### Checkpoint 1: Pre-escritura

Antes de escribir una línea:
- [ ] Tesis definida (1 oración, ≤15 palabras)
- [ ] Género, BPM, compás elegidos
- [ ] Esquema de rima elegido (ABAB, ABCB, libre, etc.)
- [ ] Arco narrativo decidido (confesión, viaje, memoria, etc.)
- [ ] Punto de vista fijado (1ª, 2ª o 3ª persona)

### Checkpoint 2: Post-primer borrador

Después de escribir:
- [ ] Auditoría léxica completa (0 palabras prohibidas)
- [ ] Auditoría semántica (0 verbos forzados)
- [ ] Prueba de concretitud (cada abstracto anclado a un objeto)
- [ ] Prueba de especificidad (0 genéricos no justificados)
- [ ] Prueba de tesis (estrofa lo apoya)

### Checkpoint 3: Pre-entrega

Antes de guardar:
- [ ] 21 safeguards del spec 002 (máx 2 fallos)
- [ ] Lectura en voz alta (sin tropiezos)
- [ ] Métrica revisada (sinalefas, acentos, conteo silábico)
- [ ] Perfil métrico construido (tabla de sílabas por sección, variación ≤2)
- [ ] Arco narrativo verificado (el narrador termina en sitio distinto al que empezó)
- [ ] Proporción verbos/adjetivos ≥ 2:1
- [ ] Al menos 1 imagen absurda o surrealista
- [ ] Al menos 1 verso con métrica quebrada
- [ ] Al menos 1 coloquialismo por estrofa
- [ ] Puente no empieza con "Pero"
- [ ] Título no se repite más de 3 veces en el estribillo
- [ ] **Paso 8 — Prueba de Realidad:** cada sustantivo concreto verificado contra física/agricultura/geografía (0 errores factuales)
- [ ] **Paso 9 — Contador de Saturación:**ninguna palabra (no estructural) aparece >3 veces en toda la canción
- [ ] **Paso 10 — Temperatura/textura:** al menos 1 verso con sensación térmica o táctil (obligatorio si el tema es atmosférico)
- [ ] **Regla del Bar en voz alta:** cada verso leído como si lo dijera un hablante nativo contando algo que le pasó

---

## 6. Referencias

- **Spec 002:** *Anti-AI-isms* (composer/specs/002-anti-ai-isms.md). — Los 21 safeguards, listados completos y validación.
- **Wikipedia:WikiProject AI Cleanup.** *Signs of AI writing.* — La referencia global para detectar escritura sintética.
- **aismells.com.** — Detector de texto con olor a IA.
- **tropes.fyi.** — Catálogo de tropos y clichés que la IA repite.
- **Reddit r/udiomusic y r/SunoAI.** — Comunidades que reportan en tiempo real los nuevos AI-ismos emergentes.
- **Jack Righteous.** — Análisis de patrones de IA en letras de música.
- **Deezer Research, ISMIR 2025.** — Investigación académica sobre detección de contenido generado.
- **Suno Wiki.** — Documentación comunitaria de flags de IA en generación musical.
- **Forbes.** "Signs of AI Writing." — Categorización de palabras quemadas por la IA.

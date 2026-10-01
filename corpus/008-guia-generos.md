# Guía de géneros para composición

Referencia de composición, armonía, producción y generación en SUNO para los géneros primarios del autor.

---

## SUNO — Guía General de Prompting

### La Fórmula de 6 Capas

El prompt de estilo SUNO se construye en este orden de prioridad. Capas superiores tienen más impacto:

| Capa | Prioridad | Qué incluye | Ejemplo |
|------|-----------|-------------|---------|
| 1. Género | 1ª | El género principal + subgéneros | `Spanish Pop, Power Pop` |
| 2. Mood/Emoción | 2ª | 2-3 adjetivos de estado anímico | `uplifting, nostalgic, bittersweet` |
| 3. Instrumentación | 3ª | Instrumentos específicos (nombrados) | `nylon guitar, Rhodes, brushed snare` |
| 4. Voz (Triple-Stack) | 4ª | Carácter + Entrega + Colocación | `male baritone, breathy, intimate` |
| 5. Estructura | 5ª | Secciones, transiciones, dinámica | `builds gradually, stripped intro, layered chorus` |
| 6. Producción | 6ª | Textura sónica, efectos, referencia | `tape saturation, plate reverb, concert hall` |

**Regla de oro**: si el prompt excede 1000 caracteres, prioriza Armonía > Instrumentación > Emoción. Corta de abajo arriba (capa 6 primero).

### Triple-Stack Vocal

Cada especificación vocal tiene 3 ejes:

1. **Carácter** — cualidad tímbrica: `baritone`, `tenor`, `warm`, `raspy`, `clear`, `ethereal`
2. **Entrega** — estilo de interpretación: `breathy`, `intimate`, `forceful`, `conversational`, `theatrical`, `spoken`
3. **Colocación** — posición en la mezcla: `close-mic`, `dry`, `with reverb`, `layered harmonies`, `doubled L/R`

**Ejemplos por género**:

| Género | Triple-Stack recomendado |
|--------|---------------------------|
| Pop | `male baritone, clear, layered harmonies in chorus` |
| Balada | `male tenor, warm expressive, close-mic intimate verses` |
| Indie | `male, conversational, slightly dry` |
| Folk | `male, warm natural, no autotune` |
| Synth-pop | `male baritone, with reverb, doubled in chorus` |
| Chamber pop | `male, theatrical but intimate, room reverb` |
| Rock | `male, raspy forceful, dry presence` |
| Pop progresivo | `male, dramatic versatile, dynamic` |

### Meta-tags: Style Field vs. Lyrics Field

SUNO acepta meta-tags en DOS lugares distintos:

**A. Style Prompt** (campo de estilo, ~300 caracteres ideal, 1000 máx):
- Formato: texto conversacional o lista separada por comas
- V5.5: mejor respuesta a párrafos descriptivos que a keywords
- No usar corchetes `[ ]` aquí (son para el campo de letra)

**B. Lyrics** (campo de letra, con meta-tags entre `[ ]`):

| Meta-tag | Función |
|----------|---------|
| `[Intro]` | Marca la sección instrumental inicial |
| `[Verse 1]`, `[Verse 2]` | Versos (numerar para variación) |
| `[Pre-Chorus]` | Transición verso → coro |
| `[Chorus]` | Estribillo |
| `[Post-Chorus]` | Extensión del estribillo |
| `[Bridge]` | Sección de contraste |
| `[Guitar Solo]`, `[Piano Solo]`, `[Synth Solo]` | Solos instrumentales |
| `[Interlude]` | Interludio instrumental |
| `[Outro]` | Cierre |
| `[End]` | Final marcado (evita fade out genérico) |
| `[Spoken Word]`, `[Rap Verse]` | Voces no melódicas |
| `[Whisper]` | Voz susurrada |
| `[Build]`, `[Drop]` | Transiciones electrónicas |

**Reglas de meta-tags**:
- 1-2 por sección, no más de 5 en toda la canción
- No mezclar moods opuestos en secciones adyacentes
- Las secciones deben tener trabajos claros (no etiquetar por etiquetar)
- `[End]` es más fiable que esperar fade out

### SUNO v5 vs v5.5: Lo Que Cambió

v5.5 NO es un motor de audio nuevo. Es una **capa de personalización** sobre el mismo motor v5. El prompt, meta-tags y límites son idénticos. Lo que cambia:

| Aspecto | v5 | v5.5 |
|---------|----|------|
| Filosofía | Motor de generación + prompt | Motor + personalización (Voz + Modelo + Gusto) |
| Voice Cloning | No | Sí — clona tu voz real |
| Custom Models | No | Sí — entrena el modelo con tu catálogo |
| My Taste | No | Sí — aprende tus preferencias pasivamente |
| Expresividad | Alta | Más alta — descriptores sutiles ahora funcionan |
| Prompt syntax | Idéntica | Idéntica (mismos meta-tags, mismos límites) |
| Calidad de audio | Studio-grade | Studio-grade (mismo motor) |

**Cuándo usar cada uno**:
- **v5**: Drafting rápido, iteración prompt-driven, estructura limpia, workflow básico sin personalización
- **v5.5**: Cuando tienes tu propia voz grabada, un catálogo consistente, o quieres que el sistema aprenda tu estilo

**Regla de decisión**: v5 para «necesito una buena canción rápido». v5.5 para «necesito que suene A MÍ».

### Estrategias Específicas de v5.5

**1. Con Voice Cloning activado**:
- QUITA los descriptores de género vocal del Style Prompt (`male vocals`, `female vocals`, `baritone`, etc.) — la voz clonada ya los define
- USA el espacio liberado para detalles de PRODUCCIÓN
- El Triple-Stack vocal se reduce a entrega + colocación (el carácter ya lo da tu voz)

| Antes (v5) | Después (v5.5 con Voice) |
|-------------|--------------------------|
| `male baritone, clear, layered harmonies in chorus` | `layered harmonies in chorus, intimate room mic, subtle plate reverb` |

**2. Con Custom Models activado**:
- El modelo ya conoce tu ADN de producción (mezcla, paleta instrumental, textura)
- El prompt se enfoca en lo ESPECÍFICO DE LA CANCIÓN (estructura, dinámica, energía)
- Prompts más ligeros, más dirección que descripción

**3. Con My Taste activo**:
- My Taste influye en DEFAULTS, no en prompts explícitos
- Un prompt detallado SIEMPRE anula My Taste
- Si das prompts vagos, My Taste llena los huecos con tu historial

**4. Apilamiento de capas (máximo poder)**:

```
Capa 1: My Taste → forma defaults según tu historial
Capa 2: Custom Model → establece ADN de producción
Capa 3: Voice → aplica tu tono vocal real
Capa 4: Prompt → dirige la canción específica (sigue siendo la capa MÁS importante)
```

### Negative Prompting (v5 y v5.5)

Añade restricciones directamente en el Style Prompt con prefijo `no`:

| Restricción | Efecto |
|-------------|--------|
| `no reverb wash` | Sonido más seco, más orgánico |
| `no autotune` | Voz natural, sin procesamiento |
| `no synths`, `no drum machines` | Producción acústica |
| `no strings` | Evita arreglos orquestales no deseados |
| `no distortion` | Sonido limpio |
| `no ballad feel` | Mantiene energía en géneros lentos |
| `no bright synths` | Oscurece la paleta sonora |

**Regla**: 2-3 restricciones al FINAL del Style Prompt, después de los descriptores positivos.

### Conversacional vs. Keyword por Versión

| Enfoque | v5 | v5.5 |
|---------|----|------|
| Conversacional | Funciona, pero menos preciso | **Óptimo** — v5.5 lee intención emocional |
| Keyword list | **Óptimo** — v5 prioriza tags | Funciona, pero infrautiliza la expresividad |
| Híbrido | Recomendado | Recomendado para géneros complejos |

**Recomendación general v5.5**: escribe como le explicarías la canción a un músico, no como una lista de tags. Ejemplo que funciona:
```
Intimate Spanish pop ballad with hushed verses, fingerpicked nylon guitar, warm Rhodes, and soft sub-bass. Sparse kick, brushed snare, and close-mic breathy vocals. Chorus opens with layered harmonies, sustained synth pad, and subtle string lines. Gentle tape saturation, plate reverb, and a restrained, confessional late-night texture.
```

### Flujo de Trabajo en 2 Fases

**Fase 1 — Generar estructura** (~4-8 generaciones):
1. Style prompt con género + mood + instrumentación base
2. Letra completa con meta-tags de sección
3. Revisar: ¿la estructura se respeta? ¿los meta-tags funcionan?

**Fase 2 — Refinar textura** (~2-4 generaciones):
1. Añadir Triple-Stack vocal detallado (o ajustar si usas Voice)
2. Añadir capa de producción (reverb, compresión, textura)
3. Si la voz no encaja: cambiar el eje de carácter (no el de entrega ni colocación), o cambiar entre v5 y v5.5
4. Si la sección no funciona: cambiar el meta-tag, no la letra

**Regla de segmentación** (crítica en v5/v5.5):
- Genera en segmentos de 1:30-2:00 minutos, NO la canción completa de 4-5 min
- Cada extensión = nuevo control de calidad
- Si la calidad se degrada en la segunda mitad, vuelve al punto más limpio y continúa desde ahí
- Usa "Create 2" para probar prompts nuevos, no generes 4 variaciones simultáneas

**Después de generar**:
- **Continue from this moment**: cuando la canción corta antes de tiempo
- **Replace Section**: para cambiar una sección que no funciona
- **Extend**: para añadir una sección nueva
- **Cover**: misma letra, género diferente
- **Remaster**: para limpiar una generación con artefactos

### Failure Modes Comunes de v5 y v5.5

| # | Problema | Causa probable | Solución |
|---|----------|---------------|----------|
| 1 | Voz genérica / sin carácter | Falta Triple-Stack vocal | Añadir carácter + entrega + colocación |
| 2 | Coro sin energía | Meta-tag faltante o sección muy larga | Acortar chorus o añadir `[Build]` antes |
| 3 | Instrumentación incorrecta | Instrumentos genéricos en prompt | Nombrar instrumentos UNO POR UNO |
| 4 | Fade out prematuro | Sin final marcado | Añadir `[End]` al final o Outro definido |
| 5 | Estribillo idéntico siempre | Variación semántica insuficiente | Cada chorus necesita cambio en L1, L3 o L4 |
| 6 | Letra ininteligible | Prosodia rota (sílaba tónica en tiempo débil) | Revisar acentuación: tónicas en tiempos fuertes |
| 7 | Suena a «biblioteca / stock» | Referencia genérica sin anclaje | Añadir «like X at their most Y» |
| 8 | Artefactos / clipping / distorsión (v5.5) | Descriptores de energía extremos | Cambiar `massive` / `wall of sound` por `powerful but clear`; añadir `clean mix, no distortion` |
| 9 | Genre drift (v5/v5.5) | Prompt sub-especificado, el modelo «deriva» a otro género | Reforzar género en tags de sección: `[Verse, pop]`; mantener 5-8 tags máximo |
| 10 | Voz robótica / plana (v5.5) | My Taste o Custom Model aplanan la expresividad | Añadir vocal performance tags: `[soulful delivery, emotional, slightly breathy]` |
| 11 | Voz femenina cuando se pidió masculina (o viceversa) | Falta especificación de género vocal | Añadir `male vocals` o `female vocals` EXPLÍCITAMENTE |
| 12 | La canción se acelera / ralentiza | BPM no especificado o conflictivo | Fijar BPM exacto en style prompt |
| 13 | Resultados inconsistentes (mismo prompt, sonido diferente) | Generación estocástica sin seed control | Aceptar variabilidad como parte del workflow; generar 3-5 y seleccionar; usar Custom Models para consistencia |
| 14 | Demasiadas capas en verso | Saturación de tags de producción | Versos: mínimo de capas. Coros: todo |
| 15 | Conflicto de tags (v5) | Más de 10 tags, señales contradictorias | Mantener 5-8 tags. Un género ancla + 1-2 modificadores máximo |
| 16 | Contradicción estructural | Descriptores opuestos: `epic orchestral` + `minimalist lo-fi` | Elegir un carril y ser consistente |
| 17 | Degradación en canciones largas (v5/v5.5) | Generación completa de 4-5 min en un solo clip | Generar en segmentos de 1:30-2:00 min; extender desde el punto más limpio |

---

## Pop

### Características generales

- **BPM**: 90–130 (streaming: 100–120)
- **Estructura**: Intro (4-8 bars) → Verse → Pre-Chorus → Chorus → Verse → Pre-Chorus → Chorus → Bridge → Final Chorus → Outro
- **Duración streaming**: 2:30–3:45. Primer chorus antes del minuto.
- **Hook**: en los primeros 30-45 segundos.
- **Extensión de chorus**: 8-16 bars, con post-chorus opcional de 4-8 bars.

### Armonía

| Progresión | Grados | Efecto emocional | Uso |
|---|---|---|---|
| Singer-songwriter | I–V–vi–IV | Épico, himno | Estribillos grandes |
| Axis | vi–IV–I–V | Nostálgico, moderno | Versos, pre-estribillos |
| Doo-wop | I–vi–IV–V | Clásico, familiar | Baladas, pop guitarrero |
| Hopscotch | IV–V–vi–I | Contemporáneo (2010+) | Pop moderno, urbano |
| Canon | I–V–vi–iii–IV–I–IV–V | Progresivo, ascendente | Puentes, finales |

- Máximo 4 acordes por sección. Economía armónica.
- Pre-estribillo: tensión con dominante (V) o acordes ascendentes.
- Puente: cambio de tonalidad (modulación a vecina) o acorde prestado.
- **Pet Shop Boys formula**: Ab–Bb–Gm7–Cm (o su transpose).

### Melodía

- Salto limpio al título en el hook, luego movimiento por grados conjuntos.
- Subir el registro un tercio del verso al coro.
- Notas largas y vocales abiertas en el coro; rítmica más densa en versos.
- Sílabas tónicas en tiempos fuertes (prosodia).

### Letra

- 6-10 palabras para el hook.
- Un detalle sensorial por verso.
- Una «miga de tiempo» (time crumb) que sitúa la historia.
- Estructura: situación → deseo → conflicto → consecuencia.

### Producción

- Versos: pocas capas (kick, bass, un textural, voz).
- Coro: capas completas, armonías vocales, stereo expandido.
- Compresión serial en voz (2:1 → 4:1).
- Reverb de placa corta (0.6–1.2s).
- Intro < 10 segundos o hook reconnaissable.

### SUNO prompting

**Style Prompt** — enfoque conversacional para v5.5:
```
Clean modern pop with warm acoustic guitar and synth pads, intimate verses with layered harmonies in the chorus, male baritone vocals, nostalgic and uplifting mood, like Coldplay at their most Spanish, 100-115 BPM
```

**Estrategia de meta-tags en letra**:
```
[Verse] → textura íntima, pocas capas
[Pre-Chorus] → tensión ascendente, añadir capas
[Chorus] → stereo expandido, armonías, energía
[Bridge] → break, quitar capas, cambio armónico
```

**Triple-Stack vocal**: `male baritone, clear, layered harmonies in chorus`

**Referencias para Style Prompt**: Coldplay, Pablo Alborán, Dani Martín, Vanesa Martín en su faceta más pop. Especificar «like X at their most Y» evade el pop genérico de biblioteca.

**Failure modes específicos**:
- Coro idéntico siempre → variar L1, L3 o L4 de cada coro
- Voz sin carácter → falta especificar entrega (`clear`, `breathy`, `conversational`)
- Instrumentación genérica → nombrar instrumentos: `nylon guitar` no `acoustic guitar`; `analog synth pad` no `synth`

### Anti-AI específico

- Cuidado con la «anaphora abuse» en pop (múltiples versos seguidos con la misma apertura).
- Pop tiende a usar abstractos vacíos («love», «heart», «dream») — aplicar regla del sustantivo concreto.
- Los coros idénticos en pop son la norma, pero el autor exige variación semántica.

---

## Balada

### Características generales

- **BPM**: 60–85 (lenta) / 85–100 (balada rítmica)
- **Estructura**: Intro (piano/guitarra sola) → Verse → Verse → Chorus → Verse → Chorus → Bridge → Final Chorus → Outro
- **Compás**: 4/4, ocasionalmente 3/4 o 6/8
- **Narrativa**: principio → medio → clímax → final. Arco dramático explícito.
- **Personajes**: máximo 1-2 principales.

### Armonía

| Progresión | Grados | Efecto |
|---|---|---|
| Balada pop | I–V–vi–IV | Épico, himno |
| Clásica española | I–vi–IV–V | Cálida, tradicional |
| Con color | ii–V–I | Sofisticada (jazz/soul) |
| Cadencia andaluza | i–VII–VI–V | Española, descendente |
| Romántica mayor | I–IV–ii–V | Alegre con giro emocional |

- Acordes abiertos (mayores, con cuerdas al aire) en estribillo.
- Inversiones en puente para oscurecer.
- Un solo acorde «exótico» (Maj7, m9) bien colocado vale más que muchos.
- **Canon de Pachelbel**: I–V–vi–iii–IV–I–IV–V, ideal para baladas crescendo.

### Melodía

- Fraseo más libre, con espacio entre líneas (respiración).
- Registro: contenido en versos, se abre en el coro.
- Clímax melódico en el puente o último coro.
- Rima: asonante o consonante, esquema ABAB o AABB.

### Letra

- Primer verso: presenta personaje/situación.
- Estructura narrativa: historia con arco, no solo estado emocional.
- Diálogo entre comillas cuando hable un personaje.
- Última estrofa: resume o da un giro.
- Balada española: octosílabo, rima asonante en pares.

### Producción

- Intro: un solo instrumento (piano, guitarra acústica).
- Crecimiento gradual: suma capas verso a verso.
- Puente: quitar capas (break) o cambiar armonía.
- Reverb más larga que pop (1.5–2.5s).
- Piano + cuerdas o guitarra fingerpicking + cello.

### SUNO prompting

**Style Prompt** — conversacional con foco en dinámica:
```
Intimate Spanish ballad with piano and strings, builds gradually from solo piano to full orchestral crescendo in the final chorus, warm male tenor vocals, close-mic and expressive, emotional and dramatic, 70-85 BPM, like Alejandro Sanz at his most vulnerable
```

**Estrategia de meta-tags en letra**:
```
[Verse] → instrumento solo (piano/guitarra), voz expuesta
[Chorus] → cuerdas entran, reverb más larga, dinámica media
[Bridge] → break, silencio, tensión armónica
[Final Chorus] → crescendo, orquesta completa, clímax
[Outro] → disolución lenta, vuelta al instrumento inicial
```

**Triple-Stack vocal**: `male tenor, warm expressive, close-mic intimate verses`

**Referencias**: Alejandro Sanz (baladas), Sin Bandera, Pablo Alborán, Manuel Carrasco. Evitar «balada épica» sin textura específica — SUNO interpreta «épico» como «himno de estadio».

**Failure modes específicos**:
- Suena a «balada de boda genérica» → añadir instrumento inesperado (`cello`, `bandoneón`, `clarinete bajo`)
- Crescendo no llega → marcar `[Build]` o `[Final Chorus]` explícitamente
- Voz demasiado melosa → añadir `restrained` o `conversational` a la entrega
- Reverb excesiva que embarra la letra → especificar `dry close-mic verses, plate reverb only in chorus`

### Anti-AI específico

- Las baladas SUNO suenan a «genérico épico» — exigir SPECIFICIDAD (objetos, lugares, nombres).
- Cuidado con clichés: «lluvia», «estrellas», «corazón roto» sin anclaje físico.
- La métrica debe coincidir con la música: sílabas tónicas en tiempos fuertes.
- La balada en español tiende al ripio (rima forzada). Auditoría léxica previa.

---

## Indie

### Características generales

- **BPM**: 80–120
- **Estructura**: más libre que pop. Puede prescindir de pre-estribillo.
- **Actitud**: introspectiva, alternativa, menos pulida que el pop mainstream.
- **Instrumentación**: guitarras eléctricas limpias o acústicas, batería orgánica, bajo melódico.

### Armonía

| Progresión | Grados | Efecto |
|---|---|---|
| Indie rock | I–IV–V | Directa, clásica |
| Modal | i–VII–VI | Menor, melancólica |
| Axis variante | vi–IV–I–V | Moderna, familiar |
| Con sorpresa | I–iii–IV–V | Inesperada, fresca |

- Menos dependencia de la progresión de 4 acordes;允许 progresiones más largas.
- Uso de modalidad (dórica, mixolidia) para color.
- Acordes suspendidos (sus2, sus4) para ambigüedad.

### Melodía

- Menos «gancho» comercial, más fraseo natural.
- Puede ser hablada-cantada (sprechgesang).
- Rango moderado, con momentos de tensión controlada.

### Letra

- Narrativa personal, observación cotidiana.
- Ironía, distancia emocional permitida.
- Objetos concretos y geografía precisa (la regla del bar).
- Menos directa que el pop, más sugerente.

### Producción

- Menos compresión que pop, dinámica más natural.
- Guitarras con carácter (no perfectamente limpias).
- Vocales con menos capas, más expuestas.
- Reverb de sala, no de placa.

### SUNO prompting

**Style Prompt** — híbrido conversacional + keywords:
```
Introspective Spanish indie pop with organic guitars and natural production, intimate male vocals slightly dry and conversational, dynamic arrangement that breathes, nostalgic and bittersweet, like Vetusta Morla or Izal at their most stripped-down, 85-110 BPM
```

**Estrategia de meta-tags en letra**:
```
[Verse] → voz expuesta, guitarras limpias, dinámica baja
[Chorus] → apertura moderada, guitarras con carácter, batería entra
[Bridge] → tensión controlada, posible cambio de compás
[Outro] → disolución, fade natural o repetición decayendo
```

**Triple-Stack vocal**: `male, conversational, slightly dry`

**Referencias**: Vetusta Morla, Izal, Love of Lesbian, Miss Caffeina, Sidonie. Indie español es un mundo propio — referenciarlo evita el «indie de biblioteca» anglosajón.

**Failure modes específicos**:
- Suena a «indie británico de biblioteca» → referenciar indie español explícitamente
- Voz demasiado procesada → especificar `dry`, `natural`, `room sound`
- Falta de dinámica → especificar `dynamic`, `breathes`, `not over-compressed`
- Guitarras sin carácter → nombrar textura: `jangle`, `clean with tremolo`, `slightly overdriven`

### Anti-AI específico

- Indie SUNO tiende a sonar a «indie genérico de biblioteca» — exigir texturas específicas.
- Sin anaphora abuse: el indie se presta a repetición poética, pero controlar.
- La métrica quebrada es un recurso válido en indie, pero no abusar.

---

## Folk

### Características generales

- **BPM**: 80–120 (lento a mid-tempo)
- **Compás**: 4/4, 3/4, 6/8
- **Estructura**: verso-centrica. El estribillo puede ser solo una línea repetida.
- **Instrumentación**: guitarra acústica (fingerpicking o rasgueo), banjo, cello, armónica, percusión mínima.

### Armonía

| Progresión | Grados | Efecto |
|---|---|---|
| Folk clásica | I–IV–V | Directa, tradicional |
| Con color | I–iii–IV–V | Suave, narrativa |
| Menor folk | i–VII–VI | Melancólica, celta |
| Americana | I–V–IV | Abierta, optimista |

- Acordes abiertos con cuerdas al aire.
- Poco uso de séptimas; si se usan, son maj7 o add9.
- Arpegios en lugar de rasgueo en versos.

### Melodía

- Narrativa: la melodía sigue el fraseo de la letra.
- Repetición con variación mínima.
- Rango vocal contenido, sin grandes saltos.

### Letra

- La letra es el centro. Historia, personajes, lugar.
- Estructura de balada folk: cuatro estrofas de cuatro versos (AABB o ABCB).
- Imágenes de la naturaleza, objetos cotidianos.
- La moraleja o giro al final.

### Producción

- Mínima. Voz + guitarra como base.
- Segunda voz o armonía en el estribillo.
- Ambiente natural, poco procesamiento.
- Evitar auto-tune visible.

### SUNO prompting

**Style Prompt** — conversacional minimalista:
```
Spanish folk with fingerpicked acoustic guitar and cello, warm natural male vocals with no detectable autotune, intimate narrative storytelling, minimal organic production with room sound, like Jorge Drexler at his most stripped-down or Silvio Rodríguez in his intimate recordings, 85-105 BPM
```

**Estrategia de meta-tags en letra**:
```
[Verse] → voz + guitarra fingerpicking, aire
[Chorus] → cello entra, armonía vocal
[Interlude] → guitarra sola, variación del tema
[Outro] → fade natural o vuelta al principio
```

**Triple-Stack vocal**: `male, warm natural, no autotune`

**Referencias**: Jorge Drexler, Silvio Rodríguez, Joaquín Díaz, Luis Pastor. El folk español NO es folk irlandés — especificar tradición hispana.

**Failure modes específicos**:
- Suena a «pub irlandés» → prohibir fiddle, especificar `cello` o `guitarra española`
- Voz con autotune audible → añadir explícitamente `no autotune`, `natural`, `organic`
- Letra ininteligible por producción → especificar `close-mic`, `intimate`, `dry`
- Arcaísmos sonoros → especificar instrumentación acústica contemporánea, no «medieval»
- Meter forzado → especificar si es fingerpicking (`fingerpicked`) o rasgueo (`strummed`)

### Anti-AI específico

- Folk SUNO suena a «pub irlandés genérico» — especificar instrumentación (cello en lugar de fiddle, por ejemplo).
- Sin palabras arcaicas forzadas («mas», «do», «cual» en lugar de coloquial actual).
- La historia debe tener arco, no solo atmósfera.
- Aplicar regla del bar sin excepción: el folk narrativo necesita lenguaje creíble.

---

## Synth-pop

### Características generales

- **BPM**: 90–120 (lento/atmósferico) / 110–130 (bailable)
- **Estructura**: Intro → Verse → Pre-Chorus → Chorus → Verse → Pre-Chorus → Chorus → Bridge/Breakdown → Double Chorus
- **Paleta sonora**: sintetizadores como elemento principal. Pads, arpegios, bass synth, drum machine.
- **Estética**: 80s o moderna (hyperpop, bedroom synth).

### Armonía

| Progresión | Grados | Efecto |
|---|---|---|
| Synth-pop clásica | I–V–vi–IV | Nostálgica, uplifting |
| Larga distancia | vi–IV–I–V | Cinemática, longing |
| Pet Shop Boys | I–♭VII–IV–V | Dance, eufórica |
| Con pedales | I–♭VII–IV–I (pedal en I) | Etérea, flotante |

- Progresiones simples con voicings lujosos (pads abiertos).
- Bajos pedal: la nota del bajo se mantiene mientras los acordes cambian arriba.
- Uso de séptimas mayores (maj7) para brillo.
- Arpegios como motor rítmico.

### Melodía

- Registro medio-alto. La melodía vive en los primeros planos.
- Saltos melódicos en el gancho, luego paso conjunto.
- Frases cortas y repetibles.
- Silabeo claro: las consonantes no se pierden en la producción.

### Letra

- Imágenes visuales fuertes: neón, lluvia, ciudades de noche.
- Nostalgia, deseo, distancia emocional.
- Menos narrativa que folk, más atmosférica.
- El título aparece temprano y se repite.

### Producción

- Sidechain del pad al kick para que respire el groove.
- Voces: dobladas en el coro (paneo L/R).
- Reverb de placa + delay sincronizado al tempo.
- Bass synth: saw wave con filtro low-pass, envuelta ajustada.
- Capas: versos estrechos (menos agudos), coros abiertos (stereo expandido).

### SUNO prompting

**Style Prompt** — keyword list (v5.5 responde bien a sintetizadores con lista):
```
Spanish synth-pop with analog synth pads, arpeggiator sequences, synth bass and drum machine, wide stereo chorus with sidechain groove, male baritone vocals with reverb, slightly dry in verses and doubled in chorus, nostalgic and cinematic, like Pet Shop Boys at their most melancholic or M83 at their most Spanish, 95-115 BPM
```

**Estrategia de meta-tags en letra**:
```
[Intro] → arpegiador solo, pad de fondo, batería entra
[Verse] → voz seca, pads estrechos, bajo pulsante
[Pre-Chorus] → subida de tensión, sidechain más evidente
[Chorus] → stereo expandido, voz doblada, capas completas
[Bridge] → breakdown, quitar batería, pad etéreo
[Final Chorus] → doble coro, energía máxima
[Outro] → fade con delay, arpegio decayendo
```

**Triple-Stack vocal**: `male baritone, with reverb, doubled in chorus`

**Referencias**: Pet Shop Boys, M83, Chromatics, The Midnight, Vangelis (bandas sonoras). Synth-pop español: Astrud, La Casa Azul, Fangoria.

**Failure modes específicos**:
- Saturación de capas → especificar texturas UNA POR UNA, no «más capas»
- Nostalgia caricaturesca → prohibir «80s style» genérico, usar «like Pet Shop Boys at their most melancholic»
- Arpegiador genérico → especificar patrón: `ascending arpeggiator`, `filtered arpeggio sequence`
- Sidechain que no se nota → pedir `sidechain groove` o `pumping pads`
- Bajo synth débil → especificar `analog synth bass`, `saw wave with filter envelope`

### Anti-AI específico

- Synth-pop SUNO tiende a saturar de layers — pedir texturas específicas, no «más».
- La nostalgia ochentera no debe ser caricatura: especificar «like Pet Shop Boys at their most melancholic», no «80s style».
- Los arpegios deben tener un patrón definido, no un «arpeggiator genérico».
- Las letras synth-pop tienden al abstracto vacío («night», «city lights», «dreams») — aplicar regla de especificidad.

---

## Chamber pop

### Características generales

- **BPM**: 70–100
- **Estructura**: clásica de pop, pero con secciones orquestales. Posible introducción larga.
- **Instrumentación**: orquesta de cámara (cuerdas, vientos madera, metales), piano, arpa, glockenspiel. Batería mínima o ausente.
- **Actitud**: sofisticación, arreglo cuidada, dinámica teatral.

### Armonía

| Progresión | Grados | Efecto |
|---|---|---|
| Clásica-pop | I–V–vi–IV | Base, con voicings orquestales |
| Con modulación | I–♭III–IV–I | Dramática, cambio de modo |
| Barroca | I–iii–IV–V | Influencia clásica |
| Cadencias extendidas | ii–V–I con extensiones | Jazz-clásica |

- Acordes con extensiones (maj7, m9, add9) para color orquestal.
- Modulaciones a tonalidades vecinas en el puente.
- Pedales de cuerda (nota larga sostenida mientras la armonía cambia).

### Melodía

- Fraseo más largo, menos sincopado.
- Rangos amplios,允许 saltos melódicos dramáticos.
- Silencios y pausas como recurso expresivo.

### Letra

- Poética sin ser pretenciosa.
- Imágenes elaboradas, metáforas extendidas.
- Tono: íntimo pero con grandeza. Como un confesionario en un teatro vacío.
- Estructura clásica de canción, pero permitiendo más versos.

### Producción

- Arreglo de cuerdas realistas (no MIDI genérico).
- Dinámica: pp a ff en el arco de la canción.
- Reverb de sala de concierto (2-3s).
- Piano como columna vertebral.

### SUNO prompting

**Style Prompt** — conversacional con instrumentos uno por uno:
```
Spanish chamber pop with string quartet, grand piano, French horn countermelody, marimba and glockenspiel, dynamic orchestral arrangement that moves from intimate piano to full ensemble, warm male vocals theatrical but never bombastic, concert hall reverb, like Antonio Luque (Sr. Chinarro) arranged by Vince Mendoza or Sufjan Stevens at his most orchestral, 75-95 BPM
```

**Estrategia de meta-tags en letra**:
```
[Intro] → piano solo o cuarteto de cuerdas, dinámica pp
[Verse] → voz + piano + cello, íntimo
[Chorus] → orquesta de cámara completa, dinámica mf
[Bridge] → cambio armónico, cuerdas en tensión, dinámica p
[Final Chorus] → tutti, dinámica ff, clímax orquestal
[Outro] → disolución, vuelta al piano solo, reverb decayendo
```

**Triple-Stack vocal**: `male baritone, theatrical but intimate, concert hall reverb`

**Referencias**: Sr. Chinarro, Sufjan Stevens, The Divine Comedy, Antonio Vega (en sus arreglos orquestales), Vicente Amigo. Evitar el «fantasy soundtrack» especificando instrumentos de cámara reales.

**Failure modes específicos**:
- Suena a «banda sonora de fantasy» → especificar instrumento por instrumento SIN etiqueta «orchestral» aislada
- Cuerdas MIDI → especificar `string quartet` (música de cámara), no `strings`
- Arpa genérica → especificar `harp harmonics` o `harp glissandi`
- Grandilocuencia vacía → cada crescendo debe corresponder a un clímax en la letra
- Falta de intimidad → asegurar secciones `piano solo` o `stripped` antes de la orquesta

### Anti-AI específico

- Chamber pop SUNO suena a «banda sonora de fantasy genérica» — especificar instrumentos uno por uno.
- Cuidado con los clichés de «música clásica» (arpegios de arpa predecibles, cuerdas melódicas sin variación).
- Las letras pueden ser más elaboradas, pero la regla del bar sigue vigente.
- Sin grandilocuencia vacía: cada explosión orquestal debe tener una razón en la letra.

---

## Rock / Pop rock

### Características generales

- **BPM**: 110–150 (pop rock más lento: 100–120)
- **Estructura**: Intro (riff) → Verse → Chorus → Verse → Chorus → Bridge/Solo → Chorus → Outro
- **Instrumentación**: guitarra eléctrica (rítmica + solista), bajo, batería enérgica. Posible segunda guitarra.
- **Actitud**: energía, ataque, menos pulido que el pop.

### Armonía

| Progresión | Grados | Efecto |
|---|---|---|
| Rock clásica | I–IV–V | Base del género |
| Power chord | I–♭VII–IV (en quintas) | Abierta, cruda |
| Menor rock | i–VII–VI | Oscura, agresiva |
| Blues rock | I–IV–V con séptimas | Con sabor a blues |

- Power chords (solo quinta y octava, sin tercera) para sonido rock.
- Menos acordes por progresión. Más repetición.
- Riff de guitarra como identidad de la canción.
- Posible uso de blues scale en solos.

### Melodía

- Más gritada o forzada que pop. Tensión vocal válida.
- Rango medio-agudo.
- Frases rítmicas, sincopadas.
- La melodía puede doblar la guitarra rítmica.

### Letra

- Directa, sin ambages. Menos metáfora, más declaración.
- Rebeldía, frustración, deseo, superación.
- Coro: simple, repetitivo, fácil de corear.
- Menos detalles sensoriales, más actitud.

### Producción

- Guitarras distorsionadas o overdrive.
- Batería: sonido natural o sampleado, con presencia.
- Bajo: sigue la guitarra rítmica o contramelódico.
- Poca reverb en voces. Presencia seca.
- Compresión de bus de guitarra para pegada.

### SUNO prompting

**Style Prompt** — híbrido con referencia de época:
```
Spanish rock with energetic electric guitars, driving bass and punchy drums, raspy male vocals with dry live feel, defiant and passionate, like early Leño at their most raw or Platero y Tú at their most direct, 110-135 BPM
```

**Estrategia de meta-tags en letra**:
```
[Intro] → riff de guitarra solo, batería marcando
[Verse] → guitarra rítmica + bajo + voz seca
[Chorus] → potencia, distorsión, batería en crash
[Guitar Solo] → solo melódico con expresión
[Bridge] → break, tensión, posible cambio armónico
[Outro] → riff se desvanece, feedback
```

**Triple-Stack vocal**: `male, raspy forceful, dry presence`

**Referencias**: Leño, Platero y Tú, Extremoduro (primeras etapas), Marea, Fito & Fitipaldis (pop rock), Héroes del Silencio (rock español con grandeza). El rock español tiene un sonido característico — referenciarlo directamente.

**Failure modes específicos**:
- Suena a «rock de estadio genérico de biblioteca» → referenciar banda española específica
- Guitarras sin pegada → especificar si es `overdriven`, `distorted`, `clean with crunch`
- Voz sin energía → `raspy`, `forceful`, `gritty`, evitar `smooth` o `clean`
- Batería débil → especificar `punchy drums`, `driving beat`, `crash cymbals in chorus`
- Solos de guitarra genéricos → especificar estilo: `blues-inflected solo`, `melodic solo`, `aggressive solo`

### Anti-AI específico

- Rock SUNO tiende a sonar a «rock de estadio genérico» — especificar la referencia (no «like rock», sino «like early Springsteen» o «like Mexican rock en español»).
- Sin clichés de «sex, drugs, rock and roll» por defecto.
- Las letras de rock pueden tener menos detalles sensoriales, pero deben tener al menos uno concreto por sección.
- La energía no excusa la vaguedad: «romper las cadenas» es abstracto vacío sin el objeto específico.

---

## Pop progresivo

### Características generales

- **BPM**: variable (60–140). Puede cambiar dentro de la canción.
- **Estructura**: no fija. Secciones múltiples, cambios de compás, puentes extendidos.
- **Compás**: variable (4/4, 3/4, 5/4, 7/8). Cambios intencionales.
- **Duración**: 4–7 minutos. Sin restricción de streaming.
- **Actitud**: ambición estructural, exploración, fusión de estilos.

### Armonía

| Progresión | Grados | Efecto |
|---|---|---|
| Con modulación | I–♭III–IV–I | Cambio modal dramático |
| Secuencia | ii–V–I en varias tonalidades | Viaje armónico |
| Cromática | I–♯I°–ii–V | Tensión, sofisticación |
| Mixta | intercambio modal | Colores impredecibles |

- Modulaciones frecuentes (ascendentes por tono o semitono).
- Acordes prestados de modos paralelos.
- Progresiones largas (8+ acordes) sin repetición cíclica.
- Cambios de centro tonal entre secciones.

### Melodía

- Motivos que se transforman (desarrollo temático).
- Rangos amplios. Saltos inesperados.
- La melodía puede cambiar de carácter por sección.
- Posible spoken word o rap en secciones específicas.

### Letra

- Narrativa compleja. Múltiples perspectivas.
- Temas: filosóficos, literarios, existenciales.
- Estructura poética libre. No obligada a estribillo repetitivo.
- Imaginería densa. Capas de significado.

### Producción

- Orquestal o de banda completa. Arreglos densos.
- Capas múltiples que entran y salen.
- Cambios de producción entre secciones (intimidad → grandeza).
- Solos instrumentales (guitarra, piano, sintetizador).

### SUNO prompting

**Style Prompt** — conversacional con énfasis en cambios de sección:
```
Spanish progressive pop with multiple movements and dynamic shifts, from intimate piano to full orchestral peaks, dramatic male vocals that move from whisper to full force, ambitious arrangement like Queen meeting Russian Red, variable tempo, unconventional structure with instrumental breaks, art pop with Spanish soul
```

**Estrategia de meta-tags en letra**:
```
[Section 1] → primera parte, tema A, íntimo
[Build] → tensión creciente, capas se acumulan
[Section 2] → tema B, cambio tonal/textural
[Instrumental Break] → desarrollo temático instrumental
[Section 3] → tema C, clímax, máxima energía
[Resolution] → vuelta al tema A, transformado, cierre
[End] → final definido, no fade
```

**Triple-Stack vocal**: `male, dramatic versatile, dynamic`

**Referencias**: Queen, Russian Red, Antony and the Johnsons, David Bowie (etapa art pop), Björk. En español: Sr. Chinarro (etapa orquestal), La Buena Vida (arreglos complejos). La referencia debe anclar la ambición sin caer en «progresivo de catálogo».

**Failure modes específicos**:
- Suena a «PowerPoint progresivo» → especificar instrumentos reales y cambios concretos
- Falta de ancla melódica → incluso en secciones complejas, asegurar un gancho
- Secciones sin transición → marcar cambios con meta-tags explícitos (`[Build]`, `[Transition]`)
- Letra ininteligible → revisar prosodia: sílabas tónicas en tiempos fuertes
- Duración excesiva (SUNO corta) → estructurar en 3:00-5:00, no más de 5:30

### Anti-AI específico

- La complejidad no es excusa para la falta de gancho. Incluso el pop progresivo necesita un ancla melódica.
- Sin «progresivo de catálogo de biblioteca» (sintetizadores que suenan a PowerPoint).
- Las letras densas deben ser inteligibles. La prosodia es crítica cuando el fraseo es complejo.
- Cada cambio de sección debe estar justificado por la letra, no al revés.

---

## Tabla de progresiones rápidas por género

| Género | Progresión estrella | Alternativa |
|---|---|---|
| Pop | I–V–vi–IV | vi–IV–I–V |
| Balada | I–vi–IV–V | i–VII–VI–V (andaluza) |
| Indie | vi–IV–I–V | I–iii–IV–V |
| Folk | I–IV–V | I–iii–IV–V |
| Synth-pop | I–V–vi–IV (pads) | I–♭VII–IV–I (pedal) |
| Chamber pop | ii–V–I (con extensiones) | I–♭III–IV–I |
| Rock | I–IV–V (power chords) | i–VII–VI |
| Pop progresivo | ii–V–I modulante | Secuencia ascendente |

---

## Recomendaciones para SUNO por género

### Prioridades en Style Prompt

| Género | Capa prioritaria | Capa secundaria | Capa terciaria | Muletilla a evitar |
|--------|-----------------|-----------------|----------------|---------------------|
| Pop | Armonía | Instrumentación | Emoción | «Pop genérico» sin referencia de artista |
| Balada | Dinámica (build-up) | Instrumentos específicos | Voz (entrega) | «Balada épica» sin textura concreta |
| Indie | Textura vocal | Guitarras con carácter | Ambiente/espacio | «Indie» sin adjetivo calificativo |
| Folk | Instrumentos NOMBRADOS | Voz natural/orgánica | Ritmo de guitarra | «Folk» sin fingerpicking/rasgueo |
| Synth-pop | Sintetizadores (analógicos) | Arpegios/patrones | Bajo synth | «80s style» sin referencia concreta |
| Chamber pop | Orquestación (1 por 1) | Dinámica (pp→ff) | Reverb/sala | «Orquestal» sin instrumentos listados |
| Rock | Guitarras (limpias/distorsión) | Ritmo/batería | Referencia de época | «Rock» sin subgénero ni época |
| Pop progresivo | Cambios de sección | Instrumentos diversos | Ancla melódica | «Progresivo» como categoría comodín |

### Peso de cada capa por género (1-5)

| Género | Género | Mood | Instrumentos | Voz | Estructura | Producción |
|--------|--------|------|-------------|-----|-----------|------------|
| Pop | 5 | 4 | 4 | 3 | 3 | 3 |
| Balada | 4 | 5 | 4 | 5 | 3 | 4 |
| Indie | 4 | 5 | 3 | 5 | 2 | 3 |
| Folk | 4 | 3 | 5 | 4 | 2 | 2 |
| Synth-pop | 5 | 4 | 5 | 3 | 4 | 4 |
| Chamber pop | 4 | 4 | 5 | 4 | 3 | 5 |
| Rock | 5 | 4 | 5 | 4 | 3 | 3 |
| Pop progresivo | 4 | 3 | 4 | 3 | 5 | 4 |

### Formato de Style Prompt recomendado por género

| Género | Formato | Ejemplo abreviado |
|--------|---------|--------------------|
| Pop | Conversacional | `Clean modern pop with warm acoustic guitar...` |
| Balada | Conversacional | `Intimate Spanish ballad with piano and strings...` |
| Indie | Híbrido | `Introspective Spanish indie pop with organic guitars...` |
| Folk | Conversacional minimalista | `Spanish folk with fingerpicked acoustic guitar...` |
| Synth-pop | Keyword list | `Analog synth pad, arpeggiator, synth bass, drum machine...` |
| Chamber pop | Conversacional detallado | `Spanish chamber pop with string quartet, grand piano...` |
| Rock | Híbrido con referencia | `Spanish rock with energetic electric guitars... like early Leño...` |
| Pop progresivo | Conversacional amplio | `Spanish progressive pop with multiple movements...` |

---

## Recomendaciones para plataformas por género

| Género | Spotify | Apple Music | TikTok/Reels | YouTube |
|--------|---------|-------------|--------------|---------|
| Pop | Hook en primeros 30s. Portada brillante. Playlist editoriales. | Bio: primera persona. Destacar colaboraciones. | Coreografía o transición visual. 15s del coro. | Lyric video con estética limpia. |
| Balada | Storytelling: la historia detrás. Marathon lists. | Bio: contexto emocional, inspiración. | Fragmento del puente o clímax. Texto superpuesto. | Visualizer atmosférico. Sesión acústica en vivo. |
| Indie | Aesthetic visual coherente. Playlist independientes. | Bio: influencias, proceso creativo. | Backstage, proceso de grabación. | Detrás de cámaras. Lyric video con textura orgánica. |
| Folk | Letra publicada aparte. Sesiones acústicas. | Bio: narrativa de origen. | Fragmento fingerpicking + voz. | Session en estudio. Una toma. |
| Synth-pop | Visual 80s/neón. Playlist synthwave. | Bio: referencias sonoras, gear. | Transiciones visuales retro. Baile. | Animación o CGI retro. |
| Chamber pop | Detalles de grabación/arreglo. Lyric videos. | Bio: formación musical, orquestación. | Fragmento orquestal. Partitura. | Video con músicos reales. |
| Rock | Energía en directo. Playlist de rock español. | Bio: influencias de banda. | Riff de guitarra. Momento enérgico. | Video en vivo. Actuación. |
| Pop progresivo | «Making of». Fans buscan profundidad. | Bio: ambición artística, concepto. | Cambio de sección impactante. | Video conceptual. Animación. |

---

## Flujo de trabajo SUNO: paso a paso

### Paso 1 — Preparar letra con meta-tags

```
[Verse 1]
Letra del verso...
Letra del verso...

[Pre-Chorus]
Transición...

[Chorus]
Estribillo...
```

**Reglas**:
- Usar `[Verse 1]`, `[Verse 2]` (no solo `[Verse]` repetido) para evitar que SUNO fusione secciones
- `[Chorus]` se repite en la letra todas las veces que aparece
- Dejar línea en blanco entre secciones
- Máximo 300 caracteres por sección (aprox 4-6 líneas)
- Si la sección es larga, partirla: `[Chorus]` + `[Post-Chorus]`

### Paso 2 — Construir Style Prompt (máx 1000 chars, ideal 300-500)

**Plantilla**:
```
[Género(s)] with [instrumentos clave], [mood], [Triple-Stack vocal], [producción], like [referencia], [BPM]
```

**Ejemplo real** (de Lo voy a decir, funciona):
```
Intimate Spanish pop ballad with hushed verses, fingerpicked nylon guitar, warm Rhodes, and soft sub-bass, Sparse kick, brushed snare, and close-mic breathy vocals, Chorus opens with layered harmonies, sustained synth pad, and subtle string lines, Gentle tape saturation, plate reverb, and a restrained, confessional late-night texture
```

### Paso 3 — Generar (Fase 1: estructura)

1. Pega el Style Prompt y la letra con meta-tags
2. Elige versión: **v5** (estructura más limpia, drafting rápido) o **v5.5** (más expresividad, personalización)
3. Usa **"Create 2"** para probar prompts nuevos (no generes 4 variaciones hasta validar)
4. Genera 2-4 variaciones
5. Escoge la que mejor respeta la estructura
6. **No te enamores de la primera generación**

### Paso 4 — Refinar (Fase 2: textura)

1. Toca el Triple-Stack vocal si la voz no convence (si usas Voice en v5.5, quita género/carácter y añade producción)
2. Añade instrumentos específicos si falta textura
3. Añade 2-3 restricciones negativas al final: `no reverb wash, no autotune`
4. Marca `[End]` si la canción se desvanece antes del final
5. **Si aparecen artefactos**: añade `clean mix, no distortion` al prompt
6. **Si hay genre drift**: refuerza el género en los tags de sección
7. **ITERAR**: cada generación debe mejorar UN aspecto. Cambia una variable cada vez.

### Paso 5 — Post-producción

| Acción | Cuándo | Cómo |
|--------|--------|------|
| Continue from this moment | SUNO corta antes del final | Pulsa Continue justo donde cortó; copia el resto de letra |
| Replace Section | Una sección no funciona | Reemplaza solo esa sección, mantén el resto |
| Extend | Necesitas más duración | Añade una sección donde termine la canción; usa meta-tag `[Extended Outro]` |
| Cover | Quieres misma letra, género diferente | Usa la misma letra con nuevo Style Prompt |
| Remaster | Artefactos o distorsión en la mezcla | Aplica Remaster para limpiar sin regenerar |

### Troubleshooting rápido (v5 + v5.5)

| Síntoma | Versión | Diagnóstico | Acción en 5 segundos |
|---------|---------|-------------|----------------------|
| Voz genérica | Ambas | Falta Triple-Stack | Añadir carácter + entrega + colocación |
| Coro sin energía | Ambas | Meta-tag o sección larga | Acortar chorus o añadir `[Build]` antes |
| Instrumentos incorrectos | Ambas | Genéricos en prompt | Nombrar 1 por 1 |
| Fade prematuro | Ambas | Sin final marcado | Añadir `[End]` al final |
| Suena a stock | Ambas | Sin referencia | Añadir «like X at their most Y» |
| Letra ininteligible | Ambas | Prosodia rota | Sílabas tónicas en tiempos fuertes |
| Se acelera/ralentiza | Ambas | BPM no fijado | Especificar BPM exacto en prompt |
| Voz incorrecta (M/F) | Ambas | Género vocal no especificado | Añadir `male vocals` o `female vocals` explícito |
| Artefactos / clipping | v5.5 | Descriptores de energía extremos | Cambiar `massive` → `powerful but clear`; añadir `clean mix, no distortion` |
| Genre drift | v5 | Prompt sub-especificado | Reforzar género en tags de sección; mantener 5-8 tags |
| Voz robótica | v5.5 | My Taste aplana expresividad | Añadir vocal performance tags: `[emotional, slightly breathy]` |
| Resultados inconsistentes | Ambas | Sin seed control, variabilidad natural | Generar 3-5 y seleccionar; usar Custom Models para consistencia |

# Especificación: Sintaxis de Meta-Tags en Suno AI

Basado en NotebookLM consulta al notebook "Guía Maestra de Prompts y Estructura para Suno AI" y documentación oficial de Suno.

## Problema

Suno AI interpreta los paréntesis `( )` y los corchetes `[ ]` de forma radicalmente distinta. Usarlos incorrectamente hace que la IA cante instrucciones de producción como si fueran letra.

## Regla fundamental

| Símbolo | Función | ¿Se canta? |
|---------|---------|------------|
| `[ ]` (corchetes) | Instrucciones de producción, secciones, transiciones, voces | **No** |
| `( )` (paréntesis) | Ad-libs, backing vocals, armonías, eco, contenido secundario | **Sí** (~7/10 veces) |

## Usos correctos de cada símbolo

### `[ ]` — Corchetes: Instrucciones que NO se cantan

- **Secciones:** `[Intro]`, `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Outro]`
- **Transiciones:** `[Pre-Chorus]`, `[Build]`, `[Drop]`
- **Voces:** `[spoken]`, `[rap verse]`, `[whisper]`, `[spoken word]` — ver catálogo completo en `specs/010-vocal-direction.md`
- **Género vocal:** `[Male]`, `[Female]`, `[Male|Female|combinated in harmonie]` — ver `specs/009-vocal-gender-tags.md`
- **Producción:** `[Guitar Solo]`, `[Break]`, `[Half-time]`, `[Piano only]`
- **Backing vocals explícitos:** `[Chorus, Backing vocals] Estoy perdido en el eco (coros: "en el eco")`
- **Catálogo completo (72+ tags):** ver `specs/011-suno-meta-tags-complete.md` — instrumentos, género, mood, energía, armonía, ritmo, producción, efectos, texturas

### `( )` — Paréntesis: Contenido que SÍ se canta

- **Ad-libs e improvisaciones:** `(yeah)`, `(oh-oh)`, `(¡Hey!)`, `(Ah-hh)`
- **Llamada y respuesta:** `I remember the day we met (yeah)`
- **Refuerzo anti-omisión:** duplicar línea `(No quiero decir adiós)`
- **Mayúsculas para volumen:** `(HEY!)` fuerza más potencia

## Error frecuente de la IA

La IA tiende a colocar instrucciones de producción entre paréntesis `( )` en lugar de corchetes `[ ]`, lo que provoca que Suno cante esas instrucciones como si fueran parte de la letra.

### Ejemplo documentado: `canciones/dorian-frente-al-cuadro.md`

En esta canción, instrucciones de producción aparecen entre paréntesis:

```
(Arpegiador synth, pads de cuerda, batería a 105 BPM — 8 compases)
(Entra bombo, sube tensión)
(Batería completa, arpegios, cuerdas)
(Staccato de cuerda, pads más oscuros)
(Música se retira. Spoken, tenso, solo voz y un pad)
(Vuelve el arpegiador, creciendo)
(Half-time, batería pesada, cuerdas sostenidas)
(Piano solo, un cello. Arpegiador decayendo.)
(Arpegiador se apaga. Silencio. Una nota de cello.)
```

Suno interpretaría esto como líneas cantadas, no como instrucciones de producción.

### Corrección

Todas las instrucciones de producción deben usar corchetes:

```
[Arpegiador synth, pads de cuerda, batería a 105 BPM — 8 compases]
[Entra bombo, sube tensión]
[Batería completa, arpegios, cuerdas]
```

### Excepción: contenido lírico entre paréntesis

Si una línea entre paréntesis es contenido lírico cantado (no instrucción), es correcto:
```
(Ese joven tan hermoso / Estaba muerto / Desde el principio)
```

## Validación post-composición

1. Identificar todo texto entre paréntesis `( )` en la letra
2. Clasificar cada uno como "instrucción" o "contenido cantado"
3. Las instrucciones deben migrarse a `[ ]`
4. No debe haber instrucciones de producción sueltas sin corchetes

## Sintaxis Avanzada: Tags Parametrizados

Los metatags pueden llevar modificadores descriptivos para control por sección.

### Sintaxis de dos puntos `[Tag: descriptor]`

```
[Verse: whispered vocals, acoustic guitar only]
Walking through the morning mist

[Chorus: full band, powerful vocals]
But I'm awake, I'm alive

[Intro: ambient pads, reversed guitar, ethereal]
```

### Sintaxis de tubería `[Tag | descriptor1 | descriptor2]`

Alternativa a los dos puntos usando `|` como separador:

```
[Chorus | chill | synth lead | soft vocal]
```

**Regla: siempre empezar con estructura.** El tag primario debe ser estructural.

### Sub-descriptores entre paréntesis `[Tag: valor (sub-atributo)]`

```
[Instrumento: Guitarra eléctrica (distorsionada)]
[Instrumento: Cuerdas (legato, fondo)]
```

### Comparación de sintaxis

| Sintaxis | Ejemplo | Uso recomendado |
|----------|---------|-----------------|
| Dos puntos | `[Verse: whispered, acoustic]` | Modificadores simples |
| Tubería | `[Chorus \| full band \| powerful]` | Stacks de atributos |
| Paréntesis | `[Tag: guitar (distorted)]` | Sub-atributos específicos |

### Reglas de apilamiento

- **Máximo 2–4 tags por stack** (más compiten entre sí)
- **Siempre estructura primero**: `[Chorus | ...]`, no `[Chill | ...]`
- Combinar sintaxis diferentes en secciones distintas de la misma canción

### Tags con parámetro temporal

| Tag | Efecto |
|-----|--------|
| `[Tempo: slow]` / `[Tempo: fast]` | Cambio de tempo a nivel de sección |
| `[Key Change]` | Modulación armónica |

## Mecanismo Interno: Cómo Suno Procesa los Tags

Cuando Suno encuentra un metatag estructural como `[Chorus]`:

1. Señala un cambio de sección en el arreglo
2. Aplica características típicas de esa sección (énfasis melódico, instrumentación completa, más energía)
3. Si el mismo tag (ej. `[Chorus]`) aparece de nuevo, intenta **repetir la melodía y el arreglo**

### Implicación de la numeración

- `[Verse 1]` → `[Verse 2]` → Suno entiende que deben tener **melodías diferentes**
- `[Chorus]` repetido textualmente → Suno entiende que debe **repetir la misma melodía**

## Cómo Eliminar el Intro Instrumental Largo

Problema recurrente: Suno genera 10–30 segundos de intro instrumental. Soluciones:

### `[Verse 1]` como primera línea (máximo impacto)

Poner `[Verse 1]` en la línea 1 del campo Lyrics reduce el intro a 3–8 segundos:

```
[Verse 1]
Walking down the empty street
```

### Tags instructivos de entrada rápida

| Tag | Efecto |
|-----|--------|
| `[Intro: Cold Open]` | Arranca en alta energía |
| `[Intro: A Cappella]` | Solo voz, sin instrumentos |
| `[Intro: Drum Count-in]` | "1, 2, 3, 4" y arranca |
| `[Intro: Hook Preview]` | Avance del hook del coro |
| `[Urgent intro]` | Entrada vocal inmediata |
| `[Verse 1 - Singer sings immediately]` | Orden directa |

### Style Prompt quirúrgico

**Eliminar** del Style Prompt: `epic`, `cinematic`, `dramatic`, `progressive`, `atmospheric`, `orchestral`, `grand`.

**Agregar:** `vocal-led`, `vocals upfront`, `no instrumental intro`.

### Tabla de efectividad

| Método | Esfuerzo | Reducción típica |
|--------|----------|------------------|
| `[Verse 1]` línea 1 | Bajo | 30s → 5–8s |
| Tags instructivos | Bajo | 30s → 3–6s |
| `[Urgent intro]` | Bajo | 30s → ~6s |
| Vocal Anchor | Medio | Variable |
| Style Prompt | Medio | Complementario |
| Short Form Mode | Bajo | 30s → 2–5s |
| Song Editor | Medio | Eliminación total |
| Regenerar | Bajo | Variable |

## Checklist de sintaxis Suno

| # | Ítem | Cumple |
|---|------|--------|
| 1 | Toda instrucción de producción usa `[ ]`, no `( )` | |
| 2 | Todo `( )` contiene solo ad-libs, eco o contenido cantado | |
| 3 | Secciones marcadas con `[Verse]`, `[Chorus]`, etc. | |
| 4 | Instrucciones de voz con `[spoken]`, `[whisper]`, etc. | |
| 5 | Tags de género vocal (`[Male]`/`[Female]`) seguidos de espec 009 | |
| 6 | Ad-libs en mayúscula `(HEY!)` para volumen forzado (opcional) | |

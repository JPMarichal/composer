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
- **Voces:** `[spoken]`, `[rap verse]`, `[whisper]`, `[spoken word]`
- **Producción:** `[Guitar Solo]`, `[Break]`, `[Half-time]`, `[Piano only]`
- **Backing vocals explícitos:** `[Chorus, Backing vocals] Estoy perdido en el eco (coros: "en el eco")`

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

## Checklist de sintaxis Suno

| # | Ítem | Cumple |
|---|------|--------|
| 1 | Toda instrucción de producción usa `[ ]`, no `( )` | |
| 2 | Todo `( )` contiene solo ad-libs, eco o contenido cantado | |
| 3 | Secciones marcadas con `[Verse]`, `[Chorus]`, etc. | |
| 4 | Instrucciones de voz con `[spoken]`, `[whisper]`, etc. | |
| 5 | Ad-libs en mayúscula `(HEY!)` para volumen forzado (opcional) | |

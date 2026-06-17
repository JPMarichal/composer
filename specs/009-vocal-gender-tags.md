# Especificación: Tags de Género Vocal en Suno AI — `[Male]` / `[Female]`

Basado en experimento exitoso del autor (junio 2026). La sintaxis `[Male]` y `[Female]` permite asignar qué voz canta cada línea en generaciones con múltiples vocalistas.

## Descubrimiento

Suno AI soporta tags de género vocal como **instrucciones de voz** (no se cantan, igual que `[spoken]` o `[whisper]`). Colocar `[Male]` o `[Female]` al inicio de una línea fuerza a Suno a asignar esa línea a una voz del género indicado.

## Sintaxis

| Tag | Efecto |
|-----|--------|
| `[Male]` | La línea siguiente la canta voz masculina |
| `[Female]` | La línea siguiente la canta voz femenina |
| `[Male\|Female\|combinated in harmonie]` | Ambas voces en armonía (call-and-response o dúo) |

### Reglas

1. El tag afecta **una línea**. Cada línea subsiguiente necesita su propio tag.
2. El tag se coloca **inmediatamente antes** de la línea correspondiente, sin línea en blanco entre tag y texto.
3. El tag NO se canta — pertenece a la categoría `[ ]` de instrucciones de voz (ver `specs/004-suno-syntax.md §Regla fundamental`).

### Ejemplo del experimento

```
[Male]Pensaba mandarte a freír patatas
[Female]Pero te gané la pista robando tu bata
[Male]Merece esta canción una secuela
[Female]Pero no te lo enseñan en la escuela
[Male]Ya casi voy llegando a la recta final
[Female]No tienes idea, vas en la inicial
[Male]Tu charla me distrae de la carrera
[Female]Estoy casi en la meta, ¿qué te desespera?
[Male|Female|combinated in harmonie]Se corre mucho, se gana poco,
porque lo que ganas se lo come el coco,
mejor brindamos por tu salud
y este bimestre no pagas la luz
```

## Prerrequisito: Style Prompt

El style prompt DEBE especificar la presencia de ambas voces. Sin esta indicación, los tags `[Male]`/`[Female]` pueden no activar correctamente la segunda voz.

### Componente vocal en el Style Prompt

Incluir en la sección de tratamiento vocal (Componente 4 de la Fórmula de 6) una descripción de voces alternadas, por ejemplo:

> Male/female lead lines interlock over [...] Male/female call-and-response vocals

### Ejemplo funcional del experimento

```
Slinky electro-pop with bilingual call-and-response vocals,
glossy sidechained synths, bubbly arpeggiators,
and crisp four-on-the-floor kick.
Male/female lead lines interlock over pitched percussion,
elastic bass, and airy vocal chops with delay throws.
Soft vocoder layering, brushed claps,
and a bright, playful, high-energy mix.
```

## Combinación en armonía: `[Male|Female|combinated in harmonie]`

El tag compuesto `[Male|Female|combinated in harmonie]` produce una sección donde ambas voces cantan juntas en armonía. Funciona para coros o secciones de dúo.

### Limitación conocida

En el experimento, la armonía resultó «demasiado perfecta» — ambas voces cantan en sincronía absoluta sin el desfase natural de un dúo real. Para un sonido más orgánico, considerar:

- Intercalar líneas individuales (`[Male]` / `[Female]`) en lugar del tag combinado
- Usar `[Male|Female|combinated in harmonie]` solo para el último tercio del coro
- Agregar instrucciones de producción como `[call and response]` o `[back and forth]` en lugar de la armonía simultánea

## Integración con specs existentes

| Spec | Relación |
|------|----------|
| `004-suno-syntax.md` | Este spec extiende la sintaxis `[ ]` con tags de género vocal |
| `010-vocal-direction.md` | Catálogo completo de dirección vocal (entrega, carácter, efectos) — los tags `[Male]`/`[Female]` son un subconjunto |
| `011-suno-meta-tags-complete.md` | Catálogo de tags no vocales (estructura, mood, instrumentos, etc.) |

## Checklist de verificación

| # | Ítem | Cumple |
|---|------|--------|
| 1 | Style prompt incluye descripción de voces masculina y femenina | |
| 2 | `[Male]`/`[Female]` colocados inmediatamente antes de la línea que afectan | |
| 3 | No hay líneas en blanco entre tag y texto | |
| 4 | `[Male\|Female\|combinated in harmonie]` usado solo para secciones de dúo real | |
| 5 | Si la armonía suena demasiado perfecta, reemplazar con alternancia de líneas | |
| 6 | Modelo de Suno compatible (chirp-v4 o superior) | |

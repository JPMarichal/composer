# Especificación: Dirección Vocal en Suno AI — Catálogo de Tags

Basado en cheat sheet de la comunidad Suno, experimentos del autor y documentación de terceros. Los tags de dirección vocal son instrucciones `[ ]` que controlan cómo se entrega cada línea.

## Regla general

Los tags de dirección vocal se colocan **inmediatamente antes** de la línea que afectan. Se pueden **apilar** múltiples tags para combinar efectos:

```
[whisper][breathy][sad]I'm fine...
```

## 1. Vocal Delivery & Style

Controlan cómo se entrega la voz: textura, intensidad y calidad.

| Tag | Efecto |
|-----|--------|
| `[whisper]` | Susurrado, íntimo, cerca del micrófono |
| `[breathy]` | Aireado, ligero, textura suave |
| `[spoken]` | Hablado, con cadencia natural |
| `[sung]` | Melódico, cantado claro (default) |
| `[yell]` | Potente, abierto, intenso |
| `[scream]` | Alta intensidad, agresivo |
| `[growl]` | Grave, rasposo, con filo |
| `[raspy]` | Textura áspera en la voz |
| `[strained]` | Voz forzada, empujada emocional o vocalmente |
| `[crack in voice]` | Quiebre vocal, emoción, vulnerabilidad |
| `[falsetto]` | Registro agudo, tono ligero |
| `[soulful]` | Rico, sentido, lleno de sentimiento |
| `[smooth]` | Limpio, pulido, tono fácil |
| `[raw]` | Sin filtro, real, sin pulir |
| `[haunting]` | Espectral, etéreo, escalofriante |
| `[dark]` | Pesado, atmosférico, oscuro |
| `[soft]` | Suave, apacible, sumiso |
| `[powerful]` | Fuerte, imponente, impactante |
| `[belting]` | Proyectado a máxima potencia |
| `[emotional]` | Lleno de sentimiento y profundidad |
| `[rap]` | Delivery rítmico hablado |
| `[rap verse]` | Estilo rap o hip-hop |
| `[spoken word]` | Poesía hablada sobre música |
| `[duet]` | Dos voces alternándose |
| `[harmonies]` / `[harmony]` | Múltiples partes vocales simultáneas |
| `[stacked harmonies]` | Armonías vocales en capas múltiples |

## 2. Vocal Character & Tone

Definen el carácter o personalidad de la voz en cada línea.
Los tags de género vocal (`[Male]`/`[Female]`) se detallan en `specs/009-vocal-gender-tags.md`.

| Tag | Efecto |
|-----|--------|
| `[young]` | Voz juvenil |
| `[mature]` | Tono más adulto, con experiencia |
| `[childlike]` | Tono inocente, infantil |
| `[seductive]` | Sensual, cautivador |
| `[confident]` | Seguro, audaz |
| `[vulnerable]` | Abierto, expuesto, sin protección |
| `[angry]` | Lleno de rabia o frustración |
| `[sad]` | Pesado, de tristeza |
| `[playful]` | Divertido, despreocupado |
| `[desperate]` | Urgente, necesidad intensa |
| `[tired]` | Cansado, agotado |
| `[broken]` | Dañado emocionalmente |
| `[hopeful]` | Optimista, edificante |
| `[calm]` | Pacífico, centrado |
| `[melancholic]` | Nostálgico, melancólico |
| `[intense]` | Alta energía, enfocado |
| `[defiant]` | Rebelde, fuerte |
| `[joyful]` | Feliz, celebratorio |
| `[sultry]` | Seductor, suave |
| `[narrator]` | Voz narrativa, como locutor |

### Caracteres de voz

| Tag | Efecto |
|-----|--------|
| `[Raspy Voice]` | Textura áspera |
| `[Clear Voice]` | Limpio, puro |
| `[Deep Voice]` | Registro grave |
| `[High Voice]` | Registro agudo |
| `[Boy]` | Voz masculina joven |
| `[Girl]` | Voz femenina joven |
| `[Man]` | Narrador adulto masculino |
| `[Woman]` | Narradora adulta femenina |

## 3. Vocal Techniques

Técnicas vocales específicas para ejecución melódica.

| Tag | Efecto |
|-----|--------|
| `[falsetto]` | Agudo, aireado |
| `[vibrato]` | Trémolo vocal |
| `[melismatic]` | Múltiples notas por sílaba |
| `[staccato]` | Corto, separado |
| `[legato]` | Suave, conectado |
| `[vocal run]` | Adorno melódico, carrera vocal |
| `[scat]` | Sílabas improvisadas (jazz) |
| `[crooning]` | Suave, íntimo, estilo jazz |
| `[operatic]` | Técnica vocal clásica |
| `[humming]` | Melodía tarareada |
| `[chant]` | Cántico rítmico, tipo mantra |

## 4. Technical & Effects

Añaden procesamiento de producción o efectos vocales.

| Tag | Efecto |
|-----|--------|
| `[echo]` | Repetición, aire, sensación de espacio |
| `[reverb]` | Sonido amplio, ambiental |
| `[delay]` | Ligero rebote o repetición |
| `[distorted]` | Granulado, overdrive, con filo |
| `[lo-fi]` | Baja fidelidad, sonido vintage |
| `[radio effect]` | Filtrado, como radio antigua |
| `[telephone effect]` | Sonido opaco, de teléfono |
| `[autotune]` | Voz afinada electrónicamente, moderno |
| `[vintage]` | Tono clásico, old school |
| `[double tracked]` | Voz doblada, capas |
| `[harmonized]` | Con armonías vocales |
| `[vocal run]` | Adorno melódico, carrera vocal |
| `[ad-lib]` | Frases vocales improvisadas |
| `[background vocals]` | Capas de acompañamiento |
| `[choir]` | Coral, voces en grupo |
| `[stutter]` | Repetición rítmica cortada |
| `[tremolo]` | Efecto trémolo, vibrato intenso |
| `[filter]` | Filtro tonal (low-pass, high-pass) |
| `[widened]` | Voz estéreo amplia |

## 5. Placement & Space

Controlan dónde se sitúa la voz en el espacio sonoro.

| Tag | Efecto |
|-----|--------|
| `[close mic]` | Cerca, íntimo |
| `[far away]` | Distante, al fondo |
| `[in your ear]` | Supercerca, estilo ASMR |
| `[center stage]` | Al frente, dominante |
| `[background]` | Sutil, detrás de la mezcla |
| `[in the distance]` | Lejano, apenas se oye |
| `[dry]` | Sin efectos, directo y limpio |
| `[wide]` | Expansivo, estéreo completo |

## Nota sobre capitalización

Se recomienda:

- **Tags de entrega/estilo**: minúscula (`[whisper]`, `[breathy]`) — consistente con cheat sheets comunitarios.
- **Tags de carácter/técnica**: minúscula (`[sad]`, `[vibrato]`) — misma convención.
- **Tags compuestos**: mayúscula inicial por palabra (`[Crack In Voice]`, `[Raspy Voice]`) o minúscula consistente.
- **Tags de género vocal**: ver `specs/009-vocal-gender-tags.md` (usan mayúscula inicial: `[Male]`, `[Female]`).

## Apilamiento (Stacking)

Múltiples tags pueden combinarse en un mismo bloque para precisión quirúrgica:

```
[whisper][breathy][sad]I'm fine...
[crack in voice]but I'm falling...
[breathy]apart...
[echo]...apart...
[fade out]
```

## Integración con specs existentes

| Spec | Relación |
|------|----------|
| `004-suno-syntax.md` | Sintaxis `[ ]` vs `( )` — este spec extiende el catálogo de instrucciones `[ ]` |
| `009-vocal-gender-tags.md` | Tags `[Male]`/`[Female]` para asignación de género vocal por línea |
| `011-suno-meta-tags-complete.md` | Catálogo de tags no vocales (estructura, mood, instrumentos, producción, etc.) |

## Checklist de verificación

| # | Ítem | Cumple |
|---|------|--------|
| 1 | Los tags de dirección vocal usan `[ ]`, no `( )` | |
| 2 | Los tags se colocan inmediatamente antes de la línea que afectan | |
| 3 | El apilamiento de tags (ej. `[whisper][sad]`) es sintácticamente válido | |
| 4 | Tags de género vocal referenciados a 009, no duplicados aquí | |
| 5 | Tags de estructura (`[verse]`, `[chorus]`) referenciados a 011, no duplicados aquí | |

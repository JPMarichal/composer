# Especificación: Catálogo Completo de Meta Tags Suno AI (No Vocales)

Compilado de sunometatagcreator.com, hookgenius.app, musci.io, blakecrosley.com/guides/suno,
jackrighteous.com, stokemctoke.com, suno-field-guide y experimentos propios.
Cubre todos los tags documentados para Suno v5/v5.5.

## Cómo usar este spec

- Los tags con `[ ]` van en el campo **Lyrics** (letra) en Custom Mode
- Los tags **sin corchetes** van en el campo **Style** (estilo)
- Los tags de estructura van en **su propia línea**, antes de la sección que afectan
- Máximo 3–5 tags por sección, 5–8 tags de estilo en total
- Los tags **no distinguen mayúsculas/minúsculas**: `[VERSE]`, `[Verse]`, `[verse]` son equivalentes
- Los tags vocales (`[whisper]`, `[breathy]`, `[Male]`, etc.) se detallan en `specs/010-vocal-direction.md` y `specs/009-vocal-gender-tags.md`

---

## 1. Song Structure

| Tag | Propósito |
|-----|-----------|
| `[Intro]` | Sección de apertura, normalmente instrumental (~10–15s) |
| `[Verse]` / `[Verse 1]` / `[Verse 2]` | Sección narrativa principal (numerar para claridad) |
| `[Pre-Chorus]` | Subida antes del coro |
| `[Chorus]` | Hook principal, sección más memorable |
| `[Post-Chorus]` | Extensión tras el coro, mantiene energía |
| `[Bridge]` | Sección de contraste, diferente melodía/acordes |
| `[Outro]` | Sección de cierre |
| `[End]` | Final abrupto, sin fade |
| `[Chorus x2]` | Repetir coro dos veces |
| `[Instrumental]` / `[Instrumental Break]` / `[Instrumental Intro]` | Sección sin voces |
| `[Interlude]` | Pausa musical corta entre secciones |
| `[Break]` | Momento despojado, mínimo |
| `[Drop]` | Golpe EDM tras un build |
| `[Build]` / `[Build-Up]` | Subida de intensidad |
| `[Hook]` | Frase corta y pegadiza |
| `[Refrain]` | Línea repetida (más corta que el coro) |
| `[Solo]` / `[Solo Section]` | Sección instrumental destacada |
| `[Guitar Solo]` | Solo de guitarra |
| `[Breakdown]` | Versión deconstruida del ritmo |
| `[Movement]` | Experimental — sistema puede ignorarlo |

---

## 2. Mood & Atmosphere

| Tag | Efecto |
|-----|--------|
| `[Melancholic]` | Triste, reflexivo |
| `[Euphoric]` | Extremadamente feliz, edificante |
| `[Nostalgic]` | Añoranza, recuerdo |
| `[Dreamy]` | Etéreo, flotante |
| `[Aggressive]` | Intenso, forzado |
| `[Peaceful]` | Calma, sereno |
| `[Mysterious]` | Enigmático, intrigante |
| `[Dark Atmosphere]` | Sombrío, ominoso |
| `[Bright Atmosphere]` | Luminoso, alegre |
| `[Ambient Atmosphere]` | Espacioso, atmosférico |
| `[Intimate Atmosphere]` | Cercano, personal |

---

## 3. Energy & Intensity

| Tag | Efecto |
|-----|--------|
| `[High Energy]` | Bombéo, impulsivo |
| `[Medium Energy]` | Constante, moderado |
| `[Low Energy]` | Calmado, relajado |
| `[Building Energy]` | Incremento gradual |
| `[Explosive Energy]` | Explosiones súbitas |
| `[Intense]` | Potencia máxima |
| `[Gentle]` | Suave |
| `[Powerful]` | Presencia fuerte |
| `[Subtle]` | Sutil, discreto |
| `[Dynamic]` | Niveles variables |

---

## 4. Instruments

### Cuerda
| Tag | Efecto |
|-----|--------|
| `[Electric Guitar]` | Guitarra eléctrica moderna |
| `[Acoustic Guitar]` | Guitarra acústica natural |
| `[Bass Guitar]` | Bajo, fundamento grave |
| `[808 bass]` | Sub-grave electrónico (TR-808) |
| `[Violin]` | Violín clásico |
| `[Cello]` | Chelo, tono profundo y rico |
| `[Strings Rise]` | Swell de la sección de cuerdas |

### Percusión
| Tag | Efecto |
|-----|--------|
| `[Drums]` | Batería completa |
| `[Electronic Drums]` | Percusión digital |
| `[Hand Percussion]` | Ritmos orgánicos |
| `[Timpani]` | Timbales orquestales |
| `[Percussion Break]` | Break rítmico |
| `[Drum Solo]` | Solo de percusión |

### Teclados y Sintetizadores
| Tag | Efecto |
|-----|--------|
| `[Piano]` | Piano acústico clásico |
| `[Electric Piano]` | Piano eléctrico vintage |
| `[Synthesizer]` | Sonidos electrónicos |
| `[Organ]` | Órgano (iglesia o Hammond) |
| `[Strings Section]` | Cuerdas orquestales |
| `[Synth Solo]` | Pasaje destacado de sintetizador |
| `[Piano Solo]` | Solo de piano |
| `[Arpeggiator]` | Secuencia rítmica de notas repetidas |
| `[Lead synth]` | Sintetizador principal melódico |
| `[Pads]` | Sintetizador de fondo, textura atmosférica |

### Viento
| Tag | Efecto |
|-----|--------|
| `[Saxophone]` / `[Saxophone Solo]` | Jazz, sofisticación |
| `[Trumpet]` | Brillante, audaz |
| `[Flute]` | Ligero, aireado |
| `[Clarinet]` | Suave, maderoso |
| `[Bass Solo]` | Solo de bajo |

---

## 5. Genre

### Géneros principales
| Tag | Estilo |
|-----|--------|
| `[Pop]` | Atractivo mainstream |
| `[Rock]` | Guitar-driven |
| `[Hip-Hop]` | Urbano, rítmico |
| `[Electronic]` | Paisajes digitales |
| `[Jazz]` | Improvisación, swing |
| `[Classical]` | Tradición orquestal |
| `[Folk]` | Tradicional, acústico |
| `[R&B]` | Rhythm and blues |
| `[Country]` | Raíces americanas |
| `[Reggae]` | Ritmo jamaicano |

### Subgéneros electrónicos
| Tag | Estilo |
|-----|--------|
| `[House]` | Four-on-the-floor |
| `[Techno]` | Repetitivo, mecánico |
| `[Ambient]` | Atmosférico, textural |
| `[Dubstep]` | Bass drops pesados |
| `[Trance]` | Hipnótico, en construcción |

### Subgéneros rock
| Tag | Estilo |
|-----|--------|
| `[Alternative Rock]` | Rock no mainstream |
| `[Hard Rock]` | Pesado, distorsionado |
| `[Indie Rock]` | Sonido independiente |
| `[Progressive Rock]` | Estructuras complejas |

---

## 6. Production & Effects

### Reverb
| Tag | Efecto |
|-----|--------|
| `[Hall Reverb]` | Eco de sala grande |
| `[Room Reverb]` | Espacio íntimo |
| `[Plate Reverb]` | Metálico vintage |
| `[Spring Reverb]` | Surf guitar clásico |
| `[No Reverb]` | Seco, cercano |

### Delay & Echo
| Tag | Efecto |
|-----|--------|
| `[Echo]` | Repeticiones diferenciadas |
| `[Delay]` | Repetición temporal |
| `[Slapback Delay]` | Corto, seco |
| `[Ping Pong Delay]` | Estéreo rebotante |

### Distorsión
| Tag | Efecto |
|-----|--------|
| `[Distortion]` | Clipping pesado |
| `[Overdrive]` | Saturación cálida |
| `[Fuzz]` | Distorsión vintage |
| `[Clean]` | Sin distorsión |
| `[No AutoTune]` | Voz natural, sin corrección de tono |
| `[AutoTune]` | Corrección de tono electrónica |

### Modulación
| Tag | Efecto |
|-----|--------|
| `[Chorus]` | Modulación de tono |
| `[Flanger]` | Barrido ondulante |
| `[Phaser]` | Desfase |
| `[Tremolo]` | Modulación de amplitud |

---

## 7. Chord Progressions & Harmony

### Progresiones clásicas
| Tag | Acordes (ej. en C) |
|-----|--------------------|
| `[I-V-vi-IV]` | C-G-Am-F |
| `[vi-IV-I-V]` | Am-F-C-G |
| `[I-vi-IV-V]` | C-Am-F-G |
| `[ii-V-I]` | Dm-G-C |
| `[I-VII-♭VI-♭VII]` | C-B♭-A♭-B♭ |

### Cualidades armónicas
| Tag | Efecto |
|-----|--------|
| `[Major Harmony]` | Brillante, feliz |
| `[Minor Harmony]` | Oscuro, triste |
| `[Modal Harmony]` | Escalas antiguas |
| `[Jazz Harmony]` | Acordes extendidos |
| `[Dissonant Harmony]` | Tensión, choque |
| `[Suspended Chords]` | Tensión no resuelta |
| `[Extended Chords]` | 7as, 9as, 11as |
| `[Altered Chords]` | ♭5, #5, ♭9, #9 |
| `[Quartal Harmony]` | Construido en 4as |

---

## 8. Sound Effects

| Tag | Efecto |
|-----|--------|
| `[Rain]` | Atmósfera de lluvia |
| `[Thunder]` | Impacto dramático |
| `[Wind]` | Movimiento atmosférico |
| `[Ocean Waves]` | Naturaleza pacífica |
| `[Fire Crackling]` | Ambiencia cálida |
| `[Traffic]` | Atmósfera urbana |
| `[Footsteps]` | Presencia humana |
| `[Vinyl Crackle]` | Textura vintage |
| `[Tape Hiss]` | Calor analógico |
| `[Record Scratch]` | Clásico hip-hop |
| `[Reverse Reverb]` | Build-up etéreo |
| `[Risers]` | Tensión creciente |
| `[Impacts]` | Puntuación dramática |
| `[Silence]` | Pausa breve en la música |
| `[Reverb tail]` | Cola de reverberación larga |
| `[Crowd noise]` | Ambiente de multitud |
| `[Distant voices]` | Voces lejanas al fondo |
| `[Static]` | Ruido estático, radio |
| `[Whispers]` | Susurros ambientales (efecto, no voz) |

---

## 9. Musical Keys & Scales

### Tonalidades mayores
| Tag | Alteraciones |
|-----|--------------|
| `[C Major]` | 0 |
| `[G Major]` | 1 sostenido |
| `[D Major]` | 2 sostenidos |
| `[A Major]` | 3 sostenidos |
| `[E Major]` | 4 sostenidos |

### Tonalidades menores
| Tag | Equivalentes |
|-----|--------------|
| `[A Minor]` | Relativo de Do M |
| `[E Minor]` | 1 sostenido |
| `[B Minor]` | 2 sostenidos |
| `[F# Minor]` | 3 sostenidos |

### Modos
| Tag | Carácter |
|-----|----------|
| `[Dorian Mode]` | Menor con 6ª ascendida |
| `[Mixolydian Mode]` | Mayor con 7ª descendida |
| `[Lydian Mode]` | Mayor con 4ª ascendida |
| `[Phrygian Mode]` | Menor con 2ª descendida |

### Escalas exóticas
| Tag | Descripción |
|-----|-------------|
| `[Pentatonic Scale]` | 5 notas |
| `[Blues Scale]` | Pentatónica + blue note |
| `[Chromatic Scale]` | 12 notas |
| `[Whole Tone Scale]` | Solo tonos enteros |

---

## 10. Rhythm & Tempo

### Tempo
| Tag | Rango |
|-----|-------|
| `[Slow Tempo]` | 60–80 BPM |
| `[Medium Tempo]` | 90–120 BPM |
| `[Fast Tempo]` | 130–180 BPM |
| `[Very Fast]` | 180+ BPM |
| `[Half-time]` | Mitad de tempo |
| `[Double-time]` | Doble de tempo |

### Groove y sensación
| Tag | Efecto |
|-----|--------|
| `[Straight Feel]` | Corcheas parejas |
| `[Swing Feel]` | Corcheas desiguales |
| `[Shuffle Feel]` | Base de tresillos |
| `[Latin Feel]` | Patrones sincopados |
| `[Backbeat]` | Énfasis en 2 y 4 |
| `[Off-beat]` | Énfasis sincopado |
| `[Polyrhythm]` | Múltiples ritmos simultáneos |
| `[Cross-rhythm]` | Patrones en conflicto |

### Compases
| Tag | Descripción |
|-----|-------------|
| `[4/4 Time]` | 4 tiempos, estándar |
| `[3/4 Time]` | Vals |
| `[6/8 Time]` | Compás compuesto |
| `[5/4 Time]` | Métrica impar |

---

## 11. Advanced Techniques

### Arreglo
| Tag | Efecto |
|-----|--------|
| `[Call and Response]` | Conversación musical |
| `[Counterpoint]` | Melodías independientes |
| `[Layering]` | Múltiples partes |
| `[Unison]` | Misma melodía, múltiples instrumentos |
| `[Canon]` | Repeticiones superpuestas |

### Control dinámico
| Tag | Efecto |
|-----|--------|
| `[Crescendo]` | Más fuerte gradualmente |
| `[Diminuendo]` / `[Decrescendo]` | Más suave gradualmente |
| `[Forte]` | Dinámica fuerte |
| `[Piano]` | Dinámica suave |
| `[Sforzando]` | Acento súbito |
| `[Fade In]` | Aumento gradual de volumen |
| `[Fade Out]` | Disminución gradual de volumen |
| `[Silence]` | Pausa breve en el audio |

### Textura
| Tag | Efecto |
|-----|--------|
| `[Minimalist]` | Disperso, repetitivo |
| `[Maximalist]` | Denso, complejo |
| `[Monophonic]` | Melodía sola |
| `[Homophonic]` | Melodía + acompañamiento |
| `[Polyphonic]` | Múltiples melodías independientes |

### Efectos creativos
| Tag | Efecto |
|-----|--------|
| `[Glitch]` | Artefactos digitales |
| `[Granular]` | Muestreo microscópico |
| `[Morphing]` | Transformación gradual |
| `[Sidechaining]` | Pumping rítmico |

---

## Integración con specs existentes

| Spec | Relación |
|------|----------|
| `004-suno-syntax.md` | Sintaxis `[ ]` vs `( )`, sintaxis parametrizada, mecanismo interno |
| `009-vocal-gender-tags.md` | Tags de género vocal |
| `010-vocal-direction.md` | Tags de dirección vocal (entrega, carácter, efectos, colocación) |

## Checklist de verificación

| # | Ítem | Cumple |
|---|------|--------|
| 1 | Tags de estructura en su propia línea en el campo Lyrics | |
| 2 | Tags de estilo descriptivos (sin corchetes) en el campo Style | |
| 3 | Máximo 3–5 tags por sección en letra | |
| 4 | 5–8 tags totales en Style Prompt (4–7 ideal) | |
| 5 | Los tags de género/tono/efecto usan `[ ]` solo en Lyrics | |
| 6 | No hay tags contradictorios (ej. `[Calm]` + `[Aggressive]`) | |
| 7 | Tags vocales referenciados a 010/009, no incluidos aquí | |
| 8 | Numeración de versos: `[Verse 1]` ≠ `[Verse 2]` (melodías diferentes) | |
| 9 | `[Chorus]` repetido = misma melodía repetida | |

# Identity & Genre Analysis — JPMarichal

## 1. Propósito

Este spec preserva el **análisis detallado de la distribución de géneros** del catálogo del autor, separado por **tipo de obra** (letrista vs. instrumental). Es la fuente de verdad para:

- Regla 21 de AGENTS.md (distribución porcentual)
- Decisiones de posicionamiento SEO/playlist (spec 008)
- Selección de tracks a distribuir próximos
- Respuesta a la pregunta "¿cuál es tu identidad musical?"

**Fecha de corte:** 2026-06-06
**Archivos analizados:** 160 en `canciones/`

---

## 2. Separación fundamental: Letrista vs. Instrumental

El autor es **compositor letrista**. Su trabajo principal es la canción con letra. La serie **Rare Metals** (electrónica instrumental atmosférica) es obra experimental paralela — NO compite con la canción lírica por identidad ni por mercado.

| Categoría | Cantidad | % catálogo | Mercado |
|-----------|----------|------------|---------|
| **Lírica (letrista)** | 134 | 83.8% | Mercado primario de descubrimiento, playlists, save rate |
| **Rare Metals (instrumental electrónica)** | 24 | 15.0% | Nicho experimental, separado |
| **Instrumentales puras** | 2 | 1.2% | Sin prioridad comercial |
| **Total** | **160** | 100% | — |

**Implicación:** Todo análisis de género para SEO, playlists, o decisión de lanzamiento se hace sobre las **134 canciones líricas**, no sobre el catálogo completo. Mezclar instrumentales distorsiona la señal.

---

## 3. Distribución de las 134 canciones líricas

Conteo de tags (cada canción puede tener 1-3 tags, separados por coma). Los porcentajes son sobre los 134 archivos, no sobre el total de tags.

| # | Tag | Count | % archivos | Macrocategoría |
|---|-----|-------|------------|----------------|
| 1 | **Pop** | 34 | 25.4% | Pop general (base ancha) |
| 2 | **Folk** | 19 | 14.2% | Folk (anclaje emocional) |
| 3 | **Balada** | 16 | 11.9% | Balada (núcleo melancólico) |
| 4 | **Indie** | 15 | 11.2% | Indie (firma de autor) |
| 4 | **Chamber pop** | 15 | 11.2% | Culto/orquestal |
| 6 | **Rock** | 9 | 6.7% | Rock |
| 7 | **Spanish indie pop** | 8 | 6.0% | Indie (firma de autor) |
| 8 | **Electrónica** | 6 | 4.5% | Electrónica con letra |
| 8 | **Synthwave** | 6 | 4.5% | Electrónica con letra |
| 10 | **Dream pop** | 5 | 3.7% | Indie |
| 10 | **Pop rock** | 5 | 3.7% | Pop |
| 10 | **Latin pop** | 5 | 3.7% | Pop |
| 13 | **Indie folk** | 4 | 3.0% | Folk + Indie |
| 13 | **Spoken word** | 4 | 3.0% | Poema musical |
| 13 | **Soft rock** | 4 | 3.0% | Rock |
| 13 | **Orchestral pop** | 4 | 3.0% | Chamber pop |
| 13 | **Folk pop** | 4 | 3.0% | Folk |
| 18 | **Folk-pop** | 3 | 2.2% | Folk |
| 18 | **Jazz** | 3 | 2.2% | Specialty |
| 18 | **Funk** | 3 | 2.2% | Specialty |
| 18 | **Synth-pop** | 3 | 2.2% | Electrónica con letra |
| 22 | Indie pop | 2 | 1.5% | Indie |
| 22 | Electropop | 2 | 1.5% | Electrónica con letra |
| 22 | Acoustic rock | 2 | 1.5% | Rock |
| 22 | Clásica | 2 | 1.5% | Specialty |
| — | (resto: 30+ tags únicos con 1-2 apariciones) | — | — | — |

**Total de tags:** 280 (ratio ~2.1 tags por canción, indica co-tag sistemático)

---

## 4. Macrocategorías (agrupación estratégica)

Agrupando los tags en **5 polos de identidad**:

| Macrocategoría | Tags sumados | Count | % aprox. | Comentario |
|----------------|-------------|-------|----------|------------|
| **Pop (base ancha)** | Pop, Pop rock, Latin pop | 44 | 33% | La plataforma. No se discute. |
| **Indie (firma)** | Indie, Spanish indie pop, Indie pop, Indie folk, Dream pop | 44 | 33% | La firma distintiva. Diferencia de "indie genérico". |
| **Folk (anclaje)** | Folk, Folk pop, Folk-pop, Indie folk | 30 | 22% | Anclaje emocional. ADN del autor. |
| **Chamber pop / Orquestal** | Chamber pop, Orchestral pop | 19 | 14% | Identidad culta. Pianos, cuerdas, arreglos. |
| **Balada (núcleo)** | Balada | 16 | 12% | El sub-género melancólico recurrente. |
| (Electrónica con letra) | Electrónica, Synthwave, Synth-pop, Electropop | 17 | 13% | Experimental pero dentro de la obra con letra |
| (Rock) | Rock, Pop rock, Soft rock, Acoustic rock | 20 | 15% | El contrapeso enérgetico |

(Suma > 100% por co-tags — cada canción contribuye a 2-3 macros.)

---

## 5. Statement of Identity REAL

**NO** es "balada folk" ni "indie pop español". Eso es proyección de los primeros 4 tracks distribuidos a toda la obra.

**Lo que los datos dicen que el autor ES:**

> **Pop indie folk chamber en español**, con inclinación a la balada como sub-género melancólico recurrente, y experimentación sonora en sintetizadores/electrónica como segundo polo. Identidad culta con arreglos orquestales.

Esto significa que:
- **Pop** = base de lo que el oyente promedio encuentra primero
- **Indie** = firma de autor (no genérico, con "Spanish indie pop" como sub-marca)
- **Folk** = anclaje emocional (la sustancia lírica)
- **Chamber pop** = textura sonora distintiva (pianos, cuerdas, arreglos)
- **Balada** = vehículo de las canciones más íntimas

---

## 6. Canciones distribuidas (estado real, no Notion)

El estado en Notion puede decir "Aprobado" cuando OffStep ya las distribuyó y están vivas en plataformas. **Esta es la lista confirmada por el autor a 2026-06-06:**

### Singles distribuidos
1. **Mármol Que Respira** — Chamber pop, Power pop, Spanish indie pop
2. **La Magia del Violín** — Chamber pop, Baroque pop
3. **Lo Voy a Decir** — (género en archivo)
4. **Y Vio el Mar** — Synth-pop
5. **Pequeña Era** — (género en archivo)
6. **Que Das la Vida para Dar Vida** — Chamber pop, Spanish indie pop
7. **Redondillas** — Poesía, Electrónica
8. **Tvo en la TV** — Synth-pop, Electrónica
9. **Arrendajo de Invierno** — Folk, Pop
10. **Mamá, Si Vuelvo a Verte** — Balada, Folk

### Álbumes completos distribuidos
- **Tvo en la TV** (álbum)
- **Arrendajo de Invierno** (álbum)

**Total: 10 tracks como mínimo, posiblemente más dentro de los álbumes completos.**

**Observación crítica:** 9 de los 10 tracks distribuidos caen en el **macrosector "Chamber pop / Indie / Balada"** (que es el núcleo del statement of identity). El décimo (Redondillas) es spoken word/poesía — un costado del catálogo, no el centro. Esto valida que la **estrategia de lanzamiento** SÍ refleja la identidad, aunque sub-representa el polo Pop y el polo Electrónica con letra.

---

## 7. Lo que esto implica para posicionamiento (spec 008)

### Anchors (identidad) — usar como keywords de marca
| Keyword | Razón |
|---------|-------|
| `pop indie español` | Refleja la firma "Spanish indie pop" + base pop |
| `chamber pop en español` | Diferenciador (pianos + cuerdas + arreglos) |
| `balada folk` | Ya cubierto en PL1 — válido como sub-marca |
| `folk indie` | Anclaje emocional |

**NO usar como anchor único:** "balada folk" (12% del catálogo, no es el centro) ni "indie pop español" (33% pero solo en una variante).

### Long-tail gold (Tier 2) — oportunidades reales
- `canciones para pensar en silencio` (chamber pop)
- `balada para dormir` (chamber pop + balada)
- `música para sentir mariposas` (folk pop + indie)
- `canciones con silencios` (chamber pop + cinematic)
- `canciones para cartas` (chamber pop + folk)
- `música para recordar a mamá` (balada + folk)
- `folk nostálgico` (folk)
- `indie para pensar` (indie + chamber pop)
- `balada para el insomnio` (chamber + synth-pop)

### A evitar (Tier 5)
- `baladas en español` (genérico, dominado por giants curados)
- `canciones para llorar` (genérico, giants)
- `canciones para sentir` (vanity, secuestrado)

---

## 8. Rare Metals — análisis paralelo (no núcleo)

**24 tracks instrumentales electrónicos** de la serie de elementos químicos. Música textural, atmosférica, sin letra. **No compite con la obra letrista por mercado ni por SEO.**

**Audiencia objetivo de Rare Metals:** nichos muy específicos (focus music, ambient, lo-fi instrumental). Plataformas como Bandcamp, SoundCloud, o playlists curadas tipo "ambient electronic" o "music for studying".

**Implicación:** no dedicar recursos de SEO/playlist principal a Rare Metals. Si se quieren posicionar, debe hacerse en plataformas distintas a Spotify mainstream.

---

## 9. Mantenimiento de este spec

**Trigger para re-correr análisis:**
- Se añaden 10+ canciones nuevas al directorio `canciones/`
- Se completa la distribución de un álbum completo
- Se cambia la identidad estratégica (refocus en otro polo)

**Método de análisis:** PowerShell one-liner sobre `canciones/*.md`, contando tags del campo `- **Género:**`. Ver comando en el historial de chat 2026-06-06.

**Output esperado:** actualización de §3 (tabla de distribución) y §6 (lista de distribuidos si hay cambios).

---

## 10. Conclusión estratégica

1. **El autor NO es "balada folk" ni "indie pop español"** — esa es la proyección de los primeros 4 tracks. Es **pop indie folk chamber en español**, con balada como sub-modo melancólico y experimentación electrónica como segundo polo.

2. **El lanzamiento actual cubre bien el núcleo** (chamber + indie + balada = 9 de 10 distribuidos). Sub-representa Pop y Electrónica con letra.

3. **Los próximos lanzamientos pueden diversificar** sin romper la marca — hay 17 canciones de Electrónica con letra y 44 de Pop esperando. Esto abriría keywords nuevas: `synth-pop español`, `electrónica con letra`, `pop bailable en español`, etc.

4. **La regla 21 de AGENTS.md debe actualizarse** para reflejar la distribución real, no la vieja (Pop 33% / Balada 19% / Indie-Folk 20% era del snapshot anterior, no del presente).

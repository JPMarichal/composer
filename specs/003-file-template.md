# Especificación: Template de Archivo de Canción

## Descripción

Formato estandarizado para archivos `.md` de canciones en `canciones/`, alineado 1:1 con los campos de la base de datos "Canciones de JPMarichal" en Notion.

## Estructura del archivo

```markdown
# <Título de la canción>

## Metadatos

### Notion DB

- **Título de la canción:** <obligatorio>
- **Género:** <obligatorio>
- **Tipo:** Canción | Instrumental
- **Año:** <aaaa>
- **Fecha de composición:** <aaaa-mm-dd>
- **Fecha de lanzamiento:** <aaaa-mm-dd | vacío>
- **Estado de publicación:** Sin procesar | Generada en SUNO | Pendiente de publicación | Distribuida en plataformas
- **Generador:** SUNO | Claude + SUNO | Manual (sin IA)
- **Temas:** <comma-separated>
- **Distribuidor:** OffStep | SoundOn | <vacío>
- **ISRC:** <vacío>
- **UPC:** <vacío | código de 12 dígitos>
- **Álbum:** <vacío | nombre del álbum>
- **NotionPageID:** <vacío | uuid>
- **Música:** <vacío | ruta al archivo>

### Producción musical

- **BPM:** <número>
- **Compás:** <fracción>
- **Tonalidad:** <tonalidad>
- **Progresión:** <acordes>
- **Estructura:** <secciones>

## Armonía

- **Progresión base:** <detalle>
- **Patrón rítmico:** <descripción>
- **Dinámica por sección:** <descripción>
- **Riff melódico:** <descripción>

### Acordes por sección

| Sección | Acordes | Notas |
|---------|---------|-------|

## Descripción

La descripción es un texto de 1-2 párrafos con esta estructura:

1. **Hook:** género, tempo (si se conoce), instrumentación destacada, para qué momento escucharla («Para escuchar cuando...»)
2. **Tesis:** de qué trata realmente la canción, sin spoilear la letra completa
3. **Simbolismo explícito:** si hay un objeto central, explicar su significado (ej. «el cajón no es un mueble: es el corazón»)
4. **Conexión:** frase que comience con «Si alguna vez has...» que conecte con la vivencia del oyente
5. **Cierre:** una línea o imagen breve que resuma el mensaje

**Reglas:**
- Máximo 2 párrafos, preferiblemente 1
- No usar la voz pasiva ni «esta canción trata sobre» — ir directo al grano
- Cada frase debe pasar la prueba del bar: «¿lo diría alguien en una conversación real?»
- Un gancho al inicio («Folk orquestal con chelo y violín. Para escuchar cuando...») sin perder tiempo
- Para instrumentales de elementos: género + sintetizadores → para qué escucharla → propiedad del elemento → conexión musical → cierre poético

## Style Prompt

```
<prompt de estilo para SUNO>
```

### Guía del Style Prompt

**Límite:** 1 000 caracteres. Punto dulce: 4–7 descriptores clave.

**Fórmula de 6 componentes (por orden de prioridad):**

1. **Género + Era** — "90s Grunge", no "Rock". Es la base.
2. **Tempo y patrón rítmico** — BPM exacto (126 BPM) o término italiano (Adagio, Presto). Puede incluir "syncopated", "half-time feel".
3. **Instrumentación y riffs** — Instrumentos concretos + cómo suenan: "distorted electric guitar riff", "pounding 808s", "evolving arpeggios", "jazzy Rhodes chords". Máximo 4–5 instrumentos.
4. **Tratamiento vocal** — Definir al cantante como personaje: registro (barítono, soprano, tenor), textura (raspy, breathy, soulful, husky), entrega (belting, whispered, spoken word, melismatic).
5. **Ambiente y tonalidad** — Estado de ánimo + clave musical: "melancholic, C Minor, cinematic atmosphere". Tonalidad mayor = brillante; menor = oscura.
6. **Intención de mezcla** — "polished radio mix", "wide stereo", "lo-fi texture", "studio grade".

**Reglas clave:**
- Suno da más peso a las primeras palabras → empezar siempre con género + tonalidad/BPM
- Evitar nombres de artistas reales (filtros de copyright). Usar descriptores de su estilo
- No saturar con términos vagos ("nice", "cool")
- Las progresiones armónicas (I-V-vi-IV) y tipos de acordes (power chords, open chords) ayudan a la IA a entender la armonía deseada
- Para voces no robóticas, definir al cantante como personaje (edad, registro, contexto emocional)

**Ejemplo efectivo:**
```
Melancholic 90s Grunge, 90 BPM, D minor, distorted electric guitar riff, heavy drums, raspy male vocals
```

**Ejemplo experto (personaje):**
```
The vocalist is a 40-year-old man with a smooth, velvety baritone, reflecting on lost love in a near-empty jazz club at 2 AM. Warm and intimate delivery with subtle cracks of vulnerability.
```

## Letra

<letra completa con meta-tags [Verse], [Chorus], etc.>

---

## Esquema de rima

<detalle del esquema>

## Checklist Anti-AI

| # | Safeguard | Cumple |
|---|-----------|--------|

## Changelog de Autoría

<registro de iteraciones>
```

## Reglas

1. El nombre del archivo debe ser el título en kebab-case: `es-la-misma-lluvia.md`
2. El H1 debe coincidir exactamente con el título de la canción
3. Los campos de `### Notion DB` deben reflejar exactamente los valores enviados a Notion
4. Los campos vacíos se dejan con valor `<vacío>` o simplemente vacío tras el `:`
5. `NotionPageID` se actualiza automáticamente al hacer sync; no se edita manualmente
6. Toda canión debe incluir `## Armonía`, `## Descripción`, `## Style Prompt`, `## Letra`, `## Checklist Anti-AI` y `## Changelog de Autoría`
6. `## Letra` lleva los meta-tags de sección (`[Verse]`, `[Chorus]`, etc.) — la versión sin tags va en el cuerpo de la página de Notion
7. Toda instrucción de producción debe usar corchetes `[ ]`, no paréntesis `( )`. Ver `specs/004-suno-syntax.md`.

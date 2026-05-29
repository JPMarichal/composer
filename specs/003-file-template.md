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

<tesis o resumen de 2-4 líneas>

## Style Prompt

```
<prompt de estilo para SUNO>
```

---

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

const [,, title, genre] = process.argv;
if (!title || !genre) {
  console.error("Uso: node src/template.js \"Título\" \"Género\"");
  process.exit(1);
}
const slug = title
  .toLowerCase()
  .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
  .replace(/[^a-z0-9\s-]/g, "")
  .trim()
  .replace(/\s+/g, "-")
  .replace(/-+/g, "-");
const content = `# ${title}

## Metadatos

### Notion DB

- **Título de la canción:** ${title}
- **Género:** ${genre}
- **Tipo:** Canción
- **Año:**
- **Fecha de composición:**
- **Fecha de lanzamiento:**
- **Estado de publicación:** Sin procesar
- **Generador:**
- **Temas:**
- **Distribuidor:**
- **ISRC:**
- **UPC:**
- **Álbum:**
- **Música:**

### Producción musical

- **BPM:**
- **Compás:**
- **Tonalidad:**
- **Progresión:**
- **Estructura:**

## Armonía

- **Progresión base:**
- **Patrón rítmico:**
- **Dinámica por sección:**
- **Riff melódico:**

### Acordes por sección

| Sección | Acordes | Notas |
|---------|---------|-------|

## Descripción



## Style Prompt

\`\`\`

\`\`\`

---

## Letra

---

## Esquema de rima

## Checklist Anti-AI

| # | Safeguard | Cumple |
|---|-----------|--------|

## Changelog de Autoría
`;
const fs = require("fs");
const path = `canciones/${slug}.md`;
if (fs.existsSync(path)) {
  console.error(`Ya existe: ${path}`);
  process.exit(1);
}
fs.writeFileSync(path, content.trimStart());
console.log(`Creado: ${path}`);

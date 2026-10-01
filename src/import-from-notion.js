const { Client } = require("@notionhq/client");
require("dotenv").config();

if (!globalThis.fetch) globalThis.fetch = require("node-fetch");

const notion = new Client({ auth: process.env.NOTION_TOKEN });

const DATA_SOURCE_ID = "86be0268-5d13-44e1-bbde-e5944c7b8d44";

function slugify(text) {
  return text
    .toLowerCase()
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

function val(prop) {
  if (!prop) return "";
  switch (prop.type) {
    case "title": return prop.title?.map(t => t.plain_text).join("") || "";
    case "rich_text": return prop.rich_text?.map(t => t.plain_text).join("") || "";
    case "select": return prop.select?.name || "";
    case "multi_select": return prop.multi_select?.map(s => s.name).join(", ") || "";
    case "number": return prop.number != null ? String(prop.number) : "";
    case "date": return prop.date?.start || "";
    case "status": return prop.status?.name || "";
    default: return "";
  }
}

async function getPageBlocks(pageId) {
  try {
    const resp = await notion.blocks.children.list({ block_id: pageId });
    return resp.results
      .filter(b => b.type === "paragraph")
      .map(b => b.paragraph.rich_text.map(t => t.plain_text).join(""))
      .filter(t => t.trim());
  } catch {
    return [];
  }
}

async function main() {
  const resp = await notion.dataSources.query({ data_source_id: DATA_SOURCE_ID });
  const pages = resp.results;

  console.log(`Encontradas ${pages.length} canciones en Notion.\n`);

  for (const page of pages) {
    const p = page.properties;
    const title = val(p["Título de la canción"]);
    const slug = slugify(title);
    const path = `canciones/${slug}.md`;

    if (require("fs").existsSync(path)) {
      console.log(`  ↻  ${title} — ya existe localmente, omitida`);
      continue;
    }

    const genre = val(p["Género"]);
    const tipo = val(p["Tipo"]) || "Canción";
    const year = val(p["Año"]);
    const fecha = val(p["Fecha de composición"]);
    const estado = val(p["Estado de publicación"]) || "Sin procesar";
    const generador = val(p["Generador"]);
    const temas = val(p["Temas"]);
    const distribuidor = val(p["Distribuidor"]);
    const isrc = val(p["ISRC"]);
    const upc = val(p["UPC"]);
    const fechaLanzamiento = val(p["Fecha de lanzamiento"]);
    const album = val(p["Álbum"]);
    const descripcion = val(p["Descripción"]);
    const stylePrompt = val(p["Estilo SUNO"]);
    const taggedLyrics = val(p["TaggedLyrics"]);

    const blocks = await getPageBlocks(page.id);

    const content = `# ${title}

## Metadatos

### Notion DB

- **Título de la canción:** ${title}
- **Género:** ${genre}
- **Tipo:** ${tipo}
- **Año:** ${year}
- **Fecha de composición:** ${fecha}
- **Estado de publicación:** ${estado}
- **Generador:** ${generador}
- **Temas:** ${temas}
- **Distribuidor:** ${distribuidor}
- **ISRC:** ${isrc}
- **UPC:** ${upc}
- **Fecha de lanzamiento:** ${fechaLanzamiento}
- **Álbum:** ${album}
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

${descripcion || ""}

## Style Prompt

\`\`\`
${stylePrompt || ""}
\`\`\`

---

## Letra

${taggedLyrics || blocks.join("\n") || ""}

---

## Esquema de rima

## Checklist Anti-AI

| # | Safeguard | Cumple |
|---|-----------|--------|

## Changelog de Autoría
`;

    require("fs").writeFileSync(path, content.trimStart());
    console.log(`  ✓  ${title} → ${path}`);
  }

  console.log("\nImportación completada.");
}

main().catch(console.error);

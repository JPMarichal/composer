const { Client } = require("@notionhq/client");
require("dotenv").config();
if (!globalThis.fetch) globalThis.fetch = require("node-fetch");

const notion = new Client({ auth: process.env.NOTION_TOKEN });

const [,, filePath] = process.argv;
if (!filePath) {
  console.error("Uso: node src/notion-sync.js canciones/mi-cancion.md");
  process.exit(1);
}

const fs = require("fs");
const content = fs.readFileSync(filePath, "utf-8");

function extractField(label) {
  const re = new RegExp(`- \\*\\*${label}:\\*\\*[ \\t]*(.*)`);
  const m = content.match(re);
  return m ? m[1].trim() : "";
}

const title = extractField("Título de la canción");
const genreRaw = extractField("Género");
const tipo = extractField("Tipo") || "Canción";
const year = parseInt(extractField("Año"), 10) || null;
const fecha = extractField("Fecha de composición");
const fechaLanzamiento = extractField("Fecha de lanzamiento");
const estado = extractField("Estado de publicación") || "Sin procesar";
const generador = extractField("Generador");
const temasRaw = extractField("Temas");
const isrc = extractField("ISRC");
const upc = extractField("UPC");
const distribuidor = extractField("Distribuidor");
const descripcion = extractSection("Descripción");

// StylePrompt and TaggedLyrics are in sections, not simple fields
function extractSection(sectionName) {
  const re = new RegExp(`## ${sectionName}\\n+([\\s\\S]*?)(?:\\n## |\\n---|$)`);
  const m = content.match(re);
  return m ? m[1].trim() : "";
}

const stylePrompt = extractSection("Style Prompt").replace(/^```\n?|```$/g, "").trim();
const taggedLyrics = extractSection("Letra");

const slug = title
  .toLowerCase()
  .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
  .replace(/[^a-z0-9\s-]/g, "").trim()
  .replace(/\s+/g, "-").replace(/-+/g, "-");

const DATA_SOURCE_ID = "86be0268-5d13-44e1-bbde-e5944c7b8d44";

function buildProperties() {
  const props = {
    "Título de la canción": { title: [{ type: "text", text: { content: title } }] },
    "Tipo": { select: { name: tipo } },
    "Estado de publicación": { status: { name: estado === "Sin procesar" ? "Sin procesar" : estado } },
  };

  if (genreRaw) {
    const genres = genreRaw.split(",").map(g => g.trim()).filter(Boolean);
    props["Género"] = { multi_select: genres.map(g => ({ name: g })) };
  }
  if (year) props["Año"] = { number: year };
  if (fecha) props["Fecha de composición"] = { date: { start: fecha } };
  if (fechaLanzamiento) props["Fecha de lanzamiento"] = { date: { start: fechaLanzamiento } };
  if (generador) props["Generador"] = { select: { name: generador } };
  if (temasRaw) {
    const temas = temasRaw.split(",").map(t => t.trim()).filter(Boolean);
    props["Temas"] = { multi_select: temas.map(t => ({ name: t })) };
  }
  if (isrc) props["ISRC"] = { rich_text: [{ type: "text", text: { content: isrc } }] };
  if (upc) props["UPC"] = { rich_text: [{ type: "text", text: { content: upc } }] };
  if (descripcion) props["Descripción"] = { rich_text: [{ type: "text", text: { content: descripcion } }] };
  if (stylePrompt) props["Estilo SUNO"] = { rich_text: [{ type: "text", text: { content: stylePrompt } }] };
  if (taggedLyrics) props["TaggedLyrics"] = { rich_text: [{ type: "text", text: { content: taggedLyrics } }] };
  props["Álbum"] = { relation: [] };
  if (distribuidor) {
    const distList = distribuidor.split(",").map(d => d.trim()).filter(Boolean);
    props["Distribuidor"] = { multi_select: distList.map(d => ({ name: d })) };
  }
  props["Música "] = { files: [] };

  return props;
}

function buildBodyBlocks() {
  if (!taggedLyrics) return undefined;
  const lines = taggedLyrics
    .split("\n")
    .filter(l => {
      const trimmed = l.trim();
      if (!trimmed) return true;
      return !l.startsWith("[") && !l.startsWith("(") && !l.startsWith(")");
    });
  const blocks = [];
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      blocks.push({ object: "block", type: "paragraph", paragraph: { rich_text: [] } });
    } else {
      blocks.push({
        object: "block",
        type: "paragraph",
        paragraph: { rich_text: [{ type: "text", text: { content: trimmed } }] },
      });
    }
  }
  return blocks.length ? blocks : undefined;
}

async function findExistingPage() {
  const resp = await notion.dataSources.query({ data_source_id: DATA_SOURCE_ID });
  for (const page of resp.results) {
    const tProp = page.properties["Título de la canción"];
    const existingTitle = tProp?.title?.map(t => t.plain_text).join("") || "";
    if (existingTitle.toLowerCase() === title.toLowerCase()) {
      return page.id;
    }
  }
  return null;
}

async function replaceBlocks(pageId, children) {
  const existing = await notion.blocks.children.list({ block_id: pageId });
  for (const block of existing.results) {
    await notion.blocks.delete({ block_id: block.id }).catch(() => {});
  }
  if (children) {
    await notion.blocks.children.append({ block_id: pageId, children });
  }
}

async function main() {
  const properties = buildProperties();
  const children = buildBodyBlocks();
  const existingId = await findExistingPage();

  if (existingId) {
    await notion.pages.update({ page_id: existingId, properties });
    await replaceBlocks(existingId, children);
    const pageUrl = `https://www.notion.so/${existingId.replace(/-/g, "")}`;
    console.log(`✓ Actualizado en Notion: ${title}`);
    console.log(`  ${pageUrl}`);
  } else {
    const resp = await notion.pages.create({
      parent: { data_source_id: DATA_SOURCE_ID, type: "data_source_id" },
      properties,
      children,
    });
    const pageUrl = resp.url || `https://www.notion.so/${resp.id.replace(/-/g, "")}`;
    console.log(`✓ Creado en Notion: ${title}`);
    console.log(`  ${pageUrl}`);
  }
}

main().catch(err => {
  console.error("Error:", err.message);
  process.exit(1);
});

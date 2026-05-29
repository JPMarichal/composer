#!/usr/bin/env node
require("dotenv").config();
if (!globalThis.fetch) globalThis.fetch = require("node-fetch");
const { Server } = require("@modelcontextprotocol/sdk/server/index.js");
const { StdioServerTransport } = require("@modelcontextprotocol/sdk/server/stdio.js");
const { Client } = require("@notionhq/client");
const { ListToolsRequestSchema, CallToolRequestSchema } = require("@modelcontextprotocol/sdk/types.js");

const notion = new Client({ auth: process.env.NOTION_TOKEN });

const server = new Server(
  { name: "notion-local", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "list_databases",
      description: "Lista las bases de datos de Notion del workspace",
      inputSchema: { type: "object", properties: {} },
    },
    {
      name: "query_database",
      description: "Consulta una base de datos de Notion por su ID",
      inputSchema: {
        type: "object",
        properties: {
          database_id: { type: "string", description: "ID de la base de datos" },
        },
        required: ["database_id"],
      },
    },
    {
      name: "get_page",
      description: "Obtiene el contenido de una página de Notion",
      inputSchema: {
        type: "object",
        properties: {
          page_id: { type: "string", description: "ID de la página" },
        },
        required: ["page_id"],
      },
    },
    {
      name: "search",
      description: "Busca en Notion por texto",
      inputSchema: {
        type: "object",
        properties: {
          query: { type: "string", description: "Texto a buscar" },
        },
        required: ["query"],
      },
    },
    {
      name: "create_page",
      description: "Crea una página en una base de datos de Notion",
      inputSchema: {
        type: "object",
        properties: {
          database_id: { type: "string", description: "ID de la base de datos (database_id o data_source_id)" },
          parent_type: { type: "string", enum: ["database_id", "data_source_id"], description: "Tipo de parent (default: database_id)" },
          properties: { type: "object", description: "Propiedades de la página" },
          children: {
            type: "array",
            description: "Bloques de contenido (opcional)",
            items: { type: "object" },
          },
        },
        required: ["database_id", "properties"],
      },
    },
    {
      name: "append_blocks",
      description: "Añade bloques de contenido a una página existente",
      inputSchema: {
        type: "object",
        properties: {
          block_id: { type: "string", description: "ID del bloque/página padre" },
          children: {
            type: "array",
            description: "Bloques a añadir",
            items: { type: "object" },
          },
        },
        required: ["block_id", "children"],
      },
    },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "list_databases": {
      const resp = await notion.search({ filter: { value: "data_source", property: "object" } });
      return {
        content: resp.results.map((db) => ({
          type: "text",
          text: `${db.id}: ${db.title?.[0]?.plain_text || "sin título"}`,
        })),
      };
    }
    case "query_database": {
      const resp = await notion.dataSources.query({ data_source_id: args.database_id });
      return {
        content: resp.results.map((page) => ({
          type: "text",
          text: JSON.stringify(page, null, 2),
        })),
      };
    }
    case "get_page": {
      const [page, blocks] = await Promise.all([
        notion.pages.retrieve({ page_id: args.page_id }),
        notion.blocks.children.list({ block_id: args.page_id }),
      ]);
      return {
        content: [
          { type: "text", text: JSON.stringify(page, null, 2) },
          { type: "text", text: JSON.stringify(blocks.results, null, 2) },
        ],
      };
    }
    case "search": {
      const resp = await notion.search({ query: args.query });
      return {
        content: resp.results.map((r) => ({
          type: "text",
          text: `${r.id}: ${r.object} — ${r.title?.[0]?.plain_text || r.url || "sin título"}`,
        })),
      };
    }
    case "create_page": {
      const parentType = args.parent_type || "database_id";
      const parent = parentType === "data_source_id"
        ? { data_source_id: args.database_id, type: "data_source_id" }
        : { database_id: args.database_id, type: "database_id" };
      const resp = await notion.pages.create({
        parent,
        properties: args.properties,
        children: args.children,
      });
      return { content: [{ type: "text", text: JSON.stringify(resp, null, 2) }] };
    }
    case "append_blocks": {
      const resp = await notion.blocks.children.append({
        block_id: args.block_id,
        children: args.children,
      });
      return { content: [{ type: "text", text: JSON.stringify(resp, null, 2) }] };
    }
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
});

const transport = new StdioServerTransport();
server.connect(transport);

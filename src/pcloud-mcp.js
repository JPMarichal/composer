require("dotenv").config();
if (!globalThis.fetch) globalThis.fetch = require("node-fetch");

const { Server } = require("@modelcontextprotocol/sdk/server/index.js");
const { StdioServerTransport } = require("@modelcontextprotocol/sdk/server/stdio.js");
const { ListToolsRequestSchema, CallToolRequestSchema } = require("@modelcontextprotocol/sdk/types.js");

const API_HOST = process.env.PCLOUD_API_HOST || "api.pcloud.com";
const FALLBACK_API_HOSTS = ["eapi.pcloud.com", "api.pcloud.com"];
const USERNAME = process.env.PCLOUD_USERNAME;
const PASSWORD = process.env.PCLOUD_PASSWORD;
const ACCESS_TOKEN = process.env.PCLOUD_AUTH_TOKEN || process.env.PCLOUD_ACCESS_TOKEN;
const CLIENT_ID = process.env.PCLOUD_CLIENT_ID;
const CLIENT_SECRET = process.env.PCLOUD_CLIENT_SECRET;
const OAUTH_CODE = process.env.PCLOUD_OAUTH_CODE;
const BASE_FOLDER = process.env.PCLOUD_BASE_FOLDER || "0";

let authToken = null;
let tokenExpires = 0;
let currentApiHost = API_HOST;

function getBaseUrl(host = currentApiHost) {
  return `https://${host}`;
}

function getCandidateHosts() {
  return [...new Set([API_HOST, ...FALLBACK_API_HOSTS].filter(Boolean))];
}

function summarizeAuthFailure(host, resp) {
  if (!resp || typeof resp !== "object") return `${host}: invalid response`;
  return `${host}: ${resp.error || "Unknown error"} (${resp.result ?? "no result"})`;
}

function api(method, params = {}, host = currentApiHost) {
  const url = new URL(`${getBaseUrl(host)}/${method}`);
  if (authToken) params.auth = authToken;
  const body = new URLSearchParams();
  for (const [k, v] of Object.entries(params)) {
    if (v !== undefined && v !== null) body.append(k, String(v));
  }
  return fetch(url.toString(), {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  }).then((r) => r.json());
}

async function ensureAuth() {
  if (authToken && Date.now() < tokenExpires) return;

  const failures = [];

  if (CLIENT_ID && CLIENT_SECRET && OAUTH_CODE) {
    const oauthResp = await api(
      "oauth2_token",
      {
        client_id: CLIENT_ID,
        client_secret: CLIENT_SECRET,
        code: OAUTH_CODE,
      },
      "api.pcloud.com"
    );

    if (oauthResp.result !== 0 || !oauthResp.access_token) {
      throw new Error(`pCloud oauth2_token exchange failed: ${JSON.stringify(oauthResp)}`);
    }

    for (const host of getCandidateHosts()) {
      const resp = await api("userinfo", { auth: oauthResp.access_token }, host);
      if (resp.result === 0) {
        authToken = oauthResp.access_token;
        tokenExpires = Number.MAX_SAFE_INTEGER;
        currentApiHost = host;
        return;
      }
      failures.push(summarizeAuthFailure(host, resp));
    }

    throw new Error(
      `pCloud oauth token exchange succeeded but validation failed. ${failures.join(" | ")}`
    );
  }

  if (ACCESS_TOKEN) {
    for (const host of getCandidateHosts()) {
      const resp = await api("userinfo", { auth: ACCESS_TOKEN }, host);
      if (resp.result === 0) {
        authToken = ACCESS_TOKEN;
        tokenExpires = Number.MAX_SAFE_INTEGER;
        currentApiHost = host;
        return;
      }
      failures.push(summarizeAuthFailure(host, resp));
    }

    throw new Error(
      `Configured pCloud access token was rejected. ${failures.join(" | ")}`
    );
  }

  if (!USERNAME || !PASSWORD) {
    throw new Error(
      "Missing pCloud credentials. Set PCLOUD_AUTH_TOKEN or PCLOUD_ACCESS_TOKEN, provide PCLOUD_CLIENT_ID/PCLOUD_CLIENT_SECRET/PCLOUD_OAUTH_CODE, or provide PCLOUD_USERNAME and PCLOUD_PASSWORD."
    );
  }

  for (const host of getCandidateHosts()) {
    const resp = await api(
      "userinfo",
      {
        getauth: 1,
        username: USERNAME,
        password: PASSWORD,
      },
      host
    );

    if (resp.result === 0 && resp.auth) {
      authToken = resp.auth;
      const expiresIn = Number(resp.expires || 86400);
      tokenExpires = Date.now() + (expiresIn - 60) * 1000;
      currentApiHost = host;
      return;
    }

    failures.push(summarizeAuthFailure(host, resp));
  }

  throw new Error(
    "pCloud password login failed on all candidate hosts. " +
      `${failures.join(" | ")}. ` +
      "If your account now requires OAuth, configure PCLOUD_AUTH_TOKEN or PCLOUD_ACCESS_TOKEN."
  );
}

function resolveFolderId(input) {
  if (!input || input === "0") return 0;
  if (/^\d+$/.test(input)) return Number(input);
  return input;
}

function formatMetadata(item) {
  if (item.isfolder) {
    return `📁 ${item.name}\n  id: ${item.folderid}\n  path: ${item.path}\n  modified: ${item.modified}`;
  }
  const sizeKB = item.size ? (item.size / 1024).toFixed(2) : "?";
  return `📄 ${item.name}\n  id: ${item.fileid}\n  path: ${item.path}\n  size: ${sizeKB} KB\n  type: ${item.contenttype || "unknown"}\n  modified: ${item.modified}`;
}

const server = new Server(
  { name: "composer--pcloud", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "list_folder",
      description: "List contents of a folder in pCloud.",
      inputSchema: {
        type: "object",
        properties: {
          path: { type: "string" },
          folderid: { type: "number" },
          recursive: { type: "boolean" },
        },
      },
    },
    {
      name: "create_folder",
      description: "Create a folder in pCloud.",
      inputSchema: {
        type: "object",
        properties: {
          path: { type: "string" },
          folderid: { type: "number" },
          name: { type: "string" },
        },
        required: ["name"],
      },
    },
    {
      name: "delete_folder",
      description: "Delete a folder in pCloud.",
      inputSchema: {
        type: "object",
        properties: {
          path: { type: "string" },
          folderid: { type: "number" },
          recursive: { type: "boolean" },
        },
        required: ["folderid"],
      },
    },
    {
      name: "upload_file",
      description: "Upload a text file to pCloud.",
      inputSchema: {
        type: "object",
        properties: {
          filename: { type: "string" },
          content: { type: "string" },
          path: { type: "string" },
          folderid: { type: "number" },
        },
        required: ["filename", "content"],
      },
    },
    {
      name: "download_file",
      description: "Download a text file from pCloud.",
      inputSchema: {
        type: "object",
        properties: {
          path: { type: "string" },
          fileid: { type: "number" },
        },
      },
    },
    {
      name: "stat",
      description: "Get metadata for a file or folder in pCloud.",
      inputSchema: {
        type: "object",
        properties: {
          path: { type: "string" },
          fileid: { type: "number" },
          folderid: { type: "number" },
        },
      },
    },
    {
      name: "rename_file",
      description: "Rename or move a file in pCloud.",
      inputSchema: {
        type: "object",
        properties: {
          path: { type: "string" },
          fileid: { type: "number" },
          toname: { type: "string" },
          topath: { type: "string" },
          tofolderid: { type: "number" },
        },
        required: ["toname"],
      },
    },
    {
      name: "delete_file",
      description: "Delete a file in pCloud.",
      inputSchema: {
        type: "object",
        properties: {
          path: { type: "string" },
          fileid: { type: "number" },
        },
        required: ["fileid"],
      },
    },
    {
      name: "search_files",
      description: "Search files and folders in pCloud by name.",
      inputSchema: {
        type: "object",
        properties: {
          query: { type: "string" },
          path: { type: "string" },
          folderid: { type: "number" },
        },
        required: ["query"],
      },
    },
    {
      name: "get_user_info",
      description: "Get pCloud account info and quota.",
      inputSchema: { type: "object", properties: {} },
    },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  try {
    await ensureAuth();
    if (name === "list_folder") {
      const folderid = resolveFolderId(args.folderid ?? BASE_FOLDER);
      const resp = await api("listfolder", {
        folderid,
        path: args.path,
        recursive: args.recursive ? 1 : 0,
      });
      if (resp.result !== 0) throw new Error(JSON.stringify(resp));
      const contents = resp.metadata?.contents || [];
      if (contents.length === 0) {
        return { content: [{ type: "text", text: `Folder "${args.path || folderid}" is empty.` }] };
      }
      return { content: [{ type: "text", text: contents.map(formatMetadata).join("\n\n") }] };
    }
    if (name === "create_folder") {
      const folderid = resolveFolderId(args.folderid);
      const resp = await api("createfolder", {
        folderid,
        name: args.name,
        path: args.path,
      });
      if (resp.result !== 0) throw new Error(JSON.stringify(resp));
      return { content: [{ type: "text", text: formatMetadata(resp.metadata) }] };
    }
    if (name === "delete_folder") {
      const folderid = resolveFolderId(args.folderid);
      const method = args.recursive ? "deletefolderrecursive" : "deletefolder";
      const resp = await api(method, { folderid });
      if (resp.result !== 0) throw new Error(JSON.stringify(resp));
      const text = args.recursive
        ? `Deleted ${resp.deletedfiles} files and ${resp.deletedfolders} folders.`
        : "Folder deleted.";
      return { content: [{ type: "text", text }] };
    }
    if (name === "upload_file") {
      const folderid = resolveFolderId(args.folderid ?? BASE_FOLDER);
      const form = new FormData();
      form.append("filename", args.filename);
      form.append("auth", authToken);
      if (folderid) form.append("folderid", String(folderid));
      form.append("file", new Blob([args.content]), args.filename);
      const resp = await fetch(`${getBaseUrl()}/uploadfile`, { method: "POST", body: form });
      const data = await resp.json();
      if (data.result !== 0) throw new Error(JSON.stringify(data));
      const meta = data.metadata?.[0] || data.metadata;
      return { content: [{ type: "text", text: formatMetadata(meta) }] };
    }
    if (name === "download_file") {
      const fileid = resolveFolderId(args.fileid);
      const resp = await api("gettextfile", { fileid, path: args.path });
      if (resp.result !== 0) throw new Error(JSON.stringify(resp));
      return { content: [{ type: "text", text: resp.content || "" }] };
    }
    if (name === "stat") {
      const fileid = resolveFolderId(args.fileid);
      const folderid = resolveFolderId(args.folderid);
      const resp = await api("stat", { fileid, folderid, path: args.path });
      if (resp.result !== 0) throw new Error(JSON.stringify(resp));
      return { content: [{ type: "text", text: formatMetadata(resp.metadata) }] };
    }
    if (name === "rename_file") {
      const fileid = resolveFolderId(args.fileid);
      const resp = await api("renamefile", {
        fileid,
        path: args.path,
        toname: args.toname,
        topath: args.topath,
        tofolderid: args.tofolderid,
      });
      if (resp.result !== 0) throw new Error(JSON.stringify(resp));
      return { content: [{ type: "text", text: formatMetadata(resp.metadata) }] };
    }
    if (name === "delete_file") {
      const fileid = resolveFolderId(args.fileid);
      const resp = await api("deletefile", { fileid, path: args.path });
      if (resp.result !== 0) throw new Error(JSON.stringify(resp));
      return { content: [{ type: "text", text: "File deleted." }] };
    }
    if (name === "search_files") {
      const resp = await api("search", { query: args.query, path: args.path, folderid: args.folderid });
      if (resp.result !== 0) throw new Error(JSON.stringify(resp));
      const results = resp.metadata || [];
      if (results.length === 0) {
        return { content: [{ type: "text", text: `No results for "${args.query}".` }] };
      }
      return { content: [{ type: "text", text: results.map(formatMetadata).join("\n\n") }] };
    }
    if (name === "get_user_info") {
      const resp = await api("userinfo");
      if (resp.result !== 0) throw new Error(JSON.stringify(resp));
      const usedGB = (resp.usedquota / (1024 * 1024 * 1024)).toFixed(2);
      const totalGB = (resp.quota / (1024 * 1024 * 1024)).toFixed(2);
      const usedPercent = ((resp.usedquota / resp.quota) * 100).toFixed(1);
      return {
        content: [
          {
            type: "text",
            text: `Email: ${resp.email}\nVerified: ${resp.emailverified ? "Yes" : "No"}\nStorage: ${usedGB} GB / ${totalGB} GB (${usedPercent}%)`,
          },
        ],
      };
    }
    throw new Error(`Unknown tool: ${name}`);
  } catch (err) {
    return {
      content: [{ type: "text", text: `Error: ${err.message}` }],
      isError: true,
    };
  }
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCP pcloud server connected");
}

main().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(1);
});

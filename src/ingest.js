const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { glob } = require("glob");
const { RecursiveCharacterTextSplitter } = require("@langchain/textsplitters");
const { OllamaEmbeddings } = require("@langchain/ollama");
const config = require("./config");

process.on("uncaughtException", () => {});

function hashContent(content) {
  return crypto.createHash("sha256").update(content, "utf-8").digest("hex");
}

function cosineSimilarity(a, b) {
  let dot = 0,
    na = 0,
    nb = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    na += a[i] * a[i];
    nb += b[i] * b[i];
  }
  return dot / (Math.sqrt(na) * Math.sqrt(nb));
}

class LocalVectorStore {
  constructor(embeddings) {
    this.embeddings = embeddings;
    this.docs = [];
    this.vectors = [];
  }

  addDocument(doc, vector) {
    this.docs.push(doc);
    this.vectors.push(vector);
    return this.docs.length - 1;
  }

  removeBySource(sourceFile) {
    const remaining = { docs: [], vectors: [] };
    let removed = 0;
    for (let i = 0; i < this.docs.length; i++) {
      if (this.docs[i].metadata.source !== sourceFile) {
        remaining.docs.push(this.docs[i]);
        remaining.vectors.push(this.vectors[i]);
      } else {
        removed++;
      }
    }
    this.docs = remaining.docs;
    this.vectors = remaining.vectors;
    return removed;
  }

  async embedAndAdd(docs) {
    const texts = docs.map((d) => d.pageContent);
    const vectors = await this.embeddings.embedDocuments(texts);
    for (let i = 0; i < docs.length; i++) {
      this.addDocument(docs[i], vectors[i]);
    }
  }

  save(dir) {
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(
      path.join(dir, "vectors.json"),
      JSON.stringify({ docs: this.docs, vectors: this.vectors }),
    );
  }

  load(dir) {
    const file = path.join(dir, "vectors.json");
    if (!fs.existsSync(file)) return false;
    const data = JSON.parse(fs.readFileSync(file, "utf-8"));
    this.docs = data.docs;
    this.vectors = data.vectors;
    return true;
  }

  get size() {
    return this.docs.length;
  }
}

function loadManifest(dir) {
  const file = path.join(dir, "manifest.json");
  if (!fs.existsSync(file)) return {};
  return JSON.parse(fs.readFileSync(file, "utf-8"));
}

function saveManifest(dir, manifest) {
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(
    path.join(dir, "manifest.json"),
    JSON.stringify(manifest, null, 2),
  );
}

async function loadDocuments(rootDir) {
  const files = await glob("**/*.{md,txt}", { cwd: rootDir, absolute: true });
  const docs = [];
  for (const file of files) {
    const stat = fs.statSync(file);
    if (!stat.isFile()) continue;
    const content = fs.readFileSync(file, "utf-8");
    const relPath = path.relative(rootDir, file);
    docs.push({ file, relPath, content });
  }
  return docs;
}

async function ingest() {
  const embeddings = new OllamaEmbeddings({
    model: config.ollama.embeddingModel,
    baseUrl: config.ollama.baseUrl,
  });

  const store = new LocalVectorStore(embeddings);
  if (store.load(config.chroma.persistDir)) {
    console.log(`Loaded ${store.size} existing vectors`);
  }

  const oldManifest = loadManifest(config.chroma.persistDir);
  const newManifest = {};
  config.dirs.root = path.resolve(__dirname, "..");

  const splitter = new RecursiveCharacterTextSplitter({
    chunkSize: config.chunk.size,
    chunkOverlap: config.chunk.overlap,
  });

  let totalAdded = 0,
    totalRemoved = 0,
    totalSkipped = 0;

  for (const [label, dir] of Object.entries(config.dirs)) {
    if (label === "root") continue;
    if (!fs.existsSync(dir)) {
      console.log(`  [${label}] does not exist, skipping`);
      continue;
    }

    const files = await loadDocuments(dir);
    const indexedFiles = new Set();

    for (const { file, relPath, content } of files) {
      const fileKey = `${label}/${relPath}`;
      indexedFiles.add(fileKey);
      const newHash = hashContent(content);

      if (oldManifest[fileKey] && oldManifest[fileKey] === newHash) {
        newManifest[fileKey] = newHash;
        totalSkipped++;
        continue;
      }

      if (oldManifest[fileKey]) {
        const removed = store.removeBySource(relPath);
        totalRemoved += removed;
        console.log(
          `  [${label}] changed: ${relPath} (${removed} old chunks removed)`,
        );
      } else {
        console.log(`  [${label}] new: ${relPath}`);
      }

      const rawDocs = [
        { pageContent: content, metadata: { source: relPath, dir: label } },
      ];
      const chunks = await splitter.splitDocuments(rawDocs);

      if (chunks.length > 0) {
        await store.embedAndAdd(chunks);
        totalAdded += chunks.length;
        console.log(`    → ${chunks.length} chunks added`);
      }

      newManifest[fileKey] = newHash;
    }

    for (const fileKey of Object.keys(oldManifest)) {
      if (fileKey.startsWith(`${label}/`) && !indexedFiles.has(fileKey)) {
        const relPath = fileKey.slice(label.length + 1);
        const removed = store.removeBySource(relPath);
        if (removed > 0) {
          totalRemoved += removed;
          console.log(
            `  [${label}] deleted: ${relPath} (${removed} chunks removed)`,
          );
        }
      }
    }
  }

  store.save(config.chroma.persistDir);
  saveManifest(config.chroma.persistDir, newManifest);

  const summary = [];
  if (totalAdded > 0) summary.push(`${totalAdded} added`);
  if (totalRemoved > 0) summary.push(`${totalRemoved} removed`);
  if (totalSkipped > 0) summary.push(`${totalSkipped} unchanged (skipped)`);
  console.log(`\nDone. Store has ${store.size} chunks. ${summary.join(", ")}`);
}

if (require.main === module) {
  ingest().catch((err) => {
    console.error("Ingest failed:", err);
    process.exit(1);
  });
}

module.exports = { ingest };

const fs = require("fs");
const path = require("path");
const http = require("http");
const { execSync } = require("child_process");
const config = require("./config");

process.on("uncaughtException", () => {});

const API = config.ollama.baseUrl + "/api";

function ollama(path, data) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify(data);
    const url = new URL(path, config.ollama.baseUrl);
    const opts = {
      hostname: url.hostname,
      port: url.port,
      path: url.pathname,
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Content-Length": Buffer.byteLength(body),
      },
      timeout: 300000,
    };
    const req = http.request(opts, (res) => {
      let data = "";
      res.on("data", (c) => (data += c));
      res.on("end", () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          reject(e);
        }
      });
    });
    req.on("error", reject);
    req.write(body);
    req.end();
  });
}

let cachedData = null;
let cachedNorms = null;

function loadStore() {
  if (cachedData) return cachedData;
  const file = path.join(config.chroma.persistDir, "vectors.json");
  if (!fs.existsSync(file)) return null;
  cachedData = JSON.parse(fs.readFileSync(file, "utf-8"));
  cachedNorms = cachedData.vectors.map((v) => {
    let sum = 0;
    for (let i = 0; i < v.length; i++) sum += v[i] * v[i];
    return Math.sqrt(sum);
  });
  return cachedData;
}

function cosineSimilarity(a, b, na, nb) {
  let dot = 0;
  for (let i = 0; i < a.length; i++) dot += a[i] * b[i];
  return dot / (na * nb);
}

function keywordSearch(question, data, k = 5) {
  const terms = question
    .toLowerCase()
    .split(/\s+/)
    .filter((t) => t.length > 3)
    .slice(0, 8);
  if (terms.length === 0) return [];

  const scores = new Array(data.docs.length).fill(0);
  try {
    const pattern = terms
      .map((t) => t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"))
      .join("|");
    const out = execSync(`rg -c -i -g "*.md" -g "*.txt" "${pattern}" .`, {
      encoding: "utf-8",
      timeout: 5000,
      cwd: config.dirs.root,
    });
    for (const line of out.trim().split("\n").filter(Boolean)) {
      const m = line.match(/^(.+?\.(?:md|txt)):(\d+)$/m);
      if (!m) continue;
      const rp = m[1].replace(/\\/g, "/").replace(/^\.\//, "");
      for (let i = 0; i < data.docs.length; i++) {
        if (
          `${data.docs[i].metadata.dir}/${data.docs[i].metadata.source}` === rp
        ) {
          scores[i] += Math.log(1 + parseInt(m[2], 10));
        }
      }
    }
  } catch {}
  return scores
    .map((s, i) => ({ index: i, score: s }))
    .filter((s) => s.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, k);
}

function semanticSearch(qv, data, k = 10) {
  const scored = data.vectors.map((v, i) => ({
    index: i,
    score: cosineSimilarity(qv, v, 1, cachedNorms[i]),
  }));
  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, k);
}

function rrfFusion(semantic, keyword, k = 60) {
  const rrf = {};
  for (const list of [semantic, keyword]) {
    for (let r = 0; r < list.length; r++) {
      const idx = list[r].index;
      if (!rrf[idx]) rrf[idx] = { index: idx, score: 0 };
      rrf[idx].score += 1 / (k + r + 1);
    }
  }
  return Object.values(rrf)
    .sort((a, b) => b.score - a.score)
    .map((r) => r.index);
}

function mmrRerank(qv, indices, data, lambda = 0.7, topK = 6) {
  const sel = [];
  const cand = new Set(indices);
  while (sel.length < topK && cand.size > 0) {
    let bestIdx = null,
      bestScore = -Infinity;
    for (const idx of cand) {
      const sim = cosineSimilarity(qv, data.vectors[idx], 1, cachedNorms[idx]);
      let maxDiv = 0;
      for (const s of sel)
        maxDiv = Math.max(
          maxDiv,
          1 -
            cosineSimilarity(
              data.vectors[s],
              data.vectors[idx],
              cachedNorms[s],
              cachedNorms[idx],
            ),
        );
      const ms = lambda * sim - (1 - lambda) * maxDiv;
      if (ms > bestScore) {
        bestScore = ms;
        bestIdx = idx;
      }
    }
    if (bestIdx !== null) {
      sel.push(bestIdx);
      cand.delete(bestIdx);
    }
  }
  return sel.map((i) => data.docs[i]);
}

const PROMPTS = {
  full: "Eres un compositor profesional. Usa el contexto para fundamentar tu respuesta.\n\nContexto:\n{context}\n\nInstrucciones:\n- Cita figuras retóricas, estructura armónica y esquema de rima\n- Responde en español\n\nConsulta: {question}\n\nRespuesta:",
  fast: "Eres un compositor. Responde en español con ideas concretas y breves.\n\nContexto:\n{context}\n\nPregunta: {question}\n\nRespuesta:",
  pro: "Eres un compositor profesional con conocimiento experto en teoría musical, retórica lírica y estructura de canciones.\n\nContexto disponible:\n{context}\n\nInstrucciones:\n- Usa el contexto para fundamentar cada elemento de tu respuesta\n- Cita figuras retóricas específicas cuando sea relevante\n- Incluye estructura armónica, esquema de rima y recursos estilísticos\n- Responde en español\n\nConsulta: {question}\n\nRespuesta:",
};

async function retrieve(question) {
  const data = loadStore();
  if (!data) throw new Error("No hay índice. Ejecuta 'just ingest' primero.");

  const embed = await ollama("/api/embeddings", {
    model: config.ollama.embeddingModel,
    prompt: question,
  }).catch(() => {
    const { OllamaEmbeddings } = require("@langchain/ollama");
    return new OllamaEmbeddings({
      model: config.ollama.embeddingModel,
      baseUrl: config.ollama.baseUrl,
    })
      .embedQuery(question)
      .then((v) => ({ embedding: v }));
  });

  const qv = embed.embedding;
  if (cachedNorms) {
    let qn = 0;
    for (let i = 0; i < qv.length; i++) qn += qv[i] * qv[i];
    cachedNorms.push(Math.sqrt(qn));
  }

  const [semantic, keyword] = await Promise.all([
    Promise.resolve(semanticSearch(qv, data, 10)),
    Promise.resolve(keywordSearch(question, data, 5)),
  ]);

  const fused = rrfFusion(semantic, keyword);
  const topDocs = mmrRerank(qv, fused, data, 0.7, 6);

  const context = topDocs
    .map((d, i) => `[${i + 1}] (${d.metadata.source}) ${d.pageContent}`)
    .join("\n\n---\n\n");

  return {
    context,
    sources: topDocs.map((d) => d.metadata.source),
    stats: {
      semanticResults: semantic.length,
      keywordResults: keyword.length,
      finalResults: topDocs.length,
    },
  };
}

async function query(question, model = config.ollama.model, stream = false) {
  const { context, sources, stats } = await retrieve(question);

  const isSmall = ["tinyllama", "llama3.2", "qwen2.5:0.5b"].some((m) =>
    model.startsWith(m),
  );
  const templateKey = model.startsWith("gemma4")
    ? "pro"
    : isSmall
      ? "fast"
      : "full";
  const prompt = PROMPTS[templateKey]
    .replace("{context}", context)
    .replace("{question}", question);

  const startTime = Date.now();
  const res = await ollama("/api/generate", {
    model,
    prompt,
    stream,
    options: {
      temperature: 0.7,
      num_predict: isSmall ? 768 : model.startsWith("gemma4") ? 2048 : 1536,
      num_ctx: isSmall ? 2048 : 4096,
    },
  });

  const answer = stream ? res.response : res.response;
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  return { answer, sources, stats: { ...stats, elapsedSeconds: elapsed } };
}

module.exports = { query };

const path = require("path");

module.exports = {
  ollama: {
    baseUrl: process.env.OLLAMA_HOST || "http://127.0.0.1:11434",
    model: process.env.OLLAMA_MODEL || "mistral:7b",
    fastModel: process.env.OLLAMA_FAST_MODEL || "llama3.2:3b",
    proModel: process.env.OLLAMA_PRO_MODEL || "gemma4",
    embeddingModel: process.env.OLLAMA_EMBEDDING || "nomic-embed-text",
  },
  chroma: {
    collectionName: "composer",
    persistDir: path.resolve(__dirname, "..", ".chroma"),
  },
  dirs: {
    docs: path.resolve(__dirname, "..", "docs"),
    specs: path.resolve(__dirname, "..", "specs"),
    corpus: path.resolve(__dirname, "..", "corpus"),
    canciones: path.resolve(__dirname, "..", "canciones"),
    inspiration: path.resolve(__dirname, "..", "inspiration"),
    bio: path.resolve(__dirname, "..", "bio"),
  },
  chunk: {
    size: 1000,
    overlap: 200,
  },
};

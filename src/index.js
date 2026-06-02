#!/usr/bin/env node
const { ingest } = require("./ingest");
const { query } = require("./query");
const config = require("./config");

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log("Uso: node src/index.js <comando> [argumentos]");
  console.log("");
  console.log("Comandos:");
  console.log("  ingest                       Indexar docs/, specs/, corpus/, inspiration/ y bio/");
  console.log(
    "  query <pregunta>             Consulta RAG (modelo configurado: " +
      config.ollama.model +
      ")",
  );
  console.log(
    "  query-fast <pregunta>        Consulta rápida con tinyllama (streaming)",
  );
  console.log("  query-pro <pregunta>         Consulta completa con gemma4");
  process.exit(0);
}

const command = args[0];

if (command === "ingest") {
  ingest()
    .then(() => process.exit(0))
    .catch((err) => {
      console.error(err);
      process.exit(1);
    });
} else if (command === "query") {
  const question = args.slice(1).join(" ");
  if (!question) {
    console.error("Error: proporciona una pregunta");
    process.exit(1);
  }
  query(question, config.ollama.model, false)
    .then(({ answer, sources, stats }) => {
      console.log("\n=== RESPUESTA ===\n");
      console.log(answer);
      console.log("\n=== FUENTES ===");
      sources.forEach((s, i) => console.log(`  ${i + 1}. ${s}`));
      console.log(
        `\n[${stats.elapsedSeconds}s | sem: ${stats.semanticResults} | kw: ${stats.keywordResults} | final: ${stats.finalResults}]`,
      );
      process.exit(0);
    })
    .catch((err) => {
      console.error(err);
      process.exit(1);
    });
} else if (command === "query-fast") {
  const question = args.slice(1).join(" ");
  if (!question) {
    console.error("Error: proporciona una pregunta");
    process.exit(1);
  }
  console.log("Modo rápido (tinyllama, streaming):\n");
  query(question, "tinyllama", true)
    .then(({ sources, stats }) => {
      console.log("\n=== FUENTES ===");
      sources.forEach((s, i) => console.log(`  ${i + 1}. ${s}`));
      console.log(
        `\n[${stats.elapsedSeconds}s | sem: ${stats.semanticResults} | kw: ${stats.keywordResults} | final: ${stats.finalResults}]`,
      );
      process.exit(0);
    })
    .catch((err) => {
      console.error(err);
      process.exit(1);
    });
} else if (command === "query-pro") {
  const question = args.slice(1).join(" ");
  if (!question) {
    console.error("Error: proporciona una pregunta");
    process.exit(1);
  }
  query(question, "gemma4", false)
    .then(({ answer, sources, stats }) => {
      console.log("\n=== RESPUESTA ===\n");
      console.log(answer);
      console.log("\n=== FUENTES ===");
      sources.forEach((s, i) => console.log(`  ${i + 1}. ${s}`));
      console.log(
        `\n[${stats.elapsedSeconds}s | sem: ${stats.semanticResults} | kw: ${stats.keywordResults} | final: ${stats.finalResults}]`,
      );
      process.exit(0);
    })
    .catch((err) => {
      console.error(err);
      process.exit(1);
    });
} else {
  console.error(`Comando desconocido: "${command}"`);
  process.exit(1);
}

#!/usr/bin/env node
/**
 * Wrapper that reads .env and launches @benborla29/mcp-server-mysql
 * with the correct environment variables.
 */
const { spawn } = require("child_process");
const { readFileSync } = require("fs");
const { resolve } = require("path");

const envPath = resolve(__dirname, "..", ".env");
const envContent = readFileSync(envPath, "utf-8");

const env = { ...process.env };

envContent.split("\n").forEach((line) => {
  line = line.trim();
  if (!line || line.startsWith("#")) return;
  const idx = line.indexOf("=");
  if (idx === -1) return;
  const key = line.slice(0, idx).trim();
  let value = line.slice(idx + 1).trim();
  // strip inline comments: "# comment"
  const commentIdx = value.indexOf("#");
  if (commentIdx !== -1) value = value.slice(0, commentIdx).trim();
  // strip surrounding quotes
  if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
    value = value.slice(1, -1);
  }
  env[key] = value;
});

const mcpArgs = ["-y", "@benborla29/mcp-server-mysql"];

const child = spawn("npx", mcpArgs, {
  env,
  stdio: "inherit",
  shell: process.platform === "win32",
});

child.on("exit", (code) => process.exit(code ?? 0));

const fs = require('fs');
const path = require('path');

const CANCIONES_DIR = path.join(__dirname, '..', 'canciones');

const accentMap = { 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u' };
const strongVowels = new Set(['a', 'e', 'o']);
const weakVowels = new Set(['i', 'u']);

function normalize(word) {
  return word.toLowerCase().replace(/[áéíóúü]/g, ch => accentMap[ch] || ch);
}

function getStressedVowelPos(word) {
  const lower = word.toLowerCase();
  for (let i = lower.length - 1; i >= 0; i--) {
    if ('áéíóú'.includes(lower[i])) return i;
  }
  const nLower = normalize(lower);
  const lastChar = nLower[nLower.length - 1];
  if (lastChar === 'n' || lastChar === 's' || strongVowels.has(lastChar) || weakVowels.has(lastChar)) {
    for (let i = nLower.length - 2; i >= 0; i--) {
      if (strongVowels.has(nLower[i]) || weakVowels.has(nLower[i])) return i;
    }
  }
  for (let i = nLower.length - 1; i >= 0; i--) {
    if (strongVowels.has(nLower[i]) || weakVowels.has(nLower[i])) return i;
  }
  return nLower.length - 1;
}

function getConsonantEnding(word) {
  const n = normalize(word);
  const pos = getStressedVowelPos(word);
  if (pos === -1) return n;
  return n.slice(pos);
}

function getAssonantVowels(word) {
  const n = normalize(word);
  const pos = getStressedVowelPos(word);
  if (pos === -1) return '';
  let vowels = '';
  for (const ch of n.slice(pos)) {
    if (strongVowels.has(ch) || weakVowels.has(ch)) vowels += ch;
  }
  return vowels;
}

function cleanLastWord(line) {
  const words = line.trim().split(/\s+/);
  let last = words[words.length - 1];
  last = last.replace(/[¿?!¡,;.:()"'\u2014\u2013\u2026\[\]¿?¡!]/g, '').trim();
  return last;
}

function isSectionHeader(line) {
  return /^\[.*\]$/.test(line.trim());
}

function isInstrumentalCue(line) {
  return /^\(.*\)$/.test(line.trim()) || /^\{.*\}$/.test(line.trim());
}

function isBlank(line) {
  return line.trim() === '';
}

function analyzeEndWords(endWords) {
  if (endWords.length < 2) return { pattern: null, type: null, rhymeEndings: [] };

  const consGroups = new Map();
  const asonGroups = new Map();
  for (const w of endWords) {
    const ck = getConsonantEnding(w);
    const ak = getAssonantVowels(w);
    if (!consGroups.has(ck)) consGroups.set(ck, []);
    if (!asonGroups.has(ak)) asonGroups.set(ak, []);
    consGroups.get(ck).push(w);
    asonGroups.get(ak).push(w);
  }

  const total = endWords.length;
  let consRhymed = 0, asonRhymed = 0;
  for (const [, group] of consGroups) { if (group.length > 1) consRhymed += group.length; }
  for (const [, group] of asonGroups) { if (group.length > 1) asonRhymed += group.length; }

  const consDensity = consRhymed / total;
  const asonDensity = asonRhymed / total;
  const isCons = consDensity >= asonDensity;

  let pairs = 0, pairHits = 0;
  for (let i = 0; i < endWords.length - 1; i += 2) {
    pairs++;
    const a = isCons ? getConsonantEnding(endWords[i]) : getAssonantVowels(endWords[i]);
    const b = isCons ? getConsonantEnding(endWords[i+1]) : getAssonantVowels(endWords[i+1]);
    if (a === b) pairHits++;
  }

  let altHits = 0, altPairs = 0;
  for (let i = 0; i < endWords.length - 2; i += 2) {
    altPairs++;
    const a = isCons ? getConsonantEnding(endWords[i]) : getAssonantVowels(endWords[i]);
    const b = isCons ? getConsonantEnding(endWords[i+2]) : getAssonantVowels(endWords[i+2]);
    if (a === b) altHits++;
  }
  for (let i = 1; i < endWords.length - 2; i += 2) {
    altPairs++;
    const a = isCons ? getConsonantEnding(endWords[i]) : getAssonantVowels(endWords[i]);
    const b = isCons ? getConsonantEnding(endWords[i+2]) : getAssonantVowels(endWords[i+2]);
    if (a === b) altHits++;
  }

  const pairRatio = pairs > 0 ? pairHits / pairs : 0;
  const altRatio = altPairs > 0 ? altHits / altPairs : 0;

  let pattern = 'libre';
  let type = 'libre';

  const density = isCons ? consDensity : asonDensity;
  const typeName = isCons ? 'consonante' : 'asonante';

  if (pairRatio >= 0.7 && density >= 0.5) {
    pattern = 'AABB';
    type = typeName;
  } else if (altRatio >= 0.5 && density >= 0.5) {
    pattern = 'ABAB';
    type = typeName;
  } else if (density >= 0.4) {
    pattern = 'parcial';
    type = typeName;
  }

  const rhymeEndings = [];
  const groups = isCons ? consGroups : asonGroups;
  for (const [ending, group] of groups) {
    if (group.length >= 2) {
      rhymeEndings.push({ ending, count: group.length, words: group.slice(0, 3) });
    }
  }
  rhymeEndings.sort((a, b) => b.count - a.count);

  return { pattern, type, rhymeEndings: rhymeEndings.slice(0, 3), density, endWords };
}

function parseSections(lyricsText) {
  const lines = lyricsText.split('\n');
  const sections = [];
  let currentSection = null;
  let currentLines = [];

  for (const line of lines) {
    if (isSectionHeader(line)) {
      if (currentSection) sections.push({ name: currentSection, lines: currentLines });
      currentSection = line.replace(/[\[\]]/g, '').trim();
      currentLines = [];
    } else {
      currentLines.push(line);
    }
  }
  if (currentSection) sections.push({ name: currentSection, lines: currentLines });

  const results = {};
  for (const section of sections) {
    const endWords = [];
    for (const line of section.lines) {
      const t = line.trim();
      if (!t || isInstrumentalCue(t) || isSectionHeader(t)) continue;
      const last = cleanLastWord(t);
      if (last) endWords.push(last);
    }
    if (endWords.length >= 2) {
      results[section.name] = analyzeEndWords(endWords);
    }
  }
  return results;
}

function analyzeAsWhole(lyricsText) {
  const lines = lyricsText.split('\n');
  const endWords = [];
  for (const line of lines) {
    const t = line.trim();
    if (!t || isInstrumentalCue(t) || isSectionHeader(t)) continue;
    const last = cleanLastWord(t);
    if (last) endWords.push(last);
  }
  if (endWords.length >= 2) {
    const result = analyzeEndWords(endWords);
    if (result.pattern !== 'libre' || result.density >= 0.3) return result;
  }
  return null;
}

function isInstrumental(content, lyrics) {
  if (/Tipo:\s*Instrumental/.test(content)) return true;
  if (lyrics) {
    const lines = lyrics.split('\n');
    // Only match exact [Instrumental] section, not [Instrumental Interlude] etc.
    if (lines.some(l => /^\[Instrumental\]$/i.test(l.trim()))) return true;
  }
  const firstLines = lyrics ? lyrics.split('\n').filter(l => l.trim()).slice(0, 3).join(' ') : '';
  if (/^instrumental$|sin letra/i.test(firstLines)) return true;
  return false;
}

function describeSection(name, result) {
  if (!result || !result.pattern) return null;
  let label = name;
  const lower = name.toLowerCase();
  if (/verse|verso|estrofa/i.test(lower)) label = 'Estrofas';
  else if (/chorus|coro|estribillo/i.test(lower)) label = 'Coro';
  else if (/bridge|puente/i.test(lower)) label = 'Puente';
  else if (/intro/i.test(lower)) label = 'Intro';
  else if (/outro/i.test(lower)) label = 'Outro';
  else if (/pre/i.test(lower)) label = 'Pre-coro';
  else if (/post/i.test(lower)) label = 'Post-coro';

  const endingDesc = result.rhymeEndings.map(r => `-${r.ending}`).join(', ');

  if (result.pattern === 'AABB') {
    return `${label}: pareados ${result.type} (AABB)${endingDesc ? ' (' + endingDesc + ')' : ''}`;
  } else if (result.pattern === 'ABAB') {
    return `${label}: alternada ${result.type} (ABAB)${endingDesc ? ' (' + endingDesc + ')' : ''}`;
  } else if (result.pattern === 'parcial') {
    return `${label}: rima ${result.type} parcial${endingDesc ? ' (' + endingDesc + ')' : ''}`;
  }
  return null;
}

function generateDescription(sectionResults, wholeResult, isInst) {
  if (isInst) return 'N/A — instrumental.';

  const parts = [];
  if (Object.keys(sectionResults).length > 0) {
    for (const [name, result] of Object.entries(sectionResults)) {
      const desc = describeSection(name, result);
      if (desc) parts.push(desc);
    }
  } else if (wholeResult) {
    const desc = describeSection('Canción', wholeResult);
    if (desc) parts.push(desc);
  }

  if (parts.length === 0) return 'Verso libre sin esquema de rima fijo.';

  // Deduplicate consecutive same descriptions
  const unique = parts.filter((p, i) => i === 0 || p !== parts[i-1]);
  return unique.join('. ') + '.';
}

function isPoemAdaptation(content) {
  return /Neruda|Machado|poema|poet/i.test(content);
}

function getManualDescription(content, lyrics) {
  const c = content.replace(/\r\n/g, '\n').toLowerCase();
  if (c.includes('machado') && c.includes('anoche cuando dormía')) {
    return 'Poema de Antonio Machado: romance octosilábico (ABCB asonante en versos pares).';
  }
  if (c.includes('neruda') && c.includes('me gustas cuando callas')) {
    return 'Poema de Pablo Neruda: verso libre con rima asonante ocasional. Estructura original del poema.';
  }
  if (c.includes('bongó') || (lyrics||'').toLowerCase().includes('bongo')) {
    return 'N/A — instrumental (percusión pura, sin letra cantada).';
  }
  if (c.includes('arrendajo')) {
    return 'Pareados consonante (AABB) en toda la canción. Estribillo con rima en -ol, -ad, -ar. Puente con rima en -ía, -al.';
  }
  if (c.includes('benedetti') && c.includes('táctica')) {
    return 'Poema de Mario Benedetti: verso libre con estructura fragmentada. Sin esquema de rima fijo, basado en repetición y paralelismo.';
  }
  return null;
}

function nl(s) {
  return s.replace(/\r\n/g, '\n');
}

function extractLyrics(content) {
  const normalized = nl(content);
  const letraMatch = normalized.match(/## Letra\n([\s\S]*?)(?=\n## )/);
  return letraMatch ? letraMatch[1].trim() : '';
}

function hasEmptyScheme(content) {
  const normalized = nl(content);
  const match = normalized.match(/## Esquema de rima\n([\s\S]*?)## Checklist/);
  if (!match) return true;
  const between = match[1].trim();
  return between === '';
}

function main() {
  const files = fs.readdirSync(CANCIONES_DIR)
    .filter(f => f.endsWith('.md'))
    .map(f => path.join(CANCIONES_DIR, f));

  let filled = 0;
  let skipped = 0;
  let manual = 0;

  for (const file of files) {
    try {
      const content = fs.readFileSync(file, 'utf-8');
      const normalized = nl(content);

      // Skip if already has proper description (not "Verso libre sin esquema")
      const schemeMatch = normalized.match(/## Esquema de rima\n([\s\S]*?)## Checklist/);
      if (schemeMatch) {
        const current = schemeMatch[1].trim();
        if (current && !current.includes('Verso libre sin esquema')) {
          skipped++;
          continue;
        }
      }

      const lyrics = extractLyrics(content) || '';

      // Manual overrides for special cases
      const manualDesc = getManualDescription(content, lyrics);
      if (manualDesc) {
        const updated = normalized.replace(
          /## Esquema de rima\n\n[\s\S]*?(?=\n## Checklist)/,
          `## Esquema de rima\n\n${manualDesc}\n`
        );
        fs.writeFileSync(file, updated, 'utf-8');
        console.log(`  ✓ ${path.basename(file)} → ${manualDesc}`);
        filled++;
        manual++;
        continue;
      }

      const isInst = isInstrumental(content, lyrics);
      const sectionResults = parseSections(lyrics);
      const wholeResult = !isInst && Object.keys(sectionResults).length === 0 && lyrics ? analyzeAsWhole(lyrics) : null;

      const description = generateDescription(sectionResults, wholeResult, isInst);

      const updated = normalized.replace(
        /## Esquema de rima\n\n[\s\S]*?(?=\n## Checklist)/,
        `## Esquema de rima\n\n${description}\n`
      );

      if (updated === normalized) {
        console.log(`  ✗ ${path.basename(file)}: could not insert`);
        continue;
      }

      fs.writeFileSync(file, updated, 'utf-8');
      console.log(`  ${isInst ? '~' : '✓'} ${path.basename(file)} → ${description}`);
      filled++;
    } catch (err) {
      console.log(`  ✗ ${path.basename(file)}: ${err.message}`);
    }
  }

  console.log(`\n=== Resumen ===`);
  console.log(`  Actualizados: ${filled} (${manual} manuales)`);
  console.log(`  Ya tenían esquema: ${skipped}`);
}

main();

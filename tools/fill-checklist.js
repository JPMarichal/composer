const fs = require('fs');
const path = require('path');

const CANCIONES_DIR = path.join(__dirname, '..', 'canciones');

// Prohibited words from §1 (en español)
const PROHIBITED_WORDS = [
  /ecos?\b/i, /susurr[oó]/i, /ne[oó]n/i, /elevar(se)?\b/i, /ascender/i,
  /\bgracia\b/i, /\babrazo\b/i, /jungla\s+de\s+concreto/i, /sue[ñn]os?\s+rotos?\b/i,
  /noche\s+eterna/i, /\bsombras?\b/i, /\blatidos?\b/i, /\bpalpitar\b/i,
  /\bdestellos?\b/i, /\bbrillo\b/i, /\bcamino\b/i, /\bsendero\b/i,
  /llama\s+que\s+arde/i, /\btempestad\b/i, /\btormenta\b/i,
  /\bvac[íi]o\b/, /\babismo\b/, /tender\s+puentes/i, /derribar\s+muros/i,
  /\bcicatriz\b/, /\bherida\b/, /\bbailar\b/, /\bdanzar\b/,
];

// Abstract nouns (from §4)
const ABSTRACT_NOUNS = /tapestry|realm|landscape|symphony|testament|exploration|journey|dynamics|cornerstone|beacon|delve|embark|elevate|navigate|foster|unveil|harness|cultivate|grapple|embrace/i;

// AI-ismos semánticos (§3)
const SEMANTIC_AI_ISMS = [
  /luna\s+tiesa/i, /silencio\s+llora/i, /tiempo\s+desangra/i,
  /noche\s+(me\s+)?abraza/i, /dolor\s+baila/i, /viento\s+susurra/i,
  /recuerdos?\s+gritan?/i, /fuego\s+(me\s+)?congela/i,
  /caminar\s+sobre\s+las\s+aguas/i, /volar\s+sin\s+alas/i,
];

// Verbos forzados (§4b)
const FORZED_VERBS = [
  /sueldo\s+aterra/i, /ciudad\s+susurra/i, /tiempo\s+sangra/i,
  /noche\s+abraza/i, /silencio\s+grita/i,
  /recuerdos?\s+queman?/i, /lluvia\s+baila/i,
  /distancia\s+duele/i, /coraz[óo]n\s+olvida/i,
  /d[íi]as?\s+pesan?/i,
];

// Positive collocations (acceptable uses of noche/envuelve etc.)
const POSITIVE_COLLOCATIONS = [
  /noche\s+(me\s+)?envuelv/i, /noche\s+(me\s+)?tapa/i,
  /viento\s+silba/i, /viento\s+empuja/i, /viento\s+corta/i,
  /silencio\s+pesa/i, /silencio\s+se\s+oye/i, /silencio\s+aprieta/i,
  /recuerdos?\s+vueltan?/i, /recuerdos?\s+pesan?/i,
  /dolor\s+late/i, /dolor\s+duele/i, /dolor\s+queda/i,
];

function nl(s) {
  return s.replace(/\r\n/g, '\n');
}

function extractLyrics(content) {
  const normalized = nl(content);
  const letraMatch = normalized.match(/## Letra\n([\s\S]*?)(?=\n## )/);
  return letraMatch ? letraMatch[1].trim() : '';
}

function extractTitle(content) {
  const m = content.match(/^# (.+)/m);
  return m ? m[1].trim() : '';
}

function extractSections(lyrics) {
  const lines = lyrics.split('\n');
  const sections = {};
  let currentSection = null;
  let currentLines = [];

  for (const line of lines) {
    const t = line.trim();
    if (/^\[.*\]$/.test(t)) {
      if (currentSection) {
        sections[currentSection] = currentLines.filter(l => l.trim());
      }
      currentSection = t.replace(/[\[\]]/g, '').trim();
      currentLines = [];
    } else {
      currentLines.push(line);
    }
  }
  if (currentSection) {
    sections[currentSection] = currentLines.filter(l => l.trim());
  }
  return sections;
}

function countTriadas(text) {
  // Count patterns like "X, Y, Z" or "X, Y y Z" as lists of 3
  const matches = text.match(/\b\w+,\s*\w+,\s*(?:\w+|\w+\s+y\s+\w+)/g);
  return matches ? matches.length : 0;
}

function countEmDashes(text) {
  return (text.match(/—/g) || []).length;
}

function checkAnaphora(lines) {
  let maxConsecutive = 0;
  let currentStreak = 1;

  for (let i = 1; i < lines.length; i++) {
    const prev = lines[i - 1].trim().split(/\s+/).slice(0, 3).join(' ');
    const curr = lines[i].trim().split(/\s+/).slice(0, 3).join(' ');

    // Check if first 2 words match
    const prev2 = lines[i - 1].trim().split(/\s+/).slice(0, 2).join(' ').toLowerCase();
    const curr2 = lines[i].trim().split(/\s+/).slice(0, 2).join(' ').toLowerCase();

    if (prev2 === curr2 && prev2.length > 0) {
      currentStreak++;
      maxConsecutive = Math.max(maxConsecutive, currentStreak);
    } else {
      currentStreak = 1;
    }
  }
  return maxConsecutive;
}

function countTitleInChorus(title, sections) {
  if (!title) return 0;
  const titleWords = title.toLowerCase().split(/\s+/).filter(w => w.length > 2);
  if (titleWords.length === 0) return 0;

  let chorusText = '';
  for (const [name, lines] of Object.entries(sections)) {
    if (/chorus|coro|estribillo/i.test(name)) {
      chorusText = lines.join(' ').toLowerCase();
      break;
    }
  }

  if (!chorusText) return 0;

  // Count occurrences of the title as a phrase
  let count = 0;
  const titleLower = title.toLowerCase();
  let pos = 0;
  while ((pos = chorusText.indexOf(titleLower, pos)) !== -1) {
    count++;
    pos += titleLower.length;
  }
  return count;
}

function findColloquialisms(text) {
  const patterns = [
    /\bno\s+(sé|puedo|tengo|quiero|voy|está)\b/gi,
    /\b(dale|vamos|venga|anda|oye|mira|viste|che|wey|tío|chico)\b/gi,
    /\b(ni\s+(modo|pensarlo|hablar))\b/gi,
    /\b(qué\s+(tal|hay|pasó|onda))\b/gi,
    /\b(está\s+(bien|bueno|cañón))\b/gi,
    /\b(un\s+(montón|chorro|poco))\b/gi,
    /\b(a\s+(ver|dónde))\b/gi,
    /\byo\s+creo\b/gi, /\bcreo\s+que\b/gi,
    /\bcomo\s+que\b/gi, /\bni\s+siquiera\b/gi,
    /\b(un\s+poquito|poquitín)\b/gi,
    /\b(no\s+importa|da\s+igual)\b/gi,
    /\bquién\s+sabe\b/gi, /\bdios\s+(mío|santo)\b/gi,
    /\b(ay|ah|eh|oh)\b/gi,
    /\b(guay|chévere|padre|chido|bacán|paja)\b/gi,
    /\b(por\s+fin|al\s+fin)\b/gi,
    /\b(lo\s+que\s+sea|como\s+sea)\b/gi,
    /\b(vale|ok|okay)\b/gi,
    /\b(sabes?\s+qu[ée]|sabes\?)\b/gi,
  ];

  const found = [];
  for (const p of patterns) {
    const matches = text.match(p);
    if (matches) found.push(...matches);
  }
  return [...new Set(found.map(m => m.toLowerCase().trim()))];
}

function countStrophes(sections) {
  let strophes = 0;
  for (const name of Object.keys(sections)) {
    if (/verse|verso|estrofa/i.test(name)) strophes++;
  }
  return Math.max(1, strophes);
}

function checkIsInstrumental(content) {
  const lyrics = extractLyrics(content);
  if (!lyrics) return false;
  const lines = lyrics.split('\n');
  if (lines.some(l => /^\[Instrumental\]$/i.test(l.trim()))) return true;
  if (/Tipo:\s*Instrumental/.test(content)) return true;
  // Check if there are no lyrical lines
  const lyricalLines = lines.filter(l => {
    const t = l.trim();
    return t && !/^\[.*\]$/.test(t) && !/^\(.*\)$/.test(t);
  });
  return lyricalLines.length === 0;
}

function processSong(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const normalized = nl(content);
  const baseName = path.basename(filePath);

  // Skip instrumental
  if (checkIsInstrumental(normalized)) {
    return { file: baseName, skipped: true, reason: 'instrumental' };
  }

  const lyrics = extractLyrics(normalized);
  if (!lyrics) {
    // Might be a poem adaptation — try to get text from Description
    const descMatch = normalized.match(/## Descripción\n([\s\S]*?)(?=\n## )/);
    const desc = descMatch ? descMatch[1] : '';
    if (!desc) {
      return { file: baseName, skipped: true, reason: 'no lyrics' };
    }
    return { file: baseName, skipped: true, reason: 'poem-adaptation' };
  }

  const title = extractTitle(normalized);
  const sections = extractSections(lyrics);
  const allLyricalLines = lyrics.split('\n').filter(l => {
    const t = l.trim();
    return t && !/^\[.*\]$/.test(t) && !/^\(.*\)$/.test(t);
  });
  const allText = allLyricalLines.join('\n').toLowerCase();

  // 1. 30%+ rimas asonantes o libres
  const schemeMatch = normalized.match(/## Esquema de rima\n([\s\S]*?)\n## Checklist/);
  let check1 = '❌ No verificado';
  if (schemeMatch) {
    const scheme = schemeMatch[1].toLowerCase();
    if (scheme.includes('asonante') || scheme.includes('libre')) {
      check1 = '✅ ' + scheme.replace(/\n/g, ' ').trim().slice(0, 120);
    } else if (scheme.includes('consonante')) {
      check1 = '⚠️ Rima consonante — no se verifica 30% asonante/libre automáticamente';
    } else {
      check1 = '⚠️ ' + scheme.replace(/\n/g, ' ').trim().slice(0, 100);
    }
  }

  // 2. Máximo 1 tríada
  const triadas = countTriadas(allText);
  const check2 = triadas <= 1 ? `✅ ${triadas} tríadas` : `❌ ${triadas} tríadas encontradas`;

  // 3. 0 em dashes consecutivos (0 em dashes en general)
  const emDashes = countEmDashes(allText);
  const check3 = emDashes === 0 ? '✅' : `⚠️ ${emDashes} em dash(es) encontrados`;

  // 4. ≥1 coloquialismo por estrofa
  const coloquialismos = findColloquialisms(allText);
  const strophes = countStrophes(sections);
  const check4 = coloquialismos.length >= strophes
    ? `✅ ${coloquialismos.slice(0, 5).join(', ')}${coloquialismos.length > 5 ? '...' : ''}`
    : `⚠️ ${coloquialismos.length} coloquialismos para ${strophes} estrofas`;

  // 5. ≥1 verso con métrica quebrada — hard to auto-detect, default
  const check5 = '✅ (asumido — validación manual requerida)';

  // 6. No etiquetar figuras retóricas
  const hasTags = /met[áa]fora|s[íi]mil|analog[íi]a|personificaci[óo]n|hip[ée]rbole|aliteraci[óo]n/i.test(allText);
  const check6 = hasTags ? '❌ Etiqueta figuras retóricas en la letra' : '✅';

  // 7. Detalles sensoriales ≥1 por estrofa
  const sensoryWords = [
    /olor/i, /huele?/i, /perfume/i, /fragancia/i, /hedor/i, /tufo/i,
    /fr[ií]o/i, /calor/i, /tibia?/i, /helad[ao]/i, /calient[ae]/i, /ardient[ae]/i,
    /suave/i, /[áa]sper[ao]/i, /rugos[ao]/i, /lis[ao]/i, /bland[ao]/i, /dulce/i,
    /amarg[ao]/i, /[áa]cid[ao]/i, /salad[ao]/i,
    /brill[ao]/i, /oscuro/i, /roj[ao]/i, /blanco/i, /negro/i, /azul/i, /verde/i,
    /sonido/i, /ruido/i, /silenc[ii]o/i, /m[úu]sic[ao]/i,
    /sabor/i, /sabe?/i, /sab[oó]r/i,
  ];
  const sensoryFound = [];
  for (const p of sensoryWords) {
    const matches = allText.match(p);
    if (matches) sensoryFound.push(matches[0]);
  }
  const check7 = sensoryFound.length >= strophes
    ? `✅ ${[...new Set(sensoryFound.map(m => m.toLowerCase()))].slice(0, 6).join(', ')}${sensoryFound.length > 6 ? '...' : ''}`
    : `⚠️ ${sensoryFound.length} referencias sensoriales para ${strophes} estrofas`;

  // 8. Verbos/adj ≥ 2:1
  const check8 = '✅ (asumido — validación manual requerida)';

  // 9. 1 imagen absurda o surrealista
  const check9 = '✅ (asumido — validación manual requerida)';

  // 10. Cero palabras listado prohibido
  const violations10 = [];
  for (const p of PROHIBITED_WORDS) {
    const m = allText.match(p);
    if (m) violations10.push(m[0]);
  }
  const check10 = violations10.length === 0
    ? '✅'
    : `❌ ${[...new Set(violations10.map(v => v.toLowerCase()))].join(', ')}`;

  // 11. Cero AI-ismos semánticos
  const violations11 = [];
  for (const p of SEMANTIC_AI_ISMS) {
    if (p.test(allText)) violations11.push(p.source);
  }
  const check11 = violations11.length === 0
    ? '✅'
    : `❌ ${violations11.join(', ')}`;

  // 12. Cero verbos forzados
  const violations12 = [];
  for (const p of FORZED_VERBS) {
    if (p.test(allText)) violations12.push(p.source);
  }
  const check12 = violations12.length === 0
    ? '✅'
    : `❌ ${violations12.join(', ')}`;

  // 13. Cero negative parallelism ("no es X, es Y")
  const negParMatch = allText.match(/no\s+es\s+\w+[^,]*,\s*es\s+/i);
  const check13 = negParMatch ? `❌ "${negParMatch[0]}"` : '✅';

  // 14. Sin parallel negation encadenada (no X, no Y, no Z)
  const negChain = allText.match(/(no\s+\w+[^,]*,\s*no\s+\w+[^,]*,\s*no\s+\w+)/i);
  const check14 = negChain ? `❌ "${negChain[0].slice(0, 80)}..."` : '✅';

  // 15. Sin anaphora abuse (máx 2 versos)
  const maxAna = checkAnaphora(allLyricalLines);
  const check15 = maxAna <= 2
    ? `✅ (máx ${maxAna} versos consecutivos)`
    : `❌ ${maxAna} versos consecutivos con misma apertura`;

  // 16. Puente sin "Pero" al inicio
  let check16 = '✅ (sin puente o sin "Pero")';
  for (const [name, lines] of Object.entries(sections)) {
    if (/bridge|puente/i.test(name) && lines.length > 0) {
      const firstLine = lines[0].trim().toLowerCase();
      if (firstLine.startsWith('pero')) {
        check16 = '❌ Puente empieza con "Pero"';
      } else {
        check16 = `✅ Puente empieza con "${firstLine.split(/\s+/).slice(0, 3).join(' ')}"`;
      }
      break;
    }
  }

  // 17. Título repetido <4 veces en chorus
  const titleCount = countTitleInChorus(title, sections);
  const check17 = titleCount < 4
    ? `✅ (${titleCount} veces en coro)`
    : `❌ ${titleCount} veces en coro`;

  // 18. Abstracto anclado a objeto concreto — hard, basic check
  const check18 = '✅ (asumido — validación manual requerida)';

  // 19. Especificidad objetual
  const specificObjects = allText.match(
    /\b(man[oa]|puerta|ventana|mesa|cama|sill[oa]n|cocina|ba[ñn]o|espejo|caj[oó]n|botella|taza|plato|cuchara|vaso|libro|hoja|l[áa]piz|coche|bus|tren|calle|plaza|esquina|banco|farol|sem[áa]foro|parque|jard[ií]n|huerta|campo|r[ií]o|mar|monta[ñn]a|[áa]rbol|flor|piedra|tierra|barro|polvo|techo|suelo|pared|escalera|puente|torre|muro|reja|llave|candado|carta|sobre|sello|reloj|vela|foto|espejo|peine|cepillo|toalla|s[áa]bana|almohada|colcha|coj[ií]n|cortina|l[áa]mpara|bombilla|cable|enchufe|grifo|piloto|nevera|horno)\b/i
  );
  const objCount = specificObjects ? specificObjects.length : 0;
  const check19 = objCount >= strophes
    ? `✅ ${objCount} objetos concretos`
    : `⚠️ ${objCount} objetos concretos para ${strophes} estrofas`;

  // 20. Sin promoción alcohol/tabaco/drogas
  const substancePatterns = [
    /whisky|whiskey|vodka|ron|cerveza|vino\s+(tinto|blanco)|champ[áa]n|cava|licor/i,
    /cigarrillo|tabaco|pitillo|fumar|humo/i,
    /coca[íi]na|marihuana|porro|hach[ií]s|\bweed\b|droga/i,
    /borrach[ao]|ebrio|embriagad[ao]/i,
  ];
  let check20 = '✅';
  for (const p of substancePatterns) {
    if (p.test(allText) && !/humo\s+de\s+la\s+chimenea/i.test(allText)) {
      // Contextual: if found, check if negative framing
      // Simple approach: flag for manual review
      check20 = '⚠️ Posible mención — revisión manual';
      break;
    }
  }

  // 21. Principios edificantes
  const problematic = [
    /venganza/i, /suicid[io]/i, /autolesión/i, /cortar[ae]se/i,
  ];
  let check21 = '✅';
  for (const p of problematic) {
    if (p.test(allText)) {
      check21 = '⚠️ Contenido a revisar — ' + p.source;
      break;
    }
  }

  const checks = [check1, check2, check3, check4, check5, check6, check7,
    check8, check9, check10, check11, check12, check13, check14,
    check15, check16, check17, check18, check19, check20, check21];

  const safeguardLabels = [
    '30%+ rimas asonantes/libres',
    'Máximo 1 tríada',
    '0 em dashes',
    '≥1 coloquialismo por estrofa',
    '≥1 verso métrica quebrada',
    'No etiquetar figuras retóricas',
    'Detalles sensoriales ≥1 por estrofa',
    'Verbos/adj ≥ 2:1',
    '1 imagen absurda o surrealista',
    'Cero palabras listado prohibido',
    'Cero AI-ismos semánticos',
    'Cero verbos forzados',
    'Cero negative parallelism',
    'Sin parallel negation encadenada',
    'Sin anaphora abuse (máx 2 versos)',
    'Puente sin "Pero" al inicio',
    'Título repetido <4 veces en chorus',
    'Abstracto anclado a objeto concreto',
    'Especificidad objetual',
    'Sin promoción alcohol/tabaco/drogas',
    'Principios edificantes',
  ];

  // Build table
  let table = '| # | Safeguard | Cumple |\n';
  table += '|---|-----------|--------|\n';
  for (let i = 0; i < checks.length; i++) {
    const num = i + 1;
    const safe = safeguardLabels[i];
    const result = checks[i];
    table += `| ${num} | ${safe} | ${result} |\n`;
  }

  return { file: baseName, table, skipped: false };
}

function hasExistingChecklist(content) {
  const normalized = nl(content);
  const m = normalized.match(/## Checklist Anti-AI\n\n\| # \| Safeguard \| Cumple \|\n\|---\|-----------\|--------\|\n([\s\S]*?)(?=\n## [\w])/);
  if (!m) return false;
  const rows = m[1].trim().split('\n').filter(r => r.trim() && r.includes('|'));
  if (rows.length === 0) return false;
  return rows.some(r => !r.includes('asumido') && !r.includes('no se verifica') && r.includes('✅'));
}

const files = fs.readdirSync(CANCIONES_DIR)
  .filter(f => f.endsWith('.md'))
  .map(f => path.join(CANCIONES_DIR, f));

let processed = 0;
let skipped = 0;
let errors = [];

for (const file of files) {
  const content = fs.readFileSync(file, 'utf-8');

  // Skip if already has a detailed checklist
  if (hasExistingChecklist(content)) {
    console.log(`  ✓ ${path.basename(file)} (ya tenía checklist)`);
    skipped++;
    continue;
  }

  const result = processSong(file);
  if (result.skipped) {
    console.log(`  ~ ${result.file} (${result.reason})`);
    skipped++;
    continue;
  }

  try {
    const content = fs.readFileSync(file, 'utf-8');
    const normalized = nl(content);

    // Try multiple patterns to match the checklist section
    const patterns = [
      /## Checklist Anti-AI\n\n[\s\S]*?(?=\n## Changelog)/,
      /## Checklist Anti-AI\n\n[\s\S]*?(?=\n## \w)/,
    ];

    let updated = normalized;
    for (const pattern of patterns) {
      const candidate = normalized.replace(pattern, `## Checklist Anti-AI\n\n${result.table}`);
      if (candidate !== normalized) {
        updated = candidate;
        break;
      }
    }

    if (updated === normalized) {
      errors.push(`${result.file}: could not insert`);
      continue;
    }

    fs.writeFileSync(file, updated, 'utf-8');
    console.log(`  ✓ ${result.file}`);
    processed++;
  } catch (err) {
    errors.push(`${result.file}: ${err.message}`);
  }
}

console.log(`\n=== Resumen ===`);
console.log(`  Procesadas: ${processed}`);
console.log(`  Omitidas: ${skipped}`);
if (errors.length > 0) {
  console.log(`  Errores: ${errors.length}`);
  for (const e of errors.slice(0, 10)) console.log(`    ${e}`);
}

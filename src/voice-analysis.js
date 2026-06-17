const fs = require('fs');
const path = require('path');

const argv = process.argv.slice(2);
const prefix = argv[0] || '';
const range = argv[1] || '';
const artist = argv[2] || '';

if (!prefix || !range || !artist) {
    console.error('Usage: node voice-analysis.js <prefix> <range> <artist>');
    process.exit(1);
}

const templatePath = path.join(__dirname, '..', 'specs', '013-voice-analysis-template.md');
let content = '';

try {
    content = fs.readFileSync(templatePath, 'utf8');
} catch (e) {
    content = '# Voice Analysis Template\n\n(Template missing: specs/013-voice-analysis-template.md)';
}

// Replace placeholders with values
const analysis = content
    .replace(/\[ARTIST\]/g, artist)
    .replace(/\[PREFIX\]/g, prefix)
    .replace(/\[RANGE\]/g, range);

process.stdout.write(analysis);

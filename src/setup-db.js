require('dotenv').config();
const fs = require('fs');
const path = require('path');
const mysql = require('mysql2/promise');

async function runSqlFile(connection, filePath) {
  console.log(`Running ${filePath}...`);
  const sql = fs.readFileSync(filePath, 'utf8');
  const statements = sql.split(';');
  for (const statement of statements) {
    const trimmed = statement.trim();
    if (trimmed) {
      await connection.query(trimmed);
    }
  }
}

async function main() {
  const connection = await mysql.createConnection({
    host: process.env.MYSQL_HOST || '127.0.0.1',
    port: parseInt(process.env.MYSQL_PORT || '3306'),
    user: process.env.MYSQL_USER || 'root',
    password: process.env.MYSQL_PASS || '',
    database: process.env.MYSQL_DB || 'composer',
    multipleStatements: true
  });

  try {
    await connection.query('CREATE DATABASE IF NOT EXISTS composer');
    await connection.query('USE composer');

    const sqlFiles = [
      'sql/schema.sql',
      'sql/seed-genres.sql',
      'sql/seed-albums.sql',
      'sql/seed-themes.sql'
    ];

    for (const file of sqlFiles) {
      await runSqlFile(connection, path.join(__dirname, '..', file));
    }

    console.log('Database setup completed successfully.');
  } catch (err) {
    console.error('Database setup error:', err);
    process.exit(1);
  } finally {
    await connection.end();
  }
}

main();
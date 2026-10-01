-- Seed data for genres table
-- Populated from docs/indice-por-genero.md and specs

-- Pop
INSERT INTO genres (name, parent_id, spotify_tag) VALUES 
('Pop', NULL, 'pop'),
('Pop rock', (SELECT id FROM genres WHERE name='Pop'), 'pop rock'),
('Latin pop', (SELECT id FROM genres WHERE name='Pop'), 'latin pop'),
('Synth-pop', (SELECT id FROM genres WHERE name='Pop'), 'synth pop'),
('Dream pop', (SELECT id FROM genres WHERE name='Pop'), 'dream pop'),
('Alt-pop', (SELECT id FROM genres WHERE name='Pop'), 'alt pop');

-- Indie
INSERT INTO genres (name, parent_id, spotify_tag) VALUES 
('Indie', NULL, 'indie'),
('Spanish indie pop', (SELECT id FROM genres WHERE name='Indie'), 'spanish indie pop'),
('Indie pop', (SELECT id FROM genres WHERE name='Indie'), 'indie pop'),
('Indie folk', (SELECT id FROM genres WHERE name='Indie'), 'indie folk');

-- Folk
INSERT INTO genres (name, parent_id, spotify_tag) VALUES 
('Folk', NULL, 'folk'),
('Folk pop', (SELECT id FROM genres WHERE name='Folk'), 'folk pop'),
('Folk latino', (SELECT id FROM genres WHERE name='Folk'), 'folk latino'),
('Neo-folk', (SELECT id FROM genres WHERE name='Folk'), 'neo folk');

-- Other genres
INSERT INTO genres (name, parent_id, spotify_tag) VALUES 
('Balada', NULL, 'balada'),
('Chamber pop', NULL, 'chamber pop'),
('Orchestral pop', NULL, 'orchestral pop'),
('Clásica', (SELECT id FROM genres WHERE name='Orchestral pop'), 'classical'),
('Electrónica', NULL, 'electronic'),
('Rock', NULL, 'rock'),
('Soft rock', (SELECT id FROM genres WHERE name='Rock'), 'soft rock'),
('Acoustic rock', (SELECT id FROM genres WHERE name='Rock'), 'acoustic rock'),
('Latin rock', (SELECT id FROM genres WHERE name='Rock'), 'latin rock'),
('Reggaetón-pop', NULL, 'reggaeton pop'),
('Cumbia', NULL, 'cumbia'),
('Vallenato', NULL, 'vallenato'),
('Acoustic pop', NULL, 'acoustic pop'),
('Cinematográfico', NULL, 'cinematic'),
('Musical theater', NULL, 'musical theater');

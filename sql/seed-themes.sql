-- Seed data for themes table
-- Categorized by type: mood, theme, activity, era

-- Mood
INSERT INTO themes (name, category) VALUES 
('nostálgico', 'mood'),
('melancólico', 'mood'),
('esperanzador', 'mood'),
('enérgico', 'mood'),
('tranquilo', 'mood'),
('íntimo', 'mood');

-- Theme
INSERT INTO themes (name, category) VALUES 
('familia', 'theme'),
('amor', 'theme'),
('superación', 'theme'),
('identidad', 'theme'),
('naturaleza', 'theme'),
('ciudad', 'theme');

-- Activity
INSERT INTO themes (name, category) VALUES 
('workout', 'activity'),
('study', 'activity'),
('sleep', 'activity'),
('driving', 'activity'),
('relaxing', 'activity');

-- Era
INSERT INTO themes (name, category) VALUES 
('2000s', 'era'),
('2010s', 'era'),
('2020s', 'era'),
('modern', 'era'),
('retro', 'era');
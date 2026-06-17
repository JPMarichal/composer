-- Composer MySQL Schema
-- Base de datos de catálogo musical

SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

-- 1. Géneros (jerárquicos)
CREATE TABLE IF NOT EXISTS genres (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE,
  parent_id INT NULL,
  spotify_tag VARCHAR(100) NULL,
  description TEXT NULL,
  FOREIGN KEY (parent_id) REFERENCES genres(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. Songs (entidad central)
CREATE TABLE IF NOT EXISTS songs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  file_path VARCHAR(500) NOT NULL UNIQUE,
  notion_id VARCHAR(36) NULL UNIQUE,
  spotify_uri VARCHAR(50) NULL,
  suno_url VARCHAR(500) NULL,
  description TEXT NULL,
  bpm INT NULL,
  key_signature VARCHAR(10) NULL,
  time_signature VARCHAR(10) NULL,
  progression VARCHAR(255) NULL,
  structure TEXT NULL,
  is_instrumental BOOLEAN DEFAULT FALSE,
  is_featured BOOLEAN DEFAULT FALSE,
  year INT NULL,
  composition_date DATE NULL,
  status_composicion ENUM('borrador','en_proceso','terminada') DEFAULT 'terminada',
  status_publicacion ENUM('sin_publicar','distribuida','publicada') DEFAULT 'sin_publicar',
  generator VARCHAR(50) NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_title (title),
  INDEX idx_status_comp (status_composicion),
  INDEX idx_status_pub (status_publicacion),
  INDEX idx_year (year),
  INDEX idx_is_instrumental (is_instrumental)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. Song‑Genres (M:N)
CREATE TABLE IF NOT EXISTS song_genres (
  song_id INT NOT NULL,
  genre_id INT NOT NULL,
  PRIMARY KEY (song_id, genre_id),
  FOREIGN KEY (song_id) REFERENCES songs(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. Themes
CREATE TABLE IF NOT EXISTS themes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE,
  category ENUM('mood','theme','activity','era') NOT NULL,
  description TEXT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 5. Song‑Themes (M:N)
CREATE TABLE IF NOT EXISTS song_themes (
  song_id INT NOT NULL,
  theme_id INT NOT NULL,
  PRIMARY KEY (song_id, theme_id),
  FOREIGN KEY (song_id) REFERENCES songs(id) ON DELETE CASCADE,
  FOREIGN KEY (theme_id) REFERENCES themes(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 6. Albums
CREATE TABLE IF NOT EXISTS albums (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  release_date DATE NULL,
  description TEXT NULL,
  cover_url VARCHAR(500) NULL,
  notion_id VARCHAR(36) NULL,
  is_single BOOLEAN DEFAULT FALSE,
  upc VARCHAR(20) NULL,
  distribuidor VARCHAR(100) NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_title (title),
  INDEX idx_release (release_date),
  INDEX idx_is_single (is_single)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 7. Album‑Tracks (M:N)
CREATE TABLE IF NOT EXISTS album_tracks (
  album_id INT NOT NULL,
  song_id INT NOT NULL,
  track_number INT NOT NULL,
  PRIMARY KEY (album_id, song_id),
  FOREIGN KEY (album_id) REFERENCES albums(id) ON DELETE CASCADE,
  FOREIGN KEY (song_id) REFERENCES songs(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 8. Keywords (SEO, fase 2)
CREATE TABLE IF NOT EXISTS keywords (
  id INT AUTO_INCREMENT PRIMARY KEY,
  word VARCHAR(100) NOT NULL,
  category ENUM('genre','mood','activity','era','instrument') NOT NULL,
  language VARCHAR(5) NOT NULL DEFAULT 'es',
  search_volume INT NULL,
  UNIQUE KEY uk_keyword (word, category, language)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 9. Playlists (fase 2)
CREATE TABLE IF NOT EXISTS playlists (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT NULL,
  spotify_playlist_id VARCHAR(36) NULL,
  spotify_url VARCHAR(500) NULL,
  target_genre VARCHAR(100) NULL,
  target_mood VARCHAR(100) NULL,
  target_activity VARCHAR(100) NULL,
  target_era VARCHAR(50) NULL,
  track_count INT DEFAULT 80,
  is_published BOOLEAN DEFAULT FALSE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 10. Playlist‑Tracks (M:N)
CREATE TABLE IF NOT EXISTS playlist_tracks (
  playlist_id INT NOT NULL,
  song_id INT NOT NULL,
  position INT NOT NULL,
  is_own_track BOOLEAN DEFAULT TRUE,
  added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (playlist_id, song_id),
  FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE,
  FOREIGN KEY (song_id) REFERENCES songs(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 11. Playlist‑Keywords (M:N)
CREATE TABLE IF NOT EXISTS playlist_keywords (
  playlist_id INT NOT NULL,
  keyword_id INT NOT NULL,
  PRIMARY KEY (playlist_id, keyword_id),
  FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE,
  FOREIGN KEY (keyword_id) REFERENCES keywords(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

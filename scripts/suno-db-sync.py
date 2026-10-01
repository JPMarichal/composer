"""Sync suno-index.json to SQLite database with full metadata.

Creates/updates a SQLite database with all clip metadata from the enriched index.
Also creates project subdirectories for organizing downloaded files.

Usage:
    python scripts/suno-db-sync.py
"""

import json, os, re, sqlite3, time
from pathlib import Path

PROJECT_ROOT = Path("C:\\own\\composer")
INDEX_PATH = PROJECT_ROOT / "suno-index.json"
DB_PATH = PROJECT_ROOT / "canciones" / "audio" / "bksuno" / "_downloads.sqlite"
BKDIR = PROJECT_ROOT / "canciones" / "audio" / "bksuno"


def sanitize_project_name(name):
    """Sanitize project name for filesystem path."""
    if not name:
        return "My_Workspace"  # Default for Unassigned
    # Remove invalid Windows path characters
    s = re.sub(r'[<>:"|?*\\/]', "", name)
    # Replace spaces and special chars with underscores
    s = re.sub(r"[\s_]+", "_", s)
    s = s.strip(". ")
    if len(s) > 100:
        s = s[:100]
    return s or "My_Workspace"


def create_table(conn):
    """Create the clips table if it doesn't exist."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS clips (
            id TEXT PRIMARY KEY,
            title TEXT,
            status TEXT,
            created_at TEXT,
            model_name TEXT,
            major_model_version TEXT,
            project_id TEXT,
            project_name TEXT,
            project_description TEXT,
            duration REAL,
            mp3_url TEXT,
            m4a_url TEXT,
            image_url TEXT,
            image_large_url TEXT,
            lyrics TEXT,
            style_prompt TEXT,
            display_tags TEXT,
            is_instrumental BOOLEAN,
            can_remix BOOLEAN,
            has_stem BOOLEAN,
            play_count INTEGER,
            upvote_count INTEGER,
            user_id TEXT,
            display_name TEXT,
            handle TEXT,
            is_public BOOLEAN,
            is_hidden BOOLEAN,
            is_trashed BOOLEAN,
            explicit BOOLEAN,
            has_hook BOOLEAN,
            batch_index INTEGER,
            created_by TEXT,
            downloaded INTEGER DEFAULT 0,
            local_path TEXT,
            mp3_local_path TEXT,
            m4a_local_path TEXT,
            downloaded_at TEXT,
            video_url TEXT,
            audio_url TEXT,
            media_urls TEXT,
            is_verified BOOLEAN DEFAULT 0,
            project_data TEXT,
            albums_data TEXT,
            has_vocal BOOLEAN DEFAULT 0,
            stream BOOLEAN DEFAULT 0,
            uses_latest_model BOOLEAN DEFAULT 0,
            clip_type TEXT,
            task TEXT
        )
    """)

    # ── WAV Download Tracking Columns ─────────────────────────
    wav_columns = {
        "wav_queued": "INTEGER DEFAULT 0",       # 0=not queued, 1=queued, 2=skipped
        "wav_status": "TEXT DEFAULT 'pending'",   # pending/converting/downloading/complete/error/skipped
        "wav_downloaded": "INTEGER DEFAULT 0",   # 0/1
        "wav_local_path": "TEXT",                # path to WAV file
        "wav_size_bytes": "INTEGER",             # file size
        "wav_converted_at": "TEXT",              # timestamp of conversion trigger
        "wav_downloaded_at": "TEXT",             # timestamp of download completion
        "wav_error": "TEXT",                     # error message
        "wav_skip_reason": "TEXT",               # why skipped (experimental, low_priority, etc.)
        "wav_priority": "INTEGER DEFAULT 0",     # 0=normal, 1=high, -1=low
        "wav_attempts": "INTEGER DEFAULT 0",     # download attempt count
    }
    for col, definition in wav_columns.items():
        try:
            conn.execute(f"ALTER TABLE clips ADD COLUMN {col} {definition}")
        except sqlite3.OperationalError:
            pass  # Column already exists (migration is idempotent)

    # ── WAV Download Log Table ────────────────────────────────
    conn.execute("""
        CREATE TABLE IF NOT EXISTS wav_download_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            clip_id TEXT NOT NULL,
            action TEXT NOT NULL,           -- "convert_wav" | "get_wav_url" | "download" | "complete" | "error" | "skip"
            status TEXT,                    -- "success" | "error" | "timeout" | "skipped"
            detail TEXT,                    -- human-readable message or error
            duration_sec REAL,               -- how long the action took
            timestamp TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_wav_log_clip ON wav_download_log(clip_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_wav_log_ts ON wav_download_log(timestamp)")

    # ── Indexes for WAV tracking ──────────────────────────────
    conn.execute("CREATE INDEX IF NOT EXISTS idx_wav_queued ON clips(wav_queued)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_wav_status ON clips(wav_status)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_wav_priority ON clips(wav_priority DESC, created_at)")

    conn.commit()


def sync_index(conn, index_data):
    """Sync clips from index data to SQLite."""
    clips = index_data.get("clips", [])
    inserted = 0
    updated = 0

    for c in clips:
        cid = c["id"]
        project_name = c.get("project_name") or "My Workspace"
        project_dir = sanitize_project_name(project_name)

        # Create project directory
        project_path = BKDIR / project_dir
        project_path.mkdir(parents=True, exist_ok=True)

        # Sanitize title for local path
        title = c.get("title") or "untitled"
        safe_title = sanitize_filename(title)

        # Determine local paths
        mp3_local = f"{project_dir}/{safe_title}.mp3"
        m4a_local = f"{project_dir}/{safe_title}.m4a"

        # Extract new fields from clip data (with defaults for missing fields)
        video_url = c.get("video_url", "") or ""
        audio_url = c.get("audio_url", "") or ""
        media_urls = (
            json.dumps(c.get("media_urls", [])) if c.get("media_urls") else None
        )
        is_verified = c.get("is_verified", False)
        project_data = json.dumps(c.get("project", {})) if c.get("project") else None
        albums_data = json.dumps(c.get("albums", [])) if c.get("albums") else None

        # Extract metadata fields
        metadata = c.get("metadata", {}) or {}
        has_vocal = metadata.get("has_vocal", False)
        stream = metadata.get("stream", False)
        uses_latest_model = metadata.get("uses_latest_model", False)
        clip_type = metadata.get("type", "")
        task = metadata.get("task", "")

        # Insert or update
        cursor = conn.execute(
            """
            INSERT OR IGNORE INTO clips (
                id, title, status, created_at, model_name, major_model_version,
                project_id, project_name, project_description, duration,
                mp3_url, m4a_url, image_url, image_large_url,
                lyrics, style_prompt, display_tags, is_instrumental,
                can_remix, has_stem, play_count, upvote_count,
                user_id, display_name, handle, is_public, is_hidden,
                is_trashed, explicit, has_hook, batch_index, created_by,
                downloaded, local_path, mp3_local_path, m4a_local_path,
                downloaded_at, video_url, audio_url, media_urls,
                is_verified, project_data, albums_data,
                has_vocal, stream, uses_latest_model, clip_type, task
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                cid,
                c.get("title"),
                c.get("status"),
                c.get("created_at"),
                c.get("model_name"),
                c.get("major_model_version"),
                c.get("project_id"),
                c.get("project_name"),
                c.get("project_description"),
                c.get("duration"),
                c.get("mp3_url"),
                c.get("m4a_url"),
                c.get("image_url"),
                c.get("image_large_url"),
                c.get("lyrics"),
                c.get("style_prompt"),
                c.get("display_tags"),
                c.get("is_instrumental"),
                c.get("can_remix"),
                c.get("has_stem"),
                c.get("play_count", 0),
                c.get("upvote_count", 0),
                c.get("user_id"),
                c.get("display_name"),
                c.get("handle"),
                c.get("is_public", False),
                c.get("is_hidden", False),
                c.get("is_trashed", False),
                c.get("explicit", False),
                c.get("has_hook", False),
                c.get("batch_index", 0),
                c.get("created_by"),
                0,  # downloaded
                c.get("local_path"),  # Will be updated by download script
                mp3_local,
                m4a_local,
                None,  # downloaded_at
                video_url,
                audio_url,
                media_urls,
                is_verified,
                project_data,
                albums_data,
                has_vocal,
                stream,
                uses_latest_model,
                clip_type,
                task,
            ),
        )

        if cursor.rowcount == 1:
            inserted += 1
        else:
            # Update existing record
            conn.execute(
                """
                UPDATE clips SET
                    title = ?, status = ?, created_at = ?, model_name = ?,
                    major_model_version = ?, project_id = ?, project_name = ?,
                    project_description = ?, duration = ?, mp3_url = ?, m4a_url = ?,
                    image_url = ?, image_large_url = ?, lyrics = ?, style_prompt = ?,
                    display_tags = ?, is_instrumental = ?, can_remix = ?, has_stem = ?,
                    play_count = ?, upvote_count = ?, user_id = ?, display_name = ?,
                    handle = ?, is_public = ?, is_hidden = ?, is_trashed = ?,
                    explicit = ?, has_hook = ?, batch_index = ?, created_by = ?,
                    video_url = ?, audio_url = ?, media_urls = ?,
                    is_verified = ?, project_data = ?, albums_data = ?,
                    has_vocal = ?, stream = ?, uses_latest_model = ?, clip_type = ?, task = ?
                WHERE id = ?
                """,
                (
                    c.get("title"),
                    c.get("status"),
                    c.get("created_at"),
                    c.get("model_name"),
                    c.get("major_model_version"),
                    c.get("project_id"),
                    c.get("project_name"),
                    c.get("project_description"),
                    c.get("duration"),
                    c.get("mp3_url"),
                    c.get("m4a_url"),
                    c.get("image_url"),
                    c.get("image_large_url"),
                    c.get("lyrics"),
                    c.get("style_prompt"),
                    c.get("display_tags"),
                    c.get("is_instrumental"),
                    c.get("can_remix"),
                    c.get("has_stem"),
                    c.get("play_count", 0),
                    c.get("upvote_count", 0),
                    c.get("user_id"),
                    c.get("display_name"),
                    c.get("handle"),
                    c.get("is_public", False),
                    c.get("is_hidden", False),
                    c.get("is_trashed", False),
                    c.get("explicit", False),
                    c.get("has_hook", False),
                    c.get("batch_index", 0),
                    c.get("created_by"),
                    video_url,
                    audio_url,
                    media_urls,
                    is_verified,
                    project_data,
                    albums_data,
                    has_vocal,
                    stream,
                    uses_latest_model,
                    clip_type,
                    task,
                    cid,
                ),
            )
            updated += 1

    conn.commit()
    return inserted, updated


def sanitize_filename(s):
    """Sanitize title for filesystem."""
    if not s:
        return "untitled"
    s = s.replace("\n", " ").replace("\r", " ").replace("\t", " ").replace("\\", " ")
    s = re.sub(r'[<>:"|?*\\/]', "", s)
    s = "".join(c for c in s if ord(c) > 31 or c == " ")
    s = re.sub(r"[\s_]+", "_", s)
    s = s.strip(". ")
    if len(s) > 200:
        s = s[:200]
    s = s.strip(". ")
    return s or "untitled"


def main():
    print("=" * 70)
    print("  Suno DB Sync — Index to SQLite")
    print("=" * 70)

    # Load index
    print("\n  Loading suno-index.json ...")
    with open(INDEX_PATH, encoding="utf-8") as f:
        index_data = json.load(f)

    clips = index_data.get("clips", [])
    print(f"  Index has {len(clips)} clips total.")

    # Create/open database
    BKDIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    create_table(conn)

    # Sync
    print("\n  Syncing to database ...")
    inserted, updated = sync_index(conn, index_data)
    print(f"  Inserted: {inserted}")
    print(f"  Updated: {updated}")

    # Stats
    cursor = conn.execute("SELECT COUNT(*) FROM clips")
    total = cursor.fetchone()[0]
    print(f"  Total in database: {total}")

    cursor = conn.execute("SELECT COUNT(*) FROM clips WHERE downloaded = 1")
    downloaded = cursor.fetchone()[0]
    print(f"  Downloaded: {downloaded}")

    cursor = conn.execute("SELECT COUNT(*) FROM clips WHERE downloaded = 0")
    pending = cursor.fetchone()[0]
    print(f"  Pending download: {pending}")

    # Project breakdown
    cursor = conn.execute("""
        SELECT COALESCE(project_name, 'My_Workspace'), COUNT(*),
               SUM(CASE WHEN is_instrumental = 1 THEN 1 ELSE 0 END)
        FROM clips
        GROUP BY project_name
        ORDER BY COUNT(*) DESC
    """)
    print(f"\n  Projects ({len(cursor.fetchall())}):")
    cursor.execute("""
        SELECT COALESCE(project_name, 'My_Workspace'), COUNT(*),
               SUM(CASE WHEN is_instrumental = 1 THEN 1 ELSE 0 END)
        FROM clips
        GROUP BY project_name
        ORDER BY COUNT(*) DESC
    """)
    for row in cursor.fetchall():
        pn = row[0] if row[0] else "My_Workspace"
        print(f"    {pn:35s} {row[1]:4d} clips ({row[2]} instrumental)")

    # WAV download stats
    wav_cursor = conn.execute("""
        SELECT
            SUM(CASE WHEN wav_downloaded = 1 THEN 1 ELSE 0 END) as wav_done,
            SUM(CASE WHEN wav_queued = 1 THEN 1 ELSE 0 END) as wav_queued,
            SUM(CASE WHEN wav_status = 'error' THEN 1 ELSE 0 END) as wav_errors,
            SUM(CASE WHEN wav_skip_reason IS NOT NULL AND wav_skip_reason != '' THEN 1 ELSE 0 END) as wav_skipped,
            SUM(CASE WHEN wav_queued = 0 AND wav_downloaded = 0 AND wav_skip_reason IS NULL THEN 1 ELSE 0 END) as wav_pending
        FROM clips
    """)
    row = wav_cursor.fetchone()
    print(f"\n  WAV Backlog:")
    print(f"    Downloaded:   {row[0] or 0}")
    print(f"    Queued:       {row[1] or 0}")
    print(f"    Pending:      {row[4] or 0}")
    print(f"    Errors:       {row[2] or 0}")
    print(f"    Skipped:      {row[3] or 0}")

    # Check "último eslabón"
    cursor = conn.execute("""
        SELECT id, title, project_name, created_at
        FROM clips
        WHERE LOWER(title) LIKE '%ultimo%' OR LOWER(title) LIKE '%eslabon%'
        ORDER BY created_at DESC
        LIMIT 15
    """)
    print("\n  'Último eslabón' clips:")
    rows = cursor.fetchall()
    if rows:
        for r in rows:
            print(f'    "{r[1]}" | {r[0][:8]}... | {r[2]} | {r[3][:10]}')
    else:
        print("    NOT FOUND")

    conn.close()
    print(f"\n  Database: {DB_PATH}")
    print("  Done.")


if __name__ == "__main__":
    main()

"""WAV Download Backlog Manager.

Manages the WAV download backlog in SQLite — queue clips for download,
skip experimental/unwanted clips, set priorities, and view stats.

Usage:
    python scripts/suno-wav-manager.py list                    # Show pending clips with project/duration
    python scripts/suno-wav-manager.py stats                   # Show WAV backlog statistics
    python scripts/suno-wav-manager.py queue <project> <n>     # Queue N clips from a project for WAV
    python scripts/suno-wav-manager.py queue all [n]           # Queue all complete clips
    python scripts/suno-wav-manager.py skip <clip_id> <reason> # Skip a clip with reason
    python scripts/suno-wav-manager.py skip-by-query <pattern> <reason>  # Skip clips matching title pattern
    python scripts/suno-wav-manager.py priority <clip_id> <level>  # Set priority (-2..+2)
    python scripts/suno-wav-manager.py clear-skips              # Clear all skip reasons
    python scripts/suno-wav-manager.py log                     # Show recent WAV download log entries
"""
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = Path(os.environ.get("WAV_DB_PATH")) if os.environ.get("WAV_DB_PATH") else PROJECT_ROOT / "canciones" / "audio" / "bksuno" / "_downloads.sqlite"

SKIP_REASONS = {
    "experimental": "Experimental/unfinished clip",
    "low_quality": "Low audio quality or error",
    "short": "Duration below threshold",
    "duplicate": "Duplicate or remix",
    "instrumental_no_vocal": "Instrumental (no vocal to preserve)",
    "not_interesting": "Content not relevant",
    "other": "Other reason (manual)",
}


def get_conn():
    if not DB_PATH.exists():
        print(f"ERROR: Database not found at {DB_PATH}")
        print("  Run 'python scripts/suno-db-sync.py' first.")
        sys.exit(1)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def run_migration():
    """Ensure WAV columns exist (idempotent)."""
    conn = get_conn()
    wav_columns = {
        "wav_queued": "INTEGER DEFAULT 0",
        "wav_status": "TEXT DEFAULT 'pending'",
        "wav_downloaded": "INTEGER DEFAULT 0",
        "wav_local_path": "TEXT",
        "wav_size_bytes": "INTEGER",
        "wav_converted_at": "TEXT",
        "wav_downloaded_at": "TEXT",
        "wav_error": "TEXT",
        "wav_skip_reason": "TEXT",
        "wav_priority": "INTEGER DEFAULT 0",
        "wav_attempts": "INTEGER DEFAULT 0",
    }
    for col, definition in wav_columns.items():
        try:
            conn.execute(f"ALTER TABLE clips ADD COLUMN {col} {definition}")
        except sqlite3.OperationalError:
            pass
    conn.execute("""
        CREATE TABLE IF NOT EXISTS wav_download_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            clip_id TEXT NOT NULL,
            action TEXT NOT NULL,
            status TEXT,
            detail TEXT,
            duration_sec REAL,
            timestamp TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_wav_log_clip ON wav_download_log(clip_id)")
    conn.commit()
    conn.close()


def cmd_list(args):
    conn = get_conn()
    query = """
        SELECT id, title, project_name, duration, model_name,
               wav_queued, wav_downloaded, wav_skip_reason, wav_priority,
               created_at
        FROM clips
        WHERE status = 'complete' AND is_trashed = 0
    """
    params = []

    # Filter by status
    status_filter = "all"
    if args and args[0] in ("pending", "queued", "downloaded", "skipped", "errors"):
        status_filter = args[0]
        if status_filter == "pending":
            query += " AND wav_queued = 0 AND wav_downloaded = 0 AND (wav_skip_reason IS NULL OR wav_skip_reason = '')"
        elif status_filter == "queued":
            query += " AND wav_queued = 1 AND wav_downloaded = 0"
        elif status_filter == "downloaded":
            query += " AND wav_downloaded = 1"
        elif status_filter == "skipped":
            query += " AND wav_skip_reason IS NOT NULL AND wav_skip_reason != ''"
        elif status_filter == "errors":
            query += " AND wav_status = 'error'"
    elif args and len(args) > 0:
        # Filter by project name (fuzzy)
        query += " AND project_name LIKE ?"
        params = [f"%{args[0]}%"]

    query += " ORDER BY wav_priority DESC, created_at DESC LIMIT 100"
    rows = conn.execute(query, params).fetchall()

    print(f"{'ID[:8]':10s} {'Title[:35]':35s} {'Project[:20]':20s} {'Dur':>6s}  {'Q':>1s} {'D':>1s} {'S':>1s} {'P':>2s}  {'QueuedAt'}")
    print("-" * 100)
    for r in rows:
        dur = f"{int(r['duration'] or 0)//60}:{int(r['duration'] or 0)%60:02d}" if r['duration'] else "--:--"
        print(
            f"{r['id'][:8]:10s} "
            f"{str(r['title'] or '')[:35]:35s} "
            f"{str(r['project_name'] or '')[:20]:20s} "
            f"{dur:>6s}  "
            f"{r['wav_queued']:>1d} {r['wav_downloaded']:>1d} "
            f"{'✓' if r['wav_skip_reason'] else '-':>1s} "
            f"{r['wav_priority'] if r['wav_priority'] is not None else 0:>2d}  "
            f"{r['created_at'][:10] if r['created_at'] else '?'}"
        )
    if len(rows) >= 100:
        print(f"\n  (showing first 100 of {len(rows)} results)")
    conn.close()


def cmd_stats(args):
    conn = get_conn()
    row = conn.execute("""
        SELECT
            COUNT(*) as total,
            SUM(CASE WHEN wav_downloaded = 1 THEN 1 ELSE 0 END) as downloaded,
            SUM(CASE WHEN wav_queued = 1 AND wav_downloaded = 0 THEN 1 ELSE 0 END) as queued,
            SUM(CASE WHEN wav_queued = 0 AND wav_downloaded = 0 AND (wav_skip_reason IS NULL OR wav_skip_reason = '') THEN 1 ELSE 0 END) as pending,
            SUM(CASE WHEN wav_skip_reason IS NOT NULL AND wav_skip_reason != '' THEN 1 ELSE 0 END) as skipped,
            SUM(CASE WHEN wav_status = 'error' THEN 1 ELSE 0 END) as errors,
            SUM(CASE WHEN is_instrumental = 1 THEN 1 ELSE 0 END) as instrumental,
            SUM(CASE WHEN is_instrumental = 0 THEN 1 ELSE 0 END) as with_vocal
        FROM clips
        WHERE status = 'complete' AND is_trashed = 0
    """).fetchone()

    print("=" * 60)
    print("  WAV DOWNLOAD BACKLOG STATISTICS")
    print("=" * 60)
    print(f"  Total complete clips:        {row['total']}")
    print(f"  ┌ WAV downloaded:             {row['downloaded'] or 0}")
    print(f"  ├ WAV queued:                 {row['queued'] or 0}")
    print(f"  ├ WAV pending (not queued):   {row['pending'] or 0}")
    print(f"  ├ WAV skipped:                {row['skipped'] or 0}")
    print(f"  └ WAV errors:                 {row['errors'] or 0}")
    print(f"\n  With vocal: {row['with_vocal'] or 0} | Instrumental: {row['instrumental'] or 0}")

    # Skip reasons breakdown
    reasons = conn.execute("""
        SELECT wav_skip_reason, COUNT(*) as cnt
        FROM clips
        WHERE wav_skip_reason IS NOT NULL AND wav_skip_reason != ''
        GROUP BY wav_skip_reason
        ORDER BY cnt DESC
    """).fetchall()
    if reasons:
        print(f"\n  Skip reasons:")
        for r in reasons:
            print(f"    {r['wav_skip_reason'][:30]:30s} {r['cnt']:4d}")

    # Priority breakdown
    prios = conn.execute("""
        SELECT wav_priority, COUNT(*) as cnt
        FROM clips
        WHERE wav_queued = 1 OR wav_downloaded = 1 OR wav_status = 'error'
        GROUP BY wav_priority
        ORDER BY wav_priority DESC
    """).fetchall()
    if prios:
        print(f"\n  Priority distribution (queued+downloaded+errors):")
        for r in prios:
            print(f"    P{r['wav_priority']:+d}: {r['cnt']:4d}")

    conn.close()


def cmd_queue(args):
    conn = get_conn()
    if len(args) >= 2 and args[0] == "all":
        count = int(args[1]) if len(args) > 1 else 999999
        if count == 999999 or count == "all":
            updated = conn.execute("""
                UPDATE clips SET wav_queued = 1, wav_status = 'pending'
                WHERE status = 'complete' AND is_trashed = 0
                  AND wav_downloaded = 0 AND (wav_skip_reason IS NULL OR wav_skip_reason = '')
            """).rowcount
        else:
            updated = conn.execute("""
                UPDATE clips SET wav_queued = 1, wav_status = 'pending'
                WHERE status = 'complete' AND is_trashed = 0
                  AND wav_downloaded = 0 AND (wav_skip_reason IS NULL OR wav_skip_reason = '')
                LIMIT ?
            """, (count,)).rowcount
        conn.commit()
        print(f"Queued {updated} clips for WAV download")
    elif len(args) >= 2:
        project = args[0]
        count = int(args[1])
        updated = conn.execute("""
            UPDATE clips SET wav_queued = 1, wav_status = 'pending'
            WHERE project_name LIKE ? AND status = 'complete' AND is_trashed = 0
              AND wav_downloaded = 0 AND (wav_skip_reason IS NULL OR wav_skip_reason = '')
            LIMIT ?
        """, (f"%{project}%", count)).rowcount
        conn.commit()
        print(f"Queued {updated} clips from project '{project}' for WAV download")
    else:
        print("Usage: queue <project> <n>  |  queue all [n]")
    conn.close()


def cmd_skip(args):
    if len(args) < 2:
        print("Usage: skip <clip_id[:8]> <reason>")
        print(f"Reasons: {', '.join(SKIP_REASONS.keys())}")
        return
    clip_id_partial = args[0]
    reason_key = args[1]
    reason = SKIP_REASONS.get(reason_key, reason_key)

    conn = get_conn()
    row = conn.execute("SELECT id FROM clips WHERE id LIKE ?", (f"{clip_id_partial}%",)).fetchone()
    if not row:
        print(f"Clip not found: {clip_id_partial}")
        return
    conn.execute(
        "UPDATE clips SET wav_queued = 2, wav_skip_reason = ?, wav_status = 'skipped'",
        (reason, row["id"]),
    )
    conn.commit()
    print(f"Skipped clip {row['id'][:8]}... with reason: {reason}")
    conn.close()


def cmd_priority(args):
    if len(args) < 2:
        print("Usage: priority <clip_id[:8]> <level (-2..+2)>")
        return
    clip_id_partial = args[0]
    level = int(args[1])
    if level < -2 or level > 2:
        print("Priority must be between -2 and +2")
        return

    conn = get_conn()
    row = conn.execute("SELECT id FROM clips WHERE id LIKE ?", (f"{clip_id_partial}%",)).fetchone()
    if not row:
        print(f"Clip not found: {clip_id_partial}")
        return
    conn.execute("UPDATE clips SET wav_priority = ?", (level, row["id"]))
    conn.commit()
    print(f"Set priority {level} for clip {row['id'][:8]}...")
    conn.close()


def cmd_clear_skips(args):
    conn = get_conn()
    updated = conn.execute("""
        UPDATE clips SET wav_skip_reason = NULL, wav_queued = 0, wav_status = 'pending'
        WHERE wav_skip_reason IS NOT NULL AND wav_skip_reason != ''
    """).rowcount
    conn.commit()
    print(f"Cleared skip reasons on {updated} clips")
    conn.close()


def cmd_skip_by_query(args):
    """Skip clips matching a title pattern or SQL condition."""
    if len(args) < 2:
        print("Usage: skip-by-query <title_pattern> <reason>")
        print("  title_pattern: regex matched against clip title (case-insensitive)")
        print(f"  Reasons: {', '.join(SKIP_REASONS.keys())}")
        return
    pattern = args[0]
    reason_key = args[1]
    reason = SKIP_REASONS.get(reason_key, reason_key)

    conn = get_conn()
    # Use SQLite REGEXP (case-insensitive) — fallback to LIKE if no regexp
    try:
        updated = conn.execute(
            "UPDATE clips SET wav_queued = 2, wav_skip_reason = ?, wav_status = 'skipped' "
            "WHERE LOWER(title) LIKE ? AND wav_queued IN (0,1) AND wav_downloaded = 0",
            (reason, f"%{pattern}%"),
        ).rowcount
    except Exception:
        conn.execute("CREATE TEMP TABLE IF NOT EXISTS regexp_stub(x)")
        conn.commit()
        updated = conn.execute(
            "UPDATE clips SET wav_queued = 2, wav_skip_reason = ?, wav_status = 'skipped' "
            "WHERE instr(LOWER(title), LOWER(?)) > 0 AND wav_queued IN (0,1) AND wav_downloaded = 0",
            (reason, pattern),
        ).rowcount
    conn.commit()
    print(f"Skipped {updated} clips matching '{pattern}' with reason: {reason}")
    conn.close()


def cmd_log(args):
    """Show recent WAV download log entries."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT clip_id, action, status, detail, duration_sec, timestamp
        FROM wav_download_log
        ORDER BY id DESC
        LIMIT 30
    """).fetchall()
    if not rows:
        print("No log entries yet. Start a WAV download to populate the log.")
        return
    print(f"{'Timestamp':<20s} {'Clip[:8]':10s} {'Action':14s} {'Status':10s} {'Dur':>6s}  Detail")
    print("-" * 100)
    for r in rows:
        dur = f"{r['duration_sec']:.1f}s" if r['duration_sec'] else "-"
        print(f"{r['timestamp'][:19]:20s} {r['clip_id'][:8]:10s} {r['action']:14s} {str(r['status'] or ''):10s} {dur:>6s}  {str(r['detail'] or '')[:30]}")
    conn.close()


COMMANDS = {
    "list": cmd_list,
    "list-pending": lambda a: cmd_list(["pending"]),
    "list-queued": lambda a: cmd_list(["queued"]),
    "list-downloaded": lambda a: cmd_list(["downloaded"]),
    "list-skipped": lambda a: cmd_list(["skipped"]),
    "list-errors": lambda a: cmd_list(["errors"]),
    "stats": cmd_stats,
    "queue": cmd_queue,
    "skip": cmd_skip,
    "priority": cmd_priority,
    "clear-skips": cmd_clear_skips,
    "skip-by-query": cmd_skip_by_query,
    "log": cmd_log,
}


def main():
    run_migration()

    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        print(f"\nCommands: {', '.join(COMMANDS.keys())}")
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]
    COMMANDS[cmd](args)


if __name__ == "__main__":
    main()

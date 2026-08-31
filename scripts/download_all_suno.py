"""Backup ALL Suno clips as MP3 + m4a-opus to canciones/audio/bksuno/.

Resume-aware sequential download with retry logic and checkpoint persistence.
Downloads both MP3 and m4a-opus formats, organized by project subdirectories.
Updates SQLite database with download status and paths.

Usage:
    python scripts/download_all_suno.py
"""

import json, os, re, sqlite3, sys, time, requests, urllib3
from pathlib import Path

# ── paths ──────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
INDEX_PATH = PROJECT_ROOT / "suno-index.json"
DB_PATH = PROJECT_ROOT / "canciones" / "audio" / "bksuno" / "_downloads.sqlite"
BKDIR = PROJECT_ROOT / "canciones" / "audio" / "bksuno"
CHECKPOINT_PATH = PROJECT_ROOT / ".suno-download-checkpoint.json"

# ── config ─────────────────────────────────────────────────────────
MAX_RETRIES = 5
REQUEST_TIMEOUT = (15, 60)  # connect, read
DELAY_BETWEEN = 0.3  # seconds between requests
RETRY_BACKOFF_BASE = 2  # exponential backoff base
RETRY_BACKOFF_MAX = 60  # max delay between retries
MIN_FILE_SIZE = 100_000  # bytes below which file is rejected
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB cap
CHECKPOINT_EVERY = 25  # save checkpoint every N downloads


def sanitize_filename(s):
    """Sanitize title for filesystem — remove ALL problematic chars for Windows."""
    s = s.replace("\n", " ").replace("\r", " ").replace("\t", " ").replace("\\", " ")
    s = re.sub(r'[<>:"|?*\\/]', "", s)
    s = "".join(c for c in s if ord(c) > 31 or c == " ")
    s = re.sub(r"[\s_]+", "_", s)
    s = s.strip(". ")
    if len(s) > 200:
        s = s[:200]
    s = s.strip(". ")
    return s or "untitled"


def sanitize_project_name(name):
    """Sanitize project name for filesystem path."""
    if not name:
        return "My_Workspace"
    s = re.sub(r'[<>:"|?*\\/]', "", name)
    s = re.sub(r"[\s_]+", "_", s)
    s = s.strip(". ")
    if len(s) > 100:
        s = s[:100]
    return s or "My_Workspace"


def load_checkpoint():
    """Load checkpoint from disk, or return empty state."""
    if not CHECKPOINT_PATH.exists():
        return {"completed": [], "failed_attempts": {}, "last_run": None}
    try:
        with open(CHECKPOINT_PATH, encoding="utf-8") as f:
            cp = json.load(f)
        if isinstance(cp.get("completed"), list) and isinstance(
            cp.get("failed_attempts"), dict
        ):
            return cp
    except (json.JSONDecodeError, OSError):
        pass
    print("  [!] Corrupted checkpoint file, starting fresh.")
    return {"completed": [], "failed_attempts": {}, "last_run": None}


def save_checkpoint(completed, failed_attempts):
    """Atomically save checkpoint to disk."""
    tmp_path = str(CHECKPOINT_PATH) + ".tmp"
    data = {
        "completed": completed,
        "failed_attempts": failed_attempts,
        "last_run": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, str(CHECKPOINT_PATH))
    except OSError:
        try:
            os.remove(tmp_path)
        except OSError:
            pass


def clean_tmp_files(bkdir):
    """Remove all pending .tmp files from previous failed downloads."""
    for tmp in bkdir.rglob("*.tmp"):
        try:
            tmp.unlink()
        except OSError:
            pass


def attempt_download_file(url, save_path, session, max_retries=MAX_RETRIES):
    """Try downloading a file with exponential backoff retries.

    Returns (success, detail, size_bytes).
    """
    last_err = "unknown"
    last_size = 0

    for attempt in range(1, max_retries + 1):
        try:
            response = session.get(url, timeout=REQUEST_TIMEOUT, stream=True)

            if response.status_code != 200:
                return (False, f"HTTP {response.status_code}", 0)

            content_length = response.headers.get("Content-Length")
            if content_length:
                cl = int(content_length)
                if cl < MIN_FILE_SIZE:
                    return (False, f"too small ({cl} bytes)", 0)
                if cl > MAX_FILE_SIZE:
                    return (False, f"too large ({cl} bytes)", 0)

            # Ensure parent directory exists
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            # Stream to temp file
            total = 0
            tmp_path = save_path + ".tmp"
            with open(tmp_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=65536):
                    if not chunk:
                        break
                    f.write(chunk)
                    total += len(chunk)
                    if total > MAX_FILE_SIZE:
                        raise ValueError("File too large (>50MB)")

            if total <= MIN_FILE_SIZE:
                try:
                    os.remove(tmp_path)
                except OSError:
                    pass
                return (False, f"too small ({total} bytes)", 0)

            # Atomic rename
            os.rename(tmp_path, save_path)
            return (True, "OK", total)

        except Exception as e:
            # Clean up temp file
            tmp_path = save_path + ".tmp"
            try:
                os.remove(tmp_path)
            except OSError:
                pass

            last_err = str(e)

            # Parse HTTP status if present
            sc = None
            err_str = str(last_err)
            if err_str.startswith("HTTP "):
                try:
                    sc = int(err_str.split()[1])
                except (ValueError, IndexError):
                    pass

            # If not retryable, give up immediately
            non_retryable = {400, 404, 410, 422}
            if sc and sc in non_retryable:
                return (False, last_err, 0)

            transient_patterns = [
                "timed out",
                "timeout",
                "connection",
                "reset",
                "broken",
                "refused",
                "temporary",
                "server error",
                "502",
                "503",
                "504",
                "ssl",
                "certificate",
                "abort",
                "closed",
                "pipe",
            ]
            msg_lower = err_str.lower() if err_str else ""
            if not any(p in msg_lower for p in transient_patterns):
                return (False, last_err, 0)

            # Wait before retry (exponential backoff)
            if attempt < max_retries:
                delay = min(RETRY_BACKOFF_BASE**attempt, RETRY_BACKOFF_MAX)
                time.sleep(delay)

    return (False, f"Gave up after {max_retries} retries: {last_err}", 0)


def main():
    bkdir = BKDIR
    bkdir.mkdir(parents=True, exist_ok=True)

    # Clean up any leftover .tmp files from previous failed runs
    clean_tmp_files(bkdir)

    # Load database
    print("=" * 70)
    print("  Suno Backup — MP3 + m4a-opus (by project)")
    print("=" * 70)
    print("\n  Loading database ...")

    if not DB_PATH.exists():
        print(
            "  ERROR: Database not found. Run 'python scripts/suno-db-sync.py' first."
        )
        return

    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.execute(
        """
        SELECT id, title, project_name, mp3_url, m4a_url,
               mp3_local_path, m4a_local_path
        FROM clips
        WHERE status = 'complete' AND is_trashed = 0
        """
    )
    clips = cursor.fetchall()
    print(f"  Database has {len(clips)} complete clips.")

    # Load checkpoint
    cp = load_checkpoint()
    completed_ids = set(cp["completed"])
    failed_attempts = cp["failed_attempts"].copy()

    # Determine which clips need work
    all_ids = set(c[0] for c in clips)
    new_clips = []
    retry_clips = []

    for row in clips:
        cid = row[0]
        title = row[1]
        project_name = row[2]
        mp3_url = row[3] or ""
        m4a_url = row[4] or ""
        mp3_local = row[5] or ""
        m4a_local = row[6] or ""

        # Check if both files exist
        mp3_exists = (
            os.path.exists(os.path.join(bkdir, mp3_local)) if mp3_local else False
        )
        m4a_exists = (
            os.path.exists(os.path.join(bkdir, m4a_local)) if m4a_local else False
        )

        if mp3_exists and m4a_exists:
            # Already downloaded
            if cid not in completed_ids:
                completed_ids.add(cid)
            continue

        # Check checkpoint
        if cid in completed_ids:
            # Marked as completed but files missing - retry
            failed_attempts[cid] = 0
            retry_clips.append(
                (cid, title, project_name, mp3_url, m4a_url, mp3_local, m4a_local)
            )
        elif cid in failed_attempts and failed_attempts[cid] < MAX_RETRIES:
            retry_clips.append(
                (cid, title, project_name, mp3_url, m4a_url, mp3_local, m4a_local)
            )
        else:
            new_clips.append(
                (cid, title, project_name, mp3_url, m4a_url, mp3_local, m4a_local)
            )

    print(f"\n  New clips to download: {len(new_clips)}")
    print(f"  Failed clips to retry: {len(retry_clips)}")
    print(f"  Already on disk (skipped): {len(completed_ids)}")

    total_to_process = len(new_clips) + len(retry_clips)
    if total_to_process == 0:
        print("\n  Nothing left to do! All clips are downloaded.")
        conn.close()
        return

    # Combine: new first, then retries
    work_queue = new_clips + retry_clips
    print(f"  Total to process this run: {total_to_process}")

    # Setup session — cdn uses self-signed certs, must disable SSL verify
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        }
    )
    session.verify = False

    # Download loop
    ok = fail = skip = 0
    results = []
    start_time = time.time()
    checkpoint_completed = list(completed_ids)
    checkpoint_failed = dict(failed_attempts)

    print(f"\n{'=' * 70}")
    print(f"  Downloading to {bkdir}")
    print(f"{'=' * 70}\n")

    for i, (
        cid,
        title,
        project_name,
        mp3_url,
        m4a_url,
        mp3_local,
        m4a_local,
    ) in enumerate(work_queue, 1):
        is_retry = cid in failed_attempts

        # Construct URLs directly (API doesn't always include them)
        if not mp3_url:
            mp3_url = f"https://cdn1.suno.ai/{cid}.mp3"
        if not m4a_url:
            m4a_url = f"https://d2lwuy8qc234o3.cloudfront.net/1/clip/{cid}.m4a"

        print(f"[{i}/{total_to_process}] {'Retry ' if is_retry else ''}{title} ({cid})")
        print(f"    MP3 URL: {mp3_url[:80]}...")
        print(f"    m4a URL: {m4a_url[:80]}...")
        print(f"    MP3 path: {mp3_local}")
        print(f"    m4a path: {m4a_local}")

        # Check if files already exist
        mp3_exists = os.path.exists(os.path.join(bkdir, mp3_local))
        m4a_exists = os.path.exists(os.path.join(bkdir, m4a_local))

        # Download only what's missing
        mp3_success = True
        mp3_detail = "already exists"
        mp3_size = 0
        if not mp3_exists:
            mp3_success, mp3_detail, mp3_size = attempt_download_file(
                mp3_url, os.path.join(bkdir, mp3_local), session
            )

        m4a_success = True
        m4a_detail = "already exists"
        m4a_size = 0
        if not m4a_exists and m4a_url:
            m4a_success, m4a_detail, m4a_size = attempt_download_file(
                m4a_url, os.path.join(bkdir, m4a_local), session
            )

        # Determine overall success
        overall_success = mp3_success and m4a_success

        if overall_success:
            ok += 1
            checkpoint_completed.append(cid)
            checkpoint_failed.pop(cid, None)

            # Update SQLite
            conn.execute(
                """
                UPDATE clips SET
                    downloaded = 1,
                    mp3_local_path = ?,
                    m4a_local_path = ?,
                    downloaded_at = ?
                WHERE id = ?
                """,
                (mp3_local, m4a_local, time.strftime("%Y-%m-%dT%H:%M:%S"), cid),
            )
            conn.commit()

            size_mb = (mp3_size + m4a_size) / (1024 * 1024)
            results.append((title, True, size_mb))

            print(
                f"    [OK] MP3: {mp3_size / (1024 * 1024):.1f} MB | m4a: {m4a_size / (1024 * 1024):.1f} MB"
            )

        else:
            fail += 1
            checkpoint_failed[cid] = checkpoint_failed.get(cid, 0) + 1
            results.append((title, False, f"MP3: {mp3_detail}, m4a: {m4a_detail}"))

            # Show detailed error for first few failures
            if fail <= 5 or i % 50 == 0:
                print(f"    [FAIL] MP3: {mp3_detail}")
                print(f"    [FAIL] m4a: {m4a_detail}")

            if i % 50 == 0:
                elapsed = time.time() - start_time
                print(
                    f"  [checkpoint saved] OK:{ok} FAIL:{fail} | {elapsed / 60:.1f}min"
                )

        # Save checkpoint periodically
        if i % CHECKPOINT_EVERY == 0:
            save_checkpoint(checkpoint_completed, checkpoint_failed)
            elapsed = time.time() - start_time
            rate = i / elapsed if elapsed > 0 else 0
            eta = (total_to_process - i) / rate if rate > 0 else 0
            print(
                f"  [checkpoint] OK:{ok} FAIL:{fail} | {elapsed / 60:.1f}min | ETA: {eta / 60:.1f}h"
            )

        # Small delay between requests
        time.sleep(DELAY_BETWEEN)

    # Final checkpoint save and DB update
    save_checkpoint(checkpoint_completed, checkpoint_failed)
    conn.close()

    # Summary
    elapsed_total = time.time() - start_time
    print(f"\n{'=' * 70}")
    print("  SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Clips processed this run: {ok + fail}")
    print(f"  Downloaded successfully:   {ok}")
    print(f"  Failed permanently:        {fail}")
    print(f"  Skipped (already on disk): {skip}")
    print(f"  Time elapsed:              {elapsed_total / 60:.1f} minutes")
    if elapsed_total > 0:
        print(
            f"  Rate:                      {total_to_process / elapsed_total * 60:.0f} clips/hour"
        )

    total_size = sum(d for _, d, _ in results if isinstance(d, (int, float)) and d > 0)
    print(f"  Downloaded this run:       {total_size / (1024 * 1024):.0f} MB")
    print(f"  Destination:               {bkdir}")

    # Show permanent failures
    perm_failures = [(t, err) for t, s, err in results if not s]
    if perm_failures:
        print(f"\n  Failed clips ({len(perm_failures)}):")
        for title, err in perm_failures[:20]:
            print(f"    - {title}: {err}")
        if len(perm_failures) > 20:
            print(f"    ... and {len(perm_failures) - 20} more")

    # Remaining to download
    remaining = (
        len(all_ids)
        - len(checkpoint_completed)
        - len([cid for cid, count in checkpoint_failed.items() if count >= MAX_RETRIES])
    )
    if remaining > 0:
        print(f"\n  Still pending (will retry next run): {remaining}")
    else:
        print(f"\n  All clips downloaded!")

    print(f"\nDone.")


if __name__ == "__main__":
    main()

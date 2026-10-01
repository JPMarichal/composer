"""Surguical WAV download for a specific Suno project.

Usage:
    python scripts/suno-download-wav.py <project_name> [output_dir]

Downloads WAVs for all clips in the given project to the output directory.
Uses SQLite for tracking (wav_download_log, wav_downloaded, wav_status).

Runs from inside the Podman container:
    WAV_DB_PATH=/app/data/_downloads.sqlite \
    python3 /app/project_wav.py "<Project>" /app/downloads/<project>_wavs
"""
import json, os, re, sqlite3, sys, time, urllib.request, urllib.error

DB_PATH = os.environ.get("WAV_DB_PATH", "/app/data/_downloads.sqlite")
API_BASE = "http://localhost:8080"
POLL_INTERVAL = 5
MAX_POLL = 24
MAX_RETRIES = 3
DOWNLOAD_TIMEOUT = 120
CONVERT_TIMEOUT = 90


def api_get(path, timeout=30):
    req = urllib.request.Request(f"{API_BASE}{path}", method="GET")
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        ct = r.headers.get("Content-Type", "")
        return r.status, json.loads(r.read()) if "json" in ct else r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:500]
    except Exception as e:
        return 0, str(e)


def api_post(path, timeout=CONVERT_TIMEOUT):
    req = urllib.request.Request(f"{API_BASE}{path}", method="POST")
    req.add_header("Content-Type", "application/json")
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:500]
    except Exception as e:
        return 0, str(e)


def sanitize_filename(s):
    if not s:
        return "untitled"
    s = s.replace("\n", " ").replace("\r", " ").replace("\t", " ").replace("\\", " ")
    s = re.sub(r'[<>:"|?*\\/]', "", s)
    s = "".join(c for c in s if ord(c) > 31 or c == " ")
    s = re.sub(r"[\s.]+", "_", s)
    s = s.strip("._ ")
    if len(s) > 200:
        s = s[:200]
    return s or "untitled"


def log_event(conn, clip_id, action, status, detail="", duration=0):
    conn.execute(
        "INSERT INTO wav_download_log (clip_id, action, status, detail, duration_sec) VALUES (?,?,?,?,?)",
        (clip_id, action, status, detail, round(duration, 2)),
    )
    conn.commit()


def download_wav(conn, clip_id, save_path):
    t_start = time.time()

    t0 = time.time()
    code, result = api_post(f"/suno/convert-wav?id={clip_id}")
    if code != 200:
        detail = f"convert failed: HTTP {code}: {result[:200]}"
        log_event(conn, clip_id, "convert_wav", "error", detail, time.time() - t0)
        return False, detail
    log_event(conn, clip_id, "convert_wav", "success", "WAV conversion triggered", time.time() - t0)

    t0 = time.time()
    wav_url = None
    for attempt in range(MAX_POLL):
        code, r = api_get(f"/suno/wav-url?id={clip_id}")
        if code == 200 and isinstance(r, dict):
            wav_url = r.get("wav_file_url")
            if wav_url:
                break
        elif code != 200:
            log_event(conn, clip_id, "get_wav_url", "error", f"HTTP {code}: {str(r)[:200]}", time.time() - t0)
            return False, f"poll error: HTTP {code}"
        time.sleep(POLL_INTERVAL)

    poll_dur = time.time() - t0
    if not wav_url:
        detail = f"URL timeout ({MAX_POLL * POLL_INTERVAL}s)"
        log_event(conn, clip_id, "get_wav_url", "timeout", detail, poll_dur)
        return False, detail
    log_event(conn, clip_id, "get_wav_url", "success", "URL obtained", poll_dur)

    for attempt in range(1, MAX_RETRIES + 1):
        t0 = time.time()
        try:
            req = urllib.request.Request(wav_url, method="GET")
            with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT) as resp:
                size = int(resp.headers.get("Content-Length", 0))
                if size < 100_000:
                    log_event(conn, clip_id, "download", "error", f"too small ({size})", 0)
                    return False, f"file too small ({size} bytes)"

                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                total = 0
                tmp_path = save_path + ".tmp"
                with open(tmp_path, "wb") as f:
                    while True:
                        chunk = resp.read(65536)
                        if not chunk:
                            break
                        f.write(chunk)
                        total += len(chunk)
                os.rename(tmp_path, save_path)

                dur = time.time() - t0
                log_event(conn, clip_id, "download", "success", f"{total/1048576:.1f} MB", dur)
                return True, f"OK ({total/1048576:.1f} MB)"
        except Exception as e:
            if attempt < MAX_RETRIES:
                time.sleep(min(2 ** attempt, 15))
        else:
            last = str(e)

    log_event(conn, clip_id, "download", "error", f"failed after {MAX_RETRIES} retries: {last}", time.time() - t0)
    return False, f"download failed: {last}"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("Usage: python3 project_wav.py <project_name> [output_dir]")
        sys.exit(1)

    project_name = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else f"/app/downloads/{project_name.replace(' ', '_').lower()}_wavs"

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    clips = conn.execute("""
        SELECT id, title, project_name, duration, wav_downloaded, wav_status
        FROM clips
        WHERE project_name LIKE ? AND status = 'complete' AND is_trashed = 0
        ORDER BY wav_priority DESC, created_at DESC
    """, (f"%{project_name}%",)).fetchall()

    print(f"Project: {project_name}")
    print(f"Found {len(clips)} complete clips")
    print(f"Output:  {output_dir}")
    print(f"Already downloaded WAV: {sum(1 for c in clips if c['wav_downloaded'] == 1)}")
    print(f"To download: {len(clips) - sum(1 for c in clips if c['wav_downloaded'] == 1)}")

    pending = [c for c in clips if c["wav_downloaded"] == 0]
    if not pending:
        print("All clips already have WAV files. Nothing to do.")
        conn.close()
        return

    os.makedirs(output_dir, exist_ok=True)
    ok = fail = skip = 0
    start = time.time()

    for i, clip in enumerate(pending, 1):
        clip_id = clip["id"]
        title = clip["title"] or "untitled"
        safe_title = sanitize_filename(title)
        save_path = os.path.join(output_dir, f"{safe_title}_{clip_id[:8]}.wav")
        dur_str = f"{int(clip['duration'] or 0)//60}:{int(clip['duration'] or 0)%60:02d}" if clip["duration"] else "--:--"

        if os.path.exists(save_path):
            print(f"[{i}/{len(pending)}] SKIP (exists): {title[:35]} ({dur_str})")
            conn.execute(
                "UPDATE clips SET wav_downloaded=1, wav_status='complete', "
                "wav_local_path=?, wav_size_bytes=?, wav_downloaded_at=datetime('now') WHERE id=?",
                (save_path, os.path.getsize(save_path), clip_id),
            )
            conn.commit()
            log_event(conn, clip_id, "skip", "success", "WAV already on disk", 0)
            skip += 1
            continue

        print(f"[{i}/{len(pending)}] {title[:35]} ({clip_id[:8]}) [{dur_str}]")

        success, detail = download_wav(conn, clip_id, save_path)
        if success:
            ok += 1
            conn.execute(
                "UPDATE clips SET wav_downloaded=1, wav_status='complete', "
                "wav_local_path=?, wav_size_bytes=?, wav_downloaded_at=datetime('now') WHERE id=?",
                (save_path, os.path.getsize(save_path), clip_id),
            )
            conn.commit()
            print(f"  WAV: {detail}")
        else:
            fail += 1
            conn.execute(
                "UPDATE clips SET wav_status='error', wav_error=?, wav_queued=2 WHERE id=?",
                (detail, clip_id),
            )
            conn.commit()
            print(f"  FAIL: {detail}")

        if i % 3 == 0:
            elapsed = time.time() - start
            rate = i / elapsed if elapsed > 0 else 0
            eta = (len(pending) - i) / rate if rate > 0 else 0
            print(f"  [checkpoint] ok={ok} fail={fail} | ETA: {eta/60:.1f}h")

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"  WAV DOWNLOAD SUMMARY")
    print(f"  Project: {project_name}")
    print(f"{'='*60}")
    print(f"  Total in project: {len(clips)}")
    print(f"  Downloaded: {ok}")
    print(f"  Failed: {fail}")
    print(f"  Skipped (exists): {skip}")
    print(f"  Time: {elapsed/60:.1f} min")
    if ok > 0:
        print(f"  Rate: {ok / elapsed * 3600:.1f} clips/hour")
    print(f"  Output: {output_dir}")

    conn.close()


if __name__ == "__main__":
    main()

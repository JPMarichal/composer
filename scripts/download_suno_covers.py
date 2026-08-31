"""Download all Suno covers from the local SQLite database.

Resume-aware sequential download with retry logic and checkpoint persistence.
Overwrites existing files. Updates SQLite database with cover download status.

Usage:
    python scripts/download_suno_covers.py
"""

import json
import logging
import os
import re
import sqlite3
import time
import unicodedata
from pathlib import Path

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PROJECT_ROOT = Path("C:\\own\\composer")
DB_PATH = PROJECT_ROOT / "canciones" / "audio" / "bksuno" / "_downloads.sqlite"
THUMBS_DIR = PROJECT_ROOT / "canciones" / "thumbs"
CHECKPOINT_PATH = PROJECT_ROOT / ".suno-covers-checkpoint.json"
LOG_PATH = PROJECT_ROOT / "logs" / "download_suno_covers.log"

MAX_RETRIES = 4
REQUEST_TIMEOUT = (15, 60)
CHECKPOINT_EVERY = 20


def setup_logging():
    PROJECT_ROOT.joinpath("logs").mkdir(parents=True, exist_ok=True)
    log_file = str(LOG_PATH)
    handler = logging.FileHandler(log_file, encoding="utf-8")
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
    )
    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler],
    )
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def slugify(value):
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "untitled"


def safe_title(value):
    value = value.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    value = re.sub(r'[<>:"|?*\\/]', "", value)
    value = re.sub(r"[\s_]+", "_", value).strip(". ")
    return value[:200] or "untitled"


def load_checkpoint():
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


def attempt_download(url, save_path, session, max_retries=MAX_RETRIES):
    last_err = "unknown"
    for attempt in range(1, max_retries + 1):
        try:
            response = session.get(
                url, timeout=REQUEST_TIMEOUT, headers={"Referer": "https://suno.com/"}
            )
            if response.status_code == 403:
                logging.warning("HTTP 403 on attempt %d for %s", attempt, url)
                print(f" [403 retry {attempt}/{max_retries}]", flush=True)
                time.sleep(2**attempt)
                continue
            if response.status_code != 200:
                return (False, f"HTTP {response.status_code}", 0)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            tmp_path = save_path + ".tmp"
            with open(tmp_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=65536):
                    f.write(chunk)
            os.replace(tmp_path, save_path)
            return (True, "OK", os.path.getsize(save_path))
        except Exception as exc:
            last_err = str(exc)
            logging.warning("Exception on attempt %d for %s: %s", attempt, url, last_err)
            print(f" [error retry {attempt}/{max_retries}: {last_err[:60]}]", flush=True)
            time.sleep(min(2**attempt, 30))
    return (False, f"Gave up after {max_retries} retries: {last_err}", 0)


def main():
    setup_logging()
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute(
        "SELECT id, title, image_url FROM clips WHERE image_url IS NOT NULL AND image_url <> ''"
    )
    clips = cursor.fetchall()
    conn.close()

    cp = load_checkpoint()
    completed_ids = set(cp["completed"])
    failed_attempts = cp["failed_attempts"].copy()

    new_clips = []
    retry_clips = []
    skipped_existing = 0
    for row in clips:
        cid = row[0]
        title = row[1]
        image_url = row[2] or ""
        extension = Path(image_url.split("?", 1)[0]).suffix or ".jpeg"
        filename = f"{slugify(title or 'untitled')}_{cid[:8]}_{safe_title(title or 'untitled')}{extension}"
        destination = THUMBS_DIR / filename

        if destination.exists():
            skipped_existing += 1
            if cid not in completed_ids:
                completed_ids.add(cid)
            continue

        if cid in completed_ids:
            failed_attempts[cid] = 0
            retry_clips.append((cid, title, image_url, filename))
        elif cid in failed_attempts and failed_attempts[cid] < MAX_RETRIES:
            retry_clips.append((cid, title, image_url, filename))
        else:
            new_clips.append((cid, title, image_url, filename))

    work_queue = new_clips + retry_clips
    total_to_process = len(work_queue)
    if total_to_process == 0:
        print(f"\n  All {len(clips)} covers already downloaded. Nothing to do.")
        return

    checkpoint_completed = list(completed_ids)
    checkpoint_failed = dict(failed_attempts)

    print(f"Downloading {total_to_process} covers to {THUMBS_DIR}")
    print(
        f"  New: {len(new_clips)} | Retry: {len(retry_clips)} | Already on disk: {skipped_existing} | DB total: {len(clips)}"
    )
    logging.info(
        "Start: total_db=%d on_disk=%d new=%d retry=%d",
        len(clips), skipped_existing, len(new_clips), len(retry_clips),
    )

    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    session.verify = False

    ok = fail = 0
    forbidden_count = 0
    pre_existing = 0
    start_time = time.time()

    try:
        for i, (cid, title, image_url, filename) in enumerate(work_queue, 1):
            is_retry = cid in failed_attempts
            destination = THUMBS_DIR / filename
            label = title or "untitled"

            print(f"[{i}/{total_to_process}] {label[:60]}... ", end="", flush=True)

            success, detail, size = attempt_download(image_url, str(destination), session)

            if success:
                ok += 1
                checkpoint_completed.append(cid)
                checkpoint_failed.pop(cid, None)
                print(f"OK ({size/1024:.1f}KB)")
                logging.info("OK id=%s file=%s size=%d", cid, filename, size)
            else:
                fail += 1
                checkpoint_failed[cid] = checkpoint_failed.get(cid, 0) + 1
                if "403" in detail:
                    forbidden_count += 1
                    print(f"403 FORBIDDEN")
                    logging.warning("FORBIDDEN id=%s url=%s attempt=%d", cid, image_url, checkpoint_failed[cid])
                else:
                    print(f"FAIL ({detail})")
                    logging.error("FAIL id=%s detail=%s url=%s", cid, detail, image_url)

            if i % CHECKPOINT_EVERY == 0 or i == total_to_process:
                elapsed = time.time() - start_time
                save_checkpoint(checkpoint_completed, checkpoint_failed)
                print(
                    f"  -> checkpoint saved | downloaded={ok} failed={fail} | {elapsed / 60:.1f}min"
                )
    except KeyboardInterrupt:
        last_index = locals().get("i", 0)
        print("\n[!] Interrupted. Saving checkpoint before exit...")
        logging.warning("Interrupted by user at item %d/%d", last_index, total_to_process)
        save_checkpoint(checkpoint_completed, checkpoint_failed)
        raise
    finally:
        save_checkpoint(checkpoint_completed, checkpoint_failed)

    print(f"\nDone: {ok} downloaded, {fail} failed.")
    if forbidden_count:
        print(f"  [!] {forbidden_count} downloads hit HTTP 403 Forbidden. See {LOG_PATH} for details.")
    print(f"Checkpoint saved to {CHECKPOINT_PATH}")
    print(f"Log saved to {LOG_PATH}")


if __name__ == "__main__":
    main()

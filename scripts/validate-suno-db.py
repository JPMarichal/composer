import json
import sqlite3

DB = r"C:\own\composer\canciones\audio\bksuno\_downloads.sqlite"
FIELDS = [
    "video_url",
    "audio_url",
    "media_urls",
    "image_url",
    "image_large_url",
    "display_tags",
    "is_verified",
    "user_id",
    "project_data",
    "albums_data",
    "lyrics",
    "style_prompt",
    "duration",
    "has_stem",
    "has_vocal",
    "stream",
    "uses_latest_model",
    "clip_type",
    "task",
]

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM clips")
total = cur.fetchone()[0]

print("=== Population checks ===")
for field in FIELDS:
    cur.execute(
        f"SELECT COUNT(*) FROM clips WHERE {field} IS NOT NULL "
        f"AND CAST({field} AS TEXT) <> ''"
    )
    print(f"{field}: {cur.fetchone()[0]}/{total}")

print("\n=== JSON checks ===")
for field in ("media_urls", "project_data", "albums_data"):
    cur.execute(f"SELECT id, {field} FROM clips WHERE {field} IS NOT NULL")
    invalid = 0
    for row in cur.fetchall():
        try:
            json.loads(row[1])
        except Exception:
            invalid += 1
    print(f"{field}: invalid={invalid}")

print("\n=== Random samples ===")
cur.execute("SELECT id FROM clips ORDER BY RANDOM() LIMIT 5")
for (clip_id,) in cur.fetchall():
    cur.execute(
        "SELECT id,title,status,created_at,model_name,major_model_version,"
        "video_url,audio_url,media_urls,image_url,image_large_url,display_tags,"
        "is_verified,user_id,project_data,albums_data,lyrics,style_prompt,duration,"
        "has_stem,has_vocal,stream,uses_latest_model,clip_type,task "
        "FROM clips WHERE id=?",
        (clip_id,),
    )
    row = cur.fetchone()
    media_count = len(json.loads(row["media_urls"])) if row["media_urls"] else 0
    print(f"\n{row['id']} | {row['title']}")
    print(
        f"status={row['status']} created={row['created_at']} model={row['model_name']} version={row['major_model_version']}"
    )
    print(
        f"urls: video={bool(row['video_url'])} audio={bool(row['audio_url'])} media={media_count}"
    )
    print(
        f"covers: small={bool(row['image_url'])} large={bool(row['image_large_url'])}"
    )
    print(
        f"owner={row['user_id']} verified={row['is_verified']} project_json={bool(row['project_data'])} albums_json={bool(row['albums_data'])}"
    )
    print(
        f"lyrics={len(row['lyrics'] or '')} chars style={len(row['style_prompt'] or '')} chars duration={row['duration']}"
    )
    print(
        f"metadata: stem={row['has_stem']} vocal={row['has_vocal']} stream={row['stream']} latest={row['uses_latest_model']} type={row['clip_type']} task={row['task']}"
    )

conn.close()

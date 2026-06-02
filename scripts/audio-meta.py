"""Audio metadata: Deezer lookup + librosa analysis.

Subcommands:
  deezer  <song> [artist]  — busca metadata desde Deezer (BPM, ISRC, gain…)
  analyze <audio-file>     — analiza archivo local con librosa
  lookup  <song> [artist]  — Deezer + descarga preview + análisis completo

Ejemplos:
  python scripts/audio-meta.py deezer "Blinding Lights" "The Weeknd"
  python scripts/audio-meta.py analyze mp3/mi_cancion.wav
  python scripts/audio-meta.py lookup "Bohemian Rhapsody" "Queen"
"""
import json, os, sys, tempfile, traceback, re, unicodedata, warnings
from pathlib import Path

import requests
warnings.filterwarnings('ignore', category=FutureWarning)

DEEZER_API = "https://api.deezer.com"

# ─── Normalización ───────────────────────────────────────────

def normalize(s):
    s = s.strip().lower()
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r'[^a-z0-9 ]', '', s)
    return re.sub(r'\s+', ' ', s).strip()


# ─── Deezer ──────────────────────────────────────────────────

def deezer_search_track(song, artist=None):
    q = f'{artist} {song}' if artist else song
    params = {'q': normalize(q)}
    r = requests.get(f'{DEEZER_API}/search/track', params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    if not data.get('data'):
        print(f"  No results for '{q}'")
        return None
    return data['data'][0]


def deezer_track_detail(track_id):
    r = requests.get(f'{DEEZER_API}/track/{track_id}', timeout=15)
    r.raise_for_status()
    return r.json()


def deezer_artist_detail(artist_id):
    r = requests.get(f'{DEEZER_API}/artist/{artist_id}', timeout=15)
    r.raise_for_status()
    return r.json()


def deezer_track_metadata(track_data):
    tid = track_data['id']
    detail = deezer_track_detail(tid)
    artist = deezer_artist_detail(detail['artist']['id'])

    meta = {
        'title':      detail.get('title'),
        'artist':     detail.get('artist', {}).get('name'),
        'album':      detail.get('album', {}).get('title'),
        'duration_s': detail.get('duration'),
        'bpm':        detail.get('bpm'),
        'gain_db':    detail.get('gain'),
        'isrc':       detail.get('isrc'),
        'explicit':   detail.get('explicit_lyrics', False),
        'release_date': detail.get('release_date'),
        'preview_url':  detail.get('preview'),
        'deezer_id':    detail.get('id'),
        'deezer_url':   detail.get('link'),
        'artist_deezer_id': detail['artist']['id'],
        'artist_fans':     artist.get('nb_fan'),
        'artist_radio':    artist.get('radio'),
        'track_position':  detail.get('track_position'),
        'disk_number':     detail.get('disk_number'),
        'rank':            detail.get('rank'),
    }
    return meta


# ─── Librosa Audio Analysis ──────────────────────────────────

def analyze_chunk(y, sr, hop_length, n_fft):
    """Analyze a single ~10s audio chunk; returns dict of features."""
    import numpy as np
    import librosa

    res = {}

    # BPM
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length,
                                              n_fft=n_fft, aggregate=np.median)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, hop_length=hop_length, aggregate=np.median)
    tempo = float(tempo) if hasattr(tempo, '__iter__') else float(tempo)
    res['bpm'] = round(tempo, 1)

    beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr, hop_length=hop_length)[1]
    beats = librosa.frames_to_time(beats, sr=sr, hop_length=hop_length) if len(beats) > 0 else np.array([])
    res['beat_count'] = int(len(beats))
    res['beat_times'] = [round(float(b), 3) for b in beats[:50]]

    # Spectral
    spec = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))
    res['spectral_centroid_mean'] = float(np.mean(librosa.feature.spectral_centroid(S=spec, sr=sr)))
    res['spectral_bandwidth_mean'] = float(np.mean(librosa.feature.spectral_bandwidth(S=spec, sr=sr)))
    res['spectral_rolloff_mean'] = float(np.mean(librosa.feature.spectral_rolloff(S=spec, sr=sr)))
    zcr = librosa.feature.zero_crossing_rate(y, hop_length=hop_length)
    res['zero_crossing_rate_mean'] = float(np.mean(zcr))
    res['spectral_flatness_mean'] = float(np.mean(librosa.feature.spectral_flatness(S=spec)))

    # RMS / Energy
    rms = librosa.feature.rms(y=y, hop_length=hop_length)
    rms_avg = float(np.mean(rms))
    res['rms_mean'] = rms_avg
    res['rms_max'] = float(np.max(rms))
    if rms_avg < 0.025:
        energy = rms_avg * 12
    elif rms_avg < 0.08:
        energy = 0.3 + (rms_avg - 0.025) * 5.45
    elif rms_avg < 0.2:
        energy = 0.6 + (rms_avg - 0.08) * 2.5
    else:
        energy = 0.9 + min(0.1, (rms_avg - 0.2) * 0.5)
    res['energy'] = min(1.0, max(0.0, energy))

    # Key detection (Krumhansl-Schmuckler)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr, hop_length=hop_length)
    chroma_mean = np.mean(chroma, axis=1)
    res['chroma_vector'] = [float(v) for v in chroma_mean]
    major_profile = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09,
                              2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
    minor_profile = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53,
                              2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
    pitch_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    major_corrs = [np.corrcoef(np.roll(chroma_mean, i), major_profile)[0, 1] for i in range(12)]
    minor_corrs = [np.corrcoef(np.roll(chroma_mean, i), minor_profile)[0, 1] for i in range(12)]
    major_best = int(np.argmax(major_corrs))
    minor_best = int(np.argmax(minor_corrs))
    if major_corrs[major_best] > minor_corrs[minor_best]:
        res['key'] = pitch_names[major_best]
        res['mode'] = 'major'
        res['key_confidence'] = float(major_corrs[major_best])
    else:
        res['key'] = pitch_names[minor_best]
        res['mode'] = 'minor'
        res['key_confidence'] = float(minor_corrs[minor_best])

    # Danceability
    beat_regularity = 1.0
    if len(beats) > 1:
        gaps = np.diff(beats)
        if len(gaps) > 1:
            beat_regularity = 1.0 - min(1.0, float(np.std(gaps)) / float(np.mean(gaps) + 1e-8))
    tempo_norm = 1.0 - abs(120.0 - tempo) / 180.0
    res['danceability'] = min(1.0, max(0.0,
        0.4 * tempo_norm + 0.35 * beat_regularity + 0.25 * res['energy']))

    # Valence
    centroid_norm = min(1.0, res['spectral_centroid_mean'] / 5000.0)
    mode_bonus = 0.15 if res['mode'] == 'major' else 0.0
    res['valence'] = min(1.0, max(0.0,
        0.4 * centroid_norm + 0.3 * res['energy'] + 0.3 * mode_bonus))

    # MFCC
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, hop_length=hop_length)
    res['mfcc_mean'] = [float(v) for v in np.mean(mfcc, axis=1)]

    # Loudness
    S_db = librosa.amplitude_to_db(spec, ref=np.max)
    res['loudness_max_db'] = float(np.max(S_db))
    res['loudness_mean_db'] = float(np.mean(S_db))

    # Onset density
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, hop_length=hop_length)
    dur = float(len(y)) / sr
    res['onset_density'] = float(len(onset_frames)) / dur if dur > 0 else 0

    return res


def merge_chunks(chunks, total_dur, sr):
    """Aggregate multiple chunk analysis dicts into one result."""
    import numpy as np
    pitch_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    merged = {}
    merged['duration_s'] = round(total_dur, 2)
    merged['sample_rate'] = sr
    merged['chunks'] = len(chunks)

    # Scalar features: weighted by beat_count (more beats = more reliable)
    scalar_fields = [
        'energy', 'danceability', 'valence',
        'spectral_centroid_mean', 'spectral_bandwidth_mean',
        'spectral_rolloff_mean', 'zero_crossing_rate_mean',
        'spectral_flatness_mean', 'rms_mean', 'rms_max',
        'loudness_max_db', 'loudness_mean_db', 'onset_density',
    ]
    weights = [max(1, c.get('beat_count', 1)) for c in chunks]
    total_w = sum(weights) or 1
    for field in scalar_fields:
        vals = [c.get(field, 0) for c in chunks]
        merged[field] = round(sum(v * w for v, w in zip(vals, weights)) / total_w, 4)

    # BPM: pick median across chunks
    bpms = sorted([c['bpm'] for c in chunks])
    bpm = bpms[len(bpms) // 2]
    merged['bpm'] = round(bpm, 1)
    merged['bpm_alt'] = round(bpm * 2, 1) if bpm < 90 else round(bpm / 2, 1) if bpm > 180 else None

    # Beats: list from all chunks
    all_beats = []
    for c in chunks:
        all_beats.extend(c.get('beat_times', []))
        # Shift beats of chunks 2+ by the chunk start offset
    merged['beat_count'] = sum(c.get('beat_count', 0) for c in chunks)

    # Key: weighted vote by key_confidence
    key_votes = {}
    for c in chunks:
        k = c.get('key', 'C')
        conf = c.get('key_confidence', 0)
        key_votes[k] = key_votes.get(k, 0) + conf
        # Track mode per key
    best_key = max(key_votes, key=key_votes.get)

    # Mode by confidence-weighted majority among chunks matching best_key
    major_conf = sum(c['key_confidence'] for c in chunks if c.get('key') == best_key and c.get('mode') == 'major')
    minor_conf = sum(c['key_confidence'] for c in chunks if c.get('key') == best_key and c.get('mode') == 'minor')
    merged['key'] = best_key
    merged['mode'] = 'major' if major_conf >= minor_conf else 'minor'
    merged['key_confidence'] = round(max(major_conf, minor_conf) / len(chunks), 3)

    # Chroma & MFCC: average vectors
    vec_fields = ['chroma_vector', 'mfcc_mean']
    for field in vec_fields:
        vecs = [c.get(field) for c in chunks if c.get(field)]
        if vecs:
            merged[field] = [round(sum(v[i] for v in vecs) / len(vecs), 4) for i in range(len(vecs[0]))]
        else:
            merged[field] = []

    # Genre classification from merged features
    genre_results = classify_genre(merged)
    merged['genre'] = [g for g, _ in genre_results]

    return merged


def classify_genre(feats):
    """Heuristic genre classification from audio features."""
    bpm = feats.get('bpm', 120)
    energy = feats.get('energy', 0.5)
    dance = feats.get('danceability', 0.5)
    valence = feats.get('valence', 0.5)
    centroid = feats.get('spectral_centroid_mean', 2000)
    zcr = feats.get('zero_crossing_rate_mean', 0.05)
    flatness = feats.get('spectral_flatness_mean', 0.02)
    onset = feats.get('onset_density', 3)

    scores = {}

    # Pop
    s = 0
    if 80 < bpm < 140: s += 2
    if energy > 0.5: s += 1.5
    if dance > 0.6: s += 2
    if centroid > 1500: s += 1
    if flatness < 0.05: s += 0.5
    scores['Pop'] = s

    # Rock
    s = 0
    if 100 < bpm < 170: s += 1.5
    if energy > 0.65: s += 2
    if centroid > 2000: s += 2
    if zcr > 0.08: s += 1.5
    if onset > 3: s += 1
    scores['Rock'] = s

    # Electronic
    s = 0
    if bpm > 120: s += 2
    if bpm < 90: s -= 1
    if dance > 0.7: s += 2
    if 0.03 < flatness < 0.2: s += 1
    if onset > 4: s += 1.5
    if centroid > 2500: s += 1
    if energy > 0.6: s += 1
    scores['Electronic'] = s

    # Hip-Hop / R&B
    s = 0
    if 70 < bpm < 110: s += 2
    if 0.3 < energy < 0.8: s += 1
    if dance > 0.6: s += 1.5
    if centroid < 2500: s += 1
    if valence < 0.6: s += 1
    scores['Hip-Hop/R&B'] = s

    # Jazz / Blues
    s = 0
    if bpm < 100: s += 1.5
    if energy < 0.5: s += 1.5
    if centroid < 2000: s += 2
    if zcr > 0.04: s += 1
    if flatness > 0.02: s += 1
    if onset < 3: s += 1
    if dance < 0.6: s += 1
    scores['Jazz/Blues'] = s

    # Classical / Ambient
    s = 0
    if bpm < 90: s += 2
    if energy < 0.4: s += 2
    if centroid < 1500: s += 2
    if zcr < 0.06: s += 1.5
    if flatness > 0.03: s += 1
    if onset < 2: s += 1.5
    if dance < 0.5: s += 1
    scores['Classical/Ambient'] = s

    # Folk / Acoustic
    s = 0
    if 70 < bpm < 140: s += 1
    if energy < 0.6: s += 1.5
    if centroid < 2000: s += 1.5
    if zcr < 0.1: s += 1
    if flatness < 0.04: s += 1
    if onset < 4: s += 1
    scores['Folk/Acoustic'] = s

    # Metal / Punk
    s = 0
    if bpm > 130: s += 2
    if energy > 0.75: s += 2
    if centroid > 3000: s += 2
    if zcr > 0.12: s += 2
    if onset > 5: s += 1.5
    if flatness > 0.03: s += 1
    scores['Metal/Punk'] = s

    # Sort by score descending
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    top_score = ranked[0][1]
    # Return genres within 80% of top score
    result = [(g, round(s / max(top_score, 1), 2)) for g, s in ranked if s >= top_score * 0.8]
    return result


def analyze_audio(filepath):
    """Extrae features sampling chunks across the full track."""
    import numpy as np
    import librosa

    print(f"  Loading: {filepath}", file=sys.stderr)
    y, sr = librosa.load(filepath, sr=22050, mono=True)
    total_dur = float(len(y)) / sr
    total_samples = len(y)

    chunk_dur = 10          # seconds per chunk (32-bit safe)
    chunk_samples = chunk_dur * sr

    # Determine chunk positions (5 chunks for full tracks, fewer for short audio)
    if total_samples <= chunk_samples:
        positions = [0]
    elif total_samples <= chunk_samples * 2:
        positions = [0, (total_samples - chunk_samples) // 2]
    elif total_samples <= chunk_samples * 4:
        stride = (total_samples - chunk_samples) // 3
        positions = [0, stride, 2 * stride]
    else:
        stride = (total_samples - chunk_samples) // 5
        positions = [0, stride, 2 * stride, 3 * stride, 4 * stride]

    chunks = []
    for i, offset in enumerate(positions):
        seg = y[offset:offset + chunk_samples]
        if len(seg) < sr * 2:  # skip if less than 2s
            continue
        chunk_result = analyze_chunk(seg, sr, hop_length=1024, n_fft=1024)

        # Shift beat_times by chunk offset
        offset_sec = offset / sr
        chunk_result['beat_times'] = [round(b + offset_sec, 3) for b in chunk_result.get('beat_times', [])]

        chunks.append(chunk_result)
        print(f"  Chunk {i + 1}/{len(positions)}: offset={int(offset_sec)}s, "
              f"bpm={chunk_result.get('bpm', '?')}, key={chunk_result.get('key', '?')} {chunk_result.get('mode', '?')} "
              f"energy={chunk_result.get('energy', '?'):.3f}", file=sys.stderr)

    if not chunks:
        print("  WARNING: no valid chunks extracted", file=sys.stderr)
        return {}

    merged = merge_chunks(chunks, total_dur, sr)
    print(f"  Merged ({len(chunks)} chunks): bpm={merged['bpm']}, key={merged['key']} {merged['mode']}, "
          f"energy={merged['energy']:.3f}, danceability={merged['danceability']:.3f}, valence={merged['valence']:.3f}",
          file=sys.stderr)
    return merged


# ─── Combined: Deezer + download preview + analyze ───────────

def deezer_download_preview(url, dest=None):
    if not url:
        print("  No preview URL available")
        return None
    if dest is None:
        dest = os.path.join(tempfile.gettempdir(), f'deezer_preview_{os.urandom(4).hex()}.mp3')
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    with open(dest, 'wb') as f:
        f.write(r.content)
    return dest


def lookup_song(song, artist=None):
    print(f"\n{'='*60}")
    print(f"  Deezer lookup: {song}" + (f" - {artist}" if artist else ""))
    print(f"{'='*60}")

    track = deezer_search_track(song, artist)
    if not track:
        return
    meta = deezer_track_metadata(track)

    print(f"\n  -- Deezer Metadata --")
    for k, v in meta.items():
        print(f"    {k:20s} = {v}")

    if meta.get('preview_url'):
        print(f"\n  Downloading 30s preview...")
        preview_path = deezer_download_preview(meta['preview_url'])
        if preview_path:
            print(f"  Saved to: {preview_path}")
            print(f"\n  -- Audio Analysis (librosa) --")
            try:
                analysis = analyze_audio(preview_path)
                for k, v in analysis.items():
                    if k in ('beat_times', 'chroma_vector', 'mfcc_mean'):
                        continue
                    print(f"    {k:25s} = {v}")
                os.unlink(preview_path)
            except Exception as e:
                print(f"  Analysis failed: {e}")
                traceback.print_exc()
    else:
        print(f"\n  No preview URL — can't analyze audio.")

    # Genre approximation via Deezer artist/chart
    print(f"\n  -- Genre Context --")
    aid = meta.get('artist_deezer_id')
    if aid:
        genres = deezer_genre_for_artist(aid)
        if genres:
            print(f"    artist_genres      = {', '.join(genres)}")
        else:
            print(f"    artist_genres      = (none found via Deezer)")
    print(f"    deezer_rank        = {meta.get('rank')}")
    print(f"    artist_radio       = {meta.get('artist_radio')}")


def deezer_genre_for_artist(artist_id):
    """Intenta obtener géneros para un artista desde Deezer."""
    try:
        r = requests.get(f'{DEEZER_API}/artist/{artist_id}/top', params={'limit': 5}, timeout=10)
        r.raise_for_status()
        data = r.json()
        genres = set()
        for t in data.get('data', []):
            album = t.get('album', {})
            gid = album.get('genre_id')
            if gid:
                genres.add(str(gid))
        if genres:
            genre_names = []
            for gid in genres:
                try:
                    gr = requests.get(f'{DEEZER_API}/genre/{gid}', timeout=5)
                    gr.raise_for_status()
                    genre_names.append(gr.json().get('name', str(gid)))
                except Exception:
                    genre_names.append(str(gid))
            return genre_names
    except Exception:
        pass
    return []


# ─── CLI ─────────────────────────────────────────────────────

def cmd_deezer(args):
    song = args[0]
    artist = args[1] if len(args) > 1 else None
    track = deezer_search_track(song, artist)
    if not track:
        return
    meta = deezer_track_metadata(track)
    print(json.dumps(meta, indent=2, ensure_ascii=False))


def cmd_deezer_raw(args):
    """Busca y muestra el JSON crudo de Deezer para debugging."""
    song = args[0]
    artist = args[1] if len(args) > 1 else None
    q = f'{artist} {song}' if artist else song
    params = {'q': normalize(q)}
    r = requests.get(f'{DEEZER_API}/search/track', params=params, timeout=15)
    data = r.json()
    if data.get('data'):
        tid = data['data'][0]['id']
        detail = requests.get(f'{DEEZER_API}/track/{tid}', timeout=15).json()
        print(json.dumps(detail, indent=2, ensure_ascii=False))


def cmd_analyze(args):
    filepath = args[0]
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
    analysis = analyze_audio(filepath)
    print(json.dumps(analysis, indent=2, ensure_ascii=False))


def cmd_lookup(args):
    song = args[0]
    artist = args[1] if len(args) > 1 else None
    lookup_song(song, artist)


def cmd_list_deezer_fields():
    print("""
Campos disponibles desde Deezer API (publica, sin auth):

  title             -> titulo del track
  artist            -> nombre del artista
  album             -> nombre del album
  duration_s        -> duracion en segundos
  bpm               -> beats per minute
  gain_db           -> loudness gain (dB)
  isrc              -> codigo ISRC
  explicit          -> contenido explicito
  release_date      -> fecha de lanzamiento
  preview_url       -> URL del preview de 30s (MP3)
  deezer_id         -> ID interno de Deezer
  deezer_url        -> enlace a Deezer
  track_position    -> numero de pista en el album
  disk_number       -> numero de disco
  rank              -> popularidad en Deezer
  artist_fans       -> seguidores del artista
  artist_radio      -> si el artista tiene radio Deezer

Campos desde librosa (analisis de archivo local):

  genre             -> genero estimado (Pop, Rock, Electronic, ...)
  bpm               -> tempo detectado
  key               -> tonalidad (C, C#, D, ..., B)
  mode              -> major / minor
  key_confidence    -> confianza 0-1
  energy            -> energia percibida 0-1
  danceability      -> bailabilidad 0-1
  valence           -> positividad musical 0-1
  spectral_centroid -> brillo espectral (Hz)
  spectral_bandwidth -> ancho espectral
  zero_crossing_rate -> tasa de cruces por cero
  spectral_flatness -> planitud espectral
  rms_mean/max      -> loudness RMS
  loudness_max_db   -> loudness pico en dB
  onset_density     -> densidad de ataques por segundo
  beat_count        -> numero de beats detectados
  mfcc_mean         -> vector MFCC (timbre 13-band)
  chroma_vector     -> vector cromatico 12-pitch
""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd == 'deezer':
        cmd_deezer(args)
    elif cmd == 'deezer-raw':
        cmd_deezer_raw(args)
    elif cmd == 'analyze':
        cmd_analyze(args)
    elif cmd == 'lookup':
        cmd_lookup(args)
    elif cmd == 'fields':
        cmd_list_deezer_fields()
    else:
        print(f"Unknown command: {cmd}\n{__doc__}")
        sys.exit(1)

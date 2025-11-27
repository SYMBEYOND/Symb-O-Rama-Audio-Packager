#!/usr/bin/env python3
import sys, os, librosa, soundfile as sf
from pathlib import Path

# ==============================================================
# Symb-O-Rama Audio Packager
# Converts MP3/WAV → mono WAV + timing grid + Star Timings XML
# Output always saved to Desktop with automatic versioning
# ==============================================================

BASE_OUT = Path.home() / "Desktop"
BASE_OUT.mkdir(parents=True, exist_ok=True)

def get_versioned_folder(base_name):
    folder = BASE_OUT / base_name
    if not folder.exists():
        return folder

    for i in range(1, 1001):
        vfolder = BASE_OUT / f"{base_name}_v{i}"
        if not vfolder.exists():
            return vfolder

    raise RuntimeError("Version limit reached (v1000). Clean Desktop and retry.")

def convert_audio(infile, outfile):
    y, sr = librosa.load(infile, sr=44100, mono=True)
    sf.write(outfile, y, sr)
    return y, sr

def detect_beats(y, sr):
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    return librosa.frames_to_time(onset_frames, sr=sr)

def make_timing_file(outtxt, beats):
    with open(outtxt, "w") as f:
        for t in beats:
            f.write(f"{t:.3f}\t{t:.3f}\tBeat\n")

def make_star_timings_grid(outxml, beats, grid_name="AutoGrid"):
    with open(outxml, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(f'<timingGrid name="{grid_name}">\n')
        for t in beats:
            f.write(f'  <marker time="{t:.3f}" label="Beat"/>\n')
        f.write('</timingGrid>\n')

def make_readme(readme_path, songname):
    content = f"""# Symb-O-Rama Package: {songname}

Generated automatically using the Symb-O-Rama Audio Packager.
Version: 1.0.0 | Platform Agnostic Processing

Contents:
• {songname}_Symb.wav
• {songname}_Symb_Timings.txt
• {songname}_Symb_StarTimings.xml
• README_{songname}_Symb.md

Sequencer:
1. New Musical Sequence → select {songname}_Symb.wav
2. Timings → Import Timings (Audacity Label File)
3. Choose {songname}_Symb_Timings.txt

Star Timings:
1. File → Import Timings
2. Choose {songname}_Symb_StarTimings.xml
"""
    with open(readme_path, "w") as f:
        f.write(content)

def main(infile):
    infile_path = Path(infile).expanduser().resolve()

    # --- SAFETY CHECKS ---
    if not infile_path.exists():
        print(f"Input file not found: {infile_path}")
        return

    if infile_path.name.endswith("_Symb.wav"):
        print("Refusing to repackage an _Symb.wav file. Pick the original audio file instead.")
        return

    # --- PROCESSING SETUP ---
    import re
    songname = re.sub(r'[^A-Za-z0-9_-]+', '_', infile_path.stem).strip('_')
    base_name = f"{songname}_Symb_Package"

    outdir = get_versioned_folder(base_name)
    outdir.mkdir(exist_ok=True)

    wav_path = outdir / f"{songname}_Symb.wav"
    txt_path = outdir / f"{songname}_Symb_Timings.txt"
    xml_path = outdir / f"{songname}_Symb_StarTimings.xml"
    readme_path = outdir / f"README_{songname}_Symb.md"

    print(f"Converting {infile_path} → {wav_path}")
    y, sr = convert_audio(infile_path, wav_path)

    # Copy original audio into the package folder
    original_copy = outdir / infile_path.name
    if not original_copy.exists():
        try:
            import shutil
            shutil.copy2(infile_path, original_copy)
            print(f"Copied original MP3: {original_copy}")
        except Exception as e:
            print(f"Failed to copy MP3: {e}")


    beats = detect_beats(y, sr)
    make_timing_file(txt_path, beats)
    make_star_timings_grid(xml_path, beats)
    make_readme(readme_path, songname)

    print()
    print(f"Package ready: {outdir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: symb_packager.py inputfile.mp3|wav")
        sys.exit(1)
    for arg in sys.argv[1:]:
        main(arg)


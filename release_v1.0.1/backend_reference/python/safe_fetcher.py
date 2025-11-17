#!/usr/bin/env python3
from yt_dlp import YoutubeDL
from pathlib import Path
import subprocess
import sys
import os

BASE_OUT = Path.home() / "Desktop"
BASE_OUT.mkdir(parents=True, exist_ok=True)

# @anchor:ffmpeg_detection
def get_ffmpeg_path():
    """
    Detect correct ffmpeg binary path for both development and packaged runtime.
    """

    app_path = Path(sys.executable).resolve()

    # Detect packaged app environment by checking if Resources exists above runtime
    resources_dir = app_path.parents[1] / "backend" / "ffmpeg" / "ffmpeg"
    if resources_dir.exists():
        return resources_dir

    # Development mode fallback
    return Path(__file__).parent.parent / "ffmpeg" / "ffmpeg"

def fetch_audio(url, out_dir=BASE_OUT):

    ffmpeg_path = get_ffmpeg_path()

    opts = {
        "format": "bestaudio/best",
        "ffmpeg_location": str(ffmpeg_path),
        "outtmpl": str(out_dir / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": False,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
            }
        ],
    }

    print(f"\nUsing ffmpeg at: {ffmpeg_path}\n")

    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        mp3_file = out_dir / f"{info['title']}.mp3"
        print(f"\nSaved as:\n{mp3_file}\n")
        return mp3_file


def run_packager(audio_path):
    script_path = Path(__file__).parent / "lor_packager.py"
    python = sys.executable

    result = subprocess.run(
        [python, str(script_path), str(audio_path)],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(result.stderr or result.stdout)
        return False

    print(result.stdout)
    return True


if __name__ == "__main__":
    url = sys.argv[1].strip() if len(sys.argv) > 1 else None

    if not url:
        print("Missing URL")
        sys.exit(1)

    mp3 = fetch_audio(url)
    ok = run_packager(mp3)

    print(f"PACKAGED_FOLDER::{mp3.stem}_LOR_Package")

    sys.exit(0 if ok else 1)


#!/usr/bin/env python3
from yt_dlp import YoutubeDL
from pathlib import Path

def fetch_audio(url, out_dir=Path.cwd()):
    opts = {
        "format": "bestaudio/best",
        "outtmpl": str(out_dir / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": False,
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ],
    }

    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        mp3_file = Path(out_dir) / f"{info['title']}.mp3"
        print(f"\nSaved as:\n{mp3_file}\n")
        return mp3_file

if __name__ == "__main__":
    try:
        url = input("Paste YouTube URL: ").strip()
        if url:
            fetch_audio(url)
    except KeyboardInterrupt:
        print("\nCancelled.")


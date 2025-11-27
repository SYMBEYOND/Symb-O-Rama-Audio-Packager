# Symb-O-Rama Audio Packager

A minimal, privacy-respecting tool for sequencing creators and holiday lighting enthusiasts.

---

## What It Does

Load a legally owned MP3/WAV — or paste a legally owned YouTube link — and the app automatically generates everything needed for sequencing.

No configuration. No command-line steps. No setup.

**Input → Process → Done.**

---

## What It Outputs

Each processed song creates a folder on your Desktop containing:

| File | Description |
|------|-------------|
| `{songname}_original.mp3` | Your original audio preserved |
| `{songname}_Symb.wav` | Clean mono WAV (44.1 kHz) optimized for sequencing |
| `{songname}_Symb_Timings.txt` | Timing grid for sequencing workflows |
| `{songname}_Symb_StarTimings.xml` | Star Timings XML |
| `README_{songname}_Symb.md` | Metadata and reference notes |

The folder name matches the song title, so everything stays organized.

---

## Download & Install

**📍 Latest Release:** [Download Here](https://github.com/SYMBEYOND/Symb-O-Rama-Audio-Packager/releases/latest)

### macOS (Apple Silicon)

1. Download the `.dmg` file
2. Open and drag the app to Applications
3. First launch: Right-click → Open (to bypass Gatekeeper)

### Windows

1. Download the `.exe` installer
2. Run the installer
3. Launch from Start Menu

### Linux

1. Download the `.AppImage` or `.deb`
2. For AppImage: `chmod +x` and run
3. For .deb: `sudo dpkg -i filename.deb`

**No Python install required. No FFmpeg setup. Everything is bundled.**

---

## How to Use

### Option 1: Local Audio File

1. Open the app
2. Click **"Process Local File"**
3. Select your MP3 or WAV
4. Wait for processing to complete
5. Find your package folder on Desktop

### Option 2: YouTube Link

1. Open the app
2. Paste a YouTube URL
3. Click **"Process YouTube"**
4. Wait for download and processing
5. Find your package folder on Desktop

---

## Supported Platforms

| Platform | Status |
|----------|--------|
| macOS (Apple Silicon) | ✅ Supported |
| macOS (Intel) | 🔜 Planned |
| Windows 10/11 | ✅ Supported |
| Linux (AppImage) | ✅ Supported |
| Linux (.deb) | ✅ Supported |

---

## Privacy

Everything is processed locally.

- Nothing is uploaded
- Nothing is tracked
- Nothing is stored remotely

You are responsible for ensuring you have the rights to the music you process — not because a warning demands it, but because **respecting creators matters**.

---

## Roadmap

Future features being explored:

- Batch processing
- Alternative timing algorithms
- Direct export for more sequencing apps
- Waveform visualization
- Plugin-style extensions

---

## License

MIT License — Copyright (c) 2025 John Thomas DuCrest Lock

See [LICENSE](LICENSE) for full details.

**Respect Clause** (not legally binding, but part of the project's ethos):

> This tool was built to help creators — not exploit them.
> Anything built from it should honor effort, community, and creativity.

---

## Contributing

This project is open for review, improvement, and thoughtful collaboration.

If this tool helped you — share it with another creator.

Tools grow when communities share them, not gatekeep them.

---

Made with care by [SYMBEYOND](https://github.com/SYMBEYOND)

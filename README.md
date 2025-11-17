# Light-O-Rama Audio Packager  
A Tool Built With Respect

---

### Purpose

This application exists to solve a real problem:
Converting a song you legally own into a clean, timing-ready package for Light-O-Rama sequencing.

No ads.  
No clutter.  
No assumptions.

Just a clear path from audio → usable sequencing assets.

---

### What This Tool Produces Automatically

When given either a **YouTube link** or a **local MP3/WAV file**, the packager generates a complete folder containing:

| File | Purpose |
|------|---------|
| `SongName.wav` | Clean mono 44.1 kHz audio optimized for sequencing |
| `SongName.mp3` | Original source format preserved |
| `SongName_LOR_Timings.txt` | Beat grid for Light-O-Rama timing tracks |
| `SongName_LOR_SuperStarGrid.xml` | Superstar-compatible beat map |
| `README_SongName_LOR.md` | Instructions and metadata for reference |

Everything is placed into a clearly named folder on your Desktop:

SONG_TITLE_LOR_Package/

yaml
Copy code

---

### Installation

#### macOS

1. Download the latest **`.dmg`** from the Releases tab.
2. Drag the app into `Applications`.
3. The first time macOS may quarantine it.  
   Run once with:

```bash
xattr -dr com.apple.quarantine "/Applications/Light-O-Rama Audio Packager.app"
After that, it opens normally.

No Python install required.
No FFmpeg setup.
No configuration.

Everything needed is already bundled.

How to Use
Open the app.

Choose either:

Download from YouTube

Process Local MP3/WAV

Wait while the system:

Fetches and normalizes audio

Converts waveform to sequencing-ready format

Generates timing data

Creates Superstar grid

When complete, Finder will open the new package automatically.

Platform Support
Platform	Status
macOS (Apple Silicon)	Fully Supported
macOS Intel	Planned
Windows 10/11	Planned
Linux	Planned

Source, Security, and Respect
All audio is processed locally.

No files are uploaded.
Nothing is stored or shared.
The tool does not check, enforce, or track licensing.

Responsibility remains with the user.

Process only music you have the legal right to use – not because a policy demands it, but because respecting creators matters.

Contributing
This project will evolve.
Upcoming milestones include:

Windows installer

Batch processing

Custom timing profiles

Direct Light-O-Rama import format

Pull requests are welcome once contribution rules are formalized.

Status
Stable Version: 1.0.1
Build Type: Bundled runtime with portable FFmpeg
Testing: Verified on macOS Sonoma ARM64

License
MIT License with one added principle:

This software is free to use and build upon —
but never exploitative.
Anything built from it should honor effort, community, and creativity.

Final Note
Tools are more than code.
They carry intent.

The intent here is simple:

Help creators build something beautiful.

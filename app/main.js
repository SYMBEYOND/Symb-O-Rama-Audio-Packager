// app/main.js
const { app, BrowserWindow, ipcMain, shell, dialog } = require("electron");
const path = require("path");
const { spawn } = require("child_process");
const os = require("os");
const fs = require("fs");

// -----------------------------
// Locate Python (Dev + Packaged)
// -----------------------------
function getPythonPath() {
    const isDev = !app.isPackaged;

    if (isDev) {
        const candidates = [
            path.join(process.cwd(), "venv/bin/python3"),
            path.join(process.cwd(), "venv/bin/python"),
            "/usr/bin/python3",
            "python3",
            "python"
        ];
        for (const candidate of candidates) {
            try { fs.accessSync(candidate); return candidate; } catch {}
        }
        return null;
    }

    // ---- Packaged Mode ----
    return path.join(process.resourcesPath, "runtime", "python", "python");
}

// -----------------------------
// Electron Window
// -----------------------------
function createWindow() {
    const win = new BrowserWindow({
        width: 780,
        height: 700,
        backgroundColor: "#0d0b1e",
        webPreferences: {
            preload: path.join(__dirname, "preload.js"),
            contextIsolation: true,
            nodeIntegration: false
        }
    });

    win.loadFile(path.join(__dirname, "index.html"));
}

app.whenReady().then(createWindow);

// -----------------------------
// Python Runner
// -----------------------------
function runPython(script, args = []) {
    return new Promise(resolve => {
        const pythonPath = getPythonPath();

        if (!pythonPath) {
            return resolve({ ok: false, error: "Python runtime missing." });
        }

        const scriptPath = app.isPackaged
            ? path.join(process.resourcesPath, "backend", "python", script)
            : path.join(process.cwd(), "backend/python", script);

        const child = spawn(pythonPath, [scriptPath, ...args]);

        let stdout = "";
        let stderr = "";

        child.stdout.on("data", d => stdout += d.toString());
        child.stderr.on("data", d => stderr += d.toString());

        child.on("close", code => {
            resolve(code === 0 ? { ok: true, stdout } : { ok: false, error: stderr });
        });
    });
}

// -----------------------------
// IPC Events
// -----------------------------
ipcMain.handle("lor:pick-file", async () => {
    const result = await dialog.showOpenDialog({
        title: "Select MP3",
        filters: [{ name: "MP3", extensions: ["mp3"] }],
        properties: ["openFile"]
    });

    return (!result.canceled && result.filePaths.length) ? result.filePaths[0] : null;
});

ipcMain.handle("lor:local", async (event, filepath) => {
    try {
        const res = await runPython("lor_packager.py", [filepath]);
        return res;
    } catch (err) {
        return { ok: false, error: err.message };
    }
});

ipcMain.handle("lor:youtube", async (event, url) => {
    const res = await runPython("safe_fetcher.py", [url]);
    if (!res.ok) return res;

    const out = res.stdout.trim();
    const marker = "PACKAGED_FOLDER::";

    let folderName = null;
    if (out.includes(marker)) {
        folderName = out.split(marker)[1].trim();
    }

    if (!folderName) {
        return { ok: false, error: "Folder name not received from Python." };
    }

    const desktop = path.join(os.homedir(), "Desktop");
    const fullFolder = path.join(desktop, folderName);

    // Copy newest MP3 inside
    const mp3Files = fs.readdirSync(desktop)
        .filter(f => f.toLowerCase().endsWith(".mp3"))
        .map(f => ({
            name: f,
            time: fs.statSync(path.join(desktop, f)).mtime.getTime()
        }))
        .sort((a, b) => b.time - a.time);

    if (mp3Files.length) {
        const newest = mp3Files[0].name;
        fs.copyFileSync(
            path.join(desktop, newest),
            path.join(fullFolder, newest)
        );
    }

    return { ok: true, folder: folderName };
});


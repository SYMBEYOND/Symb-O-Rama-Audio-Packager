// renderer.js

// ---------------- ELEMENTS ----------------
const btnYT = document.getElementById("btn-youtube-run");
const btnLocal = document.getElementById("btn-local");
const statusText = document.getElementById("status-text");
const ytInput = document.getElementById("youtube-input");

// ---------------- RESET ----------------
function resetUI() {
    ytInput.value = "";
    statusText.textContent = "Idle — Waiting for command.";
}

// ---------------- WAVEFORM ----------------
const canvas = document.getElementById("pulse-canvas");
const ctx = canvas.getContext("2d");
let t = 0;

function resizeCanvas() {
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
}

function draw() {
    resizeCanvas();
    ctx.clearRect(0,0,canvas.width,canvas.height);

    for (let i=0; i<64; i++) {
        let x = (i/64)*canvas.width;
        let h = Math.abs(Math.sin(t + i*0.25)) * canvas.height*0.45 + 6;
        ctx.fillStyle = "#7a8cffdd";
        ctx.fillRect(x, canvas.height/2 - h/2, canvas.width/64 *0.8, h);
    }

    t += 0.03;
    requestAnimationFrame(draw);
}
draw();

// ---- AUDIO REACTOR ----
let intensity = 0;

function applyAudioReactiveGlow(level) {
    const root = document.querySelector("body");
    const scaled = Math.min(level * 1.6, 1); // prevent clipping
    
    root.style.setProperty("--react-intensity", scaled);
}

// Exposed trigger from backend
window.LOR.updateBeat = (value) => {
    intensity = value;
};

// ---------------- ACTIONS ----------------

btnYT.onclick = async () => {
    const url = ytInput.value.trim();
    if (!url) return alert("Please paste a YouTube link first.");

    statusText.textContent = "Downloading and processing...";

    const res = await window.LOR.runYouTube(url);

    if (res.ok) {
        statusText.textContent = "Done! Check Desktop.";

        const again = confirm("Would you like to process another?");
        if (again) resetUI();

    } else {
        statusText.textContent = `❌ ${res.error}`;
    }
};

btnLocal.onclick = async () => {
    statusText.textContent = "Opening file picker...";

    const filePath = await window.LOR.pickLocal();

    // If user canceled
    if (!filePath) {
        statusText.textContent = "❌ No file selected.";
        return;
    }

    statusText.textContent = "Processing file...";

    try {
        const res = await window.LOR.runLocal(filePath);

        if (res.ok) {
            statusText.textContent = "✅ File processed! Check Desktop.";

            const again = confirm("Process another MP3?");
            if (again) resetUI();
        } else {
            statusText.textContent = `❌ ${res.error}`;
        }

    } catch (err) {
        statusText.textContent = `❌ Error: ${err.message}`;
    }
};


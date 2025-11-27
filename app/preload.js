const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("Symb", {
    runYouTube: (url) => ipcRenderer.invoke("symb:youtube", url),
    runLocal: (filepath) => ipcRenderer.invoke("symb:local", filepath),
    pickLocal: () => ipcRenderer.invoke("symb:pick-file")
});


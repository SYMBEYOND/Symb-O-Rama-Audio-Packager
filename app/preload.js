const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("LOR", {
    runYouTube: (url) => ipcRenderer.invoke("lor:youtube", url),
    runLocal: (filepath) => ipcRenderer.invoke("lor:local", filepath),
    pickLocal: () => ipcRenderer.invoke("lor:pick-file")
});


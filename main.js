const { app, ipcMain, BrowserWindow, Menu, MenuItem, Tray } = require('electron')
const path = require('path');
const fs = require('fs');
const { folderPath, filename } = require('./config.json');


// Check if the directory exists
const stats = fs.statSync(folderPath);
if (!stats.isDirectory()) {
  throw new Error('Directory is not valid')
}

function inputTemplate(inputData) {
  return '- [ ] ' + inputData + '\n';
}

// Function to handle data from HTML
exports.handleForm = function handleForm(targetWindow, inputData) {
  const filepath = path.join(folderPath, filename)
  fs.appendFileSync(filepath, inputTemplate(inputData));
  targetWindow.webContents.send('form-received', "added!");
};

let mainWindow;
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 650,
    height: 130,
    frame: false,
    webPreferences: {
      nodeIntegration: true
    }
  })

  mainWindow.loadFile('index.html')

  mainWindow.on('closed', function () {
    mainWindow = null
  })
}

const menu = new Menu()
menu.append(new MenuItem({
  label: 'Exit',
  accelerator: 'Esc',
  click: () => { console.log('time to print stuff') }
}))

// let tray = null
// app.on('ready', () => {
//   tray = new Tray(path.join(__dirname, 'assets', 'server.png'))
//   const contextMenu = Menu.buildFromTemplate([
//     {
//       label: 'exit', type: 'normal', click: () => {
//         app.quit();
//       }
//     },
//   ])
//   tray.setToolTip('This is my application.')
//   tray.setContextMenu(contextMenu)
// })

app.on('ready', createWindow)

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', function () {
  if (mainWindow === null) createWindow()
})
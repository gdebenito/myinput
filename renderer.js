const { remote, ipcRenderer } = require('electron');
const { handleForm } = remote.require('./main');
const currentWindow = remote.getCurrentWindow();

const submitFormButton = document.querySelector("#ipcForm2");
const responseParagraph = document.getElementById('response')

submitFormButton.addEventListener("submit", function (event) {
        event.preventDefault();   // stop the form from submitting
        let firstname = document.getElementById("inputname").value;
        handleForm(currentWindow, firstname)
});

ipcRenderer.on('form-received', function (event, args) {
        document.getElementById("inputname").value = '';
});

document.addEventListener('keyup', event => {
        if (event.key === 'Escape' || event.keyCode === 27) {
                window.close();
        }
});
function APIConnectStatus(){
    var Status = document.querySelector('.Status');
    import {PythonShell} from 'python-shell';
    let pycode = new PythonShell('APIConnect/ConnectionStatus.py');

    pycode.on('message', function(message){
        if (message === true){
            status = 1;
        }
    });
}

function Alram(){
    alert("Hello");
}
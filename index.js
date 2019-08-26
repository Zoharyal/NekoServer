const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const router = require('./router/route');
const socket = require('./socket/socket');
const path = require('path');
const cmd = require('node-cmd');
const {spawn} = require('child_process');
const {pythonShell} = require('python-shell');
// const http = require('http').createServer(app);
// const io = require('socket.io')(http);
let server;


app.use(bodyParser.json());

app.use(bodyParser.urlencoded({
    extended: true
}));

app.use('/', router);

app.use(cors({
    origin: '*'
}));

server = app.listen(3000, () => {
    console.log('listening on 8080');
});
socket.initSocket(server);

const io = socket.getInstance();

io.on('connection', function(socket) {
    console.log('connected');
    function runScript(script) {
        return spawn('python', ["-u", path.join(__dirname, `/script/${script}`)]);
    }
    // const spawn = require('child_process').spawn;
    socket.on('eat', () => {
        //script python
        // const subprocess = runScript('Shower.py');
        // subprocess.stdout.on('data', (data) => {
        //     console.log(`data:${data}`);
        //   });
        //   subprocess.stderr.on('data', (data) => {
        //     console.log(`error:${data}`);
        //   });
        //   subprocess.stderr.on('close', () => {
        //     console.log("Closed");
        //   });
        console.log('test eat');
        const file = path.join(__dirname, '/script/Shower.py');
        pythonShell.run(file, null, function (err) {
            if (err) throw err;
            console.log('finished');
        });
    });
    // dormir
    socket.on('sleep', () => {
        //script python
        // const subprocess = runScript('Shower.py');
        // subprocess.stdout.on('data', (data) => {
        //     console.log(`data:${data}`);
        //   });
        //   subprocess.stderr.on('data', (data) => {
        //     console.log(`error:${data}`);
        //   });
        //   subprocess.stderr.on('close', () => {
        //     console.log("Closed");
        //   });
        console.log('test sleep');
        const file = path.join(__dirname, '/script/Shower.py');
        pythonShell.run(file, null, function (err) {
            if (err) throw err;
            console.log('finished');
        });
    });
    // se laver
    socket.on('wash', () => {
        console.log('test wash');
        // const file = path.join(__dirname, '/script/Shower.py');
        // console.log(file);
        // const eatPython = cmd.get(`python ${file}`, 
        // function(data, err, stderr) {
        //     if(!err) {
        //         console.log('working', data);
        //     } else {
        //         console.log('error', err);
        //     }
        // })
        const file = path.join(__dirname, '/script/Shower.py');
        pythonShell.run(file, null, function (err) {
            if (err) throw err;
            console.log('finished');
        });
    });
    // aller au toilette
    socket.on('toilet', () => {
        //script pyth
        const file = path.join(__dirname, '/script/Shower.py');
        console.log('test toilet');
    });
    // se réveiller
    socket.on('wakeup', () => {
        //script python
        console.log('test wakeup');
    });
    // danser
    socket.on('danse', () => {
        //script python
        const subprocess = runScript('LaunchDance.py');
        subprocess.stdout.on('data', (data) => {
            console.log(`data:${data}`);
          });
          subprocess.stderr.on('data', (data) => {
            console.log(`error:${data}`);
          });
          subprocess.stderr.on('close', () => {
            console.log("Closed");
          });
        console.log('test danse');
    });
    // jouer
    socket.on('play', () => {
        //script python
        console.log('test play');
    });
});
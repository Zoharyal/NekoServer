const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const router = require('./router/route');
const socket = require('./socket/socket');
const path = require('path');
const {spawn} = require('child_process');
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

server = app.listen(8080, () => {
    console.log('listening on 8080');
});
socket.initSocket(server);

const io = socket.getInstance();

io.on('connection', function(socket) {
    console.log('connected');
    function runScript(script) {
        return spawn('python', ["-u", path.join(__dirname, `/script/${script}`)]);
    }
    //manger
    socket.on('eat', () => {
        console.log('test eat');
        const subprocess = runScript('Feed.py');
        subprocess.stdout.on('data', (data) => {
            console.log(`data:${data}`);
          });
          subprocess.stderr.on('data', (data) => {
            console.log(`error:${data}`);
          });
          subprocess.stderr.on('close', () => {
            console.log("Closed");
          });
    });
    // dormir
    socket.on('sleep', () => {
        console.log('test sleep');
        const subprocess = runScript('SleepFaceAnimated.py');
        subprocess.stdout.on('data', (data) => {
            console.log(`data:${data}`);
          });
          subprocess.stderr.on('data', (data) => {
            console.log(`error:${data}`);
          });
          subprocess.stderr.on('close', () => {
            console.log("Closed");
          });
    });
    // se laver
    socket.on('wash', () => {
        console.log('test wash');
        const subprocess = runScript('Shower.py');
        subprocess.stdout.on('data', (data) => {
            console.log(`data:${data}`);
          });
          subprocess.stderr.on('data', (data) => {
            console.log(`error:${data}`);
          });
          subprocess.stderr.on('close', () => {
            console.log("Closed");
          });
    });
    // aller au toilette
    socket.on('toilet', () => {
        console.log('test toilet');
        const subprocess = runScript('HappyFaceAnimated.py');
        subprocess.stdout.on('data', (data) => {
            console.log(`data:${data}`);
          });
          subprocess.stderr.on('data', (data) => {
            console.log(`error:${data}`);
          });
          subprocess.stderr.on('close', () => {
            console.log("Closed");
          });
    });
    // se réveiller
    socket.on('wakeup', () => {
        console.log('test wakeup');
        const subprocess = runScript('SleepFaceAnimated.py');
        subprocess.stdout.on('data', (data) => {
            console.log(`data:${data}`);
          });
          subprocess.stderr.on('data', (data) => {
            console.log(`error:${data}`);
          });
          subprocess.stderr.on('close', () => {
            console.log("Closed");
          });
    });
    // danser
    socket.on('danse', () => {
        console.log('test danse');
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
    });
    // jouer
    socket.on('play', () => {
        console.log('test play');
        const subprocess = runScript('Play.py');
        subprocess.stdout.on('data', (data) => {
            console.log(`data:${data}`);
            });
            subprocess.stderr.on('data', (data) => {
            console.log(`error:${data}`);
            });
            subprocess.stderr.on('close', () => {
            console.log("Closed");
            });
    });
});
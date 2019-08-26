const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const router = require('./router/route');
const socket = require('./socket/socket');
const path = require('path');
const cmd = require('node-cmd');
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
    console.log('test eat');
    // const spawn = require('child_process').spawn;
    socket.on('eat', () => {
        //script python
        const file = __dirname + '/script/Feed.py';
        console.log(file);
        // const eatPython = cmd.get(`python ${file}`, 
        // function(data, err, stderr) {
        //     if(!err) {
        //         console.log('working', data);
        //     } else {
        //         console.log('error', err);
        //     }
        // })
        const childProcess = require('child_process');
        childProcess.exec(`python ${file}`, function(err){
            if (err) {
                console.log('error', err);
            }
        })
    });
    // dormir
    socket.on('sleep', () => {
        //script python
        console.log('test sleep');
    });
    // se laver
    socket.on('wash', () => {
        const file = __dirname + '/script/Shower.py';
        console.log(file);
        const eatPython = cmd.get(`python ${file}`, 
        function(data, err, stderr) {
            if(!err) {
                console.log('working', data);
            } else {
                console.log('error', err);
            }
        })
        console.log('test wash');
    });
    // aller au toilette
    socket.on('toilet', () => {
        //script python
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
        console.log('test danse');
    });
    // jouer
    socket.on('play', () => {
        //script python
        console.log('test play');
    });
});
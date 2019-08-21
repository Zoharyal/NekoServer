const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const router = require('./router/route');
const socket = require('./socket/socket');
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
    console.log('listening on 3000');
});
socket.initSocket(server);

const io = socket.getInstance();

io.on('connection', function(socket) {
    console.log('user connected');

    // donner à manger
    socket.on('eat', () => {
        //script python
        console.log('test eat');
    });
    // dormir
    socket.on('sleep', () => {
        //script python
        console.log('test sleep');
    });
    // se laver
    socket.on('wash', () => {
        //script python
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
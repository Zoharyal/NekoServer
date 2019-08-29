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
    function runScript(script, typeSon) {
        return spawn('python', ["-u", path.join(__dirname, `/script/${script}`), typeSon]);
    }

    // function runPersistentScript(bActiv = true) {
    //   while (bActiv) {
    //     const subprocess = runScript('Iddle.py');
    //     subprocess.stdout.on('data', (data) => {
    //         console.log(`data:${data}`);
    //       });
    //     subprocess.stderr.on('data', (data) => {
    //       console.log(`error:${data}`);
    //     });
    //     subprocess.stderr.on('close', () => {
    //       console.log("Closed");
    //     });
    //   }
    // }
    // runPersistentScript();
    //manger
    socket.on('eat', () => {
        console.log('test eat');
        const subprocess = runScript('Eatting.py', 'eat');
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
    // capteur rfid
    socket.on('badge', () => {
      console.log('test badge');
      const subprocess = runScript('Read.py');
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
    // socket.on('wash', () => {
    //     console.log('test wash');
    //     const subprocess = runScript('Shower.py');
    //     subprocess.stdout.on('data', (data) => {
    //         console.log(`data:${data}`);
    //       });
    //       subprocess.stderr.on('data', (data) => {
    //         console.log(`error:${data}`);
    //       });
    //       subprocess.stderr.on('close', () => {
    //         console.log("Closed");
    //       });
    // });

    // aller au toilette
    socket.on('toilet', () => {
        console.log('test toilet');
        runPersistentScript(false);
        const subprocess = runScript('HappyPlusheen.py');
        subprocess.stdout.on('data', (data) => {
            console.log(`data:${data}`);
          });
          subprocess.stderr.on('data', (data) => {
            console.log(`error:${data}`);
          });
          subprocess.stderr.on('close', () => {
            console.log("Closed");
            runPersistentScript(true);
          });
    });
    // se réveiller
    socket.on('wakeup', () => {
        console.log('test wakeup');
        const subprocess = runScript('Wakeup.py');
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
    // main qui bouge
    // socket.on('foot', () => {
    //   console.log('test foot');
    //   // to do nom de script
    //   const subprocess = runScript('');
    //   subprocess.stdout.on('data', (data) => {
    //     console.log(`data:${data}`);
    //     });
    //   subprocess.stderr.on('data', (data) => {
    //     console.log(`error:${data}`);
    //   });
    //   subprocess.stderr.on('close', () => {
    //     console.log("Closed");
    //   });
    // });
    // ronflement 
    // socket.on('ronflement', () => {
    //   console.log('test ronflement');
    //   // to do nom de script
    //   const subprocess = runScript('');
    //   subprocess.stdout.on('data', (data) => {
    //     console.log(`data:${data}`);
    //     });
    //   subprocess.stderr.on('data', (data) => {
    //     console.log(`error:${data}`);
    //   });
    //   subprocess.stderr.on('close', () => {
    //     console.log("Closed");
    //   });
    // });
    // cold
    socket.on('cold', () => {
      console.log('test cold');
      const subprocess = runScript('ColdShower.py');
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

    // shower hot
    socket.on('hot', () => {
      console.log('test hot');
      // to do nom de script + son
      const subprocess = runScript('HotShower.py');
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

    // perfect temperature
    socket.on('perfect', () => {
      console.log('test perfect');
      // to do nom de script
      const subprocess = runScript('GoodShower.py');
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


    socket.on('beer', () => {
      console.log('test beer');
      // to do nom de script + argument
      const subprocess = runScript('Beer.py');
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

    socket.on('burger', () => {
      console.log('test burger');
      // to do nom de script + argument
      const subprocess = runScript('Feed.py', 'burger');
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
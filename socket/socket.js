const io = require('socket.io');

let socketInstance;

/**
 * Initialise le listening du socket
 */
function initSocket(server) {
  socketInstance = io.listen(server);
}

/**
 * Récupère l'instance du socket en cours d'utilisation
 */
function getInstance() {
  return socketInstance;
}

exports.initSocket = initSocket;
exports.getInstance = getInstance;

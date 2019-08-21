const express = require('express');
const router = express.Router();
// faire route pour chaque action 
// qui nécessite une action de la peluche


router.get('/test', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});
// donner à manger

// dormir

// se laver

// aller au toilette

// se réveiller

// danser

// jouer

module.exports = router;

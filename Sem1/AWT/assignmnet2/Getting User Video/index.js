const express = require('express');
const app = express();

const server = app.listen(4400, function(){
    console.log('Listening on port 4400 !!!');
});


app.use(express.static('public'));

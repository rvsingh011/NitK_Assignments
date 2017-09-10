var express = require('express');
var socket = require('socket.io');

var app = express();
var server = app.listen(4000, function(){
  console.log("server is listening");
});

app.use(express.static('public'));
//Socket setup
var io = socket(server);
io.on('connection', function(socket){
  console.log("made a socket connection" + socket.id);
  socket.on('chat', function(message){
    io.sockets.emit('chat', message);
  });
  socket.on('typing', function(data) {
    socket.broadcast.emit('typing', data);
  })
});

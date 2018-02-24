var express = require('express');
var socket = require('socket.io');
var peer_list = {};
var temp = {};
//create a server
var app = express();
var server = app.listen(4000, function() {
  console.log("server is listening");
});
//serve public things
app.use(express.static('public'));

//Socket setup on server

var io = socket(server);
io.use(function(socket, next) {
  var handshakeData = socket.request;
  temp = handshakeData._query['user'];
  temp = JSON.parse(temp);
  peer_list[temp["username"]] = temp["id"];
  console.log(peer_list);
  next();
});
io.on('connection', function(socket) {
  console.log("made a socket connection");
  socket.emit('new_user_added', JSON.stringify(peer_list));
  socket.on('chat', function(message) {
    io.sockets.emit('chat', message);
  });
  socket.on('typing', function(data) {
    socket.broadcast.emit('typing', data);
  });
});

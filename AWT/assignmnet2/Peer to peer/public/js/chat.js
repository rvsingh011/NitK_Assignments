var message = document.getElementById('message');
var button = document.getElementById('send');
var username = document.getElementById('username');
var output = document.getElementById('output');
var feedback = document.getElementById('feedback');
var online = document.getElementById('online');
var caller = document.getElementById('caller');
var callButton = document.getElementById('callButton');
var video = document.querySelector('video');
var user_info = {};
var peers = {};
var socket;
user_info["username"] = "Ravi";

var createPeer = new Promise(function(resolve, reject) {
  var peer = new Peer({
    key: 'axqvqrv6b6426gvi'
  });
  peer.on('open', function(id) {
    user_info["id"] = id;
    if (user_info.hasOwnProperty("id")) {
      resolve(peer);
    } else {
      reject(error);
    }
  });
});


createPeer.then(function(peer) {
  console.log("a New peer connection with id ");
  console.log("creating a new socket");
  socket = io.connect('http://localhost:4000', {
    query: "user=" + JSON.stringify(user_info)
  });

  button.addEventListener('click', function() {
    socket.emit('chat', {
      message: message.value,
      username: username.value
    });
  });

  // When Call Button is pushed
  callButton.addEventListener('click', () => {
    console.log(caller.value, peers);
    var localId = peers[caller.value];
    console.log(localId);
    // var conn = peer.connect(localId);
    // conn.on('open', function() {
    //   conn.send('hi!');
    // });
    var getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;
    navigator.mediaDevices.getUserMedia({
      video: true,
      audio: true
    }, function(stream) {
        video1.src = window.URL.createObjectURL(stream);
      }, function(error){
        console.log("there was an error" + errror);
      });
  });




  message.addEventListener('keypress', () => {
    socket.emit('typing', username.value);
  });

  //listen for events

  socket.on('chat', (data) => {
    feedback.innerHTML = "";
    output.innerHTML += '<p><strong>' + data.username + ' </strong>' + data.message + '</p>';
  });

  socket.on('new_user_added', (data) => {
    peers = JSON.parse(data);
    console.log(peers);
    Object.keys(peers).forEach(function(key) {
      console.log(key);
      online.innerHTML += "<h1>" + key + "</h1><br>"
    });
  });
  socket.on('typing', function(data) {
    feedback.innerHTML = "<i>" + data + " is Typing</i>......";
  });
}, function(error) {
  console.log("there was an error" + error);
});

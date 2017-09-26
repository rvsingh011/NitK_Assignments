var ul = document.getElementById('ul');
var callButton = document.getElementById('callButton');
var usr = document.getElementById('usr');
var message = document.getElementById('message');
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

  // When Call Button is pushed
  callButton.addEventListener('click', () => {
    if (!usr.value){
      alert("Enter a user");
    }
    else if (!message.value) {
      alert("enter a message");
    }
    else{
      if (peers[usr.value]){
        var destinationId = peers[usr.value];
        var conn = peer.connect(destinationId);
      }
      else{
        alert("you entred wrong username");
      }
    }
  });
  socket.on('new_user_added', (data) => {
    peers = JSON.parse(data);
    console.log(peers);
    Object.keys(peers).forEach(function(key) {
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(key));
    li.setAttribute("class", "list-group-item list-group-item-success");
     ul.appendChild(li);
    });
  });

  peer.on('connection', function(comm) { console.log("New user")});
}, function(error) {
  console.log("there was an error" + error);
});

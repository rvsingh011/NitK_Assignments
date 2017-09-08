var socket = io.connect('http://localhost:4000');
var message = document.getElementById('message');
var button = document.getElementById('send');
var username = document.getElementById('username');
var output = document.getElementById('output');
var feedback = document.getElementById('feedback');

button.addEventListener('click', function(){

  socket.emit('chat',{
    message:message.value,
    username: username.value
  });
});
message.addEventListener('keypress', () =>{
  socket.emit('typing', username.value);
});

//listen for events

socket.on('chat', (data) => {
  feedback.innerHTML = "";
  output.innerHTML += '<p><strong>' + data.username + ' </strong>' + data.message + '</p>';
});
socket.on('typing', function(data){
  feedback.innerHTML = "<i>" + data + " is Typing</i>......";
});

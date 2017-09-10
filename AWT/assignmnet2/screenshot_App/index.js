const express = require('express');

var app = express();

var server = app.listen(5000, function () {
  console.log("listening on port 5000 !!!");
});

app.use(express.static('public'));

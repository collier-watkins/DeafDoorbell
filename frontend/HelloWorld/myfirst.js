var http = require('http');
var dt = require('./myfirstmodule');

var portNumber = 8080

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write("The date and time are currently: " + dt.myDateTime());
  res.end();
}).listen(portNumber);
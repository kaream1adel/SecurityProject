const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const mqttHandler = require('./mqtt_handler.js');
const GPS = require('gps');

const app = express();
const server = http.createServer(app);
const io = socketIO(server);
const gps = new GPS;


// Serve static files from the 'public' directory
app.use(express.static('public'));

// Serve the HTML page
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

mqttHandler.run_MQTT(io);

// Set up Socket.io connection
io.on('connection', (socket) => {
  console.log('A user connected');
  
  // Handle disconnection
  socket.on('disconnect', () => {
    console.log('User disconnected');
  });
});


// Listen for GPS data updates
gps.on('data', (data) => {
  const { lat, lon } = data;
  const coordinates = { lat, lon };
  // Publish coordinates to MQTT
  mqttHandler.publishCoordinates(coordinates);
});

// Listen on a port
const Port = process.env.PORT || 3000;
server.listen(Port, () => {
  console.log(`Server is running on port ${Port}`);
});



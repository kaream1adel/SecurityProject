const mqtt = require('mqtt');
const { connectOptions } = require('./use file/use_mqtt')

let mqttClient; // Declare the MQTT client

module.exports = {

    run_MQTT: function(io){
        const options = {
        clientId:'jonathan',
        clean: true,
        connectTimeout: 4000,
        username: 'saher',
        password: '1901612',
        reconnectPeriod: 1000,
        }

        const { protocol, host, port } = connectOptions

        let connectUrl = `${protocol}://${host}:${port}`
        if (['ws', 'wss'].includes(protocol)) {
        connectUrl += '/mqtt'
        }


        mqttClient = mqtt.connect(connectUrl, options)

        const topic = 'map_test'
        const payload = "sba7 alfol ya 3m saher"
        const qos = 0

        mqttClient.on('connect', () => {
            console.log(`${protocol}: Connected`)

            mqttClient.subscribe(topic, { qos }, (error) => {
                if (error) {
                console.log('subscribe error:', error)
                return
                }
                console.log(`${protocol}: Subscribe to topic '${topic}'`)
            })
        })

        mqttClient.on('message', (topic, message) => {
            console.log('Received Message:', topic, message.toString())
            // Emit the MQTT message to connected clients
            io.emit('mqttMessage', message.toString());
        })

        mqttClient.on('reconnect', (error) => {
        console.log(`Reconnecting(${protocol}):`, error)
        })

        mqttClient.on('error', (error) => {
        console.log(`Cannot connect(${protocol}):`, error)
        })

    },
    publishCoordinates: function (coordinates) {
        // Check if the MQTT client is initialized
        if (mqttClient) {
          const topic = 'map_test';
          const qos = 0;
            
            mqttClient.publish(topic, coordinates, { qos }, (error) => {
            if (error) {
                console.error(error)
            }
            })
        }else {
          console.log('MQTT client not initialized.');
        }
      }    
};

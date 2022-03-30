# Live Temperature Monitoring using Edge Computing with Microsoft Azure 

* Mqtt Client (ESP32) publishes sensor data to (Mosquitto)broker running on server 

* Mosquitto Setup on Windows Machine

* Install Mosquitto Broker on windows
```
https://mosquitto.org/download/
```
* Open port to listen on LAN when using its IP address.
    *Create a test.conf file enter the following details in that file.
      ```
      listener 1883
      allow_anonymous true
      ```
    *Run the Mosquitto Server with this Test.conf file uing the following Command.
    ```
    mosquitto -v -c test.conf
    ```
* Node-Red Connects with the MQTT Server . 

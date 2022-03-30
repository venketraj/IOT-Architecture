# Live Temperature Monitoring using Edge Computing with Microsoft Azure 

* Mqtt Client (ESP32) publishes sensor data to (Mosquitto)broker running on server 

* Mosquitto Setup on Windows Machine

* Install Mosquitto Broker on windows
```
https://mosquitto.org/download/
```
* Open port to listen on LAN when using its IP address.
    * Create a test.conf file enter the following details in that file.
      ```
      listener 1883
      allow_anonymous true
      ```
    * Run the Mosquitto Server with this Test.conf file uing the following Command.
    ```
    mosquitto -v -c test.conf
    ```
* Node-Red Connection with the MQTT Server .
   * Replace the IP address of local machine in the Node-red MQTT palette or type in http://localhost:1880.

# Node-Red Setup for UI and Data processing.

* Upload the ``` Node_red-UI-Flows.json ``` file into import tab on the Node-red tool.
* Cick on Deploy to complete.

# Azure Config and file upload part.

* For Blob Creation and Config refer the below Link 
```
https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal
```

* Open " Azure_blob_python " folder in the repository .
* Before Running the Script the following params to be modified for your credentials.
      * Connection String of the Azure Blob.
      * Container name.
      * Blob name.
* It will check and update the CSV file on the Azure Blob if any anomaly detected.
* For Error - Please do chek the below link.
```

```

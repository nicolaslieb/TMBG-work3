import paho.mqtt.client as mqtt
import numpy as np

# MQTT configuration
broker = "mqtt-broker"  # The hostname of the Docker container running Mosquitto
port = 1883
topic = "sensor/data"

# List to hold sensor values
data_buffer = []

# Callback function for received messages
def on_message(client, userdata, message):
    value = float(message.payload.decode("utf-8"))
    print(f"Received: {value}")
    data_buffer.append(value)

    # Detect outliers using Z-score
    if len(data_buffer) > 10:  # Minimum data points for analysis
        z_scores = np.abs((value - np.mean(data_buffer)) / np.std(data_buffer))
        if z_scores > 2:  # Threshold for an outlier
            print(f"Outlier detected: {value}")

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, port)
client.subscribe(topic)
client.loop_forever()

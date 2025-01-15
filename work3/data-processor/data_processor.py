import paho.mqtt.client as mqtt
import numpy as np

# MQTT configuration
broker = "mqtt-broker"  # Service name in docker-compose.yml
port = 1883
topic = "sensor/data"

# Buffer to hold recent sensor values
data_buffer = []

# Callback function for received messages
def on_message(client, userdata, message):
    value = float(message.payload.decode("utf-8"))
    print(f"Received: {value}")
    data_buffer.append(value)

    # Keep the buffer size manageable (e.g., last 50 values)
    if len(data_buffer) > 50:
        data_buffer.pop(0)

    # Detect outliers using Z-score
    if len(data_buffer) > 10:  # Minimum data points for meaningful statistics
        mean = np.mean(data_buffer)
        std_dev = np.std(data_buffer)
        z_score = abs((value - mean) / std_dev) if std_dev > 0 else 0
        
        if z_score > 2:  # Z-score threshold for an outlier
            print(f"Outlier detected: {value} (Z-score: {z_score:.2f}, Mean: {mean:.2f}, StdDev: {std_dev:.2f})")

# Initialize MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to the broker and subscribe to the topic
try:
    client.connect(broker, port)
    print("Connected to MQTT Broker!")
    client.subscribe(topic)
    client.loop_forever()
except Exception as e:
    print(f"Error: {e}")
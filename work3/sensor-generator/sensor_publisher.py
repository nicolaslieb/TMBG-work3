import paho.mqtt.client as mqtt
import time
import random

# MQTT configuration
broker = "mqtt-broker"  # The hostname of the Docker container running Mosquitto
port = 1883
topic = "sensor/data"

client = mqtt.Client()
client.connect(broker, port)

while True:
    # Simulate sensor data
    sensor_value = random.uniform(20, 30)
    client.publish(topic, f"{sensor_value:.2f}")
    print(f"Published: {sensor_value:.2f}")
    time.sleep(1)

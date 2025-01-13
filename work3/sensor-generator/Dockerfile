FROM python:3.9-slim
WORKDIR /app
COPY sensor_publisher.py .
RUN pip install paho-mqtt
CMD ["python", "sensor_publisher.py"]

FROM python:3.9-slim
WORKDIR /app
COPY data_processor.py .
RUN pip install paho-mqtt numpy
CMD ["python", "data_processor.py"]
FROM python:3.8-slim
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY dbConsumer.py /app/
RUN pip install kafka-python psycopg2-binary
CMD ["python", "dbConsumer.py"]
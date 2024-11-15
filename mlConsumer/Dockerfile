FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY mlConsumer.py /app/
COPY resnet50.pth /app/
CMD ["python", "mlConsumer.py"]
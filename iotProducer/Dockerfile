# Base image with Python installed
FROM python:3.8-slim

# Set working directory in the container
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Install necessary packages
RUN apt-get update && apt-get install -y \
    pkg-config \
    libhdf5-dev \
    build-essential \
    libgl1-mesa-glx \ 
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy producer script and dependencies
COPY iotProducer.py /app/

# Command to run the producer script
CMD ["python", "iotProducer.py"]

from keras.datasets import cifar10
# from datasets import cifar10
import random
import json
from kafka import KafkaProducer
import cv2
import uuid
import time
import os

(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

kafka_broker_ip = "192.168.5.45"
print(F"THIS IS THE KAFKA IP: {kafka_broker_ip}")
producer = KafkaProducer(bootstrap_servers=f'{kafka_broker_ip}:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

label_map = {
    0: 'airplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck'
}

def add_noise(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def send_image_to_kafka():
    idx = random.randint(0, len(test_images) - 1)
    image = test_images[idx]
    noisy_image = add_noise(image)
    ground_truth = train_labels[idx][0]
    ground_truth_str = label_map[ground_truth]
    
    data = {
        'ID': str(uuid.uuid4()),
        'GroundTruth': ground_truth_str,
        'Data': noisy_image.tolist()
    }
    
    producer.send('image-topic', value=data)
    print(f"Sent image ID {data['ID']} to Kafka")

while True:
    send_image_to_kafka()
    time.sleep(1)

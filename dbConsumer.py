from kafka import KafkaConsumer
import json
from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['images']
collection = db['image-data']

kafka_broker_ip = '192.168.5.236'
topic_name = 'image-topic'

consumer = KafkaConsumer(
   topic_name,
   bootstrap_servers=f'{kafka_broker_ip}:9092',
   value_deserializer=lambda v: json.loads(v.decode('utf-8')),
   auto_offset_reset='earliest',
   enable_auto_commit=True,
   group_id='my-group'
)

print("Listening for messages...")

for message in consumer:
   data = message.value
   print(f"Received message: {data}")

   collection.insert_one(data)
   print("Data inserted into MongoDB")
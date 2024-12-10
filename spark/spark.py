from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Create a Spark session
spark = SparkSession.builder.appName("KafkaSparkIntegration").getOrCreate()

# Define Kafka parameters
kafka_bootstrap_servers = "kafka:9093"  # If using Docker, replace with Kafka container's name or IP
kafka_topic = "your_kafka_topic"

# Read stream from Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .load()

# Perform operations on the Kafka stream (e.g., parse the value field)
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Write the stream to the console for debugging
query = df.writeStream.outputMode("append").format("console").start()

# Await termination of the stream
query.awaitTermination()

# Use an official Ubuntu base image
FROM ubuntu:20.04

# Set environment variables
ENV SPARK_VERSION 3.5.3
ENV HADOOP_VERSION 3
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $PATH:$JAVA_HOME/bin

# Install dependencies and JDK 8
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    wget \
    curl \
    vim \
    net-tools \
    && apt-get clean

# Install Apache Spark
RUN wget https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    tar xvf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    mv spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /opt/spark && \
    rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz

# Set Spark environment variables
ENV SPARK_HOME /opt/spark
ENV PATH $PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# Expose ports for Spark (if needed for cluster or client mode)
EXPOSE 7077 8080

# Set the default command to run Spark shell
CMD ["spark-shell"]

# Install Kafka dependencies (for PySpark)
RUN pip install pyspark
RUN pip install kafka-python

#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8


echo "<<<<<<<< Database Setup >>>>>>>>>"

# python3 manage.py migrate

echo "<<<<<<<< Database Setup Successfully >>>>>>>>>>>>>>>>>>"

docker run -d --restart=always --name cashcog_kafka --network kafka-network

bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-server-start.sh config/server.properties

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

echo "<<<<<<<< API Streaming Starting >>>>>>>>>>>>>>>>>>"

python3 -m utilities.stream &

echo "<<<<<<<< Load Data into Database Starting >>>>>>>>>>>>>>>>>>"

python3 -m utilities.load_data &

python3 manage.py runserver 
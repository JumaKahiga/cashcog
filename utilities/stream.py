import os
import requests

from utilities.kafka_functions import (
    connect_kafka_producer, publish_message)

from dotenv import load_dotenv

load_dotenv()

url = os.environ.get('STREAM_URL')

kafka_producer = connect_kafka_producer()


def stream(url):
    with requests.get(url, stream=True) as response:
        for item in response.iter_lines():
            if item:
                item = item.decode("utf-8")
                publish_message(kafka_producer, 'raw_expenses', 'raw', item)


if __name__ == '__main__':
    data = stream(url)

    if not kafka_producer:
        kafka_producer.close()

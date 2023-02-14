from datetime import datetime
from kafka import KafkaProducer
import time
import random

_BOOTSTRAP_IP = "10.12.168.74"
_BOOTSTRAP_PORT = "9092"

FOOD_LIST = ["burger", "pizza", "kookbab", "kimbab", "pasta"]

def main():

    bootstrap_server = f"{_BOOTSTRAP_IP}:{_BOOTSTRAP_PORT}"

    producer = KafkaProducer(bootstrap_servers=bootstrap_server)

    topic = "food"

    while True:
        food = random.choice(FOOD_LIST)
        data = {
            'timestamp': str(datetime.now()),
            'category': category
        }
        message = json.dumps(data).encode()
        producer.send(topic, message)
        time.sleep(10)

if __name__ == "__main__":
    main()

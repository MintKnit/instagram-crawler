from datetime import datetime
from kafka import KafkaProducer
import time

_BOOTSTRAP_IP = "10.12.168.74"
_BOOTSTRAP_PORT = "9092"

def main():

    bootstrap_server = f"{_BOOTSTRAP_IP}:{_BOOTSTRAP_PORT}"

    producer = KafkaProducer(bootstrap_servers=bootstrap_server)

    topic = "food"

    while True:
        now = str(datetime.now())
        producer.send(topic, now.encode())
        print(now)
        time.sleep(10)

if __name__ == "__main__":
    main()

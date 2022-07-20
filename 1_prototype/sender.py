import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

messages = ["1", "2", "3", "4", "5"]

for message in messages:
    channel.basic_publish(exchange="", routing_key="hello", body=message)
    print(f"[x] Enviada '{message}'")
    time.sleep(1)

connection.close()

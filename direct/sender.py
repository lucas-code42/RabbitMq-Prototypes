import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

messages =   ["Primeiro log", "Segundo log", "Terceiro log", "Quarto log", "Quinto log"]
severities = ["info"        , "error"      , "warning"     , "error"     , "info"]

for i in range(len(messages)):
    time.sleep(1)
    channel.basic_publish(exchange="direct_logs", routing_key=severities[i], body=messages[i])
    print(f"[x] sent {severities[i]}{messages[i]}")

connection.close()
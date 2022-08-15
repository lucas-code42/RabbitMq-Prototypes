import queue
import pika
import sys

def callback(ch, method, properties, body):
    print("[x] %r:%r" % (method.routing_key, body))

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

biding_keys = sys.argv[1:]
if not biding_keys:
    sys.stderr.write("usage %s [biding_keys]...\n" % sys.argv[0])
    sys.exit(1)

for biding_key in biding_keys:
    channel.queue_bind(exchange="topic_logs", queue=queue_name, routing_key=biding_key)

print("[*] Waiting for logs")
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
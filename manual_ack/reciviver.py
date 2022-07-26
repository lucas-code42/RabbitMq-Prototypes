import pika

def callback(ch, method, properties, body):
    print(body)
    print(properties)
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue="hello")

channel.basic_consume(queue='hello', auto_ack=False, on_message_callback=callback) # parameter auto_ack=False
print("[*] Aguardando menssagens")
channel.start_consuming()
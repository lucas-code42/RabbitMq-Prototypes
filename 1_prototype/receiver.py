import pika


def callback(ch, method, properties, body):
    print("[x] Recebido %r" % body)


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_consume(queue="hello", auto_ack=True,
                      on_message_callback=callback)

print("[*] Aguardando menssagens")
channel.start_consuming()

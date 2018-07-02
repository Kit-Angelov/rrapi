import pika
import json
from fgis_worker import FgisWorker

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='download_order')

print(' [*] Waiting for messages. To exit press CTRL+C')

def receiver(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    fgisWorker = FgisWorker()
    fgisWorker.receive(body)


channel.basic_consume(receiver,
                      queue='download_order',
                      no_ack=True)

channel.start_consuming()
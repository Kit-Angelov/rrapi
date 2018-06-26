import pika
import json
from fgis_core import RRSurfer

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='rrd_order')

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    message_dict = json.loads(body)
    print(message_dict)
    fgis_token = message_dict.get('fgis_token', None)
    list_cad_num = message_dict.get('list_cad_num', None)
    if (fgis_token is not None) and (list_cad_num is not None):
    	rr_surfer = RRSurfer(fgis_token)
    	order_num = rr_surfer.order_document(list_cad_num[0])
    	print(order_num)


channel.basic_consume(callback,
                      queue='rrd_order',
                      no_ack=True)

channel.start_consuming()
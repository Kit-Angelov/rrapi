import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.2.233'))
channel = connection.channel()

channel.queue_declare(queue='rrd_order')

channel.basic_publish(exchange='',
                      routing_key='rrd_order',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
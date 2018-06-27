import pika


def send(queue_name, message):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='locahost'))
	channel = connection.channel()

	channel.queue_declare(queue=queue_name)

	channel.basic_publish(exchange='',
	                      routing_key=queue_name,
	                      body=message)
	print(" [x] Sent answer")
	connection.close()
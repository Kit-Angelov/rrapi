import pika


def send_answer(queue_name, message):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	channel.queue_declare(queue=queue_name)

	channel.basic_publish(exchange='',
	                      routing_key=queue_name,
	                      body=message)
	print(" [x] Sent answer")
	connection.close()
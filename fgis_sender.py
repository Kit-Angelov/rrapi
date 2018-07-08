import pika


def send_answer(conn_param, message):
	credentials = pika.PlainCredentials(conn_param['user'], conn_param['password'])

	connection = pika.BlockingConnection(pika.ConnectionParameters(host=conn_param['host'],
                                                                   virtual_host=conn_param['virtual_host'],
                                                                   credentials=credentials))

	channel = connection.channel()

	channel.queue_declare(queue=conn_param['queue'], durable=True)

	channel.basic_publish(exchange='',
	                      routing_key=conn_param['queue'],
	                      body=message,
	                      properties=pika.BasicProperties(
	                         delivery_mode = 2,
	                      ))
	print(" [x] Sent answer message: {}".format(message))
	connection.close()
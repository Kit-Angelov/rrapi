import pika


def send_answer(conn_param, message):
	credentials = pika.PlainCredentials(conn_param['user'], conn_param['password'])

	connection = pika.BlockingConnection(pika.ConnectionParameters(host=conn_param['host'],
                                                                   port=conn_param['port'],
                                                                   credentials=credentials))

	channel = connection.channel()

	channel.queue_declare(queue=conn_param['queue'])

	channel.basic_publish(exchange='',
	                      routing_key=conn_param['queue'],
	                      body=message)
	print(" [x] Sent answer message: {}".format(message))
	connection.close()
import pika
import json
from fgis_worker import FgisWorker
import argparse
from settings import mode_dict
from loggerInit import init_logger
import logging

def run(mode): # order, status or download

	conn_param = mode_dict.get(str(mode), None)

	if conn_param is None:
		try:
			raise Exception("НЕВЕРНОЕ ЗНАЧЕНИЕ MODE: {}".format(str(mode)))
		except Exception as e:
			print(e)

	# logger init
	init_logger(mode)
	logger = logging.getLogger(mode)

	credentials = pika.PlainCredentials(conn_param['user'], conn_param['password'])

	connection = pika.BlockingConnection(pika.ConnectionParameters(host=conn_param['host'], port=conn_param['port'], credentials=credentials))

	channel = connection.channel()

	channel.queue_declare(queue=conn_param['queue'], durable=True)

	logger.info(' [*] Start Consumer | Mode {}'.format(mode))

	def receiver(ch, method, properties, body):
	    logger.info(" [+] Received Message %r" % (body,))
	    fgisWorker = FgisWorker(mode)
	    fgisWorker.receive(body)
	    ch.basic_ack(delivery_tag = method.delivery_tag)


	channel.basic_consume(receiver,
	                      queue=conn_param['queue'])

	channel.start_consuming()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="RRDoc Ordering Worker")
	parser.add_argument("--mode", 
						"-m", type=str, 
						default='order', 
						help="order-заказ документа, status-проверка статуса, download-загрузка документа")

	options = parser.parse_args()
	run(options.mode)
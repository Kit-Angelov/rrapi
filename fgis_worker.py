from fgis_surfer.fgis_core import RRSurfer
from fgis_sender import send_answer
import json


class FgisWorker:

	def __init__(self):
		self.methods = {
			'to_order': self.to_order,
			'get_status': self.get_status,
			'download': self.download
		}
		self.fgis_token = str()
		self.message_dict = dict()
		self.answer_queue = str()
		self.rr_surfer = object()

	def get_status(self):
		order_num = self.message_dict.get('order_num', None)
		if isinstance(order_num, str):
			status = self.rr_surfer.get_status(order_num)
			print('status {}: {}'.format(order_num, status))
		else:
			pass

	def to_order(self):
		cad_num = self.message_dict.get('cad_num', None)
		order_id = self.message_dict.get('order_id', None)
		if isinstance(cad_num, str) and (order_id is not None):
			#order_num = self.rr_surfer.order_document(cad_num)
			order_num = 'test_order_num'
			print('order_num: {}'.format(order_num))
			self.send('to_order', order_id=order_id, order_num=order_num)
		else:
			pass

	def download(self):
		pass

	def receive(self, body):
		self.message_dict = json.loads(body)
		print('message dict', self.message_dict)
		self.fgis_token = self.message_dict.get('fgis_token', None)
		self.answer_queue = self.message_dict.get('answer_queue', None)
		method = self.message_dict.get('method', None)

		if (self.fgis_token is not None) and (method in self.methods):
			self.rr_surfer = RRSurfer(self.fgis_token)
			worker_method = self.methods[method]
			worker_method()

	def send(self, answer_type, error='', **data):
		answer = {
			'answer_type': answer_type,
			'order_id': data['order_id'],
			'order_num': data['order_num'],
			'error': error,
		}
		answer_json = json.dumps(answer)
		send_answer(self.answer_queue, answer_json)
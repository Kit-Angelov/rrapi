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
		self.answer_types = {
			'to_order': self.answer_to_order,
			'get_status': self.answer_get_status,
			'download': self.answer_download
		}
		self.fgis_token = str()
		self.message_dict = dict()
		self.answer_queue = str()
		self.rr_surfer = object()
		self.order_id = int()

	def get_status(self):
		order_num = self.message_dict.get('order_num', None)
		if isinstance(order_num, str):
			status = self.rr_surfer.get_status(order_num)
			print('status {}: {}'.format(order_num, status))
			self.send('get_status', error=None, order_id=self.order_id, order_status=status)
		else:
			pass

	def to_order(self):
		cad_num = self.message_dict.get('cad_num', None)
		if isinstance(cad_num, str) and (order_id is not None):
			# order_num = self.rr_surfer.order_document(cad_num)
			order_num = 'test_order_num'
			print('order_num: {}'.format(order_num))
			self.send('to_order', error=None, order_id=self.order_id, order_num=order_num)
		else:
			pass

	def download(self):
		order_num = self.message_dict.get('order_num', None)
		if isinstance(order_num, str):
			result_dict = self.rr_surfer.download_file(order_num)
			print('RESULT DICT', result_dict)
			if result_dict['error'] is None:
				path_to_file = result_dict['path_to_download']
				print('download_file_path {}: {}'.format(order_num, path_to_file))
				self.send('download', error=None, order_id=self.order_id, order_download_path=path_to_file)
			else:
				print('error', result_dict['error'])
		else:
			print('error: order_num is not string')
			
	def receive(self, body):
		self.message_dict = json.loads(body)
		print('message dict', self.message_dict)
		self.fgis_token = self.message_dict.get('fgis_token', None)
		self.answer_queue = self.message_dict.get('answer_queue', None)
		self.order_id = self.message_dict.get('order_id', None)
		method = self.message_dict.get('method', None)

		if (self.fgis_token is not None) and (method in self.methods):
			self.rr_surfer = RRSurfer(self.fgis_token)
			worker_method = self.methods[method]
			worker_method()

	def answer_to_order(self, answer_type, **data):
		answer = {
			'answer_type': answer_type,
			'order_id': data['order_id'],
			'order_num': data['order_num']
		}
		answer_json = json.dumps(answer)
		send_answer(self.answer_queue, answer_json)

	def answer_get_status(self, answer_type, **data):
		answer = {
			'answer_type': answer_type,
			'order_id': data['order_id'],
			'order_status': data['order_status']
		}
		answer_json = json.dumps(answer)
		print('answer_get_status: ', answer_json)
		send_answer(self.answer_queue, answer_json)

	def answer_download(self, answer_type, **data):
		answer = {
			'answer_type': answer_type,
			'order_id': data['order_id'],
			'order_download_path': data['order_download_path']
		}
		answer_json = json.dumps(answer)
		print('answer_download: ', answer_json)
		send_answer(self.answer_queue, answer_json)

	def send(self, answer_type, error=None, **data):
		if error is not None:
			print('error', error)
		else:
			if answer_type in self.answer_types:
				answer_func = self.answer_types[answer_type]
				answer_func(answer_type=answer_type, **data)
			else:
				print('error: not allowed answer type')
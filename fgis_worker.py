from fgis_surfer.fgis_core import RRSurfer
from fgis_sender import send_answer
from settings import mode_dict
import json
import logging


class FgisWorker:

	def __init__(self, mode):
		self.mode = mode
		self.logger = logging.getLogger(self.mode + '.fgis_worker')
		self.conn_param = mode_dict.get(str(self.mode), None)
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
			try:
				result_dict = self.rr_surfer.get_status(order_num)
				self.logger.info('RESULT DICT', result_dict)
				if result_dict['error'] is None:
					status = result_dict['status']
					self.send('get_status', error=None, order_id=self.order_id, order_status=status)
				else:
					self.logger.error('error', result_dict['error'])
					self.send('get_status', error=result_dict['error'], order_id=self.order_id)
			except Exception as e:
				self.logger.error('error: {}'.format(e))
		else:
			self.logger.error('error: order_num is not string')
			self.send('get_status', error='300', order_id=self.order_id)

	def to_order(self):
		cad_num = self.message_dict.get('cad_num', None)
		if isinstance(cad_num, str):
			result_dict = self.rr_surfer.order_document(cad_num)
			self.logger.info('RESULT DICT', result_dict)
			if result_dict['error'] is None:
				order_num = result_dict['order_num']
				self.send('to_order', error=None, order_id=self.order_id, order_num=order_num)
			else:
				self.logger.error('error', result_dict['error'])
				self.send('to_order', error=result_dict['error'], order_id=self.order_id)
		else:
			self.logger.error('error: cad_num is not string')
			self.send('to_order', error='300', order_id=self.order_id)

	def download(self):
		order_num = self.message_dict.get('order_num', None)
		if isinstance(order_num, str):
			result_dict = self.rr_surfer.download_file(order_num)
			self.logger.info('RESULT DICT', result_dict)
			if result_dict['error'] is None:
				path_to_file = result_dict['path_to_download']
				self.send('download', error=None, order_id=self.order_id, order_download_path=path_to_file)
			else:
				self.logger.error('error', result_dict['error'])
				self.send('download', error=result_dict['error'], order_id=self.order_id)
		else:
			self.logger.error('error: order_num is not string')
			self.send('download', error='300', order_id=self.order_id)
			
	def receive(self, body):
		self.message_dict = json.loads(body)
		self.fgis_token = self.message_dict.get('fgis_token', None)
		self.answer_queue = self.message_dict.get('answer_queue', None)
		self.conn_param['queue'] = self.answer_queue
		self.order_id = self.message_dict.get('order_id', None)
		method = self.message_dict.get('method', None)

		if (self.fgis_token is not None) and (method in self.methods) and (self.order_id is not None):
			self.rr_surfer = RRSurfer(self.fgis_token, log_mode=self.mode)
			worker_method = self.methods[method]
			worker_method()
		else:
			self.logger.error('error: not fgis_token or method or order_id')
			self.send('common', error='400', order_id=self.order_id)

	def answer_error(self, answer_type, error, order_id):
		answer = {
			'answer_type': answer_type,
			'order_id': order_id,
			'error': error
		}
		answer_json = json.dumps(answer)
		send_answer(self.conn_param, answer_json)

	def answer_to_order(self, answer_type, **data):
		answer = {
			'answer_type': answer_type,
			'order_id': data['order_id'],
			'order_num': data['order_num']
		}
		answer_json = json.dumps(answer)
		send_answer(self.conn_param, answer_json)

	def answer_get_status(self, answer_type, **data):
		answer = {
			'answer_type': answer_type,
			'order_id': data['order_id'],
			'order_status': data['order_status']
		}
		answer_json = json.dumps(answer)
		send_answer(self.conn_param, answer_json)

	def answer_download(self, answer_type, **data):
		answer = {
			'answer_type': answer_type,
			'order_id': data['order_id'],
			'order_download_path': data['order_download_path']
		}
		answer_json = json.dumps(answer)
		send_answer(self.conn_param, answer_json)

	def send(self, answer_type, error=None, **data):
		if error is not None:
			self.answer_error(answer_type=answer_type, error=error, order_id=data['order_id'])
		else:
			if answer_type in self.answer_types:
				answer_func = self.answer_types[answer_type]
				answer_func(answer_type=answer_type, **data)
			else:
				self.logger.error('error: not allowed answer type')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import os
from .app import config
from .app import utils
from .app import constants
from .app import ordering
from .app import checking_status
from .app import downloading
import logging


# главный класс инициализирует соединение, логинится и получает список элементов меню
class RRSurfer:

	def __init__(self, token, log_mode=None, env=None):
		self.token = token
		self.env = env
		if log_mode is not None:
			self.logger = logging.getLogger(str(log_mode) + '.fgis_core')
		else:
			self.logger = logging.getLogger('rrsurfer')

	def init_driver(self):
		self.logger.info('start driver init')
		self.driver = webdriver.PhantomJS() # инициализация веб-драйвера
		self.driver.implicitly_wait(30)
		self.logger.info('init driver ok')
		self.driver.set_window_size(840, 480)
		self.logger.info('set window_size')
		self.driver.get(config.rr_url) # открытие url
		self.logger.info('open url {}'.format(config.rr_url))

		self.logger.info('start login')
		self.login() # авторизация фгис по токену
		self.logger.info('finish login')
		utils.sleep(3)

		# получение элеменов меню
		self.logger.info('getting menu links')
		menu_links = self.driver.find_elements_by_class_name(constants.menu_link_class)
		self.menu_search = menu_links[0]
		self.menu_orders = menu_links[1]
		self.menu_request_owner = menu_links[2]
		self.menu_my_account = menu_links[3]

		self.logger.info('[ok] finish init RRSurfer')

	# авторизация по токену	
	def login(self):
		token_list = self.token.split("-")
		token_input_list = self.driver.find_elements_by_class_name(constants.textfield_class)
		token_input_list[0].send_keys(token_list[0])
		utils.sleep()
		token_input_list[1].send_keys(token_list[1])
		utils.sleep()
		token_input_list[2].send_keys(token_list[2])
		utils.sleep()
		token_input_list[3].send_keys(token_list[3])
		utils.sleep()
		token_input_list[4].send_keys(token_list[4])
		utils.sleep()
		enter_but = self.driver.find_element_by_class_name(constants.button_class)
		enter_but.click()

	# метод поиска и заказа документа по кадастровому номеру(принимает на вход). 
	# Возвращает номер заявки.
	def order_document(self, cad_num):
		self.init_driver() # инициализация драйвера на каждую из операций, т.к. нож в печень- токен не вечен.
		result_dict = ordering.order_document(self.driver, self.menu_search, cad_num)
		return result_dict

	# метод проверки статуса заявки по номеру заявки
	def get_status(self, order_num):
		self.init_driver() # инициализация драйвера на каждую из операций, т.к. нож в печень- токен не вечен.
		result_dict = checking_status.check_status(self.driver, self.menu_orders, order_num)
		return result_dict

	# метод скачивания документа выполненной заявки
	def download_file(self, order_num):
		self.init_driver() # инициализация драйвера на каждую из операций, т.к. нож в печень- токен не вечен.
		result_dict = downloading.download(self.driver, self.menu_orders, order_num, self.env)
		return result_dict


if __name__ == '__main__':
	rr_surfer = RRSurfer(config.token)
	# order_num = rr_surfer.order_document('36:21:0100042:35')
	status_text = rr_surfer.get_status('80-42762186')
	# rr_surfer.download_file('80-42762186', config.dir_to_download)

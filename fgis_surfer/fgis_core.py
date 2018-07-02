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


# главный класс инициализирует соединение, логинится и получает список элементов меню
class RRSurfer:

	def __init__(self, token):
		self.token = token

	def init_driver(self):
		self.driver = webdriver.PhantomJS() # инициализация веб-драйвера
		self.driver.set_window_size(840, 480)
		self.driver.get(config.rr_url) # открытие url

		self.login() # авторизация фгис по токену

		utils.sleep()

		# получение элеменов меню
		menu_links = self.driver.find_elements_by_class_name(constants.menu_link_class)
		self.menu_search = menu_links[0]
		self.menu_orders = menu_links[1]
		self.menu_request_owner = menu_links[2]
		self.menu_my_account = menu_links[3]

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
		order_num = ordering.order_document(self.driver, self.menu_search, cad_num)
		return order_num

	def get_status(self, order_num):
		self.init_driver() # инициализация драйвера на каждую из операций, т.к. нож в печень- токен не вечен.
		status_text = checking_status.check_status(self.driver, self.menu_orders, order_num)
		return status_text

	def download_file(self, order_num):
		self.init_driver()
		result_download = downloading.download(self.driver, self.menu_orders, order_num)
		return result_download


if __name__ == '__main__':
	rr_surfer = RRSurfer(config.token)
	# order_num = rr_surfer.order_document('36:21:0100042:35')
	status_text = rr_surfer.get_status('80-42762186')
	# rr_surfer.download_file('80-42762186', config.dir_to_download)

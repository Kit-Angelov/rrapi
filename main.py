from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import os
from app import config
from app import utils
from app import constants


# главный класс инициализирует соединение, логинится и получает список элементов меню
class RRSurfer:

	def __init__(self, token):
		self.token = token
		self.driver = webdriver.PhantomJS() # инициализация веб-драйвера
		self.driver.get(config.rr_url) # открытие url

		self.login() # авторизация фгис по токену

		utils.sleep()

		# получение элеменов меню
		menu_links = self.driver.find_elements_by_class_name(constants.menu_link_class)
		self.search_objects = menu_links[0]
		self.orders = menu_links[1]
		self.request_owner = menu_links[2]
		self.my_account = menu_links[3]

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
	def search_object(self, cad_num):
		# переход в раздел поиска документа
		search_objects.click()

		utils.sleep()

		# ввод кад.номера и региона и поиск документа
		cad_num_input = driver.find_element_by_class_name(constants.textfield_class)
		cad_num_input.send_keys('36:21:0100042:35')

		utils.sleep(5)

		region_input = driver.find_element_by_class_name(constants.filterselect_input_class)
		region_input.send_keys('Воронежская область')

		utils.sleep(2)

		region_popup_elems = driver.find_elements_by_class_name(constants.popup_class)
		region_popup_elems[0].click()

		search_buttons = driver.find_elements_by_class_name(constants.button_class)
		search_buttons[5].click()

		utils.sleep()

		# получени результата поиска (1ый результат)
		table_result_rows = driver.find_elements_by_class_name(constants.table_cell_cad_num_class)
		table_result_rows[0].click()

		utils.sleep()

		# заказываем документ
		create_order_buttons = driver.find_elements_by_class_name(constants.button_class)
		# create_order_buttons[4].click() !!!!!uncomment

		utils.sleep(5)

		# получение номера заявки
		order_num_elems = driver.find_elements_by_class_name(constants.order_num_class)[3]
		order_num = order_num_elems.find_element_by_tag_name('b').text
		print('Номер заявки', order_num)

if __name__ == '__main__':
	rr_surfer = RRSurfer(config.token)

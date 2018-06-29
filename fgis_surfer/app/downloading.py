import os
from . import utils
from . import constants
from . import config
import requests

def download(driver, menu_orders, order_num):
	# переходим в раздел поиска документов
	menu_orders.click()
	utils.sleep(10)

	# поиск запроса по номеру
	search_order_field = driver.find_elements_by_class_name(constants.textfield_class)[0]
	search_order_field.send_keys(order_num)

	utils.sleep(2)

	search_order_button = driver.find_elements_by_class_name(constants.button_class)[5]
	search_order_button.click()

	utils.sleep(2)

	# список запросов на выписки
	table_elem = driver.find_element_by_class_name(constants.table_order_class)
	object_list = table_elem.find_elements_by_tag_name('tr')
	object_item = object_list[0].find_elements_by_class_name(constants.table_order_cell_class)[2]

	print(object_item.text)
	link_elem = object_list[0].find_element_by_tag_name('a')

	link = link_elem.get_attribute('href')
	print('link', link)

	session = requests.Session()
	cookies = driver.get_cookies()
	for cookie in cookies: 
	    session.cookies.set(cookie['name'], cookie['value'])
	response = session.get(link)

	if os.path.isdir(dir_to_download) is False:
		os.mkdir(dir_to_download)
	name_file = '{0}{1}'.format(str(order_num), '.zip')
	path_to_download = os.path.join(dir_to_download, name_file)

	if response.status_code == 200:
	    with open(path_to_download, 'wb') as f:
	        f.write(response.content)


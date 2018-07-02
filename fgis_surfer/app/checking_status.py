import os
from . import utils
from . import constants
from .config import status_dict

def check_status(driver, menu_orders, order_num):
	# переходим в раздел поиска документов
	menu_orders.click()
	utils.sleep(10)

	# поиск запроса по номеру
	search_order_field = driver.find_elements_by_class_name(constants.textfield_class)[0]
	search_order_field.send_keys(order_num)

	utils.sleep()

	search_order_button = driver.find_elements_by_class_name(constants.button_class)[5]
	search_order_button.click()

	utils.sleep()

	# список запросов на выписки
	table_elem = driver.find_element_by_class_name(constants.table_order_class)
	object_list = table_elem.find_elements_by_tag_name('tr')
	object_item = object_list[0].find_elements_by_class_name(constants.table_order_cell_class)[2]

	print(object_item.text)
	status_text = str(object_item.text).lower()
	status_code = status_dict.get(status_text, None)
	if status_code is None:
		return status_dict['another']
	else:
		return status_code
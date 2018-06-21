import os
from . import utils
from . import constants

def check_status(driver, menu_orders, order_num):
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
	return object_item.text
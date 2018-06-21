import os
from . import utils
from . import constants

def order_document(driver, menu_search, cad_num):
		# переход в раздел поиска документа
		menu_search.click()

		utils.sleep()

		# ввод кад.номера и региона и поиск документа
		cad_num_input = driver.find_element_by_class_name(constants.textfield_class)
		cad_num_input.send_keys(cad_num)

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
		create_order_buttons = driver.find_elements_by_class_name(constants.button_class)[4]
		create_order_buttons.click()

		utils.sleep(5)

		# # получение номера заявки
		order_num_elem = driver.find_elements_by_class_name(constants.order_num_class)[3]
		order_num = order_num_elem.find_element_by_tag_name('b').text
		return order_num
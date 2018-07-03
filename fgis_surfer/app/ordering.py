import os
from . import utils
from . import constants
import logging

def order_document(driver, menu_search, cad_num):
	logger = logging.getLogger('order.fgis_core.ordering')
	logger.info('[START] Start ordering document: {}'.format(str(cad_num)))
	# переход в раздел поиска документа
	menu_search.click()

	logger.info('search doc click')
	utils.sleep()

	# ввод кад.номера и региона и поиск документа
	cad_num_input = driver.find_element_by_class_name(constants.textfield_class)
	cad_num_input.send_keys(cad_num)

	logger.info('cad num input')

	utils.sleep(5)

	region_input = driver.find_element_by_class_name(constants.filterselect_input_class)
	region_input.send_keys('Воронежская область')

	logger.info('region input')

	utils.sleep(2)

	region_popup_elems = driver.find_elements_by_class_name(constants.popup_class)

	logger.info('getting popup elems')

	region_popup_elems[0].click()

	logger.info('click opup elem')

	search_buttons = driver.find_elements_by_class_name(constants.button_class)

	logger.info('getting search button')

	search_buttons[5].click()

	logger.info('click search button')

	utils.sleep()

	# получени результата поиска (1ый результат)
	try:
		table_result_rows = driver.find_elements_by_class_name(constants.table_cell_cad_num_class)[0]
	except Exception as e:
		self.logger.error('[ERROR] Error ordering document: {}'.format(str(cad_num)))
		return {'error': 'no result for search doc', 'code': 100}

	table_result_rows.click()

	utils.sleep()

	# заказываем документ
	create_order_buttons = driver.find_elements_by_class_name(constants.button_class)[4]

	create_order_buttons.click()

	utils.sleep(5)

	# получение номера заявки
	order_num_elem = driver.find_elements_by_class_name(constants.order_num_class)[3]
	order_num = order_num_elem.find_element_by_tag_name('b').text

	if order_num is not None:
		logger.info('[FINISH] Finish ordering document: {}'.format(str(cad_num)))
		return {'error': None, 'order_num': order_num}
	else:
		self.logger.error('[ERROR] Error ordering document: {}'.format(str(cad_num)))
		return {'error': 'ordering error', 'code': '200'}
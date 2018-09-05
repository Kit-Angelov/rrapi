import os
from . import utils
from . import constants
import logging
from .regions import REGIONS

# функция оформления заявки, примает обьект драйвера, обьект пункта меню и кадастровый номер.
def order_document(driver, menu_search, cad_num):
	logger = logging.getLogger('order.fgis_core.ordering')
	logger.info('[START] Start ordering document: {}'.format(str(cad_num)))
	# переход в раздел поиска документа
	menu_search.click()

	# ввод кад.номера и региона и поиск документа
	cad_num_input = utils.limiter(driver.find_element_by_class_name, constants.textfield_class)
	cad_num_input.send_keys(cad_num)

	region_input = utils.limiter(driver.find_element_by_class_name, constants.filterselect_input_class)

	region_code = cad_num[:2]
	region_name = REGIONS.get(str(region_code), None)
	if region_name is None:
		logger.error("invalid region code")
		return {'error': 'invalid region code'}

	logger.error("region name: {}".format(str(region_name)))
	region_input.send_keys(region_name)

	region_popup_elems = utils.limiter(driver.find_elements_by_class_name, constants.popup_class)

	region_popup_elems[0].click()

	search_buttons = utils.limiter(driver.find_elements_by_class_name, constants.button_class)

	search_buttons[5].click()

	# получени результата поиска (1ый результат)
	try:
		table_result_rows = utils.limiter(driver.find_elements_by_class_name, constants.table_cell_cad_num_class, 0)
	except Exception as e:
		logger.error('[ERROR] Error ordering document: {}'.format(str(cad_num)))
		return {'error': 'no result for search doc'}

	table_result_rows.click()

	# заказываем документ
	create_order_buttons = utils.limiter(driver.find_elements_by_class_name, constants.button_class, 4)

	create_order_buttons.click()

	# получение номера заявки
	order_num_elem = utils.limiter(driver.find_elements_by_class_name, constants.order_num_class, 3)
	order_num = order_num_elem.find_element_by_tag_name('b').text

	if order_num is not None:
		logger.info('[FINISH] Finish ordering document: {}'.format(str(cad_num)))
		return {'error': None, 'order_num': order_num}
	else:
		logger.error('[ERROR] Error ordering document: {}'.format(str(cad_num)))
		return {'error': 'ordering error'}
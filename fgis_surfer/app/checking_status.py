import os
from . import utils
from . import constants
from .config import status_dict
import logging

def check_status(driver, menu_orders, order_num):
	logger = logging.getLogger('status.fgis_core.checking_status')

	logger.info('[START] Start checking status order: {}'.format(str(order_num)))

	# переходим в раздел поиска документов
	menu_orders.click()
	logger.info('menu orders click')
	utils.sleep(15)

	# поиск запроса по номеру
	search_order_field = driver.find_elements_by_class_name(constants.textfield_class)[0]
	logger.info('getting search order field')
	search_order_field.send_keys(order_num)
	logger.info('fill search order field')
	utils.sleep()

	search_order_button = driver.find_elements_by_class_name(constants.button_class)[5]
	logger.info('getting search order button')
	search_order_button.click()
	logger.info('search order button click')

	utils.sleep()

	# список запросов на выписки
	table_elem = driver.find_element_by_class_name(constants.table_order_class)
	try:
		object_list = table_elem.find_elements_by_tag_name('tr')
		object_item = object_list[0].find_elements_by_class_name(constants.table_order_cell_class)[2]
		logger.info('getting object item')
	except Exception as e:
		logger.error('[ERROR] checking status order: {}'.format(str(order_num)))
		return {'error': 'no order for check status', 'code': 100}

	logger.info('order status {}'.format(str(object_item.text)))
	status_text = str(object_item.text).lower()
	status_code = status_dict.get(status_text, 600)
	if status_code is not None:
		logger.info('[FINISH] Finish checking status order: {}'.format(str(order_num)))
		return {'error': None, 'status': status_code}
	else:
		logger.error('[ERROR] checking status order: {}'.format(str(order_num)))
		return {'error': 'checking status error', 'code': '200'}
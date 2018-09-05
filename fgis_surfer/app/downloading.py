import os
from . import utils
from . import constants
from . import config
import requests
import uuid
import logging

# функция скачивания документа выполненой заявки, принимает обьект драйвера, обьект пунка меню и номер заявки
def download(driver, menu_orders, order_num):
	logger = logging.getLogger('download.fgis_core.downloading')

	logger.info('[START] Start downloading doc: {}'.format(str(order_num)))

	# переходим в раздел поиска документов
	menu_orders.click()

	# поиск запроса по номеру
	search_order_field = utils.limiter(driver.find_elements_by_class_name, constants.textfield_class, 0)
	search_order_field.send_keys(order_num)

	search_order_button = utils.limiter(driver.find_elements_by_class_name, constants.button_class, 5)
	search_order_button.click()

	# список запросов на выписки
	table_elem = utils.limiter(driver.find_element_by_class_name, constants.table_order_class)
	try:
		object_list = table_elem.find_elements_by_tag_name('tr')
		object_item = object_list[0].find_elements_by_class_name(constants.table_order_cell_class)[2]

		link_elem = object_list[0].find_element_by_tag_name('a')

		link = link_elem.get_attribute('href')
	except Exception as e:
		logger.error('[ERROR] downloading doc: {}'.format(str(order_num)))
		return {'error': 'no order for downloading'}

	session = requests.Session()
	cookies = driver.get_cookies()
	for cookie in cookies: 
	    session.cookies.set(cookie['name'], cookie['value'])
	response = session.get(link)

	dir_to_download = os.path.join(config.dir_to_ftp, config.media_path)
	if os.path.isdir(dir_to_download) is False:
		os.mkdir(dir_to_download)

	inter_dir = str(uuid.uuid4())[:2]
	inter_path = os.path.join(dir_to_download, inter_dir)
	if os.path.isdir(inter_path) is False:
		os.mkdir(inter_path)

	name_file = '{0}{1}'.format(str(order_num), '.zip')
	path_to_download = os.path.join(inter_path, name_file) # абсолютный путь
	rel_path_to_download = os.path.join(config.media_path, inter_dir, name_file) # относительный путь

	if response.status_code == 200:
		with open(path_to_download, 'wb') as f:
			f.write(response.content)
		logger.info('[FINISH] Finish downloading doc: {}'.format(str(order_num)))
		return {'error': None, 'path_to_download': rel_path_to_download}
	else:
		logger.error('[ERROR] downloading doc: {}'.format(str(order_num)))
		return {'error': 'status_code {}'.format(str(response.status_code))}

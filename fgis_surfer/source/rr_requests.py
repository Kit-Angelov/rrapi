from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import os
import time
import requests
import shutil

token = "1d9deb88-8d5f-40a4-a58e-b9520430d053"
token_list = token.split("-")

order_num = '80-42664140'

screen_index = 0
screen_path = 'screens_requests'

if os.path.isdir(screen_path) is False:
	os.mkdir(screen_path)

# слип чтобы все успелово заполняться и нажиматься
def sleep(k=1):
	time.sleep(1*k)

# скрины чтобы отслеживать визульно ход выполенения скрипта
def make_screen(driver):
	global screen_index
	driver.save_screenshot(os.path.join(screen_path,'rr_screen_{}.png'.format(screen_index)))
	screen_index += 1

"""
    Селекторы эелеменов HTML
"""

# login page
token_input_class = 'v-textfield'
enter_button_class = 'v-button-caption'

# after login
menu_link_class = 'v-button-link'

# search objects
cad_num_input_class = 'v-textfield'
region_input_class = 'v-filterselect-input'
region_popup_class = 'gwt-MenuItem'
popup_open_class = 'v-filterselect-button'
search_button_class = 'v-button-caption'

# result search
table_row_cadnum_class = 'v-table-cell-content-cadastral_num'
create_order_button_class = 'v-button-caption'

# list objects
# object_list_class = 'v-link'
object_list_class = 'v-table-row-odd'
search_order_class = 'v-textfield'
table_orders_class = 'v-table-table'
table_cell_class = 'v-table-cell-content'

# URL 
rr_url = 'https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn'

# Logic
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768)
driver.get(rr_url)

# Заполнение токена в поля (последовательно без цикла)
token_input_list = driver.find_elements_by_class_name(token_input_class)

token_input_list[0].send_keys(token_list[0])
sleep()
token_input_list[1].send_keys(token_list[1])
sleep()
token_input_list[2].send_keys(token_list[2])
sleep()
token_input_list[3].send_keys(token_list[3])
sleep()
token_input_list[4].send_keys(token_list[4])
sleep()

make_screen(driver)

# нажатие кнопки вход
enter_but = driver.find_element_by_class_name(enter_button_class)
enter_but.click()
sleep()

make_screen(driver)

# получаем пункты меню
menu_links = driver.find_elements_by_class_name(menu_link_class)

search_objects = menu_links[0]
orders = menu_links[1]
request_owner = menu_links[2]
my_account = menu_links[3]

# переходим в раздел поиска документов
orders.click()
# sleep(10)

def limiter(func, param, ident=None):
	before = time.time()
	def execute():
		try:
			result = func(param)
			print(result)
			if ident is not None:
				result = result[ident] #  driver.find_elements_by_class_name(search_order_class)[0]
			return result
		except Exception as e:
			print("NO")
			after = time.time()
			print(after - before)
			if (after - before) > 30:
				return None
			return execute()
	return execute()

search_order_field = limiter(driver.find_elements_by_class_name, search_order_class, 0)

make_screen(driver)

search_order_field.send_keys(order_num)

sleep(2)
make_screen(driver)

# search_order_button = driver.find_elements_by_class_name(search_button_class)[5]
# search_order_button.click()

# sleep(2)
# make_screen(driver)

# # список запросов на выписки
# table_elem = driver.find_element_by_class_name(table_orders_class)
# object_list = table_elem.find_elements_by_tag_name('tr')
# print('len obj list', len(object_list))
# object_item = object_list[0].find_elements_by_class_name(table_cell_class)[2]

# print(object_item.text)
# link_elem = object_list[0].find_element_by_tag_name('a')

# link = link_elem.get_attribute('href')
# print('link', link)

# sleep(5)
# make_screen(driver)

# session = requests.Session()
# cookies = driver.get_cookies()
# for cookie in cookies: 
#     session.cookies.set(cookie['name'], cookie['value'])
# response = session.get(link)

# path_to_download = 'doc.zip'
# if response.status_code == 200:
#     with open(path_to_download, 'wb') as f:
#         f.write(response.content)


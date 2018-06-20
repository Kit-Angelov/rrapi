from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import os
import time

token = "1d9deb88-8d5f-40a4-a58e-b9520430d053"
token_list = token.split("-")

screen_index = 0
screen_path = 'screens_search'

if os.path.isdir(screen_path) is False:
	os.mkdir(screen_path)
# слип чтобы все успелово заполняться и нажиматься
def sleep(k=1):
	time.sleep(1*k)

# скрины чтобы отслеживать визульно ход выполенения скрипта
def make_screen():
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

# result_ordering
order_num_class = 'v-label-undef-w'

# URL 
rr_url = 'https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn'

# Logic
driver = webdriver.PhantomJS()
# chrome_options = Options()
# chrome_options.add_argument("--binary_location=/home")
# chrome_options.add_argument("--headless") 
# chrome_options.add_argument("--window-size=1024x768")
# chrome_driver = 'chromedriver.exe'
# driver = webdriver.Chrome('/home/kit/projects/seleniumTest/chromedriver')
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

make_screen()

# нажатие кнопки вход
enter_but = driver.find_element_by_class_name(enter_button_class)
enter_but.click()
sleep()

make_screen()

# получаем пункты меню
menu_links = driver.find_elements_by_class_name(menu_link_class)

search_objects = menu_links[0]
orders = menu_links[1]
request_owner = menu_links[2]
my_account = menu_links[3]

# переходим в раздел поиска документов
search_objects.click()
sleep()

make_screen()

# вводим в поле кад.номер номер искомого обьекта
cad_num_input = driver.find_element_by_class_name(cad_num_input_class)
# cad_num_input.send_keys('36:32:0100024:0018')
cad_num_input.send_keys('36:21:0100042:35')
sleep(5)
# вводим регион
region_input = driver.find_element_by_class_name(region_input_class)
region_input.send_keys('Воронежская область')
#region_input.send_keys(Keys.ENTER)
sleep(2)
make_screen()

region_popup_class = driver.find_elements_by_class_name(region_popup_class)
print(len(region_popup_class))
region_popup_class[0].click()

# жмем кнопку поиска документа
search_buttons = driver.find_elements_by_class_name(search_button_class)
print(len(search_buttons))
# popup_open_list = driver.find_elements_by_class_name(popup_open_class)
# print(len(popup_open_list))
# popup_open_list[0].click()

sleep(5)
search_buttons[5].click()

sleep(5)
make_screen()

# выбираем и кликаем по первому результату поиска
table_result_rows = driver.find_elements_by_class_name(table_row_cadnum_class)
table_result_rows[0].click()

sleep()
make_screen()

# заказываем документ
create_order_buttons = driver.find_elements_by_class_name(create_order_button_class)
create_order_buttons[4].click()

sleep(5)
make_screen()

order_num_elems = driver.find_elements_by_class_name(order_num_class)[3]
order_num = order_num_elems.find_element_by_tag_name('b').text

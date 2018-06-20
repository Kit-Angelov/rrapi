import time
from .config import token
from .constants import *

def sleep(k=1):
	time.sleep(1*k)

def login(driver):
	token_list = token.split("-")
	token_input_list = driver.find_elements_by_class_name(textfield_class)
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
	enter_but = driver.find_element_by_class_name(constants.button_class)
	enter_but.click()
import os

token = ""
rr_url = 'https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn'
base_dir = os.getcwd()
dir_to_ftp = '/home/ftpuser'
media_path = 'media'

# checking status
status_dict = {
	'на проверке': 200,
	'в работе': 300,
	'завершена': 400,
	'проверка не пройдена': 500
}
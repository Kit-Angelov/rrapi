import os

token = "" # токен фгис
rr_url = 'https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn' # юрл к сервису фгис росреестра
base_dir = os.getcwd() # базовая директория
dir_to_ftp = '/home/ftpuser' # путь до фтп папки
media_path = 'media' # путь до медии

# статусы фгис: код статуса в нашей системе
status_dict = {
	'на проверке': 200,
	'создана': 300,
	'в работе': 300,
	'завершена': 400,
	'проверка не пройдена': 500
}
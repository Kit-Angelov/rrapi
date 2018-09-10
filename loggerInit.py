import logging
import logging.config
from settings import other_param
import os

def init_logger(mode, env):
	logger_name = str(mode)

	BASE_DIR = os.path.dirname(__file__)  #Базовая директория приложения
 
	LOG_DIR = os.path.join(BASE_DIR, 'logs', logger_name)  # Директория с файлами логов

	if os.path.exists(LOG_DIR) is False:
		os.makedirs(LOG_DIR)

	dictLogConfig = {
	    'version': 1,
	    'disable_existing_loggers': True,
	 
	    'formatters': {
	        'console_and_file': {
	            'format': '[%(asctime)s][%(levelname)s] %(name)s '
	                      '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
	            'datefmt': '%H:%M:%S',
	            },
	        },
	 
	    'handlers': {
	        'console': {                           # обработчик логов для вывода в консоль
	            'level': 'DEBUG',
	            'class': 'logging.StreamHandler',
	            'formatter': 'console_and_file'
	        },
	        'file_error': {                        # обработчик логов с ошибками для записи в файл error.log
	            'level': 'ERROR',
	            'class': 'logging.FileHandler',
	            'formatter': 'console_and_file',
	            'filename': os.path.join(LOG_DIR, 'error.log')
	        },
	        'file_info': {                         # обработчик логов с общей информацией для записи в файл info.log
	            'level': 'INFO',
	            'class': 'logging.FileHandler',
	            'formatter': 'console_and_file',
	            'filename': os.path.join(LOG_DIR, 'info.log')
	        },
	        'sentry': {                            # обработчик логов для отправки в облачное приложения ведения логов sentry.io
	            'level': 'INFO',
	            'class': 'raven.handlers.logging.SentryHandler',
	            'dsn': other_param[env]['SENTRY_DSN'],
	            },
	        },
	 
	    'loggers': {
	        '': {
	            'handlers': ['console', 'sentry', 'file_info', 'file_error'],
	            'level': 'DEBUG',
	            'propagate': False,
	            },
	    }
	}

	logging.config.dictConfig(dictLogConfig)
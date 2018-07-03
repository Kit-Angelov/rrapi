import logging
import logging.config

def init_logger(mode):
	logger_name = str(mode)

	dictLogConfig = {
		"version":1,
		"handlers":{
				"fileHandler":{
					"class":"logging.FileHandler",
					"formatter":"myFormatter",
					"filename":"{}.log".format(logger_name)
				},
				"consoleHandler": {
					"class": "logging.StreamHandler",
					"formatter": "myFormatter",
				}
			},
			"loggers":{
				logger_name:{
					"handlers":["fileHandler", "consoleHandler"],
					"level":"INFO",
				}
			},
			"formatters":{
				"myFormatter":{
					"format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
				}
		}
	}

	logging.config.dictConfig(dictLogConfig)
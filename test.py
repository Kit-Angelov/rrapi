import types
import time
from loggerInit import init_logger
import logging

init_logger('order')
logger = logging.getLogger('order')
logger.info('log test ok')
logger_module = logging.getLogger('module')
logger_module.error('wersdf')

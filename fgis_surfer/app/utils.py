import time
from .config import time_limit

# функция возвращающая слип в к-секунд
def sleep(k=1):
	time.sleep(1*k)


def limiter(func, param, ident=None):
	before = time.time()
	def execute():
		try:
			result = func(param)
			print(result)
			if ident is not None:
				result = result[ident]
			return result
		except Exception as e:
			after = time.time()
			if (after - before) > time_limit:
				return None
			return execute()
	return execute()
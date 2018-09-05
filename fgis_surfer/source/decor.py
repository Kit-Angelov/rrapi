import time

def limiter(func_to_decor):
	def calc_limit():
		before = time.time()
		try:
			a = func_to_decor()[9]
		except:
			a = func_to_decor()
		after = time.time()
		print(after - before)
	return calc_limit

@limiter
def func():
	a = [2,3,6,7,8]
	print("sleep")
	time.sleep(2)
	return a

func()



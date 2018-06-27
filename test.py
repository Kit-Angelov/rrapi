class Test:

	def __init__(self):
		self.methods = {
			'first': self.first,
			'second': self.second
		}

	def first(self):
		print('first ok')

	def second(self):
		print('second ok')

	def run(self, method):
		if method in self.methods:
			run_method = self.methods[method]
			run_method()

if __name__ == '__main__':
	t = Test()
	t.run('second')
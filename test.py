import types
import time

def b(**data):
	print('b:', data)

def a(**data):
	print(data)
	b(**data)

a(e=4, d=5)
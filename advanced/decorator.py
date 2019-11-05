from inspect import getsource, getfile
from time import time

def timer(func):
	def f(*args, **kwargs):
		before = time()
		rv = func(*args, **kwargs)
		after = time()
		print('elapsed', after - before)
		return rv
	return f
@timer
def add(x=5,y=10):
	return x+y
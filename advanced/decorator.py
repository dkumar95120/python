from functools import wraps
from inspect import getsource, getfile
from time import time

def timer(func):
	@wraps(func)
	def f(*args, **kwargs):
		before = time()
		rv = func(*args, **kwargs)
		after = time()
		print('elapsed', after - before)
		return rv
	return f
@timer
def add(x=5,y=10):
	'adds two numbers'
	return x+y

class Trace:
	def __init__(self):
		self.enabled = True

	def __call__(self,f):
		@wraps(f)
		def wrap (*args, **kwargs):
			if self.enabled:
				print('Calling {}'.format(f.__name__))
			return f(*args, **kwargs)
		return wrap

tracer = Trace()

@tracer
def rotate_list(l):
	'rotate given list from left'
	return l[1:] + [l[0]]

l = [1,2,3,4]
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
tracer.enabled = False
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)



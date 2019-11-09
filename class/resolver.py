import socket
from functools import wraps
from time import time

def timeit(f):
	def timed(*args, **kwargs):
		ts = time()
		result = f(*args, **kwargs)
		te = time()
		print ('{}({} {}) took {:f} sec'.format(f.__name__, args, kwargs, te-ts))
		return result
	return timed

class Resolver:
	def __init__(self):
		self._cache = {}

	@timeit
	def __call__(self, host):
		if host not in self._cache:
			self._cache[host] = socket.gethostbyname(host)
		return self._cache[host]

	def clear(self):
		self._cache.clear()


resolve = Resolver()
print(resolve('google.com'))
print(resolve.__call__('google.com'))
print(resolve._cache)
print(resolve('yahoo.com'))
print(resolve._cache)
print(resolve('yahoo.com'))
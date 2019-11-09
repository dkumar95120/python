def exp(x):
	def topow(y):
		return pow(y,x)
	return topow

square = exp(2)
cube = exp(3)

[print(n, 'square =', square(n)) for n in range(2,10)]
[print(n, 'cube =', cube(n)) for n in range(2,10)]

from time import time, sleep
def make_timer():
	last_called = None

	def elapsed():
		nonlocal last_called
		now = time()
		if last_called is None:
			last_called = now
			return None
		result = now - last_called
		last_called = now
		return result

	return elapsed

t1 = make_timer()
print(t1())
sleep(2)
print(t1())
sleep(5)
print(t1())

t2 = make_timer()
print(t2())
sleep(10)
print(t2())
sleep(15)
print(t2())

import inspect
x = 8
isinstance(x, int)
dir(x)
getattr(x, 'denominator')
hasattr(x, 'index')
globals()
locals()
inspect.ismodule(inspect)
dir(inspect)
def add(x=0, y=0):
	return x+y
sig = inspect.signature(add)
print(sig)
inspect.getsource(add)
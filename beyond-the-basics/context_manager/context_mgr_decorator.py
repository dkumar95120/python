import contextlib

@contextlib.contextmanager
def my_context_manager():
	# Enter
	try:
		yield [value]
		# <Normal Exit>
	except:
		# <Exceptional exit>
		raise #optional if you want to propagate exception
		
with my_context_manager() as x:
	# ...


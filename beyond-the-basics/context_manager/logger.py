# context manager implements
# __enter__()
# __exit__() : propagates exceptions occured within the with block by default
#              unless it returns True 
# see pep-0343 for more details 
# specified by the following statement
# with context_manager as x
import contextlib
import sys

@contextlib.contextmanager
def LoggingContextManager():
	print('LoggingContextManager: enter')
	try:
		yield 'You are in a with-block'
		print('LoggingContextManager: normal exit')

	except:
		print('LoggingContextManager: Exception detected!', sys.exc_info())

with LoggingContextManager() as x:
	print(x)

with LoggingContextManager() as x:
	raise ValueError('Something went wrong')
	print(x)

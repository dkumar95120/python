def hypervolume(length, *lengths):
	v = length
	for item in lengths:
		v *= item
	return v

print(hypervolume(5))
print(hypervolume(3,5))
print(hypervolume(3,5,7))
print(hypervolume(3,5,7,9))

def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
	print(arg1)
	print(arg2)
	print(args)
	print(kwarg1)
	print(kwarg2)
	print(kwargs)

print_args(1,2,3,4,5, kwarg1=6, kwarg2=7, kwargs3=8, kwarg4=9)
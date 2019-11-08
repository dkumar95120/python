import registry

registry.register('my name')
for name in registry.registered_names():
	print (name)

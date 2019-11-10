from random import random
from itertools import islice
from datetime import datetime
from time import sleep

class Sensor:
	def __iter__(self):
		return self

	def __next__(self):
		return random()

sensor = Sensor()
timestamps = iter(datetime.now, None)

for stamp, value in islice(zip(timestamps, sensor), 10):
	print(stamp, value)
	sleep(1)

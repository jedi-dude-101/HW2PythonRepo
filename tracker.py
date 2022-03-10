def func_counter(func):
	global counter
	counter=0
	def funcy(y):
		func(y)
		global counter
		counter+=1
	return funcy


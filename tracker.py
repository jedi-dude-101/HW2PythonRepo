def func_counter(func):
	def funcy(*args, **kwargs):
		funcy.counter+=1
		return func(*args, **kwargs)
	funcy.counter=0
	return funcy

@func_counter
def potato(y):
	return y+2**3-34


def func_counter(func):
	global counter
	counter=0
	def funcy(y):
		func(y)
		global counter
		counter+=1
	return funcy
@func_counter
def foo(y):
	return y+2*3-34
y=20
foo(y)
foo(y)
print(counter)

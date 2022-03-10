def doubler(func):
	def double():
		func()
		func()
	return double
@doubler
def talk():
	print("bork")
talk()

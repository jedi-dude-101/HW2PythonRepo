def doubler(func):
	func()
	func()
def talk():
	print("bork")
doubler(talk)

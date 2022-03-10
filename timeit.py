import time
def calculate_time(func):
	start=time.time()
	func()
	end=time.time()
	xtime=end-start
	print(f'Total time {xtime}')
def testerfunc():
	total=0
	for i in range(100):
		total+=i
calculate_time(testerfunc)

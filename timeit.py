import time
def calculate_time(func):
	def timeit():
		start=time.time()
		func()
		end=time.time()
		xtime=end-start
		print(f'Total time {xtime}')
	return timeit
@calculate_time
def testerfunc():
	total=0
	for i in range(100):
		total+=i
testerfunc()

class Test:
	def __init__(self,*a):
		print('variable length arg')
t=Test()
t1=Test(10,20)
t2=Test(10,20,30)
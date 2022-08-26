class Test():
	def sum(self,*a):
		total=0
		for i in a:
			total=total+i 
		print(total)
t=Test()
t.sum(10,20,30,40,50)
t.sum(10,20,30)
t.sum(10,20)
t.sum(10)

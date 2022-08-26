class Test:
	def sum(self,a=None,b=None,c=None):
		if a!=None and b!=None and c!=None:
			result=a+b+c
			print(result) 
		elif a!=None and b!=None:
			result=a+b
			print(result)
		else:
			print('provide at least 2 or 3 argument')
t=Test()
t.sum(10,20,30)
t.sum(10,20)


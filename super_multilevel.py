class A:
	def m1(self):
		print('A class')

class B(A):
	def m1(self):
		print('B class')

class C(B):
	def m1(self):
		B.m1(self)                # calling B class method 
		#print('C class')

class D(C):
	pass

class E(D):
	def m1(self):
		super(C,self).m1()  # here we calling C class super method ans(b class)  
							#here get the parent of the c class is B

		#print('E class')

a = E()
a.m1()
b = C() 
b.m1()


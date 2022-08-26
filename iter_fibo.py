class fibo:
	def __init__(self,number):
		self.number = number
	
	def __iter__(self):
		self.a = 0
		self.b = 1
		self.n = 0
		return self

	def __next__(self):

		if self.n<=self.number:

			c = self.a + self.b
			self.b = self.a
			
			self.a = c
			
	
			self.n+=1
			return c
		else:
			raise StopIteration

fib = fibo(5)
i = iter(fib)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))



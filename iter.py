
class fabi:
	def __init__(self,num):
		self.num = num

	def __iter__(self):
		self.n = 0
		self.a = 0
		self.b = 1
		return self

	def __next__(self):
		if self.n<=self.num:
			self.c = self.a + self.b
			self.b = self.a
			self.a = self.c
			return self.a
		else:
			raise StopIteration

f = fabi(10)
iterobj = iter(f)

print(next(iterobj))
print(next(iterobj))
print(next(iterobj))
print(next(iterobj))
print(next(iterobj))



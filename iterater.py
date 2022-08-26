class powtow:
	def __init__(self,maxi=0):
		self.maxi = maxi

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n<=self.maxi:
			result = self.n ** 2
			self.n+=1
			return result
		else:
			raise StopIteration


p = powtow(5)
iterobj = iter(p)

# print(next(iterobj))
# print(next(iterobj))
# print(next(iterobj))
# print(next(iterobj))
# print(next(iterobj))

for i in iterobj:
	print(i)
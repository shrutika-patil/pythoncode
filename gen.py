def gen(maxi):

	n = 0

	while n<=maxi:
		yield 2**n
		n+=1


i = gen(10)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))







def fibo(maxi):

	n = 0
	a = 0
	b = 1

	while n<=maxi:
		c = a + b
		b=a
		a=c
		yield c
		n+=1



fib = fibo(8)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


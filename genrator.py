
def powtow(a=0):

	n = 0
	while n<a:
		yield 2**n 
		n+=1
p=powtow(10)	
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
gen=PowTwoGen(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

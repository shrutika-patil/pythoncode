def fabo(num):
	n = 0
	a=0 
	b=1

	while n<num:
		c=a+b
		b = a
		a = c
		yield b 
		n+=1

i = fabo(10)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


# for fibo in i:
# 	print(fibo)


# using even 

def even():
	n=0
	while True:
		yield n
		n+=2	

i = even()
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i)) 
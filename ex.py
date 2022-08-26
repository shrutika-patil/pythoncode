# def even(eve):
	
# 	n=1

# 	print('frist')
# 	yield n
# 	n+=1


# 	print('second')
# 	yield n
# 	n+=1
# e= even(10)
# print(next(e))
# print(next(e))

def even_number(eve):
	n=2

	while n<=eve:

		yield n
		n+=2
c=even_number(10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
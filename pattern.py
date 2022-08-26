# Q Python Program to Create Pyramid Patterns

r=int(input('Enter the row number: '))

for i in range(1,r+1):
	print(' * ' * r)
	print(' ' * (i),end='')
	r=r-1
	

	
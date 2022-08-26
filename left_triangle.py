#Q. Write a program to dispaly *s in left angled triangled form

n=int(input('Enter the number: '))

for i in range(1,n+1):
	print(' ' * (n-i),end='')

	print('*' * i)



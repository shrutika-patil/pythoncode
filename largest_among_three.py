# Q Python Program to Find the Largest Among Three Numbers

#Take Three value from user

a=int(input('Enter the number1 : '))
b=int(input('Enter the number2 : '))
c=int(input('Enter the number3 : '))

if a>b and a>c:
	print('The given three number a is {0} large number'.format(a))
elif b>c:
	print('The given three number b is {0} large number'.format(b))
else:
	print('The given three number c is {0} large number'.format(c))
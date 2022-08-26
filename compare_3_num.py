#Q. Write a programn to find smallest check whether of given 3 numbers?

# user input

a=int(input('Enter the number1: '))
b=int(input('Enter the number2: '))
c=int(input('Enter the number3: '))

# use condition statemate if___elif__else

if a<b<c:
	print('The a is {} smallest number'.format(a))
	print(f'The a is {a} smallest number')

elif b<c:
	print('The b is {} smallest number'.format(b))
	print(f'The b is {b} smallest number')

else:
	print('The c is {} smaalest number'.format(c))
	print(f'The c is {c} smallest number')
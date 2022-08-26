# Q Python Program to Check if a Number is Positive, Negative or 0

# Take number from the user

number=int(input('Enter the number : '))

#check the number is positive ,negative or 0
#Here we use the if--elis--else condition

if number>0:
	print('The given number {} is positive'.format(number))

elif 0>number:
	print('The given number {} is negative '.format(number))
else:
	print('The number is {} zero'.format(number))

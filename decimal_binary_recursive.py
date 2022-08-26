# Q Python Program to Convert Decimal to Binary Using Recursion

# USING RECURSIVE

def binary(decimal):

	if decimal>1:
		binary(decimal//2)
	print(decimal%2,end='')
decimal=int(input('Enter the decimal number: '))
print(binary(decimal))
print()


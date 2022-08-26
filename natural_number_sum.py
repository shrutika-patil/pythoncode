# Q Python Program to Find the Sum of Natural Numbers

# using for loop

n=int(input('Enter the n^th number: '))
add=0

if n<0:
	print('number is always positive')

for num in range(1,n+1):
	add=add+num

print(add)


# using while loop

n=int(input('Enter the n^th number: '))
add=0

if n<0:
	print('number is always positive')

while (n>0):
	add=add+n
	n=n-1
print(add)



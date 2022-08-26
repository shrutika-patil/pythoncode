#Q To display the sum of first n numbers

n=int(input('Enter the number: '))
add=0
i=1
while i<=n:

	add=add+i
	i+=1
print(f'The addition of the n number is {add}')
a=input('Enter the number: ')
add=0
for num in a:

	num=int(num)
	
	add=add+num
print(add)



# function

def add(a):
	add=0
	for num in a:

		num=int(num)
	
		add=add+num
	return add
a=input('Enter the number: ')
result=add(a)
print(result)

# while 
a=input('Enter the number: ')
add=0
i=0
while(i<=a):
	add=add+int(i)
	i=i+1
	print(add)


























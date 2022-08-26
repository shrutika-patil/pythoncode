# Q Python Program to Find Armstrong Number in an Interval

lower=int(input('Enter the lower number: '))
upper=int(input('Eter the upper number: '))

for number in range(lower,upper+1):



	order=len(str(number))
	i=1
	add=0
	copy_number=number

	while (number>0):

		digit=number%10
		mul=digit**order
		add=add+mul
	
		number=number//10
	if copy_number==add:
		print(copy_number)



# using for loop

low=int(input('Enter the low number: '))
high=int(input('Enter the high number: '))

lis=[]

for num in range(low,high+1):

	lis.append(num)

	
	for number in lis:
		order=len(str(number))
		add=0

		for i in str(number):
			i=int(i)

			mul=i**order
		

			add=add+mul
	
			
	if number==add:
		print(number)
	

			
	







	


# Q Python Program to Display the multiplication Table

# using while loop

num=int(input('enterb the table number: '))
i=1
table=0
while (i<=10):
	if (i>0):
		table=num*i
		print(table)
	i=i+1



# using for loop

num=int(input('Enter the number: '))

for mul in range(1,11):

	table=num*mul
	print(table)


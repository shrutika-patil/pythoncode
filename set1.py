# Q.Write a program to eliminate duplicates present in the list?

# method 1

'''lis=eval(input('Enter the list of value: '))
set1=set(lis)
print('set1=',set1)'''



# method2

lis=eval(input('Enter the list value: '))
lis1=[]

for unique in lis:
	if unique not in lis1:
		
		lis1.append(unique)
print('lis1= ',lis1)



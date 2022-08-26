# Q Python Program to Reverse a Number

# using for loop 

num=input('Enter the number: ')
num1=('')

for i in num:
	num1=i+num1
print(num1)


#using while loop

num=int(input('Enter the number: '))
copy_num=num
rev=''

while(num>0):
	digit=num%10
	digit=str(digit)
	rev=rev+digit
	num=num//10
print(rev)

# using inbuilt function
num=input('Enter the number: ')
print(num[::-1])



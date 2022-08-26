# Q. Write a function to find factorial of given number?


def factorial(num):

	
	result=1

	while (num>=1):

		result=result*num
		num-=1
	return result
		
num=int(input('Enter the given factorial number: '))
ans=factorial(num)
print('The factorial of {num} is : ',ans)

# using for loop


def fact(num):
	result=1
	for i in range(1,num+1):
		result=i*result
	return result

num=int(input('Enter the given factorial number: '))
fact=fact(num)
print('The factorial of {num} is : ',fact)



# using recursive function


def fact(num):
	if num==0:
		result=1
	else:
		result=num*fact(num-1)
	return result

num=int(input('Enter the which is the factorial num : '))
print('The factorial is: ',fact(5))
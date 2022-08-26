
def fibonacci(a):
	if a==0:
		c=0
	elif a==1:
		c=1
	else:

		c=fibonacci(a-1)+fibonacci(a-2)
		
	return c
a=int(input('Enter the number: '))
print('fibonacci of a is :',fibonacci(a))



def fibo(a):

	if a==0:
		return 0
	elif a==1:
		return 1
	else:
		return fibo(a-1)+fibo(a-2)

a=int(input('Enter the number: '))
print(' the fibonacci of {a} is ',fibo(a))
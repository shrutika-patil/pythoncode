# Q Python Program to Print the Fibonacci sequence

# using for loop

a=1
fib=0

for num in range(0,7):
	print(fib)
	c=a+fib
	fib=a
	a=c
	

#using while loop:
n1=1
n2=0
i=1
while (i<=7):
	if n2<=8:
		print(n2)
		c=n1+n2
		n2=n1
		n1=c
		
	i+=1
	
	



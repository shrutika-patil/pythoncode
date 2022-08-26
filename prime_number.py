# Q Python Program to Check Prime Number

n=int(input('Enter the number: '))

if (n==2):
	print('The given {} is prime '.format(n))
else:
	for number in range(2,n):
		if n % number==0:
			print('The given {} is  not prime '.format(n))
			break
		if (number==(n-1)):
			print('The given {} is prime '.format(n))



#using while loop
n=1

while (n<=30):
	f=0
	i=2
	while i<=(n//2):
		if n%i==0:
			f=f+1	
			break
		i+=1
	if f==0 and n!=1:
		print(n)
	n=n+1
	












	




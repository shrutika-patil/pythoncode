# Q Python program to print prime numbers using while loop


n=1

while(n<=30):
	
	count=0
	i=2

	while i<=(n//2):
		if n%i==0:
			print('n is not prime ',n)
			count=count+1
			break
		i=i+1
	if count==0 and n!=1:
		print('n is prime',n)
	n=n+1
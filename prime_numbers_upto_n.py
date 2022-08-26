# Q Python program to print prime numbers upto n

a=int(input('Enter the number :  ') )
for num in range(1,a+1):
	if num>1:
		for i in range(2,num):
			if num%i==0:
				break
		else:
			print(num,end='')

			print()
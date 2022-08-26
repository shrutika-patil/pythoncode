
def prime(num):
	if num<=1:
		print('Enter the greater number')
	else:
		for number in range(2,num):
			if (num%number==0):
				print('The number is not prime: ',num)
				break

		else:
			print('The number is prime: ',num)

num=int(input('Enter the number: '))

prime(num)



def prime(num):
	count=0
	i=2
	if num<=1:
		print('Enter the greater value')

	while(i<21):
		if num%(i)==0:
			print('The number is not prime',num)
		
			count+=1
			break
		i+=1
	if(num!=1 and count==0):
		print('The number is prime: ',num)
prime(21)




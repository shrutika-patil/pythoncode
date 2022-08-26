# For example: We have two integers 4 and 6. Let's find LCM

#using simple logic
a=in
t(input('Enter the a number: '))
b=int(input('Enter the b number: '))

if a>b:
	greater=a

else:
	greater=b

while(True):
	if((greater%a==0) and (greater%b==0)):
		break
	greater=greater+1

print(f'greater is {greater}')


# using function logic


def calculate_lcm(a,b):

	maxnum=max(a,b)
	while(True):
		if (maxnum%a==0 and maxnum%b==0):
			lcm=maxnum
			break
		maxnum=maxnum+maxnum

	return lcm

a=int(input('Enter the number of a: '))
b=int(input('Enter the number of b: '))

print('the lcm of',a, 'and',b,'is', calculate_lcm(a,b))




# using other way
def calculate_lcd(a,b,c):
	maxnum=max(a,b,c)
	while(True):
		if (maxnum%a==0 and maxnum%b==0 and maxnum%c==0):
			lcd=maxnum
			break
		maxnum+=1

	return lcd
a=int(input('Enter the number of a: '))
b=int(input('Enter the number of b: '))
c=int(input('Enter the number of c: '))

result=calculate_lcd(a,b,c)
print('The lcd of',a,b,'and',c,'is',result)	




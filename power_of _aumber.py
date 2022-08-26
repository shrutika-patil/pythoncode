# Q Python Program to Compute the Power of a Number


# using while loop

base=int(input('Enter the number: '))
exponent=int(input('Enter the exponent: '))
ans=1

while(exponent>0):
	ans=ans*base
	exponent=exponent-1
print(ans)


# using for loop
base=int(input('Enter the number: '))
exponent=int(input('Enter the exponent: '))
ans=1

for i in range(1,exponent+1):
	ans=ans*base

print(ans)


#using inbuilt function

base=int(input('Enter the number: '))
exponent=int(input('Enter the exponent: '))

ans=pow(base,exponent)
print(ans)




	
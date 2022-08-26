# HCF: Highest Common Factor

# normal method

a=int(input('Enter the number of the a: '))
b=int(input('Enter the number of the b: '))
minnum=min(a,b)
i=2

while(i<minnum):
	if(a%i==0 and b%i==0):
		hcf=i
	i+=1

print(gcd)


# using function and while loop


def calculat_hcf(a,b):
	minnum=min(a,b)
	i=2
	while(i<minnum):
		if(a%i==0 and b%i==0):
			hcf=i
		i+=1
	return hcf

a=int(input('Enter the number of a: '))
b=int(input('Enter the number of b: '))
result=calculat_hcf(a,b)
print('the hcf of',a,'and',b,'is',result)


#using for loop and function

def calculat_hcf(a,b):
	minnum=min(a,b)
	for i in range(2,minnum+1):
		if (a%i==0 and b%i==0):
			hcf=i
	return hcf

a=int(input('Enter the number of a: '))
b=int(input('Enter the number of b: '))
result=calculat_hcf(a,b)
print('hcf of the',a, 'and',b,'is',result)
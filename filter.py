
# using filter with lambda function
fruit = ['Apple','banana','orange','Africort','pear']
obj = filter(lambda f : f[0]=='A',fruit)
print(list(obj))

# using filter with normal function function

def start_with_A(s):
	return s[0]=='A'
fruit = ['Apple','banana','orange','Africort','pear']
obj = filter(start_with_A,fruit)
print(list(obj))

# find the even value using filter with normal function
def even(e):
	return e%2==0

l1 = [2,3,4,6,7,8]

eve = filter(even,l1)
print(list(eve))


# find the even no. using lambda function

lam = filter(lambda eve:eve%2==0,l1)
print(list(lam))


# Write a program to check whether the given number is even and odd?


n=int(input('Enter the number list: '))
b=[]

for number in range(n):
	a=int(input('Enter the number: '))
	b.append(a)
print(b)
for val in b:

	if val%2==0:
		print('The {} is even'.format(val))
	else:
		print('The {} is odd'.format(val))


'''
3. Write a program to count a total number of lines and count the total
number of lines starting with ‘A’, ‘B’, and ‘C’.'''
a = []
b = []
c = []
file = open('shruti.txt','r')
data = file.readlines()
print('lenth: ',len(data))


for i in data:

	if i[0]=='A':
		a.append(i)
		
	elif i[0]=='B':
		b.append(i)
		
	elif i[0]=='C':
		c.append(i)
		
print('A:',a)
print('B: ',b)
print('c: ',c)

	
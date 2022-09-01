'''2. Count the total number of upper case, lower case, and digits used in the
text file “sample.txt”.'''
upper = 0
lower = 0
l = []
digit = 0
file = open('shruti.txt')
data = file.read()
word = data.split()

for i in word:
	if i[0].isupper():
		upper+=1
print('upper: ',upper)

for i in word:
	if i[0].islower():
		lower+=1
		l.append(i)
print('l: ',l)
print('lower: ',lower)

for i in word:
	if i[0].isdigit():
		digit+=1
print('digit: ',digit)

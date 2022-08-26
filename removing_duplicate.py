# Write a program to remove duplicate characters from the given input string?
#input: ABCDABBCDABBBCCCDDEEEF
#output: ABCDEF


input='ABCDABBCDABBBCCCDDEEEF'
b=[]

for i in input:
	if i not in b:
		b.append(i) 

print('output= ',''.join(b))
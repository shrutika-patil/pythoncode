# Q2. Program to reverse order of words.
#input: Learning Python is very Easy
#output: Easy Very is Python Learning

# using inbuilt function

word='Learning Python is very Easy'
split=word.split()
rev=split[::-1]
print('join_rev= ',' '.join(rev))



#using while loop

print('using for loop')


lenth=len(split)-1

while (lenth>=0):
	split=word.split()
	lenth=lenth-1

print(' '.join(reversed(split)))







	


	
	

	

	





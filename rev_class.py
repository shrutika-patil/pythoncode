#Q1. Write a program to reverse the given String
#input=shree
#output=eerhs

string='shree'
 
# using inbuilt method 1

print('reverse= ',string[::-1])



# using inbuilt method 2

string='shree'

print('reversed= ',''.join(reversed(string)))


#using for loop:

string='shree'
rev_string=' '

for character in string:
	rev_string = character  + rev_string   

print('rev_string= ',rev_string)


#using while loop:

string='shree'
rev_string=' '
char=len(string)-1

while(char>=0):
	rev_string=rev_string+string[char]
	char=char-1
print('rev_string=',rev_string)






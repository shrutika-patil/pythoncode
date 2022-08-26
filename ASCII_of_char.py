# Q Python Program To Find ASCII value of a character

def ASCII_char(char):
	ans=ord(char)
	return ans
	

char=input('Enter the ASCII char is: ')
ans=ASCII_char(char)
print('The ASCII of the',char, 'is ',ans)

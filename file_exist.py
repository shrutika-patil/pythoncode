
'''
Q. Write a program to check whether the given file exists or not. If it is
available then print its content?
'''

import os 
import sys

fname = input('Enter the file name: ')
if os.path.isfile(fname):
	print('File is exist: ',fname)
	f = open(fname,'r')
else:
	print('File is not Exist: ',fname)
	sys.exit(0)

print('The content of the File is: ')
data = f.read()
print(data)






# Q. Write a program to enter name and percentage marks in a dictionary and display information on the screen

rec={}
n=int(input('Enter the number of student: '))
i=0

while i <= n:
	name=input('Enter the student name: ')
	mark=input('Enter the marks of student: ')
	rec[name]=mark
	i+=1
	print('student name: ',name,'\t',mark,'%')
for x in rec:
	print("\t",x,"\t\t",rec[x])
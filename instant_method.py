class student:

	def __init__ (self,name,marks):
		self.name = name
		self.marks = marks

	def disply(self):
		print('hi,',self.name)
		print('your marks is ',self.marks)

	def grade(self):
		if self.marks>60:
			print('your grade is A grade')
		elif self.marks>50:
			print('your grade is B grade')
		elif self.marks>40:
			print('your grade is C grade')
		else:
			print('your are faile,try again')
n = int(input('Enter the number of student: '))
for i in range(n):
	name = input('Enter student name: ')
	marks = float(input('Enter student marks: '))
	s=student()
	s.display()
	s.grade()
	print('#'*20)

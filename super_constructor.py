class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def display(self):
		print('The name is : ',self.name)
		print('The age is : ',self.age)

class Student(Person):
	def __init__(self,name,age,rollno,marks):
		
		super().__init__(name,age)
		self.rollno = rollno                    # when child class calling some members from parent class that 
												#purpose super method is used means some common variable we can 
												#access from the parent class by using super method it is used 
												#for constructor and method both
		self.marks = marks

	def display(self):
		super().display()
		print('Your rollno is : ',self.rollno)
		print('Your marks is : ',self.marks)


class Teacher(Person):
	def __init__(self,name,age,salary,dept):

		super().__init__(name,age)
		self.salary = salary
		self.dept = dept
	def display(self):
		super().display()
		print('salary: ',self.salary)
		print('dept: ',self.dept)

p = Person('nayra',2)
p.display()

s = Student('rohit',32,235,85)
s.display()

t = Teacher('kranti',45,50000,'comp')
t.display()
class Employee:
	def __init__(self,eno,ename,esal):
		self.eno =eno 
		self.ename = ename
		self.esal = esal
	def display(self):
		print('employee id no : ',self.eno)
		print('employee name: ',self.ename)
		print('employee salary: ',self.esal)

class Test:
	def increment(emp):
		emp.esal = emp.esal+10000
		emp.display()
e = Employee(11164,'rohit',100000)
Test.increment(e)

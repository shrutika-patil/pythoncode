import sys
class Customer:
	''' customer bank application '''
	bankname = 'BOB'

	def __init__(self,name,balance=0):
		self.name = name
		self.balance = balance

	def deposit(self,amt):
		self.balance = self.balance + amt
		print('your total balance is : ',self.balance)

	def withdraw(self,amt):
		if amt>self.balance:	
			print('balance is insufficiant')
			sys.exit()
		self.balance = self.balance - amt
		print('your remaing balance is: ',self.balance)

print('welcome to ',Customer.bankname)
name = input('Enter your name: ')

c = Customer(name)
while True:
	print('d: deposit\nw:withdraw\ne:exit')
	option = input('choose one option: ')
	if option.lower()=='d':
		amt=float(input('how much amount you want to add: '))
		c.deposit(amt)
	elif option.lower()=='w':
		amt=float(input('how much amount want to withdraw: '))
		c.withdraw(amt)
	elif option.lower()=='e':
		print('Thank you for banking')
		sys.exit()
	else:
		print('choose valid option:')







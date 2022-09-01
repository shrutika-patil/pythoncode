def star(func):
	
	print('star func: ',func)

	def inner(*args,**kwargs):
		print('*' * 30)
		func(*args,**kwargs)
		print(id(func)) #140277087678816
		print('star func1 : ',func)
		print('*' * 30)
	return inner

def parcent(func):
	print(id(func)) #140277087609456
	print('parcent func: ',func)

	def inner(*args,**kwargs):
		print('%' * 30)
		func(*args,**kwargs)
		print(id(func))  # 140277087678672
		print('parcent func: ',func)
		print('%' * 30)
	return inner

@star
@parcent
def printer(msg): #140277087678816
	print(id(msg))
	print('printer:',msg)

printer('Hello world')

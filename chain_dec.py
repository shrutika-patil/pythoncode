def star(func):
	print('##### sta #####')
	print('func: ',func)
	def inner(*args,**kwargs):
		print('*' * 30)
		func(*args,**kwargs)
		print('func: ',func)
		print('*' * 30)
	return inner

def percent(func):
	print('@@@@@@per@@@@@@')
	print('func: ',func)
	def inner(*args,**kwargs):
		print('**kwargs:',**kwargs)
		print('*args:',*args)
		print('%' * 30)
		func(*args,**kwargs)
		print('*args:',*args)
		
		print('func:',func)
		print('%' * 30)
	return inner

@star
@percent
def priter(msg):
	print(msg)

priter('Hello')
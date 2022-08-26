# def smart_divid(func):
# 	def inner(a,b):
# 		print('we are divid a and b ')
# 		if b==0:
# 			print("whoops! can't divid zero")
# 			return
# 		return func(a,b)
# 	return inner

# @smart_divid
# def divide(a,b):
# 	print(a/b)

# divide(8,2)



def make_pretty(func):
	def pretty():
		print(' i got decorator ')
		func()
	return pretty

@make_pretty
def ordinary():
	print('i got ordinary')

# pre = make_pretty(ordinary)
# pre()
ordinary()
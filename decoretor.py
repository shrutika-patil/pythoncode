# def frist(msg):
# 	print(msg)
# frist('Hello')
# second = frist
# second('hiii')


# def inc(x):
# 	return x+1
# def dec(x):
# 	return x-1

# def operate(func,x):
# 	result = func(x)
# 	print(result)
# 	return result
# operate(inc,3)
# operate(dec,3)


# def make_multipler(n):
# 	def multiple(x):
# 		return x*n
# 	return multiple

# times3 = make_multipler(3)
# times5 = make_multipler(5)

# print(times3(9))
# print(times5(3))
# print(times5(times3(2)))

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
pretty = make_pretty(ordinary)
pretty()
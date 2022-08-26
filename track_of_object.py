# Q print track of objects craeted for the class

class test:
	count=0
	def __init__(self):
		test.count=test.count+1
	@classmethod

	def getnoofobjects(cls):

		print("number of object is: ",cls.count)

t1 = test()
t2 = test()
t3 = test()
test.getnoofobjects()

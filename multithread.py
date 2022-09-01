# using function
'''
import threading
import time
def thread1(number):
	for i in range(number):
		print('Hello Nayra')
		time.sleep(2)


def thread2():
	for i in range(10):
		print('Hi Rohit')
		time.sleep(2)

t1 = threading.Thread(target=thread1,args=(10,))
t2 = threading.Thread(target = thread2)
t1.start()
time.sleep(0.2)
t2.start()
t1.join()
t2.join()
print('Bye both')'''

# using class
from threading import *
import time

class test:
	def m1(self):
		for i in range(10):
			print('Hello')
			time.sleep(1)
	def m2(self):
		for i in range(10):
			print('Hi')
			time.sleep(1)

obj = test()
t1=Thread(target=obj.m1)
t2=Thread(target=obj.m2)
t1.start()
t2.start()




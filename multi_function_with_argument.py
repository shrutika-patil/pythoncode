import threading
import time

def Square(numbers):
	for n in numbers:
		print("Square: ", n * n)
		time.sleep(1)


def Double(numbers):
	for n in numbers:
		print("Double: ", 2 * n)
		time.sleep(1)

numbers = [2,8,5,6,5,4,7]
t1 = threading.Thread(target = Square,args = (numbers,))
t2 = threading.Thread(target = Double,args = (numbers,))
t1.start()
t2.start()

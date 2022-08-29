import threading
import time
def print_hello():
	for i in range(10):
		
		time.sleep(1)
		print("Hello")
# Function to print numbers till a given number
def print_numbers(num):
	for i in range(num+1):
		time.sleep(1)
		print(i)

print("Greetings from the main thread.")
thread1 = threading.Thread(target = print_hello, args = ())
thread2 = threading.Thread(target = print_numbers, args = (20,))
# Starting the two threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("It's the main thread again!")
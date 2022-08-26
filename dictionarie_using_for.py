# Q Python Program to Iterate Over Dictionaries Using for Loop

dic={'c': 'cat', 'd' :'dog', 'h':'horse', 'r': 'rabit'}

for key,value in dic.items():
	print(key,value)


#Access both key and value without using items()
dic={'c': 'cat', 'd' :'dog', 'h':'horse', 'r': 'rabit'}
for key in dic:
	print(key,dic[key])


 # Access both key and value using iteritems()

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.iteritems():
    print(key, value)

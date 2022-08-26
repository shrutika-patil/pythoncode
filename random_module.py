import random


lis=[25,56,85,76,96]



print('randint= ',random.randint(20,80))     #any random value including 20 and 80 here
print()

getrandbits= random.getrandbits(4)    		 # 4 is the given bit size of the any number came form random number

print('getrandbits= ',getrandbits)

print('binary= ',bin(getrandbits))           # decimal number conver into binary number

print('random= ',random.random())			# this gives the random float number between the 0 and 1

print('randrange= ',random.randrange(12,80)) # here the any random number came 12 and 79 (80 is exclusive)

print('choice= ',random.choice(lis))		# given lis here any random number take

lis1=['red','white','black','yellow','green','pink']

random.shuffle(lis1)                        # return the sequence of list in random order
print(lis1)

print('uniform= ',random.uniform(20,30))   # give the floating number between the 2 given parameters


print('triangular',random.triangular(20,80,30))# give the random float num between given two parameter 

#seed

random.seed(20)
print('seed= ',random.randint(0,20))            # 1st time random number ocurrence that number is seed number it does't change


print('random= ',random.random())	

state=random.getstate()							# give current internal state of the random number

print('random= ',random.random())	

random.setstate(state)							#restre the state ofbthe random number generator by the getstate()

print('random= ',random.random())	

print('sample= ',random.sample(lis1,3))			# give the sample of sequence


# Q Python Program to Find Sum of Natural Numbers Using Recursion


def sum_natural(nums):
	if nums==0:
		return 0
	else:	

		summetion=nums+sum_natural(nums-1)
	return summetion

nums=int(input('Enter the first 10 natural number'))
print(sum_natural(nums))




def sum_natural(num):
	if num==0:
	 return 0
	else:
		return num+sum_natural(num-1)

num=int(input('Enter the higher number of addtion: '))

print(sum_natural(num))


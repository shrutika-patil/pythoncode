# Q Python Program to Check Armstrong Number

num=int(input('Enter the number: '))
a=len(str(num))
print(a)
add=0


for i in str(num):
   i=int(i)
   result=i**a
   
   add=add+result
   print(add)
if add==num:
   print(' num is armstrong ')
else:
   print('not')   



# using while loop

# Q Python Program to Check Armstrong Number

num=int(input('Enter the number: '))
order=len(str(num))
copy_num=num
add=0

while(num>0):
   
   digit=num%10
   mul=digit**order
   add=add+mul
   
   num=num//10
   
if add==copy_num:
   print('num is armstrong')

else:
   print('not')      


   


   
   

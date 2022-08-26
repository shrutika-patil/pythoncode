# Python program to print prime or not
lower=int(input('Enter the lower value: '))
upper=int(input('Enter the upper value: '))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print('The number is {} not prime'.format(num))
                break
        else:
                print('The number is {} prime'.format(num))

# Q Python Program to Convert Celsius To Fahrenheit

celsius=int(input('Enter the celsius value : '))

# covert celsius to fahrenheit 0 C=32 F  (formula= 0*1.8+32)

temp_F = (celsius*1.8)+32

print(f'The celsius temp conver into fahrenheit is {temp_F}')




# change this value for a different result
celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

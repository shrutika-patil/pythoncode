# Python Program to Convert Decimal to Binary, Octal and Hexadecimal

# all conversion in one block

def decimal_convert(decimal):

	binary=bin(decimal)
	octde=oct(decimal)
	hexde=hex(decimal)
	return binary,octde,hexde

decimal=int(input('Enter the decimal number: '))
convert=(decimal_convert(decimal))
print(f'conversion of', {decimal},' in binary,octde,hexde is :',convert)


# using seprate block

def decimal_binary(num):
	binary=bin(num)
	return binary

def decimal_octal(num):
	octal=oct(num)
	return octal

def decimal_hexdecimal(num):
	hexdecimal=hex(num)
	return hexdecimal

num=int(input('Enter the decimal number is : '))
binary=decimal_binary(num)
octal=decimal_octal(num)
hexdecimal=decimal_hexdecimal(num)

print('The decimal value convert in ',{num},' is :',binary,octal,hexdecimal)
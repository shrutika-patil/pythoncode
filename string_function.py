# string is the sequence of the character

# how to access character of the string

text='india'
print('index= ',text[1])   # here we access the character of the particular index number
print('find= ',text[1])    # here we access the character of the particular index number

i=text.index('d')          # here we access the particular character index number it come from start to first occur or end to first
print('i= ',i)

f=text.find('d')           # here we access the particular character index number it come from start to first occur or end to first
print('f= ',f)

#slice function

s="Learning Python is very very easy!!!"
print('slice= ',s[0:7:1])				# here it take the character 0 (index) to 7 (index) with one bye one character
print('slice_alternet= ',s[0:13:2])		#it take alternet character
print('default_start= ',s[:7])          # it take staring index is default zero
print('default_end= ',s[7:])            # it take default end of string index and print all character
print('def_start_end= ',s[::])			# it take both start and end dafault 
print('start_end= ',s[:])
print('reverse= ',s[::-1])				# it take revese string of given string
print('for= ',s.index('n'))

# checking membership of the string
text='india'
print('n' in text)						# it gives output in true or false
print('z' in text)

# mathematical operation on string
#(+,*)
t='shruti'
t1='patil'
print('sum= ', t + t1)                  # in string +(add) operation always two value is string format

print('mul= ',t*3)                      # in string *(mul) operation always one value is string or other is number


#Comparison of Strings

s1='nayra'
s2='shruti'
if s1==s2:
	print('s1 and s2 are the equel') 	# Comparison will be performed based on alphabetical order 
elif s1<s2:
	print('s2 is greater than the s1')
else:
	print('s1 is greater than the s2')


#String Functions/Methods:
a='india'
print('capitalize',a.capitalize())		# first latter of string conver in upper case
print('casefold',a.casefold())          # convert string into lower case
print('center= ',a.center(20,'*'))      # str.center(width, [fillchar]) paded character at center
print('count= ',a.count('i'))           #count how many time character came in the string

tex='python is fun'
print('endwith= ',tex.endswith('fun'))  # return value of endswith is true or false
print('endswith= ',tex.endswith('is'))

txt1='abc\txyz\tpqr'
print('expandtabs= ',txt1.expandtabs()) # if you don't pass argument it take default 8 tab
print('expandtabs1= ',txt1.expandtabs(2))
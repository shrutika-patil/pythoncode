text='bhjjk4558'
print("alnum= ",text.isalnum())         # string is alpha and number in the string then it give true and false result
print('alpha= ',text.isalpha())         # string has only character then it give result true otherwise false

string='203'
print('decimal= ',string.isdecimal())   # string decimal or not it give true and false result
print('digit= ',string.isdigit())       # string is digit or not it gives true or false result
print('identifier= ',string.isidentifier()) # string is identifier or not it gives true and false result
print('identifier1= ',text.isidentifier())
print('lower= ',text.islower())           # string is lower case or not

#lenth of the string

print('lenth= ',len(text))

# removing space from string

tex1='  jave'
print('tex1= ',tex1)
print('left_strip= ',tex1.lstrip())

tex2='java  '
print('tex2= ',tex2)
print('tex2= ',tex2.rstrip())

tex3='  java  '
print('tex3= ',tex3)
print('tex3= ',tex3.strip())


#replace
s="abab"
s1=s.replace("a","b")
print('s1= ',s1)
print(s,"is available at :",id(s))
print(s1,"is available at :",id(s1))


#split method
s="exacto software solutions"
l=s.split()
print('l= ',l)
for x in l:
	print(x)

#join 
t=('sunny','bunny','chinny')
s='-'.join(t)
print(s)


s='learning Python is very Easy'
print('upper=',s.upper())
print('lower=',s.lower())
print('swapcase=',s.swapcase())
print('title= ',s.title())

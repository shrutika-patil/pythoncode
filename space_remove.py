'''
4. Replace multiple spaces with single space in a text file.
'''

file = open('shruti.txt','r')
data = file.read()
print(data)
# s = data.replace(' ','')
j = " ".join(data.split())
print(j)



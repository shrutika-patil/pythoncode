# path= 'python3/Desktop/new-file.text'

path = "/home/rohit/Desktop/new-file.txt"

file = open(path, 'w')
#data = file.read()
#data = file.readline(10)
#data=file.readlines(5)
#data=file.read(5)
#data=file.readline(30)
data=file.write()
#data=file.read(10)
file.close()
print(data)

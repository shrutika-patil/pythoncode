def read_data(path): 
	f = open(path,'r')
	data = f.read()
	mb=[]
	gmail=[]
	words = data.split()
	print(words)

	for word in words:
		num = len(word)
		if num==10:
		
		
			mb.append(word)
		if '@' in word:
			gmail.append(word)

	print(gmail)

	print(mb)
	f.close()
	#print(data)
path = r"/home/rohit/Desktop/new-file.txt"
read_data(path)

def write_data(path,data):
	f=open(path,'w')
	f.write(data)

	f.close()
path = r"/home/rohit/Desktop/new1-file.txt"
data = ("hello nayra")
#write_data(path,data)


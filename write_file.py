'''
1. Write a program to accept string/sentences from the user till the user
enters “END” to. Save the data in a text file and then display only those
sentences which begin with an uppercase alphabet.'''

#with open('string.txt','w') as f:
# 	while True:
# 		sen = input('write a sentances: ')
# 		if sen=='end':
# 			break
# 		else:
# 			f.writelines(sen+'\n')
# 	f.close()
# 	print()
# 	print('print the line start with capital letter: ')
# 	file =open('string.txt','r')
# 	data = file.readlines()
# 	for i in data:
# 		if i[0].isupper():
# 			print(i)
# 	file.close()




file = open('shruti.txt','w')
while True:
	sentence = input('Enter the sentences: ')
	if sentence == 'End':
		break
	else:
		file.write(sentence+'\n')
file.close()

f = open('shruti.txt','r')
Data = f.readlines()
for i in Data:
	if i[0].isupper():
		print(i)
f.close()



import csv

def csv_read_data(path):
	fields=[]
	rows=[]

	f = open(path,'r')
	data = csv.reader(f)
	fields=next(data)
	print(fields)

	for row in data:
		print(row)
	print('Field names are:' + ', '.join(field for field in fields))


path = r'/home/rohit/Desktop/data.csv'
csv_read_data(path)



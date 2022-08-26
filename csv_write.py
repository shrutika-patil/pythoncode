
import csv
def write_data_csv(fields,rows):
	csvfile = r'employee.csv'
	file = open(csvfile,'w')
	csvwriter = csv.writer(file)
	csvwriter.writerow(fields)
	csvwriter.writerow(rows)
	print('\n')


fields = [" 'emp_id' , 'name' , 'address' , 'mob.no'"]
rows = ['''[01 , 'nikhil' , 'pune' , 9503473781] , 
		[02 , 'sushant' , 'sangli' ,9032473781 ] ''']
write_data_csv(fields,rows)



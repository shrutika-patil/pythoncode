from csv import reader
from csv import writer
import csv

with open('employee.csv','r') as read_obj, open('output1.csv','w', newline='') as write_obj:
	reade_r = reader(read_obj)
	write_r = writer(write_obj)

	for row in reade_r:
		rows = int(row[3])
		row.append(rows*12)
		write_r.writerow(row)




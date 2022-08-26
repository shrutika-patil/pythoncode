import csv

path = r'student.py'

csvfile = open(path,'w')
writer = csv.writer(csvfile)
writer.writerow()
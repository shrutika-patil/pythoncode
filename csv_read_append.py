'''
import csv

csvinput = open('employee.csv')
r = csv.reader(csvinput)
row0 = r.next(csvinput)
row0.append('age')
print(row0)'''
import csv
v = open('employee.csv')
r = csv.reader(v)
row0 = next(r)
row0.append('age')
print (row0)


'''
with open('employee.csv','r') as csvinput:
    with open('employee.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('age')
        all.append(row)

        for row in reader:
            row.append(row[0])
            all.append(row)

        writer.writerows(all)
'''



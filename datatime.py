import datetime

now = datetime.datetime.now()
print(now)


d = datetime.date.today()
print(d)




#timestamp

timestamp = datetime.date.fromtimestamp(1626244364)
print('timestamp= ',timestamp)

# datetime.date class

date = datetime.date(2020,5,19)
print(date)
date = datetime.date(11,5,20)
print(date)

# get todays year day month

today = datetime.date.today()
print('year:',today.year)
print('day:',today.day)
print('month:',today.month)
import datetime
t1 = datetime.date(year = 2020, month = 5, day = 25)
t2 = datetime.date(year = 2012 , month = 10, day = 30)
t3 = t1 - t2
print(t3)
print(type(t3)) #--- (class datetime.timedelta)

t4 = datetime.datetime(year = 2020, day = 23, month = 2,hour = 23, minute = 52 , second = 32 )
t5 = datetime.datetime(year = 2012, day = 25, month = 12,hour = 15, minute = 59 , second = 12 )
t6 = t5 - t4
print(t6)
print(type(t6))  #--- (class datetime.timedelta)

'''
Python strftime() - datetime object to string
The strftime() method is defined under classes date, datetime and time.
The method creates a formatted string from a given date, datetime or
time object.'''

# current date and time 

now = datetime.datetime.now()
t = now.strftime('%H:%M:%S')
print(t)

d = now.strftime('%y-%d-%m')
print(d)

dt = now.strftime('%y-%d-%m,%H:%M:%S')
print(dt)

date_object = '21,6,20'	
print('date_object: ',date_object)

s = datetime.datetime.strptime(date_object,'%d,%m,%y')
print(s)
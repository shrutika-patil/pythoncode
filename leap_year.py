# Q Python Program to Check Leap Year

#Take a year from user

year=int(input('Enter the year : '))

# Check the year is leap or not

if year%4==0:
	if year%100==0:
		if year%400==0:
			
			print(f'The year is leap {year} year') 

		else:
			print(f'The year is not leap {year} year') 
		
	else:
		print(f'The year leap {year} year') 	

else:
	print(f'The year is not leap {year} year') 
import psycopg2

connection = psycopg2.connect(	user= 'postgres',
								host='localhost',
								password='root',
								port='5432',
								database='query'
								)

print(connection.get_dsn_parameters(),'\n')


cursor = connection.cursor

cursor.execute('shruti_schema.employee')
cursor.commit()
print('create table successfully in postgreSQl')
cursor.close()
connection.close()
print('postgreSql is closed')



import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mysql2023',

)

cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE prvmysql')
print('All Done!')
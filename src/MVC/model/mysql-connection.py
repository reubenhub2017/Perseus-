import mysql.connector
from mysql.connector import Error

""" Connection with MYSQL Database on Localhost """
try:
    connection = mysql.connector.connect(host='localhost',
                                         user='',
                                         password='',
<<<<<<< HEAD
                                         database='')
=======
                                         auth_plugin='mysql_native_password')
>>>>>>> 73be496... Finish
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

    #Querying Data from the user
    mysql_selector = 'SELECT * FROM user'
    cursor = connection.cursor()
    cursor.execute(mysql_selector)
    records = cursor.fetchall()
    print("Total number of rows found", cursor.rowcount)
    print("printing each user record")
    for rows in records:
        print("id:", rows[0])
        print("username :", rows[1])
        print("password :", rows[2])
        print("---------")

except Exception as e:
    print("Error while connecting to MySQL", e)
<<<<<<< HEAD
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
=======
>>>>>>> 73be496... Finish

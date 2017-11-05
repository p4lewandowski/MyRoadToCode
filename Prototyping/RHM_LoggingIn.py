import mysql.connector
from mysql.connector import Error

def CallAuthentication (UserName, UserPassword):
    print (UserName, UserPassword)
    try:
        conn = mysql.connector.connect(host='10.9.121.128',
                                       database='patientsdata',
                                       user='root',
                                       password='W950418w')
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()
            cursor.execute("SELECT * from patientcredentials")
            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        conn.close()


CallAuthentication('root','dasd')
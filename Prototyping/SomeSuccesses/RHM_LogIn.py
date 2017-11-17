from mysql.connector import MySQLConnection, Error
from ConfigFileParser import read_db_config
from RunningMainWindow import RunMainWindow


def connect(Username, Userpass):
    """ Connect to MySQL database """

    db_config = read_db_config()
    db_config['user'] = Username
    db_config['password'] = Userpass
    #print(db_config)

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')

            cursor = conn.cursor()


            MainWindowInstance = RunMainWindow()
            MainWindowInstance.show()

            cursor.execute("show global variables like '%ssl%'")

            QueryResults(cursor)

        else:
            print('connection failed.')

    except Error as e:
        print(e)

    finally:
        conn.close()
        print('Connection closed.')

def QueryResults(input_cursor):
    DataFromQuery = input_cursor.fetchone()
    while DataFromQuery is not None:
        print(DataFromQuery)
        DataFromQuery = input_cursor.fetchone()

if __name__ == '__main__':
    connect()
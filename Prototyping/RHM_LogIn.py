from mysql.connector import MySQLConnection, Error
from ConfigFileParser import read_db_config


def connect(Username, Userpass):
    """ Connect to MySQL database """

    db_config = read_db_config()
    db_config['user'] = Username
    db_config['password'] = Userpass
    print(db_config)

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as e:
        print(e)

    finally:
        conn.close()
        print('Connection closed.')


if __name__ == '__main__':
    connect()
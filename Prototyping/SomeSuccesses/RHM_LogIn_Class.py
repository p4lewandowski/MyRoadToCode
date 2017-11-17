from mysql.connector import MySQLConnection, Error
from ConfigFileParser import read_db_config
from RunningMainWindow import RunMainWindow


class MySQL_Connection():


    def connect(self, Username, Userpass):
        """ Connect to MySQL database """

        db_config = read_db_config()
        db_config['user'] = Username
        db_config['password'] = Userpass

        try:
            print('Connecting to MySQL database...')
            conn = MySQLConnection(**db_config)

            if conn.is_connected():
                print('connection established.')

                self.cursor = conn.cursor()


                MainWindowInstance = RunMainWindow()
                MainWindowInstance.show()

                self.cursor.execute("show global variables like '%ssl%'")

                self.QueryResults(self.cursor)

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


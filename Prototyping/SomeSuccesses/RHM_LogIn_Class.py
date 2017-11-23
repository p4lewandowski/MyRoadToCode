from mysql.connector import MySQLConnection, Error

class MySQL_Connection():
    def __init__(self, db_config, command='none'):
        super().__init__()

        self.db_config = db_config
        self.command = command

        self.connect()

    def connect(self):
        """ Connect to MySQL database """
        self.conn = None

## connecton has to be open, check something with that
        print('Connecting to MySQL database...')
        self.conn = MySQLConnection(**self.db_config)

        if self.conn.is_connected():
            print('connection established.')

        else:
            print('connection failed.')



    def query(self,command):

        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(command)

        except Error as e:
            print(e)

        self.QueryResults()
        return self.cursor

       # finally:
            #conn.close()
            #print('Connection closed.')

    def call_stored_procedure(self, procedure, args):

        try:
            self.cursor = self.conn.cursor()
            self.cursor.callproc(procedure, args)

            for result in self.cursor.stored_results():
                print(result.fetchall())

        except Error as e:
            print(e)

        self.QueryResults()
        return self.cursor

    def QueryResults(self):
        DataFromQuery = self.cursor.fetchone()
        while DataFromQuery is not None:
            print(DataFromQuery)
            DataFromQuery = self.cursor.fetchone()

from mysql.connector import MySQLConnection, Error
from ConfigFileParser import read_db_config
from RunningMainWindow import RunMainWindow
from RHM_LogIn_Class import MySQL_Connection
import sys

class SteadyConnection():
    def __init__(self, Username, Userpass):
        super().__init__()

        self.Username = Username
        self.Userpass = Userpass
        db_config = read_db_config()
        db_config['user'] = self.Username
        db_config['password'] = self.Userpass

        self.new_connection = MySQL_Connection(db_config)

        self.new_connection.query("show global variables like '%ssl%'")
        self.control_panel = RunMainWindow(self.new_connection)





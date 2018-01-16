from SQL_Connector.ConfigFileParser import read_db_config
from PyQt5.QtSql import QSqlDatabase
import os

class mysql_connector():

    def mysql_connection(self, username, password):

        # Full path needs to be specified
        config_file_path = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..//SQL_Connector"))

        db_config = read_db_config('{}//ConnectionConfig.ini'.format(str(config_file_path)), 'mysql')
        db_config['user'] = username
        db_config['password'] = password

        ### QtSQL Connection
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setConnectOptions("CLIENT_SSL=1;");
        db.setHostName(db_config['host'])
        db.setPort(int(db_config['port']))
        db.setDatabaseName(db_config['database'])
        db.setUserName(db_config['user'])
        db.setPassword(db_config['password'])
        db.open()

        if not db.open():
            print("Database Connection Error", "Database Error: %s" % db.lastError().text())
            connection_bool = False
        else:
            print('Connection established')
            connection_bool = True

        return db, connection_bool

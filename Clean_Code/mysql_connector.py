from ConfigFileParser import read_db_config
from PyQt5.QtSql import QSqlDatabase


class mysql_connector():

    def mysql_connection(self):

        db_config = read_db_config()
        db_config['user'] = self.username_cred
        db_config['password'] = self.userpass_cred

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
        else:
            print('Connection established')

        return db
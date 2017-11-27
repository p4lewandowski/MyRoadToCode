import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtSql import *
from ConfigFileParser import read_db_config
from ApplicationWindow import ApplicationForm

class MainWindow(QMainWindow, ApplicationForm):
    def __init__(self, username, userpass):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__() # Inheritance
        self.setupUi(self)

        # Connection settings
        self.username_cred = username
        self.userpass_cred = userpass

        # Cosmetic settings
        # Setting up icon and window title
        self.setWindowTitle('Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))

        # Inserting the logo
        logo_pic = QLabel('LogoPic')
        logo_pic.setPixmap(QPixmap("RHM_LogoR.png"))

        # Creating database connection
        self.db_connection = self.mysql_connection()

        # Calling different functions
        self.find_patient_bttn.clicked.connect(self.call_find_patient)

        self.show()


    def mysql_connection(self):

        username_cred = self.username_cred
        userpass_cred = self.userpass_cred
        db_config = read_db_config()
        db_config['user'] = username_cred
        db_config['password'] = userpass_cred

        ### QtSQL Connection
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setConnectOptions("CLIENT_SSL=1;"
                             "SSL_KEY=C:\ProgramData\MySQL\Certificates\client-key.pem;"
                             "SSL_CERT=C:\ProgramData\MySQL\Certificates\client-cert.pem;"
                             "SSL_CA=C:\ProgramData\MySQL\Certificates\ca-cert.pem;"
                             "CLIENT_IGNORE_SPACE=1"
                             );
        db.setHostName(db_config['host'])
        db.setPort(int(db_config['port']))
        db.setDatabaseName(db_config['database'])
        db.setUserName(db_config['user'])
        db.setPassword(db_config['password'])


        if not db.open():
            print("Database Connection Error", "Database Error: %s" % db.lastError().text())
        else:
            print('Connection established')

        return db


    def call_find_patient(self):

        # For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
        entered_name = self.name_le.text()
        entered_surname = self.surname_le.text()
        entered_pesel = self.pesel_le.text()

        args = [entered_name, entered_surname, entered_pesel]
        print(args)


        # QSqlQuery calling
        # query = QSqlQuery(self.db_connection)
        # query.exec("select Name, SurName from patientcredentials")
        # query.exec("SHOW STATUS LIKE 'Ssl_cipher'")
        # while (query.next()):
        #     print(query.value(0), query.value(1))

        # Calling QSqlQueryModel with specified query
        new_query_model = QSqlQueryModel()
        #new_query_model.setQuery("select * from patientcredentials", self.db_connection)
        new_query_model.setQuery("SHOW STATUS LIKE 'Ssl_cipher'", self.db_connection)

        # Changing table display
        self.main_table.setModel(new_query_model)
        self.main_table.show()


if __name__ == '__main__':        # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow('root', 'W950418w')  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

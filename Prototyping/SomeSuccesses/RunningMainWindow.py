from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
import MainPanel
import sys
from ConfigFileParser import read_db_config
from RHM_LogIn_Class import MySQL_Connection
import ApplicationWindow

class RunMainWindow(QMainWindow, ApplicationWindow.CApplicationWindow):
    def __init__(self, Username, Userpass):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Connection settings
        self.Username = Username
        self.Userpass = Userpass
        self.db_config = read_db_config()
        self.db_config['user'] = self.Username
        self.db_config['password'] = self.Userpass

        # Cosmetic settings
        # Setting up icon and window title
        self.setWindowTitle('Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))
        # Inserting the logo
        LogoPic = QLabel('LogoPic')
        LogoPic.setPixmap(QPixmap("RHM_LogoR.png"))

        # Calling connection
        self.new_connection = MySQL_Connection(self.db_config)
        self.show() # Only after connection is established will the second window appear

        # Calling different functions
        #self.new_connection.query("SELECT * from rhm_database.patientdata where Name = 'Przemyslaw' and Surname = 'Lewandowski'")
        self.find_patient_bttn.clicked.connect(self.CallFindPatient)



    def CallFindPatient(self):

        # For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
        entered_name = self.name_le.text()
        entered_surname = self.surname_le.text()
        entered_pesel = self.pesel_le.text()

        args = [entered_name, entered_surname, entered_pesel]
        print(args)

        #args = ['Kamil', 'Wojtasiak', '9504111697] # In storedprocedures is null, in python is None
        self.new_connection.call_stored_procedure('FindPatient', args)

        new_query_model = QSqlQueryModel()
        #new_query_model.setQuery("Call FindPatient(?, ?)",*args)
        new_query_model.setQuery("select * from patientdata")
        self.main_table.setModel(new_query_model)
        newtable = QTableView()
        newtable.setModel(new_query_model)
        newtable.show()



if __name__ == '__main__':              # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = RunMainWindow('root', 'W950418w')  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import MainPanel
import sys
from ConfigFileParser import read_db_config
from RHM_LogIn_Class import MySQL_Connection


class RunMainWindow(QMainWindow, MainPanel.Ui_MainWindow):
    def __init__(self, Username, Userpass):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Cosmetic settings
        # Setting up icon and window title
        self.setWindowTitle('Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))
        # Inserting the logo
        LogoPic = QLabel('LogoPic')
        LogoPic.setPixmap(QPixmap("RHM_LogoR.png"))

        # Connection settings
        self.Username = Username
        self.Userpass = Userpass
        db_config = read_db_config()
        db_config['user'] = self.Username
        db_config['password'] = self.Userpass

        # Calling connection
        self.new_connection = MySQL_Connection(db_config)
        self.show() # Only after connection is established will the second window appear

        # Calling different functions
        self.new_connection.query("SELECT * from rhm_database.patientdata where Name = 'Przemyslaw' and Surname = 'Lewandowski'")
        self.FindPatientButton.clicked.connect(self.CallFindPatient)



    def CallFindPatient(self):
        entered_name = self.NameLineEdit.text()
        entered_surname = self.SurnameLineEdit.text()
        entered_pesel = self.PESELLineEdit.text()
        print(entered_name,entered_surname,entered_pesel)
        args = ['null', 'null', '95042305697']
        self.new_connection.call_stored_procedure('FindPatient', args)




if __name__ == '__main__':              # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = RunMainWindow()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtSql import *
from ApplicationWindow2 import Ui_main_app_window
from sql_show_all import sql_show_all
from mysql_connector import mysql_connector
from sql_find_patient import sql_find_patient

class MainWindow(QMainWindow, Ui_main_app_window,sql_show_all,mysql_connector,sql_find_patient):
    def __init__(self, username, userpass):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__() # Inheritance

        self.username_cred = username
        self.userpass_cred = userpass

        # If connected
        self.setupUi(self)

        # Creating database connection
        self.db_connection = self.mysql_connection()

        # Cosmetic settings
        # Setting up icon and window title
        self.setWindowTitle('Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))

        # Inserting the logo
        logo_pic = QLabel('LogoPic')
        logo_pic.setPixmap(QPixmap("RHM_LogoR.png"))



        # Creating table model for patientcredentials
        self.patienttable_tablemodel = QSqlTableModel()
        self.patienttable_tablemodel.setTable('patientdata')


        # Creating query model for patientcredentials
        self.findpatient_querymodel = QSqlQueryModel()


        # Calling different functions

        # Find Patient
        self.findpatient_search_button.clicked.connect(self.call_find_patient)
        self.name_le.returnPressed.connect(self.call_find_patient)
        self.surname_le.returnPressed.connect(self.call_find_patient)
        self.pesel_le.returnPressed.connect(self.call_find_patient)
        self.dateofbirth_le.returnPressed.connect(self.call_find_patient)
        self.phonenumber_le.returnPressed.connect(self.call_find_patient)
        self.city_le.returnPressed.connect(self.call_find_patient)
        self.postalcode_le.returnPressed.connect(self.call_find_patient)

        # Show All
        self.findpatient_showall_button.clicked.connect(self.show_all_patients)

        # Show the gui layout
        self.show()


if __name__ == '__main__':        # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow('root', 'W950418w')  # We set the form to be our ExampleApp (design)
    #form = MainWindow()
    form.show()  # Show the form
    app.exec_()  # and execute the app

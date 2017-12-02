import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt, QVariant
from ConfigFileParser import read_db_config
from ApplicationWindow import ApplicationForm
from ApplicationWindow2 import Ui_main_app_window

#class MainWindow(QMainWindow, ApplicationForm):
class MainWindow(QMainWindow, Ui_main_app_window):
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
        self.findpatient_search_button.clicked.connect(self.call_find_patient)
        self.name_le.returnPressed.connect(self.call_find_patient)
        self.surname_le.returnPressed.connect(self.call_find_patient)
        self.pesel_le.returnPressed.connect(self.call_find_patient)
        self.dateofbirth_le.returnPressed.connect(self.call_find_patient)
        self.phonenumber_le.returnPressed.connect(self.call_find_patient)
        self.city_le.returnPressed.connect(self.call_find_patient)
        self.postalcode_le.returnPressed.connect(self.call_find_patient)

        self.findpatient_showall_button.clicked.connect(self.show_all_patients)

        self.show()


    def mysql_connection(self):

        username_cred = self.username_cred
        userpass_cred = self.userpass_cred
        db_config = read_db_config()
        db_config['user'] = username_cred
        db_config['password'] = userpass_cred

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

    def show_all_patients(self):

        #findpatient_showall_querymodel = QSqlQueryModel()
        #findpatient_showall_querymodel.setQuery("SELECT * FROM patientdata")

        findpatient_showall_querymodel = QSqlTableModel()
        findpatient_showall_querymodel.setTable('patientdata')
        findpatient_showall_querymodel.select()

        self.patient_table.setModel(findpatient_showall_querymodel)
        self.patient_table.resizeColumnsToContents()

    def call_find_patient(self):

        # For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
        entered_name = self.name_le.text()
        entered_surname = self.surname_le.text()
        entered_dateofbirth = self.dateofbirth_le.text()
        entered_gender = self.gender_cb.currentText()
        entered_country = self.country_cb.currentText()
        entered_city = self.city_le.text()
        entered_postalcode = self.postalcode_le.text()
        entered_phonenumber = self.phonenumber_le.text()
        entered_pesel = self.pesel_le.text()

        find_patient_args = [entered_name, entered_surname, entered_dateofbirth,entered_gender,entered_country, \
                             entered_city,entered_postalcode,entered_phonenumber,entered_pesel]

        findpatient_querymodel = QSqlQueryModel()

        if self.enable_a_search.isChecked():
            for index, values in enumerate(find_patient_args):
                if not find_patient_args[index]:
                    find_patient_args[index] = 'Null'

            # Calling QSqlQueryModel with specified query
            findpatient_querymodel.setQuery("call FindPatient('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(*find_patient_args))

        else:
            for index, values in enumerate(find_patient_args):
                if not find_patient_args[index]:
                    find_patient_args[index] = '%'
            findpatient_querymodel.setQuery("call FindPatientA('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(*find_patient_args))

        # Changing table display
        self.patient_table.setModel(findpatient_querymodel)
        self.patient_table.resizeColumnsToContents()


if __name__ == '__main__':        # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow('root', 'W950418w')  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

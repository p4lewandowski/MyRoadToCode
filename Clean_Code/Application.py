import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtSql import *
from ApplicationWindow2 import Ui_main_app_window
from sql_show_all import sql_show_all
from mysql_connector import mysql_connector
from sql_find_patient import sql_find_patient
#from LogIn import LogInWindow
import time

class MainWindow(QMainWindow, Ui_main_app_window,sql_show_all,mysql_connector,sql_find_patient):
    def __init__(self,username_cred, userpass_cred):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__() # Inheritance

        #self.LogInInstance = LogInWindow()
        #self.LogInInstance.initUi()
        self.username_cred = 'root'
        self.userpass_cred = 'W950418w'

        # If connected
        self.setupUi(self)

        # Creating database connection
        try:
            self.db_connection = self.mysql_connection()
        except Exception as ex:
            print(ex)

        # Cosmetic settings
        # Setting up icon and window title
        self.setWindowTitle('Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))

        # Inserting the logo
        logo_pic = QLabel('LogoPic')
        logo_pic.setPixmap(QPixmap("RHM_LogoR.png"))


        # Creating table model for patientdata
        self.patienttable_tablemodel = QSqlTableModel()
        self.patienttable_tablemodel.setTable('patientdata')

        # Creating table model for patientexamination
        self.examinationtable_tablemodel = QSqlTableModel()
        self.examinationtable_tablemodel.setTable('patientexamination')

        # Creating query model for patientcredentials
        self.findpatient_querymodel = QSqlQueryModel()

        # Creating query model for patientexaminastion
        self.queryexamination_querymodel = QSqlQueryModel()



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

        # Query examinations
        self.examination_search_button.clicked.connect(self.query_examination)

        # Query examination reset
        self.examination_search_reset_button.clicked.connect(self.query_examination_reset)

        # Show the gui layout
        self.show()

    def query_examination_reset(self):
        self.examinationtable_tablemodel.select()
        self.examination_table.setModel(self.examinationtable_tablemodel)
        self.examination_table.resizeColumnsToContents()
        examination_reset_query = QSqlQuery();
        examination_reset_query.exec_("call Examination_reset");

    def query_examination(self):
        entered_parameter_col_1 = self.parameter_cb_1.currentText()
        entered_operator_1 = self.operator_cb_1.currentText()
        entered_parameter_val_1 = self.parameter_le_1.text()

        exam_args = [entered_parameter_col_1, entered_operator_1, entered_parameter_val_1]
        # if entered_parameter1_operator == '>':
        #     entered_parameter1_operator = '1'
        # elif entered_parameter1_operator == '=':
        #     entered_parameter1_operator = '0'
        # else:
        #     entered_parameter1_operator = '-1'

        # for index, values in enumerate(entered_parameter1_operator):
        #     if entered_parameter1_operator[index] == '>':
        #         entered_parameter1_operator[index] = '1'

        # for index, values in enumerate(exam_args):
        #     if not exam_args[index]:
        #         exam_args[index] = 'Null'

        print(exam_args)

        # Examination_str
        self.queryexamination_querymodel.setQuery("call Examination_int('{}', '{}', '{}')".format(*exam_args))
        self.examination_table.setModel(self.queryexamination_querymodel)
        self.examination_table.resizeColumnsToContents()

        # Examination_reset

        # Examination_str


if __name__ == '__main__':        # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow('root', 'W950418w')  # We set the form to be our ExampleApp (design)
    #form = MainWindow()
    form.show()  # Show the form
    app.exec_()  # and execute the app

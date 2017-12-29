import sys

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox

from RHM_GUI.ApplicationWindow import Ui_main_app_window

from SQL_Tabs.SQL_PatientCredentials import patient_credentials_func
from SQL_Tabs.SQL_PatientExamination import patient_examination_func
from SQL_Tabs.SQL_QueryModelExport import export_query_model



class MainWindow(QMainWindow, Ui_main_app_window, patient_credentials_func, patient_examination_func, export_query_model):

    def __init__(self):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__() # Inheritance

        ################## Initialize the application ##################
        self.setupUi(self)

        ################## Cosmetic settings ##################
        # Setting up icon and window title
        self.setWindowTitle('Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))

        # Inserting the logo
        logo_pic = QLabel('LogoPic')
        logo_pic.setPixmap(QPixmap("RHM_LogoR.png"))

        ################## Table Model Creation ##################
        # Creating table model for patientdata
        self.patienttable_tablemodel = QSqlTableModel()
        self.patienttable_tablemodel.setTable('patientdata')
        # Make it default to show the table
        self.patienttable_tablemodel.select()
        self.patient_table.setModel(self.patienttable_tablemodel)
        self.patient_table.resizeColumnsToContents()

        # Creating table model for patientexamination
        self.examinationtable_tablemodel = QSqlTableModel()
        self.examinationtable_tablemodel.setTable('examination_view')
        # Make it default to show the table
        self.examinationtable_tablemodel.select()
        self.examination_table.setModel(self.examinationtable_tablemodel)
        self.examination_table.resizeColumnsToContents()

        ################## Query Model Creation ##################
        # Creating query model for patientcredentials
        self.findpatient_querymodel = QSqlQueryModel()

        # Creating query model for patientexaminastion
        self.queryexamination_querymodel = QSqlQueryModel()

        ################## Function Calling ##################

        # Find Patient, enable enter
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

        # Add query criteria and create an array to store it
        # Prepare dictionary for possible criteria labels
        self.criteria_labels = dict()
        self.examination_add_criteria_button.clicked.connect(self.examination_add_criteria)
        self.prepared_criteria = []
        self.criteria_index = 1

        # Delete one of the criteria
        #self.examination_remove_criteria_button.clicked.connect(self.examination_criteria_removal)

        # Allow file export with a click of a button
        self.export_tabledata_button.clicked.connect(lambda: self.export_query_examination_data(self.queryexamination_querymodel))
        self.findpatient_export_button.clicked.connect(lambda: self.export_query_examination_data(self.findpatient_querymodel))

        # Show the gui layout
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Session Termination',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':        # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow()  # We set the form to be our ExampleApp (design)
    #form = MainWindow()
    form.show()  # Show the form
    app.exec_()  # and execute the app

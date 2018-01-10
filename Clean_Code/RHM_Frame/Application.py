import sys

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox

from RHM_DataVisualization.Visualization_FunctionCalling import visualization_func_call
from RHM_DataVisualization.Visualization_SteadyPlot import visualization_plot
from RHM_GUI.ApplicationWindow import Ui_main_app_window
from SQL_Tabs.SQL_PatientCredentials import patient_credentials_func
from SQL_Tabs.SQL_PatientExamination import patient_examination_func
from SQL_Tabs.SQL_QueryModelExport import export_query_model


class MainWindow(QMainWindow, Ui_main_app_window, patient_credentials_func, patient_examination_func,
                 export_query_model, visualization_plot, visualization_func_call):

    def __init__(self):
        # Enable access to inherieted variables, methods, classes etc.
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
        self.patienttable_tablemodel.setTable('patientdata_view')
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

        # Creating query model for patientexamination
        self.queryexamination_querymodel = QSqlQueryModel()

        # Creating query model for trends
        self.trend_findpatient_querymodel = QSqlQueryModel()
        self.trend_patient_examination_querymodel = QSqlQueryModel()

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

        # Enable buttons with functions for Trend tab
        self.trend_find_patient_bttn.clicked.connect(self.trend_patientpart)
        # Call plot and define variables
        self.trend_plot_button.released.connect(self.examination_parameter_plotting)

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
    form = MainWindow()  # New instance of application
    form.show()  # Show the form
    app.exec_()  # and execute the app

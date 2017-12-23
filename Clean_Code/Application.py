import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtSql import *
from PyQt5 import QtCore, QtWidgets
from ApplicationWindow2 import Ui_main_app_window
from sql_show_all import sql_show_all
from mysql_connector import mysql_connector
from sql_find_patient import sql_find_patient

#from LogIn import LogInWindow
import time
import csv

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
        # Make it default to show the table
        self.examinationtable_tablemodel.select()
        self.examination_table.setModel(self.examinationtable_tablemodel)
        self.examination_table.resizeColumnsToContents()



        # Creating query model for patientcredentials
        self.findpatient_querymodel = QSqlQueryModel()

        # Creating query model for patientexaminastion
        self.queryexamination_querymodel = QSqlQueryModel()

        ### Calling different functions

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

        # Add query criteria and create an array to store it
        # Prepare dictionary for possible criteria labels
        self.criteria_labels = dict()

        self.examination_add_criteria_button.clicked.connect(self.examination_add_criteria)
        self.prepared_criteria = []
        self.criteria_index = 1

        # Delete one of the criteria
        #self.examination_remove_criteria_button.clicked.connect(self.examination_criteria_removal)

        # Allow file export with the click of a button
        self.export_tabledata_button.clicked.connect(self.export_query_examination_data)



        # Show the gui layout
        self.show()


    def export_query_examination_data(self):

        FILE_NAME = 'export.csv'
        self.exportFile = open(FILE_NAME, 'wt')
        self.writer = csv.writer(self.exportFile)

        # If your don't have header data, Your can delete this section
        listsTmpData = []
        for column in range(self.queryexamination_querymodel.columnCount()):
            listsTmpData.append(str(self.queryexamination_querymodel.headerData(column, QtCore.Qt.Horizontal)))
        self.writer.writerow(listsTmpData)

        # Write file
        for row in range(self.queryexamination_querymodel.rowCount()):
            listsTmpData = []
            for column in range(self.queryexamination_querymodel.columnCount()):
                if str(self.queryexamination_querymodel.record(row).value(column)) == '':
                    listsTmpData.append('')
                    print('!!!')
                else:
                    listsTmpData.append(str(self.queryexamination_querymodel.record(row).value(column)))
                    print(str(self.queryexamination_querymodel.record(row).value(column)))

            self.writer.writerow(listsTmpData)
        self.exportFile.close()


        # FILE_NAME = 'export.csv'
        # self.exportFile = open(FILE_NAME, 'wt')
        # self.writer = csv.writer(self.exportFile)
        # for row in range(self.queryexamination_querymodel.rowCount()):
        #     rowdata = []
        #     for column in range(self.queryexamination_querymodel.columnCount()):
        #         item = self.queryexamination_querymodel.item(row, column)
        #         if item is not None:
        #             rowdata.append(item.text())
        #         else:
        #             rowdata.append('')
        #     self.writer.writerow(rowdata)

        # listsTmpData = []
        #
        # for row in range(self.queryexamination_querymodel.rowCount()):
        #     listsTmpData.append([])
        #     for column in range(self.queryexamination_querymodel.columnCount()):
        #         index = self.queryexamination_querymodel.index(row, column)
        #         # We suppose data are strings
        #         listsTmpData[row].append(str(self.queryexamination_querymodel.data(index).toString()))

    def examination_add_criteria(self):

        entered_parameter_col = self.parameter_cb.currentText()
        entered_operator = self.operator_cb.currentText()
        entered_parameter_val = self.parameter_le.text()

        divider = ' '
        criteria_label_text = (str(self.criteria_index), entered_parameter_col,entered_operator, entered_parameter_val)
        criteria_label_text = divider.join(criteria_label_text)

        criteria_parameters = [entered_parameter_col,entered_operator, entered_parameter_val]
        self.prepared_criteria.append(criteria_parameters)

        name = 'examination_criteria_label_{}'.format(self.criteria_index)
        label = QLabel(self.criteria_container_groupbox)
        label.setObjectName(name)
        label.setText(criteria_label_text)
        label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        label.setMaximumSize(QtCore.QSize(16777215, 25))
        label.setMinimumSize(QtCore.QSize(16777215, 25))
        self.verticalLayout.addWidget(label)
        self.criteria_labels[name] = label

        self.criteria_index += 1

    def query_examination_reset(self):

        self.examinationtable_tablemodel.select()
        self.examination_table.setModel(self.examinationtable_tablemodel)
        self.examination_table.resizeColumnsToContents()
        examination_reset_query = QSqlQuery();
        examination_reset_query.exec_("call Examination_reset") # deleting temporary tables in the database

        # Reset the criteria labels
        for i in range(1, self.criteria_index):
            self.criteria_labels['examination_criteria_label_{}'.format(i)].deleteLater()

        # Reset the criteria index count
        self.criteria_index = 1

        # Empty the criteria with its paremeters
        self.prepared_criteria = []


    def query_examination(self):

        for i in self.prepared_criteria:

            if (i[0] == 'Name' or i[0] == 'Surname' or i[0] == 'Examination Date' or i[0] == 'Parameter Warning'):

                self.queryexamination_querymodel.setQuery("call Examination_str('{}', '{}')".format(i[0], i[2]))
                self.examination_table.setModel(self.queryexamination_querymodel)
                self.examination_table.resizeColumnsToContents()

            else:

                self.queryexamination_querymodel.setQuery("call Examination_int('{}', '{}', '{}')".format(*i))
                self.examination_table.setModel(self.queryexamination_querymodel)
                self.examination_table.resizeColumnsToContents()


if __name__ == '__main__':        # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow('root', 'W950418w')  # We set the form to be our ExampleApp (design)
    #form = MainWindow()
    form.show()  # Show the form
    app.exec_()  # and execute the app

import sys
from PyQt5.QtWidgets import QApplication #QApplication is required to make connection
from mysql_connector import mysql_connector
from PyQt5.QtSql import QSqlQuery
from random import randint
from datetime import datetime, timedelta

class MainWindow(mysql_connector):
    def __init__(self,username_cred, userpass_cred):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__() # Inheritance

        self.username_cred = 'root'
        self.userpass_cred = 'W950418w'

        # Creating database connection
        try:
            self.db_connection = self.mysql_connection()
        except Exception as ex:
            print(ex)

        self.current_day = 1

        # Creating query storing model
        self.insert_data_query = QSqlQuery();

        # Do it some strict number of times
        for i in range(1,3000):

            # random examination type and patient id
            examination_type = randint(1, 3)
            patientID = randint(1, 897)

            # Random time, increasing by strict amount of time per iteration cycle
            examination_date = datetime.now()
            examination_date = examination_date + timedelta(randint(10, 111))
            examination_date = examination_date.strftime("%Y-%m-%d %H:%M:%S")

            if examination_type == 1:
                body_height = randint(150, 200)
                body_weight = randint(45, 140)

                transferred_string = '{}___{}___{}___{}___{}'.format(str(examination_type),str(patientID),str(examination_date),str(body_height),str(body_weight))
                self.Query_execution(transferred_string)


            elif examination_type == 2:
                heart_rate = randint(60, 100)

                transferred_string = '{}___{}___{}___{}'.format(str(examination_type),str(patientID),str(examination_date),str(heart_rate))
                self.Query_execution(transferred_string)

            elif examination_type == 3:
                systolic_p = randint(100, 140)
                diastolic_p = randint(60, 100)

                transferred_string = '{}___{}___{}___{}___{}'.format(str(examination_type),str(patientID),str(examination_date),str(systolic_p),str(diastolic_p))
                self.Query_execution(transferred_string)


        sys.exit()

    def Query_execution(self, transferred_string):
        transferred_string = '{}{}{}'.format("call Examination_data_insert('", transferred_string, "')")
        self.insert_data_query.exec_(transferred_string)


if __name__ == '__main__':        # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow('root', 'W950418w')  # We set the form to be our ExampleApp (design)
    app.exec_()  # and execute the app

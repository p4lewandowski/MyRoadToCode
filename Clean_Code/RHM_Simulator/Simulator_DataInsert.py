import sys
from PyQt5.QtWidgets import QApplication #QApplication is required to make connection
from mysql_connector import mysql_connector
from PyQt5.QtSql import QSqlQuery
from random import randint
from datetime import datetime, timedelta
from time import sleep


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
        insert_data_query = QSqlQuery();

        for i in range(1,31):

            # random examination type
            examination_type = randint(1,3)
            # Random time, increasing
            examination_date = datetime.now()
            examination_date = examination_date + timedelta(randint(10,1111))
            examination_date = examination_date.strftime("%Y-%m-%d %H:%M:%S")
            patientID = randint (1, 57)

            if examination_type == 1:

                body_height = randint(150, 200)
                body_weight = randint(45, 140)
                insert_data_query.exec_("call Data_insert(1,{},'{}', {}, {},0,0,0,'','','','','','')".format(patientID, examination_date, body_height, body_weight))

            elif examination_type == 2:

                heart_rate = randint (60,100)
                insert_data_query.exec_("call Data_insert(2,{},'{}', {}, 0,0,0,0,'','','','','','')".format(patientID, examination_date, heart_rate))

            elif examination_type == 3:

                systolic_p = randint(100, 140)
                diastolic_p = randint(60, 100)
                insert_data_query.exec_("call Data_insert(3,{},'{}', {}, {},0,0,0,'','','','','','')".format(patientID, examination_date, systolic_p, diastolic_p))

        sys.exit()

if __name__ == '__main__':        # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow('root', 'W950418w')  # We set the form to be our ExampleApp (design)
    app.exec_()  # and execute the app

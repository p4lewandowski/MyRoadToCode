import sys
from PyQt5.QtWidgets import QApplication #QApplication is required to make connection
from SQL_Connector.mysql_connector import mysql_connector
from PyQt5.QtSql import QSqlQuery
from random import randint
from datetime import datetime, timedelta


class MainWindow(mysql_connector):
    def __init__(self,username_cred, userpass_cred):

        super(self.__class__, self).__init__()


        # Creating database connection
        try:
            self.db_connection = self.mysql_connection(username_cred, userpass_cred)
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow('root', 'W950418w')
    app.exec_() 

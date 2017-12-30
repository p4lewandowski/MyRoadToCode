from PyQt5.QtWidgets import QApplication #QApplication is required to make connection
from PyQt5.QtSql import QSqlQuery

from SQL_Connector.mysql_connector import mysql_connector

import sys
import datetime

from random import randint
from faker import Faker



class MainWindow(mysql_connector):
    def __init__(self,username_cred, userpass_cred):

        super(self.__class__, self).__init__()

        # Creating database connection
        try:
            self.db_connection = self.mysql_connection(username_cred, userpass_cred)
        except Exception as ex:
            print(ex)

        self.current_day = 1

        # Creating query storing model
        self.insert_data_query = QSqlQuery();

        # Generate random parameters
        # Do it some strict number of times
        for i in range(0,100):

            fakesa = Faker()
            PESEL = randint(10000000000, 99999999999)
            fakesa.birthdate = fakesa.date_between_dates(date_start=datetime.date(1980, 12, 20), date_end=datetime.date(2000, 12, 25))
            fakesa.birthdate = fakesa.birthdate.strftime('%Y-%m-%d')
            fakesa.first_name()
            fakesa.last_name()
            random_gender =['M', 'F']
            fakesa.gender = random_gender[randint(0,1)]
            fakesa.country()
            fakesa.city()
            fakesa.postalcode()
            fakesa.phone_number()

            patient_data = (PESEL, fakesa.birthdate, fakesa.name(), fakesa.last_name(), fakesa.gender, fakesa.country(), fakesa.city(), fakesa.postalcode(), fakesa.phone_number())

            add_patient_query_string = 'INSERT INTO patientcredentials (PESEL,DateOfBirth, Name,SurName,Gender,Country,City,PostalCode,PhoneNumber) VALUES ' + str(patient_data)
            self.insert_data_query.exec_(add_patient_query_string)

        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow('root', 'W950418w')
    app.exec_()

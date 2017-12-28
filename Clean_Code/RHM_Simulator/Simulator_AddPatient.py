import sys
from PyQt5.QtWidgets import QApplication #QApplication is required to make connection
from mysql_connector import mysql_connector
from PyQt5.QtSql import QSqlQuery
from random import randint
from datetime import datetime, timedelta
from faker import Faker
import datetime
from time import strftime
from string import digits

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
        for i in range(1,400):
            fakesa = Faker()

            PESEL = randint(10000000000, 99999999999)

            fakesa.birthdate = fakesa.date_between_dates(date_start=datetime.date(1980, 12, 20), date_end=datetime.date(2000, 12, 25))
            fakesa.birthdate = fakesa.birthdate.strftime('%Y-%m-%d')
            #fakesa.birthdate = str(fakesa.birthdate.split("(", 1)[1])
            #fakesa.birthdate=(fakesa.birthdate[:-1])
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


if __name__ == '__main__':        # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow('root', 'W950418w')  # We set the form to be our ExampleApp (design)
    app.exec_()  # and execute the app

import sys
from PyQt5.QtWidgets import QApplication #QApplication is required to make connection
from PyQt5.QtSql import QSqlQuery
from SQL_Connector.mysql_connector import mysql_connector
from Data_Simulator.Simulator_Sensor import sensor_simulator

class DataInsert(mysql_connector):
    def __init__(self,username_cred, userpass_cred):

        super(self.__class__, self).__init__() #


        #### Creating database connection ####
        try:
            self.db_connection = self.mysql_connection(username_cred, userpass_cred)
        except Exception as ex:
            print(ex)

        self.current_day = 1


        #### Creating query storing model ####
        self.insert_data_query = QSqlQuery();


        #### Do it some strict number of times ####
        for i in range(0,5000):

            sensor_output = sensor_simulator()
            self.Query_execution(sensor_output)

        sys.exit()


    def Query_execution(self, transferred_string):

        # Compared to AddPatient - sensor simulator input uses stored procedure
        transferred_string = '{}{}{}'.format("call Examination_data_insert('", transferred_string, "')")
        self.insert_data_query.exec_(transferred_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = DataInsert('SensorInput', 'SensorInput%') # Data transmitter credentials
    app.exec_()

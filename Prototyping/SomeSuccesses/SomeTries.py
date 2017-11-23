from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
import MainPanel
import sys
from ConfigFileParser import read_db_config
from RHM_LogIn_Class import MySQL_Connection
import ApplicationWindow
import time

class TryingShowing():
    def __init__(self):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()

        db = QSqlDatabase.addDatabase("QMYSQL") #database type!
        db.setHostName("localhost")
        db.setDatabaseName("rhm_database")
        db.setUserName("root")
        db.setPassword("W950418w")
        #db.database('rhm_database')
        #db.setPort(3306)

        print(db.open())

        if (db.open()):
            print('Connected)')
            # qry = QSqlQuery()
            # qry = db.exec("SELECT * FROM patientdata")
            # print (qry.value())
            tablemodel=QSqlQueryModel()
            tablemodel.setQuery("select * from patientdata")
            newtable = QTableView()
            newtable.setModel(tablemodel)
            newtable.show()
            time.sleep(10)
        else:
            print('not Connected')

            ### QSQL MODEL CASE
            # new_query_model = QSqlQueryModel()
            # # new_query_model.setQuery("Call FindPatient(?, ?)",*args)
            # new_query_model.setQuery("SELECT * FROM patientdata")

            ### QSQL QUERY CASE
            # new_query = QSqlQuery
            # new_query.prepare("SELECT * FROM patientdata")
            # new_query.exec()

            # newtable = QTableView()
            # newtable.setModel(new_query_model)
            # newtable.show()
            # # self.main_table.show()


if __name__ == '__main__':              # if we're running file directly and not importing it

    form = TryingShowing()  # We set the form to be our ExampleApp (design)

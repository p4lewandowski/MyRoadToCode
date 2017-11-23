import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import site

app = QApplication(sys.argv)

#site_pack_path = site.getsitepackages()[1]
#app.addLibraryPath('{0}\\PyQt5\\plugins'.format(site_pack_path))
#print(QSqlDatabase.drivers())
#print(db.isDriverAvailable("QMYSQL"))
#db.addDatabase("QMYSQL")

db = QSqlDatabase.addDatabase("QMYSQL")
db.setConnectOptions("SSL_KEY=C:\ProgramData\MySQL\Certificates\client-key.pem;" "SSL_CERT=C:\ProgramData\MySQL\Certificates\client-cert.pem;" "SSL_CA=C:\ProgramData\MySQL\Certificates\ca-cert.pem");
db.setHostName("localhost")
db.setPort(3306)
db.setDatabaseName("rhm_database")
db.setUserName("root")
db.setPassword("W950418w")
db.open() # not sure if needed

if not db.open():
    print("Database Connection Error", "Database Error: %s" % db.lastError().text())
else:
    print('working')

query = QSqlQuery(db)
query.exec("select Name, SurName from patientcredentials")
while (query.next()):
    print(query.value(0), query.value(1))



new_query_model = QSqlQueryModel()
new_query_model.setQuery("select * from patientcredentials",db)

projectView = QTableView()
projectView.setModel(new_query_model)
projectView.show()

# # WORKS
# projectModel = QSqlTableModel()
# projectModel.setTable("patientcredentials")
# projectModel.select()
# projectView = QListView()
# projectView.setModel(projectModel)
# projectView.setModelColumn(3)
# projectView.show()



app.exec_()
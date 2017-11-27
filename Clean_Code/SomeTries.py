# Connection settings
from ConfigFileParser import read_db_config
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtSql import *

username_cred = 'root'
userpass_cred = 'W950418w'
db_config = read_db_config()
db_config['user'] = username_cred
db_config['password'] = userpass_cred


# print "dsada {}".format('dasda')
# print 'SSL_KEY="{};" SSL_CERT="{};" SSL_CA="{};"'.format(db_config['ssl_key'], db_config['ssl_cert'], db_config['ssl_ca'])
print('SSL_KEY='+db_config['ssl_key'], 'SSL_CERT='+db_config['ssl_cert'], 'SSL_CA='+db_config['ssl_ca'])

s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print (s.join( seq ))


# ### QtSQL Connection
# db = QSqlDatabase.addDatabase("QMYSQL")
# db.setConnectOptions(
#     "SSL_KEY=C:\ProgramData\MySQL\Certificates\client-key.pem;" "SSL_CERT=C:\ProgramData\MySQL\Certificates\client-cert.pem;" "SSL_CA=C:\ProgramData\MySQL\Certificates\ca-cert.pem");
# db.setHostName(db_config['host'])
# db.setPort(int(db_config['port']))
# db.setDatabaseName(db_config['database'])
# db.setUserName(db_config['user'])
# db.setPassword(db_config['password'])
# print(db.open())  # not sure if needed


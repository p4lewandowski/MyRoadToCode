import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from RHM_Frame import AuxiliaryFunctions
from RHM_Frame.Application import MainWindow
from SQL_Connector.mysql_connector import mysql_connector


class LogInWindow(QWidget, mysql_connector):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Creating window and centering it
        #self.resize(500, 350)
        # Setting up icon and window title
        self.setWindowTitle('Log in to Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))
        AuxiliaryFunctions.center(self)
        # self.setWindowModality(Qt.ApplicationModal)


        # Specyfying the font for WelcomeLabel
        welcome_font = QFont()
        welcome_font.setPixelSize(15)
        welcome_font.setBold(True)

        # Creating the labels and edits
        welcome_label = QLabel('WELCOME \n\n Please provide your credentials to connect to the database.')
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setFont(welcome_font)
        username_label = QLabel('Username')
        username_label.setAlignment(Qt.AlignCenter)
        password_label = QLabel('Password')
        password_label.setAlignment(Qt.AlignCenter)
        self.username_edit = QLineEdit(self)
        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.Password)

        #Enabling 'ENTER' key
        self.username_edit.returnPressed.connect(self.passing_credentials)
        self.password_edit.returnPressed.connect(self.passing_credentials)

        # Inserting the logo
        logo_pic = QLabel('LogoPic')
        logo_pic.setPixmap(QPixmap("RHM_LogoR.png"))

        # Creating the Buttons
        log_in_button = QPushButton("Log In", self)
        log_in_button.clicked.connect(self.passing_credentials)
        exit_button = QPushButton("Exit", self)
        exit_button.clicked.connect(QCoreApplication.instance().quit)

        # Preparing the layout
        log_layout = QGridLayout(self)
        log_layout.setSpacing(10)

        log_layout.addWidget(welcome_label, 0, 0, 2, 10)
        log_layout.addWidget(logo_pic, 1, 0, 10, 6)
        log_layout.addWidget(username_label,2,7)
        log_layout.addWidget(self.username_edit,3, 7)
        log_layout.addWidget(password_label, 4, 7)
        log_layout.addWidget(self.password_edit, 5, 7)
        log_layout.addWidget(log_in_button,7, 7)
        log_layout.addWidget(exit_button,10,7)

        self.setLayout(log_layout)
        self.show()

    def passing_credentials(self):
        username_cred = self.username_edit.text()
        userpass_cred = self.password_edit.text()
        _, connection_status = self.mysql_connection(username_cred, userpass_cred)

        # If credentials allright go to application
        if connection_status == True:
            self.hide()
            self.new_connection = MainWindow(username_cred, userpass_cred)


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Session Termination',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LogInWindow()
    sys.exit(app.exec_())

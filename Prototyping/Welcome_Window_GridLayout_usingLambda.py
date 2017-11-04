import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import RHM_LoggingIn

# RHM_LoggingIn
#
# def Logging_in (UserName, UserPassword):
#     print (UserName, UserPassword)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Creating window and centering it
        self.resize(600, 350)
        self.center()
        self.setWindowTitle('Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))

        # Specyfying the font for WelcomeLabel
        WelcomeFont = QFont()
        WelcomeFont.setBold(True)

        # Creating the labels and edits
        Welcome = QLabel('WELCOME \n\n Please provide your credentials to connect to the database.')
        Welcome.setAlignment(Qt.AlignCenter)
        Welcome.setFont(WelcomeFont)
        Username = QLabel('Username')
        Username.setAlignment(Qt.AlignCenter)
        Password = QLabel('Password')
        Password.setAlignment(Qt.AlignCenter)
        UsernameEdit = QLineEdit(self)
        PasswordEdit = QLineEdit(self)
        PasswordEdit.setEchoMode(QLineEdit.Password)

        # Inserting the logo
        LogoPic = QLabel('LogoPic')
        LogoPic.setPixmap(QPixmap("RHM_LogoR.png"))

        # Creating the Buttons
        LogMeInButton = QPushButton("Log In", self)
        LogMeInButton.clicked.connect(lambda: RHM_LoggingIn.Logging_in(UsernameEdit.text(),PasswordEdit.text()))
        ExitButton = QPushButton("Exit", self)
        ExitButton.clicked.connect(QCoreApplication.instance().quit)
        #LogMeInButton.setMaximumSize(300,100)
        #ExitButton.setMaximumSize(300,100)

        # Preparing the layout
        LogScreenLayout = QGridLayout(self)
        LogScreenLayout.setSpacing(10)

        LogScreenLayout.addWidget(Welcome, 0, 0, 2, 10)
        LogScreenLayout.addWidget(LogoPic, 1, 0, 10, 6)
        LogScreenLayout.addWidget(Username,2,7)
        LogScreenLayout.addWidget(UsernameEdit,3, 7)
        LogScreenLayout.addWidget(Password, 4, 7)
        LogScreenLayout.addWidget(sPasswordEdit, 5, 7)
        LogScreenLayout.addWidget(LogMeInButton,7, 7)
        LogScreenLayout.addWidget(ExitButton,10,7)


        self.setLayout(LogScreenLayout)
        self.show()



    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
    ex = Example()
    sys.exit(app.exec_())
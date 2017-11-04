import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import RHM_LoggingIn
import AuxiliaryFunctions


class LogInWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Creating window and centering it
        self.resize(500, 350)
        AuxiliaryFunctions.center(self)
        self.setWindowTitle('Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))

        # Specyfying the font for WelcomeLabel
        WelcomeFont = QFont()
        WelcomeFont.setPixelSize(15)
        WelcomeFont.setBold(True)

        # Creating the labels and edits
        Welcome = QLabel('WELCOME \n\n Please provide your credentials to connect to the database.')
        Welcome.setAlignment(Qt.AlignCenter)
        Welcome.setFont(WelcomeFont)
        Username = QLabel('Username')
        Username.setAlignment(Qt.AlignCenter)
        Password = QLabel('Password')
        Password.setAlignment(Qt.AlignCenter)
        self.UsernameEdit = QLineEdit(self)
        self.PasswordEdit = QLineEdit(self)
        self.PasswordEdit.setEchoMode(QLineEdit.Password)

        # Inserting the logo
        LogoPic = QLabel('LogoPic')
        LogoPic.setPixmap(QPixmap("RHM_LogoR.png"))

        # Creating the Buttons
        LogMeInButton = QPushButton("Log In", self)
        #LogMeInButton.clicked.connect(lambda: RHM_LoggingIn.Logging_in(UsernameEdit.text(),PasswordEdit.text()))
        LogMeInButton.clicked.connect(self.PassingCredentials)
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
        LogScreenLayout.addWidget(self.UsernameEdit,3, 7)
        LogScreenLayout.addWidget(Password, 4, 7)
        LogScreenLayout.addWidget(self.PasswordEdit, 5, 7)
        LogScreenLayout.addWidget(LogMeInButton,7, 7)
        LogScreenLayout.addWidget(ExitButton,10,7)


        self.setLayout(LogScreenLayout)
        self.show()

    def PassingCredentials(self):
        UserName = self.UsernameEdit.text()
        UserPassword = self.PasswordEdit.text()
        RHM_LoggingIn.CallAuthentication(UserName, UserPassword)

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
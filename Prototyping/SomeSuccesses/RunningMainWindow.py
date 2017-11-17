from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import MainPanel
import sys


class RunMainWindow(QMainWindow, MainPanel.Ui_MainWindow):
    def __init__(self):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Setting up icon and window title
        self.setWindowTitle('Remote Health Monitoring System')
        self.setWindowIcon(QIcon('Cardiology.png'))

        # Inserting the logo
        LogoPic = QLabel('LogoPic')
        LogoPic.setPixmap(QPixmap("RHM_LogoR.png"))

        self.FindPatientButton.clicked.connect(self.CallFindPatient)

    def CallFindPatient(self):
        entered_name = self.NameLineEdit.text()
        entered_surname = self.SurnameLineEdit.text()
        entered_pesel = self.PESELLineEdit.text()
        print(entered_name,entered_surname,entered_pesel)




if __name__ == '__main__':              # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = RunMainWindow()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

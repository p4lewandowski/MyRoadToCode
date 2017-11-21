import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from RHM_LogIn import connect
import AuxiliaryFunctions
from RHM_LogIn_Class import MySQL_Connection
from RunningMainWindow import RunMainWindow
from Welcome_Window_GridLayout import LogInWindow
from RunningMainWindow import RunMainWindow

class MainWindow():
    def __init__(self):
        # ^ double underscore (dunder) methods are usually special.  This one
        #  gets called immediately after a new instance is created.
        #super(self.__class__, self).__init__()
        #print (self.UserPassword)
        self.newConnection = LogInWindow()

        self.MainWindowInstance = RunMainWindow()
        #self.MainWindowInstance.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    sys.exit(app.exec_())
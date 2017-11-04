import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QMainWindow
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import AuxiliaryFunctions



class LoadingWindowInstance(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Creating window and centering it
        self.resize(220, 130)
        AuxiliaryFunctions.center(self)
        self.setWindowTitle('Loading')
        self.setWindowIcon(QIcon('Cardiology.png'))

        # Specyfying the font
        CommunicatingFont = QFont()
        CommunicatingFont.setBold(True)
        CommunicatingFont.setPixelSize(30)
        CommunicatingInfo = QLabel(' LOADING\n\n PLEASE WAIT', self)
        CommunicatingInfo.setAlignment(Qt.AlignCenter)
        CommunicatingInfo.setFont(CommunicatingFont)

        self.show()

        def close(self):
            for childQWidget in self.findChildren(QWidget):
                childQWidget.close()
            self.isDirectlyClose = True
            return QMainWindow.close(self)

        def closeEvent(self, eventQCloseEvent):
            if self.isDirectlyClose:
                eventQCloseEvent.accept()
            else:
                answer = QMessageBox.question(
                    self,
                    'Are you sure you want to quit ?',
                    'Task is in progress !',
                    QMessageBox.Yes,
                    QMessageBox.No)
                if (answer == QMessageBox.Yes) or (self.isDirectlyClose == True):
                    eventQCloseEvent.accept()
                else:
                    eventQCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoadingWindowInstance()
    sys.exit(app.exec_())
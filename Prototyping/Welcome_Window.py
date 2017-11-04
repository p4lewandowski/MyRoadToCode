import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication



class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(600, 350)
        self.center()

        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('Cardiology.png'))

        LogMeInButton = QPushButton("Log In", self)
        ExitButton = QPushButton("Exit", self)
        ExitButton.clicked.connect(QCoreApplication.instance().quit)


        CustomLayoutH = QHBoxLayout()
        CustomLayoutH.addWidget(LogMeInButton)
        CustomLayoutH.addWidget(ExitButton)

        CustomLayoutV =QVBoxLayout()
        CustomLayoutV.addStretch(1)
        CustomLayoutV.addLayout(CustomLayoutH)

        self.setLayout(CustomLayoutV)

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
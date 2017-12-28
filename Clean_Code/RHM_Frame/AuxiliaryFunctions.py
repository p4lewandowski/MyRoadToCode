from PyQt5.QtWidgets import QDesktopWidget, QMessageBox

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
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Virneal\Documents\IFE\Bachelor_code\Prototyping\SomeSuccesses\MainPanel.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(868, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 90, 158, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.NameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.NameLabel.setObjectName("NameLabel")
        self.gridLayout.addWidget(self.NameLabel, 3, 0, 1, 1)
        self.PESELLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PESELLabel.setObjectName("PESELLabel")
        self.gridLayout.addWidget(self.PESELLabel, 7, 0, 1, 1)
        self.SurnameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.SurnameLabel.setObjectName("SurnameLabel")
        self.gridLayout.addWidget(self.SurnameLabel, 4, 0, 1, 1)
        self.NameLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.NameLineEdit.setText("")
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.gridLayout.addWidget(self.NameLineEdit, 3, 1, 1, 1)
        self.PESELLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PESELLineEdit.setText("")
        self.PESELLineEdit.setObjectName("PESELLineEdit")
        self.gridLayout.addWidget(self.PESELLineEdit, 7, 1, 1, 1)
        self.SurnameLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SurnameLineEdit.setText("")
        self.SurnameLineEdit.setObjectName("SurnameLineEdit")
        self.gridLayout.addWidget(self.SurnameLineEdit, 4, 1, 1, 1)
        self.FindPatientButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.FindPatientButton.setObjectName("FindPatientButton")
        self.gridLayout.addWidget(self.FindPatientButton, 2, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(260, 90, 511, 461))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.GeneralTable = QtWidgets.QTableView(self.gridLayoutWidget_2)
        self.GeneralTable.setObjectName("GeneralTable")
        self.gridLayout_2.addWidget(self.GeneralTable, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NameLabel.setText(_translate("MainWindow", "Name"))
        self.PESELLabel.setText(_translate("MainWindow", "Pesel"))
        self.SurnameLabel.setText(_translate("MainWindow", "Surname"))
        self.FindPatientButton.setText(_translate("MainWindow", "Find Patient"))


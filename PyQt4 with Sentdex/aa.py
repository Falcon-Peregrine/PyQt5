# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qt_tut(object):
    def setupUi(self, Qt_tut):
        Qt_tut.setObjectName("Qt_tut")
        Qt_tut.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Qt_tut)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 59, 151, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setEnabled(True)
        self.listView.setGeometry(QtCore.QRect(265, 321, 181, 121))
        self.listView.setObjectName("listView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 70, 141, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)
        self.pushButton_666 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_666.setObjectName("pushButton_666")
        self.verticalLayout.addWidget(self.pushButton_666)
        Qt_tut.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Qt_tut)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Qt_tut.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Qt_tut)
        self.statusbar.setObjectName("statusbar")
        Qt_tut.setStatusBar(self.statusbar)

        self.retranslateUi(Qt_tut)
        QtCore.QMetaObject.connectSlotsByName(Qt_tut)

    def retranslateUi(self, Qt_tut):
        _translate = QtCore.QCoreApplication.translate
        Qt_tut.setWindowTitle(_translate("Qt_tut", "MainWindow"))
        self.pushButton.setText(_translate("Qt_tut", "PushButton"))
        self.checkBox.setText(_translate("Qt_tut", "CheckBox"))
        self.pushButton_2.setText(_translate("Qt_tut", "PushButton"))
        self.toolButton.setText(_translate("Qt_tut", "..."))
        self.pushButton_666.setText(_translate("Qt_tut", "PushButton"))


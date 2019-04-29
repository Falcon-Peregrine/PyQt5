# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Qt_tut(object):
    def setupUi(self, Qt_tut):
        Qt_tut.setObjectName(_fromUtf8("Qt_tut"))
        Qt_tut.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Qt_tut)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 59, 151, 131))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setEnabled(True)
        self.listView.setGeometry(QtCore.QRect(265, 321, 181, 121))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 70, 141, 191))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolButton = QtGui.QToolButton(self.verticalLayoutWidget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.verticalLayout.addWidget(self.toolButton)
        self.pushButton_666 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_666.setObjectName(_fromUtf8("pushButton_666"))
        self.verticalLayout.addWidget(self.pushButton_666)
        Qt_tut.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Qt_tut)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Qt_tut.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Qt_tut)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Qt_tut.setStatusBar(self.statusbar)

        self.retranslateUi(Qt_tut)
        QtCore.QMetaObject.connectSlotsByName(Qt_tut)

    def retranslateUi(self, Qt_tut):
        Qt_tut.setWindowTitle(_translate("Qt_tut", "MainWindow", None))
        self.pushButton.setText(_translate("Qt_tut", "PushButton", None))
        self.checkBox.setText(_translate("Qt_tut", "CheckBox", None))
        self.pushButton_2.setText(_translate("Qt_tut", "PushButton", None))
        self.toolButton.setText(_translate("Qt_tut", "...", None))
        self.pushButton_666.setText(_translate("Qt_tut", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Qt_tut = QtGui.QMainWindow()
    ui = Ui_Qt_tut()
    ui.setupUi(Qt_tut)
    Qt_tut.show()
    sys.exit(app.exec_())


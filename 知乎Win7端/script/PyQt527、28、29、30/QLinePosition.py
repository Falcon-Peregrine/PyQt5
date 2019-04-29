
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QApplication, QAction, QDialog,QMessageBox
from PyQt5.QtGui import QIcon

import sys
class Line(QDialog):
    def __init__(self):
        super().__init__()
        self.Ui()

    def Ui(self):
        self.line = QLineEdit(self)
        self.line.move(20,20)
        action = QAction(self)
        action.setIcon(QIcon('check.ico'))
        action.triggered.connect(self.Check)
        self.line.addAction(action,QLineEdit.TrailingPosition)

    def Check(self):
        word = self.line.text()
        if correct(word) != word:
            QMessageBox.information(self,'提示信息','你或许想要表达的单词是：'+correct(word))
        else:
            QMessageBox.information(self,'提示信息','你填写的单词是：'+word)

app = QApplication(sys.argv)
ex = Line()
sys.exit(app.exec_())
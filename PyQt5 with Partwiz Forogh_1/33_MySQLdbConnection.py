# pip install mysqlclient==1.3.12﻿
# install win-32 version of XAMPP

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys
import MySQLdb as mdb

class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Connecting DataBase"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500
		self.InitWindow()


	def InitWindow(self):
		self.button = QPushButton('DB Connection Status', self)
		self.button.setGeometry(100,100,200,50)
		self.button.clicked.connect(self.connectDB)


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

	def connectDB(self):
		try:
			db = mdb.connect('localhost', 'pyqt5', ) # the second and third para not written, cause not username and psswd required 
			QMessageBox.about(self, 'Connection', 'Successfully Connected to DB')

		except mdb.Error as e:
			QMessageBox.about(self, 'Connection', 'Not Successfully Connected')
			sys.exit(1)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
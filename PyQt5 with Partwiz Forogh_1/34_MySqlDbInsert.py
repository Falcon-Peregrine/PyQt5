from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QMessageBox
import sys
import MySQLdb as mdb

class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Insert Data"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500
		self.InitWindow()


	def InitWindow(self):
		
		self.lineedit1 = QLineEdit(self)
		self.lineedit1.setPlaceholderText("Please Enter Your Name")
		self.lineedit1.setGeometry(200,100,200,30)

		self.lineedit2 = QLineEdit(self)
		self.lineedit2.setPlaceholderText("Please Enter Your Email")
		self.lineedit2.setGeometry(200,150,200,30)

		self.lineedit3 = QLineEdit(self)
		self.lineedit3.setPlaceholderText("Please Enter Your Phone")
		self.lineedit3.setGeometry(200,200,200,30)

		self.button = QPushButton("Insert Data", self)
		self.button.setGeometry(200,250,100,30)
		self.button.clicked.connect(self.InsertData)


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

	def InsertData(self):
		con = mdb.connect('localhost', 'pyqt5') # root , passwd not written
		with con:
			cur = con.cursor()

			cur.execute("INSERT INTO data(name, email, phone)"
				"VALUES('%s', '%s', '%s')" % (''.join(self.lineedit1.text()),
				 ''.join(self.lineedit2.text()),
				  ''.join(self.lineedit3.text())))

			QMessageBox.about(self, 'Connection', 'Data Inserted Successfully')
			self.close()






App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys

class Window(QWidget):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Tables"
		self.top = 100
		self.left = 100
		self.width = 500
		self.height = 400
		self.InitWindow()


	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))

		self.creatingTables()
		self.vBoxLayout = QVBoxLayout()
		self.vBoxLayout.addWidget(self.tableWidget)
		self.setLayout(self.vBoxLayout)
		self.show()

	def creatingTables(self):
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(5)
		self.tableWidget.setColumnCount(3)
		
		self.tableWidget.setItem(0,0,QTableWidgetItem("Name"))
		self.tableWidget.setItem(0,1,QTableWidgetItem("Email"))
		self.tableWidget.setItem(0,2,QTableWidgetItem("PhoneNo."))
		
		self.tableWidget.setItem(1,0,QTableWidgetItem("Falcon"))
		self.tableWidget.setItem(1,1,QTableWidgetItem("Falcon01235@gmail.com"))
		self.tableWidget.setItem(1,2,QTableWidgetItem("1656566"))
		self.tableWidget.setColumnWidth(1,200) # set the first column width to 200

		self.tableWidget.setItem(2,0,QTableWidgetItem("Ness"))
		self.tableWidget.setItem(2,1,QTableWidgetItem("callmeness@gmail.com"))
		self.tableWidget.setItem(2,2,QTableWidgetItem("65989896"))

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
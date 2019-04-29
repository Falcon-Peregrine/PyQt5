from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QGroupBox
import sys

class Window(QDialog):  # Inherite from QDialog, and it runs normally
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Layouts"
		self.top = 100
		self.left = 100
		self.width = 300
		self.height = 100
		self.InitWindow()


	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.HorizontalLayout()
		

		
		self.show()

	def HorizontalLayout(self):
		self.groupBox = QGroupBox("What Is Your Favorite Sport?")
		hBoxlayout =QHBoxLayout()
		
		button1 = QPushButton("Football", self)
		button1.clicked.connect(self.button1Clicked)
		hBoxlayout.addWidget(button1)

		button2 = QPushButton("Criket", self)
		button2.clicked.connect(self.button2Clicked)
		hBoxlayout.addWidget(button2)
		
		button3 = QPushButton("Tennis", self)
		button3.clicked.connect(self.button3Clicked)
		hBoxlayout.addWidget(button3)

		self.groupBox.setLayout(hBoxlayout)

		vBox = QVBoxLayout()
		vBox.addWidget(self.groupBox)
		self.setLayout(vBox)

	def button1Clicked(self):
		QMessageBox.information(self, "Football", "Yes I Like Football")

	def button2Clicked(self):
		QMessageBox.information(self, "Criket", "Yes I Like Criket")

	def button3Clicked(self):
		QMessageBox.information(self, "Tennis", "Yes I Like Tennis")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
		

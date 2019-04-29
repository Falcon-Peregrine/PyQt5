from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout
import sys

class Window(QDialog):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 GridLayout"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500
		self.InitWindow()


	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))

		self.gridLayoutCreation()
		self.show()

	def gridLayoutCreation(self):
		
		gridLayout = QGridLayout()

		gridLayout.addWidget(QPushButton('1'), 0, 0)
		gridLayout.addWidget(QPushButton('2'), 0, 1)
		gridLayout.addWidget(QPushButton('3'), 0, 2)
		gridLayout.addWidget(QPushButton('4'), 1, 0)
		gridLayout.addWidget(QPushButton('5'), 1, 1)
		gridLayout.addWidget(QPushButton('6'), 1, 2)
		
		self.groupBox = QGroupBox("Grid Layout Example")
		self.groupBox.setLayout(gridLayout)
		
		vboxLayout = QVBoxLayout()
		vboxLayout.addWidget(self.groupBox)
		self.setLayout(vboxLayout)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
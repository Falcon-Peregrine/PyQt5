from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Image"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500
		self.InitWindow()


	def InitWindow(self):
		self.label = QLabel(self)
		self.label.setPixmap(QPixmap('./icon/shore.jpg'))
		self.label.setGeometry(0,0,1920,1080)

		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
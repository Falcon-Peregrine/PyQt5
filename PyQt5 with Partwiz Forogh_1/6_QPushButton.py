import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.title = "PyQt5 Push Button"
		self.left = 100
		self.top = 100
		self.width = 680
		self.height = 540

		button = QPushButton("Click Me", self)
		button.move(200,200)
		button.setToolTip("<h3>This Is A QPushButton</h3>") # <h3></h3> is a HTML Tag


		self.InitUI()

	def InitUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon("./icon/icon.png"))

		self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())

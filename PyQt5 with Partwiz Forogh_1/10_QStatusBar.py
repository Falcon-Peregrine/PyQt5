import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title = "QStatus Bar"
		self.top = 200
		self.left = 200
		self.width = 600
		self.height = 500
		self.InitUI()

	def InitUI(self):
		self.statusBar().showMessage("This is Simple Status Bar")
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
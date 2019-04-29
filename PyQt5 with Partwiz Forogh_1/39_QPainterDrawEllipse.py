from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen 
from PyQt5.QtCore import Qt 
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Draw Ellipse"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500
		self.InitWindow()


	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

	def paintEvent(self, e):
		painter = QPainter(self)
		painter.setPen(QPen(Qt.blue, 8, Qt.SolidLine))
		# painter.setPen(QPen(Qt.blue, 8, Qt.DashLine))
		# painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
		painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))

		painter.drawEllipse(100,100,400,200)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
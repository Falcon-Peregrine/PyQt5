from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygon
from PyQt5.QtCore import Qt, QPoint
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Drawing Polygon"
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

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
		# painter.setBrush(QBrush(Qt.red, Qt.VerPattern))


		points = QPolygon([
			QPoint(10,10),
			QPoint(10,100),
			QPoint(100,10),
			QPoint(100,100)
			])

		painter.drawPolygon(points)





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
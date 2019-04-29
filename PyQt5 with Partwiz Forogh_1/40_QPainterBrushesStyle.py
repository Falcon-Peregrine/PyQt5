from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
import sys
from PyQt5.QtCore import Qt 

class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Window"
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

	def paintEvent(self, event): # overwrite paint event
		painter = QPainter(self)
		painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))
		painter.drawRect(10,100,150,100)

		painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.red, Qt.Dense1Pattern))
		painter.drawRect(180,100,150,100)

		painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.red, Qt.HorPattern))
		painter.drawRect(350,100,150,100)

		painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.red, Qt.VerPattern))
		painter.drawRect(10,220,150,100)


		painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.red, Qt.BDiagPattern))
		painter.drawRect(180,220,150,100)

		painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.red, Qt.Dense4Pattern))
		painter.drawRect(350,220,150,100)

		painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.red, Qt.Dense4Pattern))
		painter.drawRect(10,340,150,100)





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
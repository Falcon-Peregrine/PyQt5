from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
import sys
from PyQt5.QtGui import QBrush, QPen
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
		
		scene = QGraphicsScene(self)
		redBrush = QBrush(Qt.red)
		blueBrush = QBrush(Qt.blue)
		blackPen = QPen(Qt.black)
		blackPen.setWidth(7)

		ellipse = scene.addEllipse(10,10,200,200, blackPen, redBrush)
		rect = scene.addRect(-100,-100,200,200, blackPen, blueBrush)

		ellipse.setFlag(QGraphicsItem.ItemIsMovable) # set it to movable
		rect.setFlag(QGraphicsItem.ItemIsMovable)

		view = QGraphicsView(scene, self)
		view.setGeometry(0,0,680,500)


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
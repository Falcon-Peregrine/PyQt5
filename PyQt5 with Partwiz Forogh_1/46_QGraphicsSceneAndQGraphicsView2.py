from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem, QPushButton
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

		self.button1 = QPushButton("Rotate - ", self)
		self.button1.setGeometry(200,420,100,50)
		self.button1.clicked.connect(self.rotateMinus)

		self.button2 = QPushButton("Rotate +", self)
		self.button2.setGeometry(400,420,100,50)
		self.button2.clicked.connect(self.rotatePlus)

		scene = QGraphicsScene(self)
		redBrush = QBrush(Qt.red)
		blueBrush = QBrush(Qt.blue)
		blackPen = QPen(Qt.black)
		blackPen.setWidth(7)

		ellipse = scene.addEllipse(10,10,200,200, blackPen, redBrush)
		rect = scene.addRect(-100,-100,200,200, blackPen, blueBrush)

		ellipse.setFlag(QGraphicsItem.ItemIsMovable) # set it to movable
		rect.setFlag(QGraphicsItem.ItemIsMovable)

		self.view = QGraphicsView(scene, self)
		self.view.setGeometry(0,0,680,400)


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

	def rotateMinus(self):
		self.view.rotate(-10)

	def rotatePlus(self):
		self.view.rotate(10)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
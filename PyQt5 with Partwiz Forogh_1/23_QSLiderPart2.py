from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QWidget
from PyQt5.QtGui import QPixmap
import sys

class Window(QWidget):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Slider Part2"
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 300
		self.InitWindow()


	def InitWindow(self):

		self.slider = QSlider(Qt.Horizontal, self)
		self.slider.setGeometry(60,60,100,20)
		self.slider.valueChanged[int].connect(self.ChangedValue)

		self.label = QLabel(self)
		self.label.setPixmap(QPixmap('./icon/pocketmon.png'))
		self.label.setGeometry(60,100,150,150)

		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

	def ChangedValue(self, value): # self.slider.valueChanged will generate signal
		print(value)
		if value == 0:
			self.label.setPixmap(QPixmap('./icon/pocketmon.png'))
		elif value < 50:
			self.label.setPixmap(QPixmap('./icon/bitcoin.png'))
		else:
			self.label.setPixmap(QPixmap('./icon/mail.png'))

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
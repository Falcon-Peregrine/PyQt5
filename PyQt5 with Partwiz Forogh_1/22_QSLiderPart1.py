from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QSlider, QVBoxLayout
import sys

class Window(QMainWindow): # also can inherite from QWidget
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Slider Part One"
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 200
		self.InitWindow()


	def InitWindow(self):

		vboxLayout = QVBoxLayout()
		self.lineEdit = QLineEdit(self)
		vboxLayout.addWidget(self.lineEdit)
		self.lineEdit.move(100, 50)


		self.slider = QSlider(Qt.Horizontal, self)
		self.slider.move(100, 20)
		self.slider.setMinimum(1)
		self.slider.setMaximum(99)
		self.slider.setValue(20)  # default value
		self.slider.setTickPosition(QSlider.TicksBelow) # show the scale
		self.slider.setTickInterval(10)
		vboxLayout.addWidget(self.slider)
		self.slider.valueChanged.connect(self.changedValue)


		self.slider2 = QSlider(Qt.Vertical, self)
		self.slider2.move(50,100)


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

	def changedValue(self):
		size = str(self.slider.value()) # QLineEdit does not accept int value
		self.lineEdit.setText(size)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
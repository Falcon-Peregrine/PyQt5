from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QLabel, QVBoxLayout, QHBoxLayout, QDoubleSpinBox
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 SpinBox"
		self.top = 100
		self.left = 100
		self.width = 300
		self.height = 200
		self.InitWindow()


	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))

		vBoxLayout = QVBoxLayout()


		self.label = QLabel("Current Value", self)
		self.label.move(60,60)
		
		self.spinBox = QDoubleSpinBox(self) # QSpinBox or QDoubleSpinBox
		self.spinBox.move(60,30)
		
		vBoxLayout.addWidget(self.label)
		vBoxLayout.addWidget(self.spinBox)
		self.spinBox.valueChanged.connect(self.valueChanged)
		self.spinBox.setMinimum(10)
		self.spinBox.setMaximum(20)

		self.show()

	def valueChanged(self):
		self.label.setText("Current Value: " + str(self.spinBox.value()))

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
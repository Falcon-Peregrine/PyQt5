from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
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
		checkBox = QCheckBox("Do you Like Football ?", self)
		checkBox.move(100,100)
		checkBox.toggle() # 打勾
		checkBox.stateChanged.connect(self.checkBoxChanged)

		self.label = QLabel("Hello", self)
		self.label.move(100,150)
		
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

	def checkBoxChanged(self, state): #PyQt5.Qtcore.Qt
		if state == Qt.Checked:
			self.label.setText('Yes I Like Football')
		else:
			self.label.setText("No I Don't Like It")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())

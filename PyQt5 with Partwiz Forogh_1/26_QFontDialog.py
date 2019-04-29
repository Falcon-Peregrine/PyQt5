from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFontDialog, QPushButton, QTextEdit
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 FontDialog"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500
		self.InitWindow()


	def InitWindow(self):

		self.button = QPushButton("Open Font Dialog", self)
		self.button.setGeometry(100,100,120,50)
		self.button.clicked.connect(self.createFontDialog)
		self.textEdit = QTextEdit(self)
		self.textEdit.setGeometry(100,150,200,200)

		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

	def createFontDialog(self):
		font, ok = QFontDialog.getFont()
		if ok:
			self.textEdit.setFont(font)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
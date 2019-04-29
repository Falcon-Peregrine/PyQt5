from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
import sys
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog

class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		self.title = "PyQt5 Print Dialog"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500
		self.InitWindow()


	def InitWindow(self):
		self.button = QPushButton("Print", self)
		self.button.setGeometry(100,100,100,50)
		self.button.clicked.connect(self.createPrintDialog)

		self.button2 = QPushButton("Print Preview", self)
		self.button2.setGeometry(200,100,100,50)
		self.button2.clicked.connect(self.printPreviewDialog)

		self.textEdit = QTextEdit(self)
		self.textEdit.setGeometry(100,150,150,200)


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/icon.png'))
		self.show()

	def createPrintDialog(self):
		printer = QPrinter(QPrinter.HighResolution)
		dialog = QPrintDialog(printer, self)

		if dialog.exec_() == QPrintDialog.Accepted:
			self.textEdit.print_(printer)

	def printPreviewDialog(self):
		printer = QPrinter(QPrinter.HighResolution)
		previewDialog = QPrintPreviewDialog(printer, self)
		previewDialog.paintRequested.connect(self.printPreview)
		previewDialog.exec_()

	def printPreview(self, printer):
		self.textEdit.print(printer)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys

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

		exitAct = QAction(QIcon('./icon/exit.png'), 'Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(self.CloseApp)

		mailAct = QAction(QIcon('./icon/mail.png'), 'mail', self)
		mailAct.setShortcut('Ctrl+M')

		coinAct = QAction(QIcon('./icon/bitcoin.png'), 'bitcoin', self)
		coinAct.setShortcut('Ctrl+B')

		packAct = QAction(QIcon('./icon/pack.png'), 'packman', self)
		packAct.setShortcut('Ctrl+P')

		pocketAct = QAction(QIcon('./icon/pocketmon.png'), 'pocketmon', self)
		pocketAct.setShortcut('Ctrl+O')

		self.toolbar = self.addToolBar('Toolbar')
		self.toolbar.addAction(exitAct)
		self.toolbar.addAction(mailAct)
		self.toolbar.addAction(coinAct)
		self.toolbar.addAction(packAct)
		self.toolbar.addAction(pocketAct)



		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setWindowIcon(QtGui.QIcon('./icon/bitcoin.png'))
		self.show()

	def CloseApp(self):
		self.close()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
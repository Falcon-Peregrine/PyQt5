#coding = utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.InitUI()

	def InitUI(self):
		self.statusBar().showMessage('Ready')
		self.setWindowTitle('SubMenu')
		self.setGeometry(300,300,400,300)

		exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit the App')
		exitAct.triggered.connect(qApp.quit)

		saveMenu = QMenu('Save as..(&S)', self)
		saveAct = QAction(QIcon('save.png'), '保存..', self)
		saveAct.setShortcut('Ctrl+S')
		saveAct.setStatusTip('Save File')
		saveAsAct = QAction(QIcon('saveas.png'), '另存为..(&O)', self)
		saveAct.setStatusTip('Save As..')
		saveMenu.addAction(saveAct)
		saveMenu.addAction(saveAsAct)

		newAct = QAction(QIcon('new.png'), '新建(&N)', self)
		newAct.setShortcut('Ctrl+N')

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('文件(&F)')
		fileMenu.addAction(newAct)
		fileMenu.addMenu(saveMenu)
		fileMenu.addSeparator()
		fileMenu.addAction(exitAct)

		toolbar = self.addToolBar('工具栏')
		toolbar.addAction(newAct)
		toolbar.addAction(exitAct)
		self.show()

	def contextMenuEvent(self, event):  # 重新实现contextMenuEvent方法，所以这里方法名字不能改变
		cmenu = QMenu(self)

		newAct = cmenu.addAction('新建')
		openAct = cmenu.addAction('保存')
		quitAct = cmenu.addAction('退出')
		action = cmenu.exec_(self.mapToGlobal(event.pos())) # global the position of the mouse, and the the context menu to be executed globally
		if action == quitAct:
			qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

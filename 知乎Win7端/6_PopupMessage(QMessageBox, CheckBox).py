import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300,300,330,300)
		self.setWindowTitle('QMessageBox, QCheckBox')

		self.la = QLabel('这里将会显示我们选择的按钮信息',self)
		self.la.move(20, 20)

		self.bt1 = QPushButton('提示', self)
		self.bt1.move(20, 70)

		self.bt2 = QPushButton('询问',self)
		self.bt2.move(120,70)
		self.bt3 = QPushButton('警告',self)
		self.bt3.move(220,70)
		self.bt4 = QPushButton('错误',self)
		self.bt4.move(20,140)
		self.bt5 = QPushButton('关于',self)
		self.bt5.move(120,140)
		self.bt6 = QPushButton('关于Qt',self)
		self.bt6.move(220,140)

		self.bt1.clicked.connect(self.info)
		self.bt2.clicked.connect(self.question)
		self.bt3.clicked.connect(self.warning)
		self.bt4.clicked.connect(self.critical)
		self.bt5.clicked.connect(self.about)
		self.bt6.clicked.connect(self.aboutQt)


		self.show()


	def info(self):
		reply = QMessageBox.information(self, '提示infomation', 'This is a MsgBox',QMessageBox.Ok|QMessageBox.Close, QMessageBox.Close)
		if reply == QMessageBox.Ok:
			self.la.setText('OK!')
		else:
			self.la.setText('Close!')

	def question(self):
		reply =QMessageBox.question(self, '询问question', '询问消息对话框，默认No', QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel, QMessageBox.No)
		if reply == QMessageBox.Yes:
			self.la.setText('Yes!!')
		elif reply == QMessageBox.No:
			self.la.setText('No!!')
		else:
			self.la.setText('Cancel')

	def warning(self):
		cb = QCheckBox('所有文档都按此操作')

		msgBox = QMessageBox()
		msgBox.setWindowTitle('警告了！QMessageBox')
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setText('这是一个警告消息对话框')
		msgBox.setInformativeText('出现更改愿意保存吗?')

		save = msgBox.addButton('保存', QMessageBox.AcceptRole)
		NoSave = msgBox.addButton('取消', QMessageBox.RejectRole)
		Cancel = msgBox.addButton('不保存', QMessageBox.DestructiveRole)
		msgBox.setDefaultButton(save)
		
		msgBox.setCheckBox(cb)
		cb.stateChanged.connect(self.check)
		reply = msgBox.exec()
		
		if reply == msgBox.AcceptRole:
			self.la.setText('你选择了保存')
		elif reply == msgBox.RejectRole:
			self.la.setText('You choose cancel!')
		else:
			self.la.setText('你选择了不保存')

	def critical(self):
		msgBox = QMessageBox()
		msgBox.setWindowTitle('错误！！QMessageBox')
		msgBox.setIcon(QMessageBox.Critical)
		msgBox.setText('这是一个错误消息对话框')
		msgBox.setStandardButtons(QMessageBox.Retry|QMessageBox.Abort|QMessageBox.Ignore) # 注意这里有s
		msgBox.setDefaultButton(QMessageBox.Retry)
		msgBox.setDetailedText('这里是详细的信息3.1465689866666')
		reply = msgBox.exec()

		if reply == QMessageBox.Retry:
			self.la.setText('retry chosen!')
		elif reply ==QMessageBox.Abort:
			self.la.setText('Abort chosen')
		else:
			self.la.setText('Ignore chosen')

	def check(self):
		if self.sender().isChecked():
			self.la.setText('你打勾了哦')
		else:
			self.la.setText('怎么又不打勾了')

	def about(self):
		msgBox = QMessageBox(QMessageBox.NoIcon, '关于QMessageBox', 'some text')
		msgBox.setIconPixmap(QPixmap('save.png'))
		msgBox.exec()

	def aboutQt(self):
		QMessageBox.aboutQt(self, '这关于Qt aboutQt')


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
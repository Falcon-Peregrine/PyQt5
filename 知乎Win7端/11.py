import sys
from PyQt5.QtWidgets import QToolButton, QPushButton, QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtCore import Qt

'''QAction可能包含图标，菜单文本，快捷方式，状态文本，
“这是什么？”文本和工具提示。其中大部分可以在构造函数中设置。
它们也可以用setIcon()，setText()，setIconText()，setShortcut()，setStatusTip()，setWhatsThis()和setToolTip()独立设置。
对于菜单项，可以使用setFont()设置单个字体。'''

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		tb = QToolButton(self)  # Qt.ToolButtonIconOnly  Qt.ToolButtonFollowStyle(Unix) Qt.ToolButtonFollowStyle
		tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
		tb.setArrowType(Qt.DownArrow)
		tb.setToolTip('选择你的支付方式')
		tb.setPopupMode(QToolButton.InstantPopup) # QToolButton.DelayedPopup QToolButton.MenuButtonPopup QToolButton.InstantPopup QToolButton.MenuButtonPopup
		tb.setText('支付方式')
		tb.setIcon(QIcon('ali.png'))
		tb.setAutoRaise(True)

		menu = QMenu(self)
		self.alipayAct = QAction(QIcon('ali.png'), '支付宝', self)
		self.masterAct = QAction(QIcon('mastercard.png'), 'MaterCard', self)
		self.visaAct = QAction(QIcon('visa.png'), 'VisaCard', self) # 第二个其实是 setText()方法
		self.visaAct.setText('ddd')
		menu.addAction(self.alipayAct)
		menu.addSeparator()
		menu.addAction(self.masterAct)
		

		tb.setMenu(menu)
		self.show()

		self.alipayAct.triggered.connect(self.on_click)
		self.masterAct.triggered.connect(self.on_click)
		self.visaAct.triggered.connect(self.on_click)
		#值得注意的是，当setChecked()或toggle()被调用时，它不会被发射。

	def on_click(self):
		if self.sender() == self.alipayAct:
			QDesktopServices.openUrl(QUrl('https://www.alipay.com/'))
		
		elif self.sender() == self.visaAct:
			QDesktopServices.openUrl(QUrl('https://www.visa.com.cn/'))
		else:
			QDesktopServices.openUrl(QUrl('https://www.mastercard.com.cn/zh-cn.html'))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
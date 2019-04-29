import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout
# horizontal box layout and vertical box layout
class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.Init_UI()
	def Init_UI(self):
		self.setGeometry(300, 300, 400, 300)
		self.setWindowTitle('箱式布局')

		bt1 = QPushButton('剪刀', self)
		bt2 = QPushButton('石头', self)
		bt3 = QPushButton('布', self)

		hbox = QHBoxLayout()
		hbox.addStretch(0) # 伸缩量
		hbox.addWidget(bt1)
		hbox.addWidget(bt2)
		hbox.addWidget(bt3)

		vbox = QVBoxLayout()
		vbox.addStretch(0)
		vbox.addLayout(hbox) # 水平布局放置在垂直布局中

		self.setLayout(vbox)

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

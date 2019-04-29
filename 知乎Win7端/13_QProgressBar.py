#coding=utf-8

from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QBasicTimer
import sys

class Example(QWidget):
	"""docstring for Example"""
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.resize(600,480)
		self.setWindowTitle('QProgressBar')
		self.pb11 = QProgressBar(self)
		self.pb12 = QProgressBar(self)
		self.pb13 = QProgressBar(self)
		self.pb14 = QProgressBar(self)
		self.pb21 = QProgressBar(self)
		self.pb22 = QProgressBar(self)
		
		self.pb11.setOrientation(Qt.Horizontal) # 进度条是可以设置方向的，你可以选择垂直或是水平
		self.pb12.setOrientation(Qt.Vertical)
		self.pb13.setOrientation(Qt.Horizontal)
		self.pb14.setOrientation(Qt.Vertical)

		self.pb11.setGeometry(70, 40, 450, 20)
		self.pb12.setGeometry(490, 40, 20, 400)
		self.pb13.setGeometry(70, 420, 450, 20)
		self.pb14.setGeometry(70, 40, 20, 400)

		self.pb21.setGeometry(200, 100, 200, 20)
		self.pb22.setGeometry(200, 340, 200, 20)

		self.pb21.setFormat('%v')
		'''％p - 被完成的百分比取代
		％v - 被当前值替换
		％m - 被总step所取代
		默认值是”％p％'''
		self.pb22.setInvertedAppearance(True) # progressbar从右向左

		self.b1 = QPushButton('OuterBar',self)
		self.b2 = QPushButton('InnerBar',self)

		self.b1.move(250,180)
		self.b2.move(250,250)
		self.show()

		self.timer = QBasicTimer()
		self.step = 0
		self.b1.clicked.connect(self.running)
		self.b2.clicked.connect(self.doaction)

	def timerEvent(self, e):
		if self.step >= 100:
			self.timer.stop()
			QMessageBox.information(self,'tips','InnerDone')
			self.b2.setText('Again')
			self.step = 0
			return

		self.step = self.step + 1
		self.pb21.setValue(self.step)
		self.pb22.setValue(self.step)

	def doaction(self):
		if self.timer.isActive():
			self.timer.stop()
			self.b2.setText('Continue')
		else:
			self.timer.start(100, self)
			self.b2.setText('Stop')
	def running(self):
		self.pb11.setMinimum(0)
		self.pb11.setMaximum(0)

		self.pb12.setInvertedAppearance(True)
		self.pb12.setMinimum(0)
		self.pb12.setMaximum(0)

		self.pb13.setInvertedAppearance(True)
		self.pb13.setMinimum(0)
		self.pb13.setMaximum(0)
		

		self.pb14.setMinimum(0)
		self.pb14.setMaximum(0)
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QToolButton, QWidget, QPushButton, QApplication, QMainWindow, QAction, qApp, QMenu

from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtCore import Qt

class Example(QWidget):
    def initUI(self):

        bt1 = QPushButton("这是什么",self)

        self.bt2 = QPushButton('发送验证码',self)

        menu = QMenu(self)
        menu.addAction('我是')
        menu.addSeparator()
        menu.addAction('世界上')
        menu.addSeparator()
        menu.addAction('最帅的')

        bt1.setMenu(menu)

        self.count = 10

        self.bt2.clicked.connect(self.Action)

        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)

        self.show()

    def Action(self):
        if self.bt2.isEnabled():
            self.time.start()
            self.bt2.setEnabled(False)
    
    def Refresh(self):
        if self.count > 0:
            self.bt2.setText(str(self.count)+'秒后重发')
            self.count -= 1
        else:
            self.time.stop()
            self.bt2.setEnabled(True)
            self.bt2.setText('发送验证码')
            self.count = 10

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
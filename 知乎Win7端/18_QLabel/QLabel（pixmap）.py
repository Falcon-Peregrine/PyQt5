#coding=utf-8

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.resize(550,500)
        self.setWindowTitle('关注微信公众号：学点编程吧--标签:图画（QLabel）')
        
        pix = QPixmap('sexy.jpg')
        
        lb1 = QLabel(self)
        lb1.setGeometry(0,0,300,200)
        lb1.setStyleSheet("border: 2px solid red")
        lb1.setPixmap(pix)
        
        lb2 = QLabel(self)
        lb2.setGeometry(0,250,300,200)
        lb2.setPixmap(pix)
        lb2.setStyleSheet("border: 2px solid red")
        lb2.setScaledContents(True)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
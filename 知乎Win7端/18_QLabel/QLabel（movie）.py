#coding=utf-8

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QMovie, QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.resize(550,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--标签:动画（QLabel）')

        self.lb = QLabel(self)
        self.lb.setGeometry(100,50,300,200)
        
        self.bt1 = QPushButton('开始',self)
        self.bt2 = QPushButton('停止',self)
        
        self.bt1.move(100,20)
        self.bt2.move(280,20)
        
        self.pix = QPixmap('movie.gif')
        self.lb.setPixmap(self.pix)
        self.lb.setScaledContents(True)
        
        self.bt1.clicked.connect(self.run)
        self.bt2.clicked.connect(self.run)
        
        self.show()
        
    def run(self):
        movie = QMovie("movie.gif")
        self.lb.setMovie(movie)
        if self.sender() == self.bt1:
            movie.start()
        else:
            movie.stop()
            self.lb.setPixmap(self.pix)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
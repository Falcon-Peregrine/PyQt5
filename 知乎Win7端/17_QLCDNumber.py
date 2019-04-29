#coding=utf-8

from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QDateTime, QDate, QTime
from PyQt5.QtGui import QFont
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.resize(370,190)
        self.setWindowTitle('关注微信公众号：学点编程吧--倒计时：LCD数字')

        self.lcd = QLCDNumber(self)
        lb = QLabel("距离2022年北京-张家口冬季奥林匹克运动会还有",self)
        ft = QFont()
        ft.setPointSize(15)
        lb.setFont(ft)
        vbox = QVBoxLayout(self)
        vbox.addWidget(lb)
        vbox.addWidget(self.lcd)

        self.lcd.setDigitCount(12)
        self.lcd.setMode(QLCDNumber.Dec) # etMode()该属性保存当前的显示模式（数字库）,对应于当前显示模式，
        self.lcd.setStyleSheet("border: 2px solid black; color: blue; background: silver; border-radius:10px;border-width:3px;")

        time = QTimer(self)
        time.setInterval(1000) # 1000毫秒=1秒
        time.timeout.connect(self.refresh) # 以固定时间1秒，向refresh槽发出信号
        time.start()

        self.show()

    def refresh(self):
        startDate = QDateTime.currentMSecsSinceEpoch()
        endDate = QDateTime(QDate(2020, 2, 4), QTime(0, 0, 0)).toMSecsSinceEpoch() # 假设是0:0:0开始的，我们创建一个QDatetime对象，并使用toMSecsSinceEpoch()返回2020年2月4日0:0:0自1970-01-01T00：00：00.000世界协调时间以来的毫秒数。
        interval = endDate - startDate
        if interval > 0:
            days = interval // (24 * 60 * 60 * 1000)
            hour = (interval - days * 24 * 60 * 60 * 1000) // (60 * 60 * 1000)
            min = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000) // 1000
            intervals = str(days) + ':' + str(hour) + ':' + str(min) + ':' + str(sec)
            self.lcd.display(intervals)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
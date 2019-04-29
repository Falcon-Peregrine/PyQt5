from PyQt5.QtWidgets import QWidget, QRadioButton, QApplication, QPushButton, QMessageBox, QButtonGroup
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.rb11 = QRadioButton('你是',self)
        self.rb12 = QRadioButton('我是',self)
        self.rb13 = QRadioButton('他是',self)
        self.rb21 = QRadioButton('大美女',self)
        self.rb22 = QRadioButton('大帅哥',self)
        self.rb23 = QRadioButton('小屁孩',self) # 这个6个单选按钮是互斥的，因为单选按钮默认为autoExclusive（自动互斥）
        bt1 = QPushButton('提交',self)

        self.rb11.move(20, 30)
        self.rb12.move(40, 50)
        self.rb13.move(60, 70)
        self.rb21.move(80, 90)
        self.rb22.move(100, 110)
        self.rb23.move(120, 130)
        bt1.move(150, 200)

        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.rb11, 11)
        self.bg1.addButton(self.rb12, 12)
        self.bg1.addButton(self.rb13, 13)

        self.bg2 = QButtonGroup(self)
        self.bg2.addButton(self.rb21, 21)
        self.bg2.addButton(self.rb22, 22)
        self.bg2.addButton(self.rb23, 23)

        self.info1 = ''
        self.info2 = ''

        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bg2.buttonClicked.connect(self.rbclicked)
        bt1.clicked.connect(self.submit)

        self.show()

    def submit(self):
        if self.info1 == '' or self.info2 == '':
            QMessageBox.information(self, 'what?', '貌似没选')
        else:
            QMessageBox.information(self, 'what>?', self.info1+self.info2)

    def rbclicked(self):
        sender = self.sender()
        if sender ==self.bg1:
            if self.bg1.checkedId() == 11:
                self.info1 = '你是'
            elif self.bg1.checkedId() == 12:
                self.info1 = '我是'
            elif self.bg1.checkedId() == 13:
                self.info1 = '他是'
            else:
                self.info = ''
        else:
            if self.bg2.checkedId() == 21:
                self.infor2 = 'beauty'
            elif self.bg2.checkedId() == 22:
                self.info2 = 'handsome'
            elif self.bg2.checkedId() == 23:
                self.info2 = 'pigass'
            else:
                info2 = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,300)
        self.setWindowTitle('Color, Font, File')

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20,20,300,270)

        self.bt1 = QPushButton('打开文件',self)
        self.bt1.move(350, 20)

        self.bt2 = QPushButton('选择字体',self)
        self.bt2.move(350,70)
        self.bt3 = QPushButton('选择颜色',self)
        self.bt3.move(350,120)


        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choosefont)
        self.bt3.clicked.connect(self.choosecolor)

        self.show()

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', './', '*.csv *.jpg *.png') # returns ('C:/Users/Administrator/Desktop/PyQt5/知乎Win7端/2_LayOut_QHBoxLayout.py', 'All Files (*)')
        if fname[0]:
            with open(fname[0], 'r', encoding='UTF-8', errors='ignore') as f:
                self.tx.setText(f.read())
    def choosefont(self):
        font, ok = QFontDialog.getFont() # returns <PyQt5.QtGui.QFont object at 0x01E1F8F0> True
        if ok:
            self.tx.setCurrentFont(font)
    def choosecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
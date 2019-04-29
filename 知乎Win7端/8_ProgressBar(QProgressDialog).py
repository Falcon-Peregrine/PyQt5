#coding=utf-8

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog
from PyQt5.QtCore import Qt
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,150)
        self.setWindowTitle("进度对话框")

        self.lb = QLabel("文件数量",self)
        self.lb.move(20,40)

        self.bt1 = QPushButton('开始',self)
        self.bt1.move(20,80)

        self.edit = QLineEdit('100000',self)
        self.edit.move(100,40)

        self.show()

        self.bt1.clicked.connect(self.showDialog)
    
    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")  
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5) # milsecond 现实任务大于5毫秒，所以会显示
        progress.setWindowModality(Qt.WindowModal) # 此属性保留由模态小部件阻止的窗口。默认情况下，此属性为Qt.NonModal
        progress.setRange(0,num) 
        for i in range(num):
            progress.setValue(i) 
            if progress.wasCanceled():
                QMessageBox.warning(self,"提示","操作失败") 
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self,"提示","操作成功")
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

"""
Module implementing Dialog_selected.
"""

from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
import json, requests, sys
from Ui_ui import Ui_Dialog

class Dialog_selected(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog_selected, self).__init__(parent)
        self.setupUi(self)
        self.appkey = "你的appkey"
    
    @pyqtSlot(QDate)
    def on_calendarWidget_clicked(self, date):
        """
        Slot documentation goes here.
        
        @param date DESCRIPTION
        @type QDate
        """
        date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd dddd")
        self.request1(self.appkey, date)
    
    def request1(self, appkey, date):
        url = "http://v.juhe.cn/laohuangli/d"
        params = {
            "key" : appkey, #应用APPKEY(应用详细页查询)
            "date" : date #日期，格式2014-09-09
        }
        f = requests.get(url, params=params)

        content = f.text
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            data = res["result"]
            if error_code == 0:
                #成功请求
                self.label.setText("阳历：" + date)
                self.label_2.setText("阴历：" + data["yinli"])
                self.label_3.setText("忌：" + data["ji"])
                self.label_4.setText("宜：" + data["yi"])
            else:
                QMessageBox.Warning(self, "警告", "错误代码:" + res["error_code"] + "错误原因:" + res["reason"])
        else:
            QMessageBox.Warning(self,"警告","API请求失败")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    Dialog = Dialog_selected()
    Dialog.show()
    sys.exit(app.exec_())

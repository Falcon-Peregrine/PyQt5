from PyQt5.QtWidgets import QToolBox, QApplication, QToolButton, QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon 
import sys, webbrowser

class Example(QToolBox):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(280,500)
		self.setWindowTitle('QToolBox')
		self.setWindowFlags(Qt.Dialog)
		favorites =[
                        [
                            {'des':'百度搜索', 'pic':'image/se/baidu.ico'},
                            {'des':'搜狗搜索', 'pic':'image/se/sougo.ico'},
                            {'des':'必应搜索', 'pic':'image/se/bing.ico'},
                            {'des':'360搜索', 'pic':'image/se/360.ico'},
                            {'des':'谷歌搜索', 'pic':'image/se/google.ico'},
                            {'des':'雅虎搜索', 'pic':'image/se/yahoo.ico'}
                        ],
                        [
                            {'des':'腾讯视频', 'pic':'image/v/tengxun.ico'},
                            {'des':'搜狐视频', 'pic':'image/v/sohuvideo.ico'},
                            {'des':'优酷视频', 'pic':'image/v/youku.ico'},
                            {'des':'土豆视频', 'pic':'image/v/tudou.ico'},
                            {'des':'AcFun弹幕', 'pic':'image/v/acfun.ico'},
                            {'des':'哔哩哔哩', 'pic':'image/v/bilibili.ico'}
                        ]
        ]

        for item in favorites:
        	groupbox = QGroupBox()
        	vlayout = QVBoxLayout(groupbox)
        	vlayout.setAlignment(Qt.AlignCenter)

        	for category in item:
        		toolButton = QToolButton()
        		toolButton.setText(category['des'])
        		toolButton.setIcon(QIcon(category['pic']))
        		toolButton.setIconSize(QSize(64,64))
        		toolButton.setAutoRaise(True)
        		toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        		vlayout.addWidget(toolButton)
        		name = category['des']
        		toolButton.clicked.connect(self.run)
        	if name == '雅虎搜索':
        		self.addItem(groupbox, '搜索引擎')
        	else:
        		self.addItem(groupbox, '视频网站')

        self.show()

    def run(self):
    	if self.sender().text() == '百度搜索':
    		webbrowser.open('https://www.baidu.com')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())




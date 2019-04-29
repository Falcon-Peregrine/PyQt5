from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtGui import QIcon
import sys

def run():
	app = QApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.load('50_QtQuickRectangle.qml')
	app.setWindowIcon(QIcon('./icon/icon.png'))

	if not engine.rootObjects():
		return -1

	return app.exec_()


if __name__ == '__main__':
	sys.exit(run())

# introduce width and height property
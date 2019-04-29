from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication 
import sys

def run():
	app = QApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.load('48_QtQml.qml')

	if not engine.rootObjects():
		return -1

	return app.exec_()


if __name__ == '__main__':
	sys.exit(run())
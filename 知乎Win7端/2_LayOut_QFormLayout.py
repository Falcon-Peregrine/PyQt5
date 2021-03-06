import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLabel, QLineEdit, QTextEdit

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.Init_UI()

	def Init_UI(self):
		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('QFormLayout')

		formlayout = QFormLayout()
		nameLabel = QLabel('姓名')
		nameLineEdit = QLineEdit("")
		introductionLabel = QLabel('简介')
		introductionLineEdit = QTextEdit("")

		formlayout.addRow(nameLabel, nameLineEdit)
		formlayout.addRow(introductionLabel, introductionLineEdit)
		self.setLayout(formlayout)
		self.show()

if __name__ == '__main__':
	app =QApplication(sys.argv)
	ex = Example()
	app.exit(app.exec_())
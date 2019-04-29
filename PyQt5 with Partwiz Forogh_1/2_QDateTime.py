from PyQt5.QtCore import QDateTime, QDate, QTime, Qt 

datetime = QDateTime.currentDateTime()
print(datetime.toString())
print(datetime.toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate))

print('***************')

date = QDate.currentDate()
print(date.toString())
print(date.toString(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))

print('***************')

time = QTime.currentTime()
print(time.toString())
print(time.toString(Qt.DefaultLocaleLongDate))
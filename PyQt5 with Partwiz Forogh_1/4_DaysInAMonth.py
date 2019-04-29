from PyQt5.QtCore import QDate
date = QDate.currentDate()

d = QDate(2019, 3, 21)
print("Days In A Month:{0} ". format(d.daysInMonth()))
print("Days In A Year:{0}". format(d.daysInYear()))

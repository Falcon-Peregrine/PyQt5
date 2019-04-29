from PyQt5.QtCore import QDateTime, Qt 

datetime = QDateTime.currentDateTime()

print("Today Date and Time Is: " + datetime.toString(Qt.ISODate))
print("Adding 12 Days To The Date: {}".format((datetime.addDays(12)).toString(Qt.ISODate)))
print("Subtracting 25 Days: {}".format((datetime.addDays(-25)).toString(Qt.ISODate)))
print("Adding 50 Seconds {}".format((datetime.addSecs(50).toString(Qt.ISODate))))
print("Adding 3 Months {}".format((datetime.addMonths(3).toString(Qt.ISODate))))
print("Adding 12 Years {}".format((datetime.addYears(12).toString(Qt.ISODate))))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import smtplib
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 465)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_email = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_email.setGeometry(QtCore.QRect(140, 70, 311, 21))
        self.txt_email.setObjectName("txt_email")
        self.txt_password = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_password.setGeometry(QtCore.QRect(140, 100, 311, 21))
        self.txt_password.setObjectName("txt_password")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(90, 70, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(60, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label_to_list = QtWidgets.QLabel(self.centralwidget)
        self.label_to_list.setGeometry(QtCore.QRect(460, 40, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_to_list.setFont(font)
        self.label_to_list.setObjectName("label_to_list")
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setGeometry(QtCore.QRect(60, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_message.setFont(font)
        self.label_message.setObjectName("label_message")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(410, 332, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.txt_message = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_message.setGeometry(QtCore.QRect(140, 140, 311, 181))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.txt_message.setFont(font)
        self.txt_message.setObjectName("txt_message")
        self.txt_to_list = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_to_list.setGeometry(QtCore.QRect(460, 70, 331, 251))
        self.txt_to_list.setObjectName("txt_to_list")
        self.label_warning = QtWidgets.QLabel(self.centralwidget)
        self.label_warning.setGeometry(QtCore.QRect(200, 0, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_warning.setFont(font)
        self.label_warning.setObjectName("label_warning")
        self.label_success = QtWidgets.QLabel(self.centralwidget)
        self.label_success.setGeometry(QtCore.QRect(110, 370, 671, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_success.setFont(font)
        self.label_success.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_success.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_success.setObjectName("label_success")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.label_password.setText(_translate("MainWindow", "Password:"))
        self.label_to_list.setText(_translate("MainWindow", "To List:"))
        self.label_message.setText(_translate("MainWindow", "Message:"))
        self.button.setText(_translate("MainWindow", "SEND"))
        self.label_warning.setText(_translate("MainWindow", "Warning: Allow less secure apps on google."))




class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.clicked)

    def clicked(self):
        host = "smtp.gmail.com"
        port = 587
        username = self.ui.txt_email.text()
        password = self.ui.txt_password.text()
        from_email = username
        to_list = list(map(str,self.ui.txt_to_list.text().split()))
        message = self.ui.txt_message.text()
        try:
            email_conn = smtplib.SMTP(host, port)
            email_conn.starttls()
            email_conn.login(username, password)
            email_conn.sendmail(from_email, to_list, message)
            email_conn.quit()
            self.ui.label_success.setText("Mail Sending Successful")
        except smtplib.SMTPException as e:
            self.ui.label_success.setText(str(e))
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()

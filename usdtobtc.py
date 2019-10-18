import sys
import requests
import json
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Örnek Uygulama")
        self.setGeometry(200, 200, 250, 250)
        self.setWindowIcon(QIcon("logo.png"))
        self.setToolTip('my tooltip')
        self.initUI()

    def initUI(self):
        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setText("USD to BTC converter")
        self.label_title.resize(250, 30)
        self.label_title.move(50, 15)
        self.label_title.setStyleSheet("font: 12pt Comic Sans MS")
        self.label_usd = QtWidgets.QLabel(self)
        self.label_usd.setText("USD value:")
        self.label_usd.move(25,50)
        self.label_result = QtWidgets.QLabel(self)
        self.label_result.move(25, 125)
        self.label_result.setStyleSheet("font: 10pt Comic Sans MS")
        self.label_result.resize(200, 32)
        self.txt_usd = QtWidgets.QLineEdit(self)
        self.txt_usd.move(85, 50)
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Convert")
        self.button.move(85, 85)
        self.button.clicked.connect(self.convert)

    def convert(self):
        result = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd/")
        result = json.loads(result.text)
        result = int(self.txt_usd.text()) / float(result["last"])
        self.label_result.setText("result:" + str(result))
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()

    sys.exit(app.exec_())
window()

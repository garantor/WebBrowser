import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import time

page , _ = loadUiType('web.ui')



class MainApp(QMainWindow, page):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.HandleBtn()
        self.groupBox.setEnabled(False)
        self.setWindowTitle('Welcome Page')
        self.url = ""
        self.btn1 = ""
        self.setFixedSize(794, 591)

        


    def HandleBtn(self):
        self.pushButton_3.clicked.connect(lambda: self.whichbtn(self.pushButton_3))
        self.pushButton.clicked.connect(lambda: self.whichbtn(self.pushButton))
        self.pushButton_2.clicked.connect(lambda: self.whichbtn(self.pushButton_2))
        self.pushButton_4.clicked.connect(lambda: self.whichbtn(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.whichbtn(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.whichbtn(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.whichbtn(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.whichbtn(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.whichbtn(self.pushButton_9))
        self.pushButton_11.clicked.connect(lambda: self.whichbtn(self.pushButton_11))
        self.pushButton_10.clicked.connect(self.othernewUrl)
        self.pushButton_12.clicked.connect(lambda: self.whichbtn(self.pushButton_12))

    def whichbtn(self, b):
        if b.text() == 'Linkedin':
            self.url = "https://www.linkedin.com/"
            self.linkedin()
            self.web.setWindowTitle(b.text())
            
        elif b.text() == 'Facebook':
            self.url = "https://web.facebook.com/"
            self.linkedin()
            self.web.setWindowTitle(b.text())
            
        elif b.text() == 'BoomPlay':
            self.url = "https://www.boomplaymusic.com/BoomPlayer/#/webitem/music"
            self.linkedin()
            self.web.setWindowTitle(b.text())
            

        elif b.text() == "YahooMail":
            self.url = "https://mail.yahoo.com/"
            self.linkedin()
            self.web.setWindowTitle(b.text())

        elif b.text() == "Gmail":
            self.url = "https://gmail.com/"
            self.linkedin()
            self.web.setWindowTitle(b.text())
        elif b.text() == "Reddit":
            self.url = "https://reddit.com/"
            self.linkedin()
            self.web.setWindowTitle(b.text())

        elif b.text() == "WhatsApp":
            self.url = "https://web.whatsapp.com/"
            self.linkedin()
            self.web.setWindowTitle(b.text())
            
        elif b.text() == "Telegram":
            self.url = "https://web.telegram.org/"
            self.linkedin()
            self.web.setWindowTitle(b.text())

        elif b.text() == "Twitter":
            self.url = "https://twitter.com/"
            self.linkedin()
            self.web.setWindowTitle(b.text())

        elif b.text() == "Google":
            self.url = "https://google.com/"
            self.linkedin()
            self.web.setWindowTitle(b.text())

        elif b.text() == "Others":
            self.groupBox.setEnabled(True)
            

        else:
            self.statusBar().showMessage('Enter details here')


    def othernewUrl(self):
        btn1 = self.lineEdit.text()
        if 'https://' and '.com' not in btn1:
            self.label.setText('please Use a Valid Url or Use the Google Option')
        else:
            self.url = btn1
            self.web = QWebEngineView()
            self.web.load(QUrl(self.url))
            self.web.show()
            self.web.setWindowTitle(btn1)
        

    def linkedin(self):
        self.web = QWebEngineView()
        self.web.load(QUrl(self.url))
        self.web.show()
        self.groupBox.setEnabled(False)
        self.statusBar().showMessage(self.url)



def RunAll():
    app = QApplication(sys.argv)
    window =MainApp()
    window.show()
    app.exec_()


if __name__=='__main__':
    RunAll()
 
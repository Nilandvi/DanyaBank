import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from autorization_app import Authorization
from registration_app import CheckReg


class CheckUserRegistration(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\start.ui', self)
        self.setWindowTitle('Start DanyaBank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.autorization.clicked.connect(self.autorizat)
        self.registration.clicked.connect(self.registr)
    
    def autorizat(self):
        self.a = Authorization()
        self.a.show()
        self.hide()

    def registr(self):
        self.r = CheckReg()
        self.r.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckUserRegistration()
    ex.show()
    sys.exit(app.exec_())
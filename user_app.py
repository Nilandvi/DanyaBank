import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
from PyQt5 import QtCore
from inicializator_programm import Iniciai


class User(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\profile.ui', self)
        self.setWindowTitle('User info DanyaBank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        sqlite_connection = sqlite3.connect('bases\\users_info.db')
        file = open("files\\user.txt", "r").read()
        cursor = sqlite_connection.cursor()
        for value_users in cursor.execute(f"SELECT * FROM Info WHERE username = '{file}'"):
            self.name.setText(value_users[1])
            self.surname.setText(value_users[2])
            self.para.setText(value_users[3])

        self.exit_menu.clicked.connect(self.menubtn)

    def menubtn(self):
        self.menu = Iniciai()
        self.menu.show()
        self.hide()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Q:
            self.menu = Iniciai()
            self.menu.show()
            self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex =  User()
    ex.show()
    sys.exit(app.exec_())
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from inicializator_programm import Iniciai
import sqlite3


class Authorization(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = None
        uic.loadUi('windows\\autorization.ui', self)
        self.setWindowTitle('Authorization DanyaBank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.passworld_input.setPlaceholderText(' введите пароль')
        self.login_input.setPlaceholderText(' введите логин')
        self.continue_button.clicked.connect(self.check)

    def check(self):
        sqlite_connection = sqlite3.connect('bases\\users_info.db')
        cursor = sqlite_connection.cursor()
        passworld_input = self.passworld_input.text()
        login_input = self.login_input.text()
        res = cursor.execute(f'''SELECT password, username FROM Info WHERE username= "{login_input}"''').fetchall()
        sqlite_connection.commit()
        ##########################
        with open('files\\user.txt', 'r') as f:
            old = f.read()
        seans = str(login_input)
        seans = old.replace(old, seans)
        with open('files\\user.txt', 'w') as f:
            f.write(seans)
        ###########################
        cursor.close()
        pas = res[0][0]
        nick = res[0][1]
        loop = QEventLoop()
        if passworld_input == "":
            self.error.setText("Ошибка: Пустые строка")
            QTimer.singleShot(2000, loop.quit)
            loop.exec_()
        elif passworld_input != pas or login_input != nick:
            from errors import user
            user(self)
            self.error.setText("Логин/пароль неверны")
            QTimer.singleShot(2000, loop.quit)
            loop.exec_()
        elif passworld_input == pas and login_input == nick:
            self.error.setText("Пароль верный! Здравия!")
            QTimer.singleShot(2000, loop.quit)
            loop.exec_()
            self.w1 = Iniciai()
            self.w1.show()
            self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Authorization()
    ex.show()
    sys.exit(app.exec_())
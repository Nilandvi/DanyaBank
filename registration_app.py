import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sqlite3
from PyQt5.QtCore import QTimer, QEventLoop
from PyQt5.QtGui import QIcon



class CheckReg(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\registration.ui', self)
        self.setWindowTitle('Registration DanyaBank') 
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.name.setPlaceholderText('Имя')
        self.surname.setPlaceholderText('Фамилия')
        self.patronymic.setPlaceholderText('Отчество')
        self.passworld.setPlaceholderText('Пароль')
        self.username.setPlaceholderText('Логин')
        self.continue_button.clicked.connect(self.registr_button)

    def registr_button(self):
        sqlite_connection = sqlite3.connect('bases\\users_info.db')
        cursor = sqlite_connection.cursor()
        n = self.name.text()
        s = self.surname.text()
        p = self.patronymic.text()
        u = self.username.text()
        pas = self.passworld.text()
        cursor.execute(f"INSERT INTO Info (name, surname, patronymic, username, password) VALUES ('{n}', '{s}', '{p}', '{u}', '{pas}')")
        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу", cursor.rowcount)
        cursor.close()
        
        self.info_table.setText("Вы зарегистрировались!")
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckReg()
    ex.show()
    sys.exit(app.exec_())
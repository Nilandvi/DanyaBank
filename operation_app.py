import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
from PyQt5 import QtCore
from inicializator_programm import Iniciai

gett = 0
transf = 0

class Operation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\operation.ui', self)
        self.setWindowTitle('Operations DanyaBank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.transfer_btn.clicked.connect(self.transfer)
        self.exit_menu.clicked.connect(self.menubtn)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Q:
            self.menu = Iniciai()
            self.menu.show()
            self.hide()

    def transfer(self):
        uic.loadUi('windows\\transfer.ui', self)
        self.setWindowTitle('Transfer DanyaBank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.to_name.setPlaceholderText('Кому переводим:')
        self.value.setPlaceholderText('Сумма перевода:')
        self.transf_btn.clicked.connect(self.transfer_operation)

    def transfer_operation(self):
        loop = QEventLoop()
        file = open("files\\user.txt", "r").read()
        sqlite_connection1 = sqlite3.connect('bases\\users_info.db')
        cursor1 = sqlite_connection1.cursor()
        sqlite_connection = sqlite3.connect('bases\\history.db')
        cursor = sqlite_connection.cursor()
        debet = cursor1.execute(f"SELECT balance FROM Info WHERE username = '{file}'").fetchall()
        if not self.value.text().isdigit():
            from errors import meaning
            meaning(self)
        elif self.to_name.text() != "" and self.value.text() != "":
            us = cursor1.execute(f"SELECT username FROM Info").fetchall()
            for i in range(len(us)):
                if self.to_name.text() in us[i]:
                    debet = int(debet[0][0])
                    val = int(self.value.text())
                    if val > debet:
                        self.info_table.setText("Недостаточно средств")
                        QTimer.singleShot(2000, loop.quit)
                        loop.exec_()
                        self.menu = Iniciai()
                        self.menu.show()
                        self.hide()
                    elif val <= debet:
                        self.info_table.setText("Успешно!")
                        new_balance = debet - val
                        n = self.to_name.text()
                        s = "Перевод " + self.value.text() + "Р"
                        r = new_balance
                        cursor.execute(f"INSERT INTO History (name, sum, remains, useroper) VALUES ('{n}', '{s}', '{r}', '{file}')")
                        cursor1.execute(f"UPDATE Info SET balance='{new_balance}' WHERE username = '{file}'")
                        vruser = self.to_name.text()
                        debet_vruser = cursor1.execute(f"SELECT balance FROM Info WHERE username = '{vruser}'").fetchall()
                        new_balance_user = int(debet_vruser[0][0]) + val
                        cursor1.execute(f"UPDATE Info SET balance='{new_balance_user}' WHERE username = '{vruser}'")
                        p = "Зачисление " + str(new_balance_user) + "Р"
                        d = new_balance_user
                        cursor.execute(f"INSERT INTO History (name, sum, remains, useroper) VALUES ('{file}', '{p}', '{d}', '{vruser}')")
                        
                        sqlite_connection1.commit()
                        cursor1.close()
                        sqlite_connection.commit()
                        cursor.close()
                        QTimer.singleShot(2000, loop.quit)
                        loop.exec_()
                        self.menu = Iniciai()
                        self.menu.show()
                        self.hide()
                        continue

        else:
            from errors import empty
            empty(self)

 
    def menubtn(self):
        self.menu = Iniciai()
        self.menu.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Operation()
    ex.show()
    sys.exit(app.exec_())
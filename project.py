import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
import sqlite3
from PyQt5 import uic


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\menu.ui', self)
        self.setWindowTitle('Menu DanyaBank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.exit_button.clicked.connect(self.exit_app)
        self.profile_button.clicked.connect(self.user_acc)
        self.history_button.clicked.connect(self.history_us)
        self.operations_button.clicked.connect(self.oper_us)
        self.value_button.clicked.connect(self.converter_val)
        self.credits.clicked.connect(self.credit_calc)
        self.free_money.clicked.connect(self.money)
        sqlite_connection = sqlite3.connect('bases\\users_info.db')
        cursor = sqlite_connection.cursor()
        file = open("files\\user.txt", "r").read()

        for value_users in cursor.execute(f"SELECT * FROM Info WHERE username='{file}'"):
            n, s, p = value_users[1], value_users[2], value_users[3]
            itog = n + " " + p + " " + s + " "
            self.us_name.setText(itog)

        debet = cursor.execute(f"SELECT balance FROM Info WHERE username='{file}'").fetchall()
        self.balans_info1.setText(str(debet[0][0]))

    def exit_app(self):  # +
        from exit_app import Exit
        self.ex = Exit()
        self.ex.show()
        self.hide()

    def user_acc(self):  # +
        from user_app import User
        self.use = User()
        self.use.show()
        self.hide()

    def history_us(self):  # +
        from history_app import History
        self.ex = History()
        self.ex.show()
        self.hide()

    def oper_us(self):  # +
        from operation_app import Operation
        self.op = Operation()
        self.op.show()
        self.hide()

    def converter_val(self):  # +
        from converter_app import Converter
        self.co = Converter()
        self.co.show()
        self.hide()

    def credit_calc(self):
        from credit_app import Credit
        self.cre = Credit()
        self.cre.show()
        self.hide()
    
    def money(self):
        file = open("files\\user.txt", "r").read()
        sqlite_connection1 = sqlite3.connect('bases\\users_info.db')
        cursor1 = sqlite_connection1.cursor()
        debet = cursor1.execute(f"SELECT balance FROM Info WHERE username = '{file}'").fetchall()
        new_balance = int(debet[0][0]) + 100
        cursor1.execute(f"UPDATE Info SET balance='{new_balance}' WHERE username = '{file}'")
        sqlite_connection1.commit()
        cursor1.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())

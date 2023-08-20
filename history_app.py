import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3, webbrowser
from PyQt5 import QtCore
from inicializator_programm import Iniciai


class History(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\history.ui', self)
        self.setWindowTitle('History DanyaBank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        file = open("files\\user.txt", "r").read()
        sqlite_connection = sqlite3.connect('bases\\history.db')
        cursor = sqlite_connection.cursor()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(('Имя', 'Операция', 'Баланс', 'ID операции'))
        res = cursor.execute(f'''SELECT name, sum, remains, id FROM History WHERE useroper = "{file}" ORDER BY id DESC''')
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.exit_menu.clicked.connect(self.menubtn)
        self.get_btn.clicked.connect(self.cheque)

    def menubtn(self):
        self.menu = Iniciai()
        self.menu.show()
        self.hide()

    def cheque(self):
        uic.loadUi('windows\\operation_check.ui', self)
        self.setWindowTitle('Cheque Danya Bank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.temm_btn.clicked.connect(self.temmie)
        sqlite_connection = sqlite3.connect('bases\\users_info.db')
        cursor = sqlite_connection.cursor()
        sqlite_connection1 = sqlite3.connect('bases\\history.db')
        cursor1 = sqlite_connection1.cursor()
        n = cursor.execute("SELECT name FROM Info").fetchall()
        na = cursor1.execute("SELECT name FROM History WHERE id=(SELECT max(id) FROM History)").fetchall()
        op = cursor1.execute("SELECT sum FROM History WHERE id=(SELECT max(id) FROM History)").fetchall()
        ost = cursor1.execute("SELECT remains FROM History WHERE id=(SELECT max(id) FROM History)").fetchall()
        n = str(*n[0])
        na = str(*na[0])
        op = str(*op[0])
        ost = str(*ost[0])
        self.user_name.setText(n)
        self.name.setText(na)
        self.operation.setText(op)
        self.ostat.setText(ost)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection1.commit()
        cursor1.close()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Q:
            self.menu = Iniciai()
            self.menu.show()
            self.hide()

    def temmie(self):
        webbrowser.open_new_tab("https://s3.amazonaws.com/colorslive/png/3181477-uvZR_3inW_ONvNsJ.png")
        self.menu = Iniciai()
        self.menu.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = History()
    ex.show()
    sys.exit(app.exec_())
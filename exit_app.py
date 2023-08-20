import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
from PyQt5 import QtCore
from inicializator_programm import Iniciai
count_clicks = 0


class Exit(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\exit.ui', self)
        self.setWindowTitle('Ты реально хочешь выйти с этого шедевра?')
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.setMouseTracking(True)
        self.coords = [310, 490]
        self.btn_size = [131, 61]
        self.d = 15
        self.w = 550
        self.h = 736
        self.yes_button.move(*self.coords)
        self.yes_button.resize(*self.btn_size)
        self.show()

        self.yes_button.clicked.connect(self.button_yes)
        self.no_button.clicked.connect(self.button_no)

    def button_yes(self):
        global count_clicks
        loop = QEventLoop()
        if count_clicks < 5:
            count_clicks += 1
            self.coords[0] = random.randint(0, self.width() - self.btn_size[0])
            self.coords[1] = random.randint(0, self.height() - self.btn_size[1] - 100)
            self.yes_button.move(*self.coords)
        else:
            self.sucesfull_ex.setText("Раз ты так сильно этого хочешь...")
            QTimer.singleShot(2000, loop.quit)
            loop.exec_()
            self.close()

    def button_no(self):
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
    ex = Exit()
    ex.show()
    sys.exit(app.exec_())
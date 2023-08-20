import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from inicializator_programm import Iniciai

cheat_check = 0
insur = False
bet = 0

class Credit(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\credit.ui', self)
        self.setWindowTitle('Menu DanyaBank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.sum_zaim.setPlaceholderText('Сумма займа')
        self.term.setPlaceholderText('Срок займа')
        self.term.setEnabled(False)
        self.continue_button.clicked.connect(self.itog)
        self.cheat.toggled.connect(self.cheater)
        self.not_cheat.toggled.connect(self.not_cheater)
        self.spinBox.valueChanged.connect(self.srok)
        self.insurance.stateChanged.connect(self.strah)
        self.bet.activated[str].connect(self.onActivated)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Q:
            self.menu = Iniciai()
            self.menu.show()
            self.hide()

    def onActivated(self, text):
        global bet
        bet = float(text) / 100

    def srok(self, value):
        self.term.setText(str(value))

    def strah(self, state):
        global insur
        if self.insurance.isChecked():
            insur = True
        else:
            insur = False

    def cheater(self, _):
        global cheat_check
        cheat = self.sender()
        if cheat.isChecked() == True:
            cheat_check = 1

    def not_cheater(self, _):
        global cheat_check
        not_cheat = self.sender()
        if not_cheat.isChecked() == True:
            cheat_check = 0

    def itog(self):
        global cheat_check
        global bet

        if self.term.text() != "" and self.sum_zaim.text() != "" and self.spinBox.text() != "":
            if not self.sum_zaim.text().isdigit():
                from errors import meaning
                meaning(self)
            else:
                if cheat_check == 0:
                    txt1 = "Платата в месяц: "
                    txt2 = "\nПлата в год: "
                    txt3 = "\nВ конце срока: "
                    txt4 = "\nСрок: "
                    txt5 = "\nЕжемес %: "
                    term = int(self.term.text())
                    sum_zaim = int(self.sum_zaim.text())
                    if insur == True:
                        form = (sum_zaim + (bet * sum_zaim)) // 12 + 100
                    elif insur == False:
                        form = (sum_zaim + (bet * sum_zaim)) // 12
                    itog = (txt1 + str(form)) + (txt2 + str(form * 12)) + (txt3 + str(form * (term * 12))) + \
                        (txt4 + str(term)) + (txt5 + str(bet))
                    itog = str(itog)
                    self.table.setText(itog)
                else:
                    self.table.setText("Ай ай ай, обманывать плохо!")
                    loop = QEventLoop()
                    QTimer.singleShot(2000, loop.quit)
                    loop.exec_()
                    self.menu = Iniciai()
                    self.menu.show()
                    self.hide()
        else:
            from errors import empty
            empty(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Credit()
    ex.show()
    sys.exit(app.exec_())
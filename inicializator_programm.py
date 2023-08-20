import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Iniciai(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\inicial.ui', self)
        self.setWindowTitle('Loading DanyaBank')
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.btn.clicked.connect(self.click)
        
    def click(self):
        from project import Menu
        self.proj = Menu()
        self.proj.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Iniciai()
    ex.show()
    sys.exit(app.exec_())
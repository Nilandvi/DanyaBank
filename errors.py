from PyQt5.QtWidgets import *

def empty(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Имеются пустые строки!")
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    retval = msg.exec_()

def meaning(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Имеются недопустимые значения!")
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    retval = msg.exec_()

def value_error(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Такой валюты не существует! Проверьте правильность ввода. Пишите аббревиатуры наименования"
                " валют капсом")
    msg.setWindowTitle("Валюта не существует!")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    retval = msg.exec_()

def user(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Такого аккаунта не существует, или введен неправильный пароль или логин, повторите попытку")
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    retval = msg.exec_()

def user1(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Такой аккаунт не зарегестрирован в DanyaBank`е")
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    retval = msg.exec_()
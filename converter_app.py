import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import requests, xmltodict
from PyQt5 import QtCore
from inicializator_programm import Iniciai

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows\\convert.ui', self)
        self.setWindowTitle('Converter DanyaBank')
        self.setWindowIcon(QIcon('icon.png'))
        self.output_amount.setEnabled(False)
        self.input_currency.setPlaceholderText('Из валюты:')
        self.input_amount.setPlaceholderText('Сумма денег:')
        self.output_currency.setPlaceholderText('В валюту:')
        self.output_amount.setPlaceholderText('Сумма денег:')
        self.convert_button.clicked.connect(self.converter)
        self.exit_btn.clicked.connect(self.menubtn)

    def converter(self):
        if self.input_currency.text() != "" and self.output_currency.text() != "" \
                and self.input_currency.text() != "":
            valutes = "AUD AZN GBP AMD BYN BGN BRL HUF HKD DKK USD EUR INR KZT SAD KGS CNY MDL" \
                      " NOK PLN RON XDR SGD TJS TRY TMT UZS UAH CZK SEK CHF ZAR KRW JPY RUB".split(" ")
            if not self.input_amount.text().isdigit():
                from errors import meaning
                meaning(self)
            else:
                if self.input_currency.text() in valutes and self.output_currency.text() in valutes:
                    input_currency = self.input_currency.text()
                    output_currency = self.output_currency.text()
                    input_amount = int(self.input_amount.text())
                    link = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="
                    data = requests.get(link)
                    dct = xmltodict.parse(data.text)
                    if input_currency == "RUB" or output_currency == "RUB":
                        self.convert_button.clicked.connect(self.ruble)
                    else:
                        for u in dct['ValCurs']['Valute']:
                            if u['CharCode'] == 'USD':
                                USD = float(u['Value'].replace(',', '.'))
                        for i in dct['ValCurs']['Valute']:
                            if i['CharCode'] == output_currency:
                                value1 = USD / float(i['Value'].replace(',', '.'))
                        for d in dct['ValCurs']['Valute']:
                            if d['CharCode'] == input_currency:
                                value2 = USD / float(d['Value'].replace(',', '.'))

                        output_amount = (value1 / value2) * int(input_amount)
                        output_amount = round(output_amount, 2)
                        self.output_amount.setText(str(output_amount))
                else:
                    from errors import value_error
                    value_error(self)
        else:
            from errors import empty
            empty(self)

    def ruble(self):
        input_currency = self.input_currency.text()
        output_currency = self.output_currency.text()
        input_amount = int(self.input_amount.text())
        link = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="
        data = requests.get(link)
        dct = xmltodict.parse(data.text)
        for r in dct['ValCurs']['Valute']:
            if r['CharCode'] == input_currency and output_currency == "RUB":
                output_amount = float(r['Value'].replace(',', '.')) * int(input_amount)
                output_amount = round(output_amount, 2)
        for y in dct['ValCurs']['Valute']:
            if y['CharCode'] == output_currency and input_currency == "RUB":
                output_amount = float(y['Value'].replace(',', '.')) / int(input_amount)
                output_amount = round(output_amount, 2)

        self.output_amount.setText(str(output_amount))

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
    ex = Converter()
    ex.show()
    sys.exit(app.exec_())
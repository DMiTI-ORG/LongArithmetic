from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QFontDatabase, QPixmap, QIcon
import sys
from screen_manager import Screen
import json
from qt_for_python.uic import main_app, first_choice, second_choice
import input_forms
from LongArithmetic.Modules.NaturalNumber import NaturalNumber
from LongArithmetic.Modules.IntegerNumber import IntegerNumber
from LongArithmetic.Modules.RationalNumber import RationalNumber
#from LongArithmetic.Modules.Polynomial import Polynomial

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = main_app.Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_json()
        self.screen_loader()
        self.button_loader()
        self.main_module = None
        self.secondary_module = None

    def read_json(self):
        """
        Get data from json file
        """
        with open("data.json", "r", encoding='utf-8') as read_file:
            self.data = json.load(read_file)

    def button_loader(self):
        """
        Connect all buttons to functions
        """
        self.first_choice.ui.buttonGroup.buttonClicked.connect(self.select_global_module)
        self.second_choice.ui.back_button.clicked.connect(lambda: self.ui.menu.setCurrentWidget(self.first_choice))
        self.second_choice.ui.select_module.currentTextChanged.connect(self.select_local_module)
        self.second_choice.ui.run.clicked.connect(self.run)

    def screen_loader(self):
        """
        Loading all screens for app
        """
        self.first_choice = Screen(first_choice.Ui_Form())
        self.ui.menu.addWidget(self.first_choice)
        self.ui.menu.setCurrentWidget(self.first_choice)

        self.second_choice = Screen(second_choice.Ui_Form())
        self.ui.menu.addWidget(self.second_choice)

    def select_global_module(self, button):
        """
        Select module from class for test
        """
        string_array = self.data.get(button.text())
        self.main_module = button.text()
        string_array = map(lambda module: module.get('system_name') + ' : '+ module.get('human_name'), string_array)
        self.ui.menu.setCurrentWidget(self.second_choice)
        self.second_choice.ui.select_module.clear()
        self.second_choice.ui.select_module.addItems(string_array)

    def select_local_module(self):
        """
        Select module from class for test
        """
        self.input_array = [Screen(input_forms.InputForm1()),
                            Screen(input_forms.InputForm2()),
                            Screen(input_forms.InputForm3()),
                            Screen(input_forms.InputForm4()),
                            Screen(input_forms.InputForm5()),
                            Screen(input_forms.InputForm6()),
                            Screen(input_forms.InputForm7()),
                            Screen(input_forms.InputForm8()),
                            Screen(input_forms.InputForm9()),
                            Screen(input_forms.InputForm10())]
                            
        for screen in self.input_array:
            self.second_choice.ui.stackedWidget.addWidget(screen)
        index = self.data[self.main_module][self.second_choice.ui.select_module.currentIndex()]['input_type']
        self.secondary_module = self.second_choice.ui.select_module.currentIndex()
        self.second_choice.ui.stackedWidget.setCurrentIndex(index + 1)

    def get_natural(self, source):
        if source.text().isdigit():
            return list(map(int, source.text()))
        else:
            return [0]

    def get_integer(self, source):
        text = source.text()
        if text[0] == '-':
            text = list(map(int, source.text()[1:]))
            sign = 1
        else:
            text = self.get_natural(source)
            sign = 0
        return sign, text

    def get_rational(self, source_1, source_2):
        sign, numenator = self.get_integer(source_1)
        denominator = self.get_natural(source_2)
        return sign, numenator, denominator

    def run(self):
        if self.main_module == 'Натуральные числа':
            screen = self.second_choice.ui.stackedWidget.currentWidget()
            if self.secondary_module == 0:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                res = str(num_1.compare(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 1:
                text_1 = self.get_natural(screen.ui.number_1)
                num_1 = NaturalNumber(len(text_1), text_1)
                res = str(num_1.is_zero())
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 2:
                text_1 = self.get_natural(screen.ui.number_1)
                num_1 = NaturalNumber(len(text_1), text_1)
                res = str(num_1.add_one())
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 3:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                res = (num_1.add(num_2))
                print(res.highest_position, res.array)
                self.second_choice.ui.result.setText(str(res))
                
            elif self.secondary_module == 4:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                res = (num_1.subtract(num_2))
                self.second_choice.ui.result.setText(str(res))

            elif self.secondary_module == 5:
                text_1 = self.get_natural(screen.ui.number_1)
                digit_1 = screen.ui.digit_1.value()
                num_1 = NaturalNumber(len(text_1), text_1)
                res = (num_1.multiply_digit(digit_1))
                print(res.highest_position, res.array)
                res = str(res)
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 6:
                text_1 = self.get_natural(screen.ui.number_1)
                digit_1 = screen.ui.digit_1.value()
                num_1 = NaturalNumber(len(text_1), text_1)
                res = (num_1.multiply_by_powered_ten(digit_1))
                print(res.highest_position, res.array)
                self.second_choice.ui.result.setText(str(res))

            elif self.secondary_module == 7:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                res = (num_1.multiply(num_2))
                self.second_choice.ui.result.setText(str(res))

            elif self.secondary_module == 8:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                digit_2 = screen.ui.digit_2.value()
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                digit_1 = screen.ui.digit_2.value()
                res = str(num_1.subtract_k_by_number(num_2, digit_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 9:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                digit_2 = screen.ui.digit_2.value()
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                res = str(num_1.first_division_digit(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 10:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                res = str(num_1.quotient(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 11:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                res = str(num_1.remainder(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 12:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                res = str(num_1.gcd(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 13:
                text_1 = self.get_natural(screen.ui.number_1)
                text_2 = self.get_natural(screen.ui.number_2)
                num_1 = NaturalNumber(len(text_1), text_1)
                num_2 = NaturalNumber(len(text_2), text_2)
                res = str(num_1.lcm(num_2))
                self.second_choice.ui.result.setText(res)
        
        if self.main_module == 'Целые числа':
            screen = self.second_choice.ui.stackedWidget.currentWidget()
            if self.secondary_module == 0:
                sign, text_1 = self.get_integer(screen.ui.number_1)
                num_1 = IntegerNumber(sign, len(text_1), text_1)
                res = str(num_1.abs())
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 1:
                sign, text_1 = self.get_integer(screen.ui.number_1)
                num_1 = IntegerNumber(sign, len(text_1), text_1)
                res = str(num_1.is_positive())
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 2:
                sign, text_1 = self.get_integer(screen.ui.number_1)
                num_1 = IntegerNumber(sign, len(text_1), text_1)
                res = str(num_1.multiply_by_minus_one())
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 3:
                text_1 = self.get_natural(screen.ui.number_1)
                num_1 = IntegerNumber(0, len(text_1), text_1)
                res = (IntegerNumber.natural_to_integer(num_1))
                print(type(res))
                self.second_choice.ui.result.setText(str(res))

            elif self.secondary_module == 4:
                sign, text_1 = self.get_integer(screen.ui.number_1)
                num_1 = IntegerNumber(sign, len(text_1), text_1)
                res = num_1.to_natural()
                print(type(res))
                self.second_choice.ui.result.setText(str(res))

            elif self.secondary_module == 5:
                sign_1, text_1 = self.get_integer(screen.ui.number_1)
                sign_2, text_2 = self.get_integer(screen.ui.number_2)
                num_1 = IntegerNumber(sign_1, len(text_1), text_1)
                num_2 = IntegerNumber(sign_2, len(text_2), text_2)
                res = str(num_1.add(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 6:
                sign_1, text_1 = self.get_integer(screen.ui.number_1)
                sign_2, text_2 = self.get_integer(screen.ui.number_2)
                num_1 = IntegerNumber(sign_1, len(text_1), text_1)
                num_2 = IntegerNumber(sign_2, len(text_2), text_2)
                res = (num_1.subtract(num_2))
                print(res.sign, res.highest_position, res.array)
                self.second_choice.ui.result.setText(str(res))

            elif self.secondary_module == 7:
                sign_1, text_1 = self.get_integer(screen.ui.number_1)
                sign_2, text_2 = self.get_integer(screen.ui.number_2)
                num_1 = IntegerNumber(sign_1, len(text_1), text_1)
                num_2 = IntegerNumber(sign_2, len(text_2), text_2)
                res = (num_1.multiply(num_2))
                self.second_choice.ui.result.setText(str(res))

            elif self.secondary_module == 8:
                sign_1, text_1 = self.get_integer(screen.ui.number_1)
                sign_2, text_2 = self.get_integer(screen.ui.number_2)
                num_1 = IntegerNumber(sign_1, len(text_1), text_1)
                num_2 = IntegerNumber(sign_2, len(text_2), text_2)
                res = str(num_1.quotient(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 9:
                sign_1, text_1 = self.get_integer(screen.ui.number_1)
                sign_2, text_2 = self.get_integer(screen.ui.number_2)
                num_1 = IntegerNumber(sign_1, len(text_1), text_1)
                num_2 = IntegerNumber(sign_2, len(text_2), text_2)
                res = str(num_1.remainder(num_2))
                self.second_choice.ui.result.setText(res)

        if self.main_module == 'Рациональные числа':
            screen = self.second_choice.ui.stackedWidget.currentWidget()
            if self.secondary_module == 0:
                sign, num, denom = self.get_rational(screen.ui.numerator_1, screen.ui.denominator_1)
                num_1 = RationalNumber((sign, len(num), num), (len(denom), denom))
                res = str(num_1.reduce())
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 1:
                sign, num, denom = self.get_rational(screen.ui.numerator_1, screen.ui.denominator_1)
                num_1 = RationalNumber((sign, len(num), num), (len(denom), denom))
                res = str(num_1.is_integer())
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 2:
                sign, text_1 = self.get_integer(screen.ui.number_1)
                num_1 = IntegerNumber(sign, len(text_1), text_1)
                res = RationalNumber.integer_to_rational(num_1)
                self.second_choice.ui.result.setText(str(res) + ' ' + str(type(res)))

            elif self.secondary_module == 3:
                sign, num, denom = self.get_rational(screen.ui.numerator_1, screen.ui.denominator_1)
                num_1 = RationalNumber((sign, len(num), num), (len(denom), denom))
                res = str(num_1.to_integer())
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 4:
                sign, num, denom = self.get_rational(screen.ui.numerator_1, screen.ui.denominator_1)
                num_1 = RationalNumber((sign, len(num), num), (len(denom), denom))
                sign, num, denom = self.get_rational(screen.ui.numerator_2, screen.ui.denominator_2)
                num_2 = RationalNumber((sign, len(num), num), (len(denom), denom))
                res = str(num_1.add(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 5:
                sign, num, denom = self.get_rational(screen.ui.numerator_1, screen.ui.denominator_1)
                num_1 = RationalNumber((sign, len(num), num), (len(denom), denom))
                sign, num, denom = self.get_rational(screen.ui.numerator_2, screen.ui.denominator_2)
                num_2 = RationalNumber((sign, len(num), num), (len(denom), denom))
                res = str(num_1.subtract(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 6:
                sign, num, denom = self.get_rational(screen.ui.numerator_1, screen.ui.denominator_1)
                num_1 = RationalNumber((sign, len(num), num), (len(denom), denom))
                sign, num, denom = self.get_rational(screen.ui.numerator_2, screen.ui.denominator_2)
                num_2 = RationalNumber((sign, len(num), num), (len(denom), denom))
                res = str(num_1.multiply(num_2))
                self.second_choice.ui.result.setText(res)

            elif self.secondary_module == 7:
                sign, num, denom = self.get_rational(screen.ui.numerator_1, screen.ui.denominator_1)
                num_1 = RationalNumber((sign, len(num), num), (len(denom), denom))
                sign, num, denom = self.get_rational(screen.ui.numerator_2, screen.ui.denominator_2)
                num_2 = RationalNumber((sign, len(num), num), (len(denom), denom))
                res = str(num_1.divide(num_2))
                self.second_choice.ui.result.setText(res)
       







if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = App()
    application.show()
    sys.exit(app.exec())
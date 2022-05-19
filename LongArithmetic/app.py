import json
import os
import sys
from tkinter import Button

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QFontDatabase, QIcon, QPixmap

from . import input_forms
from .Modules.IntegerNumber import IntegerNumber
from .Modules.NaturalNumber import NaturalNumber
from .Modules.Polynomial import Polynomial
from .Modules.RationalNumber import RationalNumber
from .qt_for_python.uic import global_module, local_module, main_app
from .screen_manager import Screen


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = main_app.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.read_json()
        self.screen_loader()
        self.button_loader()
        self.main_module = None

    @staticmethod
    def resource_path(relative_path):
        try: 
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def read_json(self):
        """
        Get data from json file
        """
        print(os.getcwd())
        with open(self.resource_path(os.path.dirname(os.path.abspath(__file__))) + "/resourses/data.json", "r", encoding='utf-8') as read_file:
            self.data = json.load(read_file)

    def button_loader(self):
        """
        Connect all buttons to functions
        """
        self.global_module.ui.buttonGroup.buttonClicked.connect(self.select_global_module)
        self.local_module.ui.select_module.currentTextChanged.connect(self.select_local_module)
        self.local_module.ui.back_button.clicked.connect(lambda: self.ui.menu.setCurrentWidget(self.global_module))
        self.local_module.ui.run.clicked.connect(self.run)
        self.ui.info.triggered.connect(self.information)

        self.global_modules = ('Натуральные числа', 'Целые числа', 'Рациональные числа', 'Многочлены')
        human_module_name = lambda module: module['system_name'] + ' : '+ module['human_name']
        self.local_modules = [tuple(map(human_module_name, self.data[module])) for module in self.global_modules]

    def information(self, s):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("Справка")
        with open(self.resource_path(os.path.dirname(os.path.abspath(__file__))) + '/resourses/info.txt', encoding='utf-8') as f:
            dlg.setText(f.read())
        dlg.exec()

    def screen_loader(self):
        """
        Loading all screens for app
        """
        self.global_module = Screen(global_module.Ui_Form())
        self.local_module = Screen(local_module.Ui_Form())
        self.ui.menu.addWidget(self.global_module)
        self.ui.menu.addWidget(self.local_module)

        self.input_array = [Screen(input_forms.InputForm1()),
                            Screen(input_forms.InputForm2()),
                            Screen(input_forms.InputForm3()),
                            Screen(input_forms.InputForm4())]
                            
        for local_screen in self.input_array:
            self.local_module.ui.stackedWidget.addWidget(local_screen)

    def select_global_module(self, button):
        """
        Select module from class for test
        """
        self.main_module = button.text()
        self.ui.menu.setCurrentWidget(self.local_module)
        self.local_module.ui.select_module.clear()
        index = self.global_modules.index(self.main_module)
        self.local_module.ui.select_module.addItems((self.local_modules[index]))

    def select_local_module(self):
        """
        Select module from class for test
        """
        index = self.data[self.main_module][self.local_module.ui.select_module.currentIndex()]['input_type'] - 1
        self.local_module.ui.stackedWidget.setCurrentIndex(index)

    def run(self):
        """
        Calculating the result of choosen module
        """
        screen = self.local_module.ui.stackedWidget.currentWidget().ui
        module = self.local_module.ui.select_module.currentIndex()
        if self.main_module == 'Натуральные числа':
            if module == 0:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.compare(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 1:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                res = str(num_1.is_zero())
                self.local_module.ui.result.setText(res)

            elif module == 2:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                res = str(num_1.add_one())
                self.local_module.ui.result.setText(res)

            elif module == 3:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.add(num_2))
                self.local_module.ui.result.setText(res)
                
            elif module == 4:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.subtract(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 5:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                digit_1 = screen.digit_1.value()
                res = str(num_1.multiply_digit(digit_1))
                self.local_module.ui.result.setText(res)

            elif module == 6:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                digit_1 = screen.digit_1.value()
                res = str(num_1.multiply_by_powered_ten(digit_1))
                self.local_module.ui.result.setText(res)

            elif module == 7:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.multiply(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 8:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                digit_2 = screen.digit_2.value()
                res = str(num_1.subtract_k_by_number(num_2, digit_2))
                self.local_module.ui.result.setText(res)

            elif module == 9:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                digit_2 = screen.digit_2.value()
                res = str(num_1.first_division_digit(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 10:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.quotient(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 11:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.remainder(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 12:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.gcd(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 13:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                num_2 = NaturalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.lcm(num_2))
                self.local_module.ui.result.setText(res)
        
        if self.main_module == 'Целые числа':
            if module == 0:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                res = str(num_1.abs())
                self.local_module.ui.result.setText(res)

            elif module == 1:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                res = str(num_1.is_positive())
                self.local_module.ui.result.setText(res)

            elif module == 2:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                res = str(num_1.multiply_by_minus_one())
                self.local_module.ui.result.setText(res)

            elif module == 3:
                num_1 = NaturalNumber.str_to_num(screen.number_1.text())
                res = str(IntegerNumber.natural_to_integer(num_1))
                self.local_module.ui.result.setText(str(res))

            elif module == 4:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                res = num_1.to_natural()
                self.local_module.ui.result.setText(str(res))

            elif module == 5:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                num_2 = IntegerNumber.str_to_num(screen.number_2.text())
                res = str(num_1.add(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 6:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                num_2 = IntegerNumber.str_to_num(screen.number_2.text())
                res = str(num_1.subtract(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 7:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                num_2 = IntegerNumber.str_to_num(screen.number_2.text())
                res = (num_1.multiply(num_2))
                self.local_module.ui.result.setText(str(res))

            elif module == 8:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                num_2 = IntegerNumber.str_to_num(screen.number_2.text())
                res = str(num_1.quotient(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 9:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                num_2 = IntegerNumber.str_to_num(screen.number_2.text())
                res = str(num_1.remainder(num_2))
                self.local_module.ui.result.setText(res)

        if self.main_module == 'Рациональные числа':
            if module == 0:
                num_1 = RationalNumber.str_to_num(screen.number_1.text())
                res = str(num_1.reduce())
                self.local_module.ui.result.setText(res)

            elif module == 1:
                num_1 = RationalNumber.str_to_num(screen.number_1.text())
                res = str(num_1.is_integer())
                self.local_module.ui.result.setText(res)

            elif module == 2:
                num_1 = IntegerNumber.str_to_num(screen.number_1.text())
                res = str(RationalNumber.integer_to_rational(num_1))
                self.local_module.ui.result.setText(res)

            elif module == 3:
                num_1 = RationalNumber.str_to_num(screen.number_1.text())
                res = str(num_1.to_integer())
                self.local_module.ui.result.setText(res)

            elif module == 4:
                num_1 = RationalNumber.str_to_num(screen.number_1.text())
                num_2 = RationalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.add(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 5:
                num_1 = RationalNumber.str_to_num(screen.number_1.text())
                num_2 = RationalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.subtract(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 6:
                num_1 = RationalNumber.str_to_num(screen.number_1.text())
                num_2 = RationalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.multiply(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 7:
                num_1 = RationalNumber.str_to_num(screen.number_1.text())
                num_2 = RationalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.divide(num_2))
                self.local_module.ui.result.setText(res)
       
        if self.main_module == 'Многочлены':
            if module == 0:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                num_2 = Polynomial.str_to_num(screen.number_2.text())
                res = str(num_1.add(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 1:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                num_2 = Polynomial.str_to_num(screen.number_2.text())
                res = str(num_1.subtract(num_2))
                self.local_module.ui.result.setText(res)
            
            elif module == 2:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                num_2 = RationalNumber.str_to_num(screen.number_2.text())
                res = str(num_1.multiply_by_rational(num_2))
                self.local_module.ui.result.setText(res)
        
            elif module == 3:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                digit_2 = screen.digit_1.value()
                res = str(num_1.multiply_by_monomial(digit_2))
                self.local_module.ui.result.setText(res)

            elif module == 4:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                res = str(num_1.highest_coefficient())
                self.local_module.ui.result.setText(res)

            elif module == 5:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                res = str(num_1.get_degree())
                self.local_module.ui.result.setText(res)

            elif module == 6:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                res = str(num_1.take_out_gdc_lcm())
                self.local_module.ui.result.setText(res)

            elif module == 7:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                num_2 = Polynomial.str_to_num(screen.number_2.text())
                res = str(num_1.multiply(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 8:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                num_2 = Polynomial.str_to_num(screen.number_2.text())
                res = str(num_1.quotient(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 9:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                num_2 = Polynomial.str_to_num(screen.number_2.text())
                res = str(num_1.remainder(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 10:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                num_2 = Polynomial.str_to_num(screen.number_2.text())
                res = str(num_1.gcd(num_2))
                self.local_module.ui.result.setText(res)

            elif module == 11:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                res = str(num_1.derivative())
                self.local_module.ui.result.setText(res)

            elif module == 12:
                num_1 = Polynomial.str_to_num(screen.number_1.text())
                res = str(num_1.multiple_roots_to_simple())
                self.local_module.ui.result.setText(res)

            

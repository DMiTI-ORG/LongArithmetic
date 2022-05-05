
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
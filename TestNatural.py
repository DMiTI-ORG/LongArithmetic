import imp
from unittest import TestCase
from unittest.mock import patch

from NaturalNumber import NaturalNumber


class TestNatural(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar'
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    @patch.object(NaturalNumber, 'multiply_digit')
    @patch.object(NaturalNumber, 'compare')
    @patch.object(NaturalNumber, 'subtract')
    def test_subtract_k_by_number(self, subtract, compare, multiply_digit):
        number_1 = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(2, [3, 0])
        number_3 = NaturalNumber(2, [1, 1])

        compare.return_value = 2
        subtract.return_value = NaturalNumber(2, [1, 1])
        multiply_digit.return_value = NaturalNumber(2, [3, 0])
        self.assertEqual(str(number_3), str(number_1.subtract_k_by_number(number_2, 1)))

        multiply_digit.return_value = NaturalNumber(1, [5])
        compare.return_value = 1
        subtract.return_value = NaturalNumber(1, [-1])
        self.assertEqual(number_1.subtract_k_by_number(number_2, 1), 'Error')

    def test_add_one(self):
        number_1 = NaturalNumber(3, [2, 7, 9])
        number_2 = NaturalNumber(3, [2, 8, 0])
        number_3 = NaturalNumber(2, [9, 9])
        number_4 = NaturalNumber(3, [1, 0, 0])
        self.assertEqual(number_2, number_1.add_one())
        self.assertEqual(number_4, number_3.add_one())


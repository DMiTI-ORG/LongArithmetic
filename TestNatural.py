from unittest import TestCase
from unittest.mock import patch

import NaturalNumber

class TestNatural(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    @patch.object(NaturalNumber.NaturalNumber, 'multiply_digit')
    @patch.object(NaturalNumber.NaturalNumber, 'compare')
    @patch.object(NaturalNumber.NaturalNumber, 'subtract')
    def test_subtract_k_by_number(self, multiply_digit, compare, subtract):
        multiply_digit.return_value = (0, [3])
        compare.return_value = 2
        subtract.return_value = (0, [1])
        self.number = NaturalNumber.NaturalNumber(0, [4])
        self.assertEqual(self.number.subtract_k_by_number((0, [3]), 1), (0, [1]))
        multiply_digit.return_value = (0, [5])
        compare.return_value = 1
        subtract.return_value = (0, [-1])
        self.assertEqual(self.number.subtract_k_by_number((0, [5]), 1), 'Error')
 

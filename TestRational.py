import imp
from unittest import TestCase
from unittest.mock import patch
from WholeNumber import WholeNumber
from NaturalNumber import NaturalNumber
from RationalNumber import RationalNumber

class TestRational(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    @patch.object(WholeNumber, 'abs')
    @patch.object(NaturalNumber, 'gcd')
    @patch.object(WholeNumber, 'quotient')
    def test_reduce(self, quotient, gcd, abs):
        number_1 = RationalNumber((0, 2, [1, 4]), (1, [7])) 
 
        abs.return_value = NaturalNumber(2, [1, 4])
        gcd.return_value = NaturalNumber(1, [7])
        quotient.side_effect = [WholeNumber(0, 1, [2]), WholeNumber(0, 1, [1])]
        self.assertEqual(RationalNumber((0, 1, [2]), (1, [1])), number_1.reduce())
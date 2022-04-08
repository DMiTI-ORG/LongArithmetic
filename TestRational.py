from unittest import TestCase
from unittest.mock import patch
from NaturalNumber import NaturalNumber
from RationalNumber import RationalNumber
from WholeNumber import WholeNumber

class TestRational(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''
    @patch.object(WholeNumber, 'mul_zz_z')
    @patch.object(NaturalNumber, 'mul_nn_n')
    def test_multiply(self, mul_nn_n, mul_zz_z):
        number_1 = RationalNumber([0, 2, [2, 3]], [2, [1, 4]])
        number_2 = RationalNumber([1, 3, [1, 4]], [3, [2, 5, 7]])
        number_3 = RationalNumber([0, 1, [5]], [4, [4, 5, 8, 6]])

        mul_zz_z.return_value = WholeNumber([0, 3, [3, 2, 2]])
        mul_nn_n.return_value = NaturalNumber([0, 4, [3, 5, 9, 8]])
        self.assertEqual(RationalNumber([0, 3, [3, 2, 2]], [0, 4, [3, 5, 9, 8]]), number_1.multiply(number_2))

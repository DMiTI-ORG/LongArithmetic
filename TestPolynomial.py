from unittest import TestCase
from unittest.mock import patch, Mock
from Polynomial import Polynomial
from NaturalNumber import NaturalNumber

class TestPolynomial(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    def test_get_degree(self):
        number_1 = Polynomial(5, [1, 0, 0, 1, 6, 9])
        number_2 = NaturalNumber(1, [5])

        self.assertEqual(str(number_1.get_degree()), str(number_2))

        number_1 = Polynomial(3, [1, 0, 0, 1])
        number_2 = NaturalNumber(1, [3])

        self.assertEqual(str(number_1.get_degree()), str(number_2))
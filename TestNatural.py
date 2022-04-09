
from unittest import TestCase
from unittest.mock import patch

from NaturalNumber import NaturalNumber


class TestNatural(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    @patch.object(NaturalNumber, 'gcd')
    @patch.object(NaturalNumber, 'multiply')

    def test_lcm(self, multiply, gcd):

        number_1 = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(2, [3, 0])
        number_3 = NaturalNumber(4, [1, 2, 3, 0])

        gcd.return_value = 1
        multiply.return_value = 1230

        self.assertEqual(str(number_3), str(number_1.lcm(number_2)))

        multiply.return_value = 0
        gcd.return_value = 1
        self.assertEqual(number_1.lcm(number_2), 'Error')


from unittest import TestCase
from unittest.mock import patch, Mock
from Polynomial import Polynomial
from RationalNumber import RationalNumber

class TestPolynomial(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''


    @patch.object(RationalNumber, 'multiply')
    def test_multiply(self, multiply):
        number_1 = Polynomial(3, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [1]), (1, [1]))])
        number_2 = RationalNumber((0, 3, [2, 4, 1]), (1, [1]))
        number_3 = Polynomial(3, [RationalNumber((0, 3, [2, 4, 1]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 3, [2, 4, 1]), (1, [1]))])

        c1 = RationalNumber((0, 3, [2, 4, 1]), (1, [1]))
        c2 = RationalNumber((0, 1, [0]), (1, [1]))
        c3 = RationalNumber((0, 1, [0]), (1, [1]))
        c4 = RationalNumber((0, 3, [2, 4, 1]), (1, [1]))

        multiply.side_effect = [c1, c2, c3, c4]

        self.assertEqual(str(number_1.multiply_by_rational(number_2)), str(number_3))

        number_1 = Polynomial(3, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [1]), (1, [1]))])
        number_2 = RationalNumber((1, 3, [2, 4, 1]), (1, [1]))
        number_3 = Polynomial(3, [RationalNumber((1, 3, [2, 4, 1]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((1, 3, [2, 4, 1]), (1, [1]))])

        c1 = RationalNumber((1, 3, [2, 4, 1]), (1, [1]))
        c2 = RationalNumber((0, 1, [0]), (1, [1]))
        c3 = RationalNumber((0, 1, [0]), (1, [1]))
        c4 = RationalNumber((1, 3, [2, 4, 1]), (1, [1]))

        multiply.side_effect = [c1, c2, c3, c4]

        self.assertEqual(str(number_1.multiply_by_rational(number_2)), str(number_3))
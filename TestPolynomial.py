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


    @patch.object(Polynomial, 'multiply_by_rational')
    @patch.object(Polynomial, 'add')
    def test_multiply(self, add, multiply_by_rational):
        number_1 = Polynomial(1, [1, 1])
        number_2 = Polynomial(2, [1, -1, 1])
        number_3 = Polynomial(3, [1, 0, 0, 1])

        number_2.multiply_by_monomial = Mock(side_effect=[Polynomial(3, [1, -1, 1, 0]), Polynomial(2, [1, -1, 1])])
        multiply_by_rational.return_value = number_2
        add.return_value = number_3
        self.assertEqual(str(number_1.multiply(number_2)), str(number_3))

    @patch.object(Polynomial, 'remainder')
    def test_gcd(self, remainder):
        #x^3 – x^2 – 5x – 3
        number_1 = Polynomial(3, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((1, 1, [1]), (1, [1])),
                                  RationalNumber((1, 1, [5]), (1, [1])), RationalNumber((1, 1, [3]), (1, [1]))])
        #x^2 + x – 12
        number_2 = Polynomial(2, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [1]), (1, [1])),
                                  RationalNumber((1, 2, [1, 2]), (1, [1]))])
        #x - 3
        number_3 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((1, 1, [3]), (1, [1]))])

        #x - 3
        c1 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((1, 1, [3]), (1, [1]))])
        c2 = Polynomial(0, [])
        remainder.side_effect = [c1, c2]
        self.assertEqual(number_3, number_1.gcd(number_2))

        #x^2 + 2x - 24
        number_1 = Polynomial(2, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [2]), (1, [1])),
                                  RationalNumber((1, 2, [2, 4]), (1, [1]))])
        #x + 6
        number_2 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [6]), (1, [1]))])
        # x + 6
        number_3 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [6]), (1, [1]))])

        # x + 6
        c1 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [6]), (1, [1]))])
        c2 = Polynomial(0, [])
        remainder.side_effect = [c1, c2]
        self.assertEqual(number_3, number_1.gcd(number_2))

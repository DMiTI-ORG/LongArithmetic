from unittest import TestCase
from unittest.mock import patch, Mock
from RationalNumber import RationalNumber
from Polynomial import Polynomial


class TestPolynomial(TestCase):
    """
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)
     """


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


    @patch.object(RationalNumber, 'multiply')
    def test_derivative(self, multiply):
        # 2x^2+5x-7 = 4x + 5
        orig = Polynomial(2, [RationalNumber((0, 1, [2]), (1, [1])), RationalNumber((0, 1, [5]), (1, [1])),
                              RationalNumber((1, 1, [7]), (1, [1]))])
        c1 = RationalNumber((0, 1, [4]), (1, [1]))
        c2 = RationalNumber((0, 1, [5]), (1, [1]))
        multiply.side_effect = [c1, c2]
        self.assertEqual(orig.derivative().array[0].numerator.array,
                         Polynomial(1, [c1, c2]).array[0].numerator.array)

        # 3x^3+4x^2+8x-10 = 9x^2+8x+9
        orig = Polynomial(2, [RationalNumber((0, 1, [2]), (1, [1])), RationalNumber((0, 1, [5]), (1, [1])),
                              RationalNumber((1, 1, [7]), (1, [1]))])
        c1 = RationalNumber((0, 1, [9]), (1, [1]))
        c2 = RationalNumber((0, 1, [8]), (1, [1]))
        c3 = RationalNumber((0, 1, [9]), (1, [1]))
        multiply.side_effect = [c1, c2, c3]
        self.assertEqual(orig.derivative().array[0].numerator.array,
                         Polynomial(1, [c1, c2, c3]).array[0].numerator.array)


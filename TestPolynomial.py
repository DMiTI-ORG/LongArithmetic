from unittest import TestCase
from unittest.mock import patch, Mock
from Polynomial import Polynomial

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
        number_1 = Polynomial(2, [6.25, -17.5, 12.25])
        number_2 = Polynomial(1, [2.5, -3.5])
        number_3 = Polynomial(1, [2.5, -3.5])

        c1 = Polynomial(1, [2.5, -3.5])
        c2 = Polynomial(0, [])
        remainder.side_effect = [c1, c2]
        self.assertEqual(number_3, number_1.gcd(number_2))

        number_1 = Polynomial(3, [0.125, -1.6875, 7.59375, -11.390625])
        number_2 = Polynomial(2, [0.25, -2.25, 5.0625])
        number_3 = Polynomial(1, [0.5, -2.25])

        c1 = Polynomial(1, [0.5, -2.25])
        c2 = Polynomial(0, [])
        remainder.side_effect = [c1, c2]
        self.assertEqual(number_3, number_1.gcd(number_2))

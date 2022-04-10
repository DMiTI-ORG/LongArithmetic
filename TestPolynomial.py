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

    def test_multiply_by_monomial(self):
        polynomial_1 = Polynomial(3, [2, 3, 4, 5])
        polynomial_2 = Polynomial(2, [1, 0, 0])
        polynomial_3 = Polynomial(0, [5])
        degree_1 = 0
        degree_2 = 3
        degree_3 = 2
        self.assertEqual(polynomial_1.multiply_by_monomial(degree_1), Polynomial(3, [2, 3, 4, 5]))
        self.assertEqual(polynomial_2.multiply_by_monomial(degree_2), Polynomial(5, [1, 0, 0, 0, 0, 0]))
        self.assertEqual(polynomial_3.multiply_by_monomial(degree_3), Polynomial(2, [5, 0, 0]))

    @patch.object(Polynomial, 'derivative')
    @patch.object(Polynomial, 'gcd')
    @patch.object(Polynomial, 'quotient')
    def test_multiple_roots_to_simple(self, quotient, gcd, derivative):
        number_1 = Polynomial(5, [1, -8, 25, -38, 28, 8])

        derivative.return_value = Polynomial(4, [5, -32, 75, -76, 28])
        gcd.return_value = Polynomial(3, [1, -5, 8, -4])
        quotient.return_value = Polynomial(2, [1, -3, 2])
        self.assertEqual(number_1.multiple_roots_to_simple(), Polynomial(2, [1, -3, 2]))
from unittest import TestCase
from unittest.mock import patch

import Polynomial

class TestPolynomial(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    @patch.object(Polynomial.Polynomial, 'multiply_by_monomial')
    @patch.object(Polynomial.Polynomial, 'multiply_by_rational')
    @patch.object(Polynomial.Polynomial, 'add')
    def test_multiply(self, multiply_by_monomial, multiply_by_rational, add):
        multiply_by_monomial.return_value = (0, [2])
        multiply_by_rational.return_value = (0, [4])
        add.return_value = (0, [4])
        self.polynom = Polynomial.Polynomial(0, [2])
        self.assertEqual(self.polynom.multiply((0, [2])), (0, [4]))
 

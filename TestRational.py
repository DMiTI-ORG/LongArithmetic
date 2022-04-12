from unittest import TestCase
from unittest.mock import patch
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
    def test_whole_to_rational(self):
        number1 = WholeNumber(1, 2, [1,2,3])
        number2 = RationalNumber((1, 2, [1,2,3]), (1,[1]))
        self.assertEqual(number1.whole_to_rational(), number2)

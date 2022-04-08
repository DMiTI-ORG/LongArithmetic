from unittest import TestCase
from unittest.mock import patch

from WholeNumber import WholeNumber

class TestWhole(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)
    '''
    def test_multiply_by_minus_one(self):
        number_1 = WholeNumber(1, 2, [4, 1])
        number_2 = WholeNumber(0, 2, [3, 0])
        number_3 = WholeNumber(0, 2, [4, 1])
        number_4 = WholeNumber(1, 2, [3, 0])

        self.assertEqual(str(number_3), str(number_1.multiply_by_minus_one()))
        self.assertEqual(str(number_4), str(number_2.multiply_by_minus_one()))
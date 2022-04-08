from unittest import TestCase
from unittest.mock import patch
from NaturalNumber import NaturalNumber

from WholeNumber import WholeNumber

class TestWhole(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''
    def test_to_natural(self):
        number_1 = WholeNumber(0, 2, [2, 1])
        number_2 = WholeNumber(0, 1, [0])
        number_3 = WholeNumber(1, 1, [7])

        self.assertEqual(NaturalNumber(2, [2, 1]), number_1.to_natural())
        self.assertEqual(NaturalNumber(1, [0]), number_2.to_natural())
        self.assertEqual('Error', number_3.to_natural())
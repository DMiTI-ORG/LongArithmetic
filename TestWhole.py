import imp
from unittest import TestCase
from unittest.mock import patch
from WholeNumber import WholeNumber
from NaturalNumber import NaturalNumber

class TestWhole(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    def test_natural_to_whole(self):
        number_1 = NaturalNumber(2, [2,1])
        number_2 = NaturalNumber(1, [0])
        number_3 = NaturalNumber(1, [7])

        self.assertEqual(str(WholeNumber(0, 2, [2, 1])), str(WholeNumber.natural_to_whole(number_1)))
        self.assertEqual(str(WholeNumber(0, 1, [0])), str(WholeNumber.natural_to_whole(number_2)))
        self.assertEqual(str(WholeNumber(0, 1, [7])), str(WholeNumber.natural_to_whole(number_3)))
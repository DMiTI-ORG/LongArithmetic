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

    @patch.object(WholeNumber, 'abs')
    @patch.object(NaturalNumber, 'add')
    @patch.object(NaturalNumber, 'compare')
    @patch.object(NaturalNumber, 'subtract')
    def test_add1(self, subtract, compare, add, abs):
        number_1 = WholeNumber(1, 3, [1, 2, 3])
        number_2 = WholeNumber(1, 3, [1, 2, 3])
        number_3 = WholeNumber(1, 3, [2, 4, 6])
        number_4 = WholeNumber(1, 3, [1, 2, 3])
        number_5 = WholeNumber(0, 2, [2, 3])
        number_6 = WholeNumber(1, 3, [1, 0, 0])

        abs.return_value = NaturalNumber(3, [1, 2, 3])
        abs.return_value = NaturalNumber(3, [1, 2, 3])
        add.return_value = NaturalNumber(3, [2, 4, 6])
        self.assertEqual(number_3, number_1.add1(number_2))

        abs.return_value = NaturalNumber(3, [1, 2, 3])
        abs.return_value = NaturalNumber(2, [2, 3])
        compare.return_value = 0
        subtract.return_value = NaturalNumber(3, [1, 0, 0])
        self.assertEqual(number_6, number_4.add1(number_5))
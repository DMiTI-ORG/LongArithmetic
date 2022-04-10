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

    def test_to_whole(self):
        number_1 = RationalNumber((1, 4, [2, 3, 4, 5]),(1,[1]))
        number_2 = WholeNumber(1, 4, [2, 3, 4, 5])
        self.assertEqual(str(number_2), str(number_1.to_whole()))

        number_1 = RationalNumber((1, 6, [2, 6, 4, 8, 3, 9]), (1, [1]))
        number_2 = WholeNumber(1, 6, [2, 6, 4, 8, 3, 9])
        self.assertEqual(str(number_2), str(number_1.to_whole()))

        number_1 = RationalNumber((1, 8, [2, 4, 8, 1, 2, 9, 3, 6]), (1, [1]))
        number_2 = WholeNumber(1, 8, [2, 4, 8, 1, 2, 9, 3, 6])
        self.assertEqual(str(number_2), str(number_1.to_whole()))

        number_1 = RationalNumber((1, 6, [2, 6, 4, 8, 3, 9]), (1, [7]))
        self.assertEqual('ERROR', str(number_1.to_whole()))

        number_1 = RationalNumber((1, 3, [4, 2, 9]), (1, [0]))
        self.assertEqual('ERROR', str(number_1.to_whole()))
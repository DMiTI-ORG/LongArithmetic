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
        self.assertEqual(self.calc.foo(100, 200), 5)
    '''

    @patch.object(WholeNumber, 'multiply')
    @patch.object(WholeNumber, 'subtract')
    def test_subtract(self, subtract, multiply):
        # 1/2 - 1/3 = 1/6
        multiply.side_effect = [WholeNumber(0, 1, [3]), WholeNumber(0, 1, [2])]
        subtract.return_value = WholeNumber(0, 1, [1])
        self.assertEqual(RationalNumber((0, 1, [1]), (1, [2])).subtract(RationalNumber((0, 1, [1]), (1, [3]))).
                         numerator.array, RationalNumber((0, 1, [1]), (1, [6])).numerator.array)
        # 5/6 - 1/1 = -1/6
        multiply.side_effect = [WholeNumber(0, 1, [5]), WholeNumber(0, 1, [6])]
        subtract.return_value = WholeNumber(1, 1, [1])
        self.assertEqual(RationalNumber((0, 1, [5]), (1, [6])).subtract(RationalNumber((0, 1, [1]), (1, [1]))).
                         numerator.array, RationalNumber((1, 1, [1]), (1, [6])).numerator.array)
        # 3/7 - 2/11 = 19/77
        multiply.side_effect = [WholeNumber(0, 2, [3, 3]), WholeNumber(0, 2, [1, 4])]
        subtract.return_value = WholeNumber(0, 2, [1, 9])
        self.assertEqual(RationalNumber((0, 1, [3]), (1, [7])).subtract(RationalNumber((0, 1, [2]), (2, [1, 1]))).
                         numerator.array, RationalNumber((0, 2, [1, 9]), (2, [7, 7])).numerator.array)


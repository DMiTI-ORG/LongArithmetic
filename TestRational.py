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

    @patch.object(RationalNumber, 'multiply')
    @patch.object(WholeNumber, 'subtract')
    def test_subtract(self, subtract, multiply):
        # 1/2 - 1/3 = 1/6
        multiply.side_effect = [WholeNumber(0, 1, [3]), WholeNumber(0, 1, [2])]
        subtract.return_value = WholeNumber(0, 1, [1])
        self.assertEqual(RationalNumber((0, 1, [1]), (1, [2])).subtract(RationalNumber((0, 1, [1]), (1, [3]))),
                         RationalNumber((0, 1, [1]), (1, [6])))


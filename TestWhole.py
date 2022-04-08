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

    def test_is_positive(self):
        res_1 = 1 #negative
        res_2 = 2 #positive
        res_3 = 0 #zero

        num_1 = WholeNumber(1, 2, [1, 0]) #negative
        num_2 = WholeNumber(0, 2, [3, 3]) #positive
        num_3 = WholeNumber(1, 2, [0, 0]) #zero
        num_4 = WholeNumber(0, 2, [0, 0]) #zero

        self.assertEquals(res_1, num_1.is_positive())

    def test_abc(self):
        res = NaturalNumber(3, [1, 2, 3])

        num = WholeNumber(1, 3, [1, 2, 3])

        self.assertEqual(res, num.abs())

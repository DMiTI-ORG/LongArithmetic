import imp
from unittest import TestCase
from unittest.mock import patch

from NaturalNumber import NaturalNumber


class TestNatural(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    @patch.object(NaturalNumber, 'multiply_digit')
    @patch.object(NaturalNumber, 'compare')
    @patch.object(NaturalNumber, 'subtract')
    def test_subtract_k_by_number(self, subtract, compare, multiply_digit):
        number_1 = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(2, [3, 0])
        number_3 = NaturalNumber(2, [1, 1])

        compare.return_value = 2
        subtract.return_value = NaturalNumber(2, [1, 1])
        multiply_digit.return_value = NaturalNumber(2, [3, 0])
        self.assertEqual(str(number_3), str(number_1.subtract_k_by_number(number_2, 1)))

        multiply_digit.return_value = NaturalNumber(1, [5])
        compare.return_value = 1
        subtract.return_value = NaturalNumber(1, [-1])
        self.assertEqual(number_1.subtract_k_by_number(number_2, 1), 'Error')


    def test_compare(self):
        number_1 = NaturalNumber(3, [4, 1, 0])
        number_2 = NaturalNumber(2, [3, 0])
        number_3 = NaturalNumber(2, [3, 0])
        number_4 = NaturalNumber(3, [4, 1, 0])
        number_5 = NaturalNumber(2, [3, 0])
        number_6 = NaturalNumber(2, [3, 1])
        number_7 = NaturalNumber(3, [5, 3, 1])
        number_8 = NaturalNumber(3, [5, 3, 0])
        number_9 = NaturalNumber(2, [1, 1])
        number_10 = NaturalNumber(2, [1, 1])

        self.assertEqual(2, number_1.compare(number_2))
        self.assertEqual(1, number_3.compare(number_4))
        self.assertEqual(1, number_5.compare(number_6))
        self.assertEqual(2, number_7.compare(number_8))
        self.assertEqual(0, number_9.compare(number_10))

    def test_is_zero(self):
        number_1 = NaturalNumber(5, [4, 1, 0, 6, 7])
        number_2 = NaturalNumber(1, [3])
        number_3 = NaturalNumber(1, [0])

        self.assertEqual(False, number_1.is_zero())
        self.assertEqual(False, number_2.is_zero())
        self.assertEqual(True, number_3.is_zero())

    def test_add(self):
        number_1 = NaturalNumber(3, [4, 1, 0])
        number_2 = NaturalNumber(3, [3, 0, 5])
        number_3 = NaturalNumber(3, [3, 5, 7])
        number_4 = NaturalNumber(3, [4, 6, 8])
        number_5 = NaturalNumber(2, [3, 1])
        number_6 = NaturalNumber(2, [3, 1])
        number_7 = NaturalNumber(5, [5, 3, 1, 2, 3])
        number_8 = NaturalNumber(3, [5, 3, 0])
        number_9 = NaturalNumber(2, [1, 1])
        number_10 = NaturalNumber(4, [1, 1, 5, 6])
        number_11 = NaturalNumber(3, [9, 9, 9])
        number_12 = NaturalNumber(3, [9, 9, 9])

        self.assertEqual([7, 1, 5], number_1.add(number_2))
        self.assertEqual([8, 2, 5], number_3.add(number_4))
        self.assertEqual([6, 2], number_5.add(number_6))
        self.assertEqual([5, 3, 6, 5, 3], number_7.add(number_8))
        self.assertEqual([1, 1, 6, 7], number_9.add(number_10))
        self.assertEqual([1, 9, 9, 8], number_11.add(number_12))




import unittest
from unittest import TestCase
from NaturalNumber import NaturalNumber
from unittest.mock import patch


class TestNatural(TestCase):
    """
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
    """

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

    @patch.object(NaturalNumber, 'compare')
    @patch.object(NaturalNumber, 'subtract_k_by_number')
    @patch.object(NaturalNumber, 'first_division_digit')
    def test_quotient(self, first_division_digit, subtract_k_by_number, compare):
        # 999 // 988 = 1
        compare.return_value = 2
        subtract_k_by_number.return_value = NaturalNumber(2, [1, 1])
        first_division_digit.return_value = NaturalNumber(1, [1])
        self.assertEqual(NaturalNumber(3, [9, 9, 9]).quotient(NaturalNumber(3, [9, 8, 8])).array,
                         NaturalNumber(1, [1]).array)
        # 1005 // 17 = 59
        compare.side_effect = [1, 2]
        subtract_k_by_number.side_effect = [NaturalNumber(2, [1, 5]), NaturalNumber(1, [2])]
        first_division_digit.side_effect = [NaturalNumber(1, [5]), NaturalNumber(1, [9])]
        self.assertEqual(NaturalNumber(4, [1, 0, 0, 5]).quotient(NaturalNumber(2, [1, 7])).array,
                         NaturalNumber(2, [5, 9]).array)





if __name__ == '__main__':
    unittest.main()


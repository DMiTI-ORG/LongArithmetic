from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from ..Modules.NaturalNumber import NaturalNumber


class TestNatural(TestCase):
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

    def test_add_one(self):
        number_1 = NaturalNumber(3, [2, 7, 9])
        number_2 = NaturalNumber(3, [2, 8, 0])
        number_3 = NaturalNumber(2, [9, 9])
        number_4 = NaturalNumber(3, [1, 0, 0])
        self.assertEqual(number_2, number_1.add_one())
        self.assertEqual(number_4, number_3.add_one())

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

        self.assertEqual(NaturalNumber(3, [7, 1, 5]), number_1.add(number_2))
        self.assertEqual(NaturalNumber(3, [8, 2, 5]), number_3.add(number_4))
        self.assertEqual(NaturalNumber(2, [6, 2]), number_5.add(number_6))
        self.assertEqual(NaturalNumber(5, [5, 3, 6, 5, 3]), number_7.add(number_8))
        self.assertEqual(NaturalNumber(4, [1, 1, 6, 7]), number_9.add(number_10))
        self.assertEqual(NaturalNumber(4, [1, 9, 9, 8]), number_11.add(number_12))
        self.assertEqual(NaturalNumber(4, [1, 9, 9, 8]), number_11.add(number_12))


    @patch.object(NaturalNumber, 'compare')
    def test_subtract(self, compare):
        number_1 = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(2, [3, 0])
        number_3 = NaturalNumber(2, [1, 1])
        number_4 = NaturalNumber(2, [1, 2])
        number_5 = NaturalNumber(2, [1, 1])
        number_6 = NaturalNumber(1, [1])

        n1 = NaturalNumber(2, [1, 2])
        n2 = NaturalNumber(1, [4])
        n3 = NaturalNumber(1, [8])

        compare.return_value = 2
        self.assertEqual(number_3, number_1.subtract(number_2))
        self.assertEqual(number_6, number_4.subtract(number_5))
        self.assertEqual(n1.subtract(n2), n3)

    def test_multiply_digit(self):
        number_1 = NaturalNumber(3, [1, 1, 1])
        self.assertEqual(str(NaturalNumber(3, [4, 4, 4])), str(number_1.multiply_digit(4)))

    def test_multiply_by_powered_ten(self):
        number = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(4,[4,1,0,0])
        number_3 = number.multiply_by_powered_ten(2)
        self.assertEqual(str(number_3), str(number_2))

    @patch.object(NaturalNumber, 'add')
    @patch.object(NaturalNumber, 'multiply_by_powered_ten')
    def test_multiply(self, multiply_by_powered_ten, add):
        number_1 = NaturalNumber(3, [1, 1, 1])
        number_2 = NaturalNumber(2, [2, 4])
        number_3 = NaturalNumber(4, [2, 6, 6, 4])
        number_1.multiply_digit = Mock(side_effect=[NaturalNumber(3, [4, 4, 4]), NaturalNumber(3, [2, 2, 2])])
        multiply_by_powered_ten.side_effect = [NaturalNumber(3, [4, 4, 4]), NaturalNumber(4, [2, 2, 2, 0])]
        add.side_effect = [NaturalNumber(3, [4, 4, 4]), NaturalNumber(4, [2, 6, 6, 4])]
        self.assertEqual(str(number_2.multiply(number_1)), str(number_3))

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
    @patch.object(NaturalNumber, 'subtract')
    @patch.object(NaturalNumber, 'multiply_by_powered_ten')
    def test_first_division_digit(self, multiply_by_powered_ten, subtract, compare):
        number_1 = NaturalNumber(5, [4, 4, 4, 6, 0])
        number_2 = NaturalNumber(3, [2, 2, 2])

        compare.side_effect = [2, 2, 2, 1, 1]
        subtract.side_effect = [NaturalNumber(5, [2, 2, 2, 6, 0]), NaturalNumber(2, [6, 0])]
        multiply_by_powered_ten.return_value = NaturalNumber(5, [2, 2, 2, 0, 0])
        self.assertEqual(number_1.first_division_digit(number_2), NaturalNumber(1, [2]))

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

    @patch.object(NaturalNumber, 'subtract_k_by_number')
    @patch.object(NaturalNumber, 'multiply')
    @patch.object(NaturalNumber, 'quotient')
    def test_remainder(self, quotient, multiply, subtract_k_by_number):
        number = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(2, [4, 0])
        number_3 = NaturalNumber(1, [1])
        quotient.return_value = NaturalNumber(1, [1])
        multiply.return_value = NaturalNumber(2, [4, 0])
        subtract_k_by_number.return_value = NaturalNumber(1, [1])
        self.assertEqual(str(number.remainder(number_2)), str(number_3))

    @patch.object(NaturalNumber, 'remainder')
    @patch.object(NaturalNumber, 'compare')
    @patch.object(NaturalNumber, 'is_zero')
    def test_gcd(self, is_zero, compare, remainder):
        num_1 = NaturalNumber(3, [1, 0, 1])
        num_2 = NaturalNumber(2, [1, 1])
        res_num = NaturalNumber(1, [1])

        num_1.is_zero = Mock(side_effect=['yes', 'yes', 'yes', 'no'])
        num_2.is_zero = Mock(side_effect=['yes', 'yes', 'yes', 'yes'])
        num_1.compare = Mock(side_effect=[2, 1, 2])
        remainder.side_effect = [NaturalNumber(1, [2]), NaturalNumber(0, [0])]
        remainder.side_effect = [NaturalNumber(1, [1])]
        self.assertEqual(num_1.gcd(num_2), res_num)

    @patch.object(NaturalNumber, 'gcd')
    @patch.object(NaturalNumber, 'multiply')
    def test_lcm(self, multiply, gcd):
        number_1 = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(2, [3, 0])
        number_3 = NaturalNumber(4, [1, 2, 3, 0])

        gcd.return_value = 1
        multiply.return_value = 1230
        self.assertEqual(str(number_3), str(number_1.lcm(number_2)))

        multiply.return_value = 0
        gcd.return_value = 1
        self.assertEqual(number_1.lcm(number_2), 'Error')
        
from unittest import TestCase
from unittest.mock import patch
from mock.mock import Mock

from NaturalNumber import NaturalNumber

class TestNatural(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar'
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)
    '''

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

        multiply_digit.return_value = NaturalNumber(1, [5])
        compare.return_value = 1
        subtract.return_value = NaturalNumber(1, [-1])
        self.assertEqual(number_1.subtract_k_by_number(number_2, 1), 'Error')

    def test_add_one(self):
        number_1 = NaturalNumber(3, [2, 7, 9])
        number_2 = NaturalNumber(3, [2, 8, 0])
        number_3 = NaturalNumber(2, [9, 9])
        number_4 = NaturalNumber(3, [1, 0, 0])
        self.assertEqual(number_2, number_1.add_one())
        self.assertEqual(number_4, number_3.add_one())

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


    def test_multiply_digit(self):
        number_1 = NaturalNumber(3, [1, 1, 1])
        self.assertEqual(str(NaturalNumber(3, [4, 4, 4])), str(number_1.multiply_digit(4)))

    @patch.object(NaturalNumber, 'compare')
    def test_subtract(self, compare):
        number_1 = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(2, [3, 0])
        number_3 = NaturalNumber(2, [1, 1])
        number_4 = NaturalNumber(2, [1, 2])
        number_5 = NaturalNumber(2, [1, 1])
        number_6 = NaturalNumber(1, [1])

        compare.return_value = 2
        self.assertEqual(number_3, number_1.subtract(number_2))
        self.assertEqual(number_6, number_4.subtract(number_5))

    def test_multiply_by_powered_ten(self):
        number = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(4,[4,1,0,0])
        number.multiply_by_powered_ten(2)
        self.assertEqual(str(number), str(number_2))


    @patch.object(NaturalNumber, 'subtract_k_by_number')
    @patch.object(NaturalNumber, 'multiply')
    @patch.object(NaturalNumber, 'quotient')
    def test_remainder(self, quotient, multiply, subtract_k_by_number):
        number = NaturalNumber(2, [4, 1])
        number_2 = NaturalNumber(2,[4,0])
        number_3 = NaturalNumber(1,[1])
        quotient.return_value = NaturalNumber (1,[1])
        multiply.return_value = NaturalNumber (2, [4,0])
        subtract_k_by_number.return_value = NaturalNumber (1, [1])
        self.assertEqual(str(number.remainder(number_2)), str(number_3))

    @patch.object(NaturalNumber, 'is_zero')
    @patch.object(NaturalNumber, 'compare')
    @patch.object(NaturalNumber, 'remainder')
    def test_gcd(self, is_zero, compare, ramainder):
        num_1 = NaturalNumber(4, [3, 5, 4, 6])
        num_2 = NaturalNumber(2, [24, 12])
        res_num = NaturalNumber(4, [0, 0, 4, 6])

        num_1.is_zero = Mock(side_effect=['yes', 'yes', 'yes', 'yes'])
        num_2.is_zero = Mock(side_effect=['no', 'no', 'yes', 'yes'])
        num_1.compare = Mock(side_effect=[1, 1])
        self.assertEqual(num_1.gcd(num_2), res_num)

    @patch.object(NaturalNumber, 'compare')
    @patch.object(NaturalNumber, 'subtract')
    @patch.object(NaturalNumber, 'multiply_by_powered_ten')
    def test_first_division_digit(self, multiply_by_powered_ten, subtract,  compare):
        number_1 = NaturalNumber(5, [4, 4, 4, 6, 0])
        number_2 = NaturalNumber(3, [2, 2, 2])

        compare.side_effect=[2, 2, 2, 1, 1]
        subtract.side_effect=[NaturalNumber(5, [2, 2, 2, 6, 0]), NaturalNumber(2, [6, 0])]
        multiply_by_powered_ten.return_value = NaturalNumber(5, [2, 2, 2, 0, 0])
        self.assertEqual(number_1.first_division_digit(number_2), NaturalNumber(1, [2]))

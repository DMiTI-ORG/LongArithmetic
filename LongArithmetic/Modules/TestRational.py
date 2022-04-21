from unittest import TestCase
from unittest.mock import patch
from RationalNumber import RationalNumber
from WholeNumber import WholeNumber
from NaturalNumber import NaturalNumber


class TestRational(TestCase):
    @patch.object(WholeNumber, 'abs')
    @patch.object(NaturalNumber, 'gcd')
    @patch.object(WholeNumber, 'quotient')
    def test_reduce(self, quotient, gcd, abs):
        number_1 = RationalNumber((0, 2, [1, 4]), (1, [7]))

        abs.return_value = NaturalNumber(2, [1, 4])
        gcd.return_value = NaturalNumber(1, [7])
        quotient.side_effect = [WholeNumber(0, 1, [2]), WholeNumber(0, 1, [1])]
        self.assertEqual(RationalNumber((0, 1, [2]), (1, [1])), number_1.reduce())

    def test_is_whole(self):
        number_one = RationalNumber([1, 4, [1, 2, 3, 9]], [3, [4, 1, 3]])  # -1239 413
        self.assertEqual(str(number_one.is_whole()), 'True')

        number_two = RationalNumber([1, 3, [1, 2, 3]], [3, [1, 2, 3]])  # -123 123
        self.assertEqual(str(number_two.is_whole()), 'True')

        number_free = RationalNumber([0, 4, [1, 2, 3, 9]], [5, [1, 5, 4, 1, 3]])  # 1239 15413
        self.assertEqual(str(number_free.is_whole()), 'False')

        number_four = RationalNumber([0, 1, [0]], [5, [1, 5, 4, 1, 3]])  # 0 15413
        self.assertEqual(str(number_four.is_whole()), 'True')

        number_five = RationalNumber([1, 3, [1, 0, 0]], [1, [2]])
        self.assertEqual(str(number_five.is_whole()), 'True')  # -100 2

        number_six = RationalNumber([0, 6, [1, 2, 3, 2, 4, 6]], [3, [1, 2, 3]])  # 123246 123
        self.assertEqual(str(number_six.is_whole()), 'True')

    def test_whole_to_rational(self):
        number1 = RationalNumber((1, 1, [0]), (1, [1]))
        number2 = RationalNumber((0, 2, [3, 4]), (1, [1]))
        number3 = RationalNumber((1, 2, [3, 4]), (1, [1]))
        number4 = RationalNumber((0, 1, [0]), (1, [1]))
        testnum1 = WholeNumber(1, 1, [0])
        testnum2 = WholeNumber(0, 2, [3, 4])
        testnum3 = WholeNumber(1, 2, [3, 4])
        testnum4 = WholeNumber(0, 1, [0])
        self.assertEqual(RationalNumber.whole_to_rational(testnum1), number1)
        self.assertEqual(RationalNumber.whole_to_rational(testnum2), number2)
        self.assertEqual(RationalNumber.whole_to_rational(testnum3), number3)
        self.assertEqual(RationalNumber.whole_to_rational(testnum4), number4)

    def test_to_whole(self):
        number_1 = RationalNumber((1, 4, [2, 3, 4, 5]),(1,[1]))  # -2345/1
        number_2 = WholeNumber(1, 4, [2, 3, 4, 5])  # -2345
        self.assertEqual(str(number_2), str(number_1.to_whole()))

        number_1 = RationalNumber((1, 6, [2, 6, 4, 8, 3, 9]), (1, [1]))  # -264839/1
        number_2 = WholeNumber(1, 6, [2, 6, 4, 8, 3, 9])  # -264839
        self.assertEqual(str(number_2), str(number_1.to_whole()))

        number_1 = RationalNumber((0, 8, [2, 4, 8, 1, 2, 9, 3, 6]), (1, [1]))  # 24812936/1
        number_2 = WholeNumber(0, 8, [2, 4, 8, 1, 2, 9, 3, 6])  # 24812936
        self.assertEqual(str(number_2), str(number_1.to_whole()))

        number_1 = RationalNumber((1, 6, [2, 6, 4, 8, 3, 9]), (1, [7]))  # -264839/7
        self.assertEqual('ERROR', str(number_1.to_whole()))

        number_1 = RationalNumber((0, 3, [4, 2, 9]), (1, [0]))  # 429/0
        self.assertEqual('ERROR', str(number_1.to_whole()))

    @patch.object(WholeNumber, 'add')
    @patch.object(WholeNumber, 'multiply')
    @patch.object(NaturalNumber, 'quotient')
    @patch.object(NaturalNumber, 'lcm')
    def test_add(self, lcm, quotient, multiply, add):
        num_1 = RationalNumber((0, 2, [1, 5]), (2, [4, 0]))
        num_2 = RationalNumber((0, 2, [3, 0]), (2, [6, 0]))
        res_num = RationalNumber((0, 3, [1, 0, 5]), (3, [1, 2, 0]))

        lcm.side_effect = [NaturalNumber(3, [1, 2, 0])]
        quotient.side_effect = [NaturalNumber(1, [3])]
        quotient.side_effect = [NaturalNumber(1, [2])]
        multiply.side_effect = [WholeNumber(0, 2, [4, 5])]
        multiply.side_effect = [WholeNumber(0, 2, [6, 0])]
        add.side_effect = [WholeNumber(0, 3, [1, 0, 5])]

        self.assertEqual(num_1.add(num_2), res_num)

    @patch.object(WholeNumber, 'multiply')
    @patch.object(WholeNumber, 'subtract')
    @patch.object(NaturalNumber, 'lcm')
    @patch.object(NaturalNumber, 'quotient')
    def test_subtract(self, quotient, lcm, subtract, multiply):
        # 1/2 - 1/3 = 1/6
        multiply.side_effect = [WholeNumber(0, 1, [3]), WholeNumber(0, 1, [2])]
        subtract.return_value = WholeNumber(0, 1, [1])
        lcm.return_value = NaturalNumber(1, [6])
        quotient.side_effect = [NaturalNumber(1, [3]), NaturalNumber(1, [2])]
        self.assertEqual(RationalNumber((0, 1, [1]), (1, [2])).subtract(RationalNumber((0, 1, [1]), (1, [3]))).
                         numerator.array, RationalNumber((0, 1, [1]), (1, [6])).numerator.array)
        # 5/6 - 1/1 = -1/6
        multiply.side_effect = [WholeNumber(0, 1, [5]), WholeNumber(0, 1, [6])]
        subtract.return_value = WholeNumber(1, 1, [1])
        lcm.return_value = NaturalNumber(1, [6])
        quotient.side_effect = [NaturalNumber(1, [1]), NaturalNumber(1, [6])]
        self.assertEqual(RationalNumber((0, 1, [5]), (1, [6])).subtract(RationalNumber((0, 1, [1]), (1, [1]))).
                         numerator.array, RationalNumber((1, 1, [1]), (1, [6])).numerator.array)
        # 3/7 - 2/11 = 19/77
        lcm.return_value = NaturalNumber(2, [7, 7])
        quotient.side_effect = [NaturalNumber(2, [1, 1]), NaturalNumber(1, [7])]
        multiply.side_effect = [WholeNumber(0, 2, [3, 3]), WholeNumber(0, 2, [1, 4])]
        subtract.return_value = WholeNumber(0, 2, [1, 9])
        self.assertEqual(RationalNumber((0, 1, [3]), (1, [7])).subtract(RationalNumber((0, 1, [2]), (2, [1, 1]))).
                         numerator.array, RationalNumber((0, 2, [1, 9]), (2, [7, 7])).numerator.array)

    @patch.object(WholeNumber, 'multiply')
    @patch.object(NaturalNumber, 'multiply')
    def test_multiply(self, multiply2, multiply1):
        number_1 = RationalNumber((0, 2, [2, 3]), (2, [1, 4]))
        number_2 = RationalNumber((1, 3, [1, 4]), (3, [2, 5, 7]))
        number_3 = RationalNumber((0, 1, [5]), (4, [4, 5, 8, 6]))

        multiply1.return_value = WholeNumber(0, 3, [3, 2, 2])
        multiply2.return_value = NaturalNumber(4, [3, 5, 9, 8])
        self.assertEqual(RationalNumber((0, 3, [3, 2, 2]), (4, [3, 5, 9, 8])), number_1.multiply(number_2))

        multiply1.return_value = WholeNumber(0, 2, [7, 0])
        multiply2.return_value = NaturalNumber(7, [1, 1, 7, 8, 6, 0, 2])
        self.assertEqual(RationalNumber((0, 2, [7, 0]), (7, [1, 1, 7, 8, 6, 0, 2])), number_2.multiply(number_3))
        
        multiply1.return_value = WholeNumber(0, 3, [3, 2, 2])
        multiply2.return_value = NaturalNumber(5, [6, 4, 2, 0, 4])
        self.assertEqual(str(RationalNumber((0, 3, [3, 2, 2]), (5, [6, 4, 2, 0, 4]))), str(number_3.multiply(number_1)))

    @patch.object(WholeNumber, 'multiply')
    def test_divide(self, multiply):
        number_1 = RationalNumber((1, 2, [2, 9]), (3, [1, 7, 2]))  # -29/172
        number_2 = RationalNumber((0, 2, [1, 3]), (2, [1, 9]))  # 13/19
        multiply.side_effect = [WholeNumber(1, 3, [5, 5, 1]), WholeNumber(0, 4, [2, 2, 3, 6])]
        self.assertEqual(str(RationalNumber((1, 3, [5, 5, 1]), (4, [2, 2, 3, 6]))),
                         str(number_1.divide(number_2)))  # -551/2236

        number_1 = RationalNumber((1, 2, [4, 5]), (2, [1, 1]))  # -45/11
        number_2 = RationalNumber((1, 3, [1, 0, 0]), (2, [9, 9]))  # -100/99
        multiply.side_effect = [WholeNumber(1, 4, [4, 4, 5, 5]), WholeNumber(1, 4, [1, 1, 0, 0])]
        self.assertEqual(str(RationalNumber((0, 4, [4, 4, 5, 5]), (4, [1, 1, 0, 0]))),
                         str(number_1.divide(number_2)))  # 4455/1100

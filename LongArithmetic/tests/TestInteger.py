from unittest import TestCase
from unittest.mock import patch
from ..Modules.IntegerNumber import IntegerNumber
from ..Modules.NaturalNumber import NaturalNumber


class TestInteger(TestCase):
    def test_abc(self):
        res = NaturalNumber(3, [1, 2, 3])

        num = IntegerNumber(1, 3, [1, 2, 3])

        self.assertEqual(res, num.abs())

    def test_is_positive(self):
        res_1 = 1  # negative
        res_2 = 2  # positive
        res_3 = 0  # zero

        num_1 = IntegerNumber(1, 2, [1, 0])  # negative
        num_2 = IntegerNumber(0, 2, [3, 3])  # positive
        num_3 = IntegerNumber(1, 2, [0, 0])  # zero
        num_4 = IntegerNumber(0, 2, [0, 0])  # zero

        self.assertEqual(res_1, num_1.is_positive())
        self.assertEqual(res_2, num_2.is_positive())
        self.assertEqual(res_3, num_3.is_positive())
        self.assertEqual(res_3, num_4.is_positive())

    def test_multiply_by_minus_one(self):
        number_1 = IntegerNumber(1, 2, [4, 1])
        number_2 = IntegerNumber(0, 2, [3, 0])
        number_3 = IntegerNumber(0, 2, [4, 1])
        number_4 = IntegerNumber(1, 2, [3, 0])

        self.assertEqual(str(number_3), str(number_1.multiply_by_minus_one()))
        self.assertEqual(str(number_4), str(number_2.multiply_by_minus_one()))

    def test_natural_to_integer(self):
        number_1 = NaturalNumber(2, [2,1])
        number_2 = NaturalNumber(1, [0])
        number_3 = NaturalNumber(1, [7])

        self.assertEqual(str(IntegerNumber(0, 2, [2, 1])), str(IntegerNumber.natural_to_integer(number_1)))
        self.assertEqual(str(IntegerNumber(0, 1, [0])), str(IntegerNumber.natural_to_integer(number_2)))
        self.assertEqual(str(IntegerNumber(0, 1, [7])), str(IntegerNumber.natural_to_integer(number_3)))

    def test_to_natural(self):
        number_1 = IntegerNumber(0, 2, [2, 1])
        number_2 = IntegerNumber(0, 1, [0])
        number_3 = IntegerNumber(1, 1, [7])

        self.assertEqual(NaturalNumber(2, [2, 1]), number_1.to_natural())
        self.assertEqual(NaturalNumber(1, [0]), number_2.to_natural())
        self.assertEqual('Error', number_3.to_natural())

    @patch.object(IntegerNumber, 'abs')
    @patch.object(NaturalNumber, 'add')
    @patch.object(NaturalNumber, 'compare')
    @patch.object(NaturalNumber, 'subtract')
    def test_add(self, subtract, compare, add, abs):
        number_1 = IntegerNumber(1, 3, [1, 2, 3])
        number_2 = IntegerNumber(1, 3, [1, 2, 3])
        number_3 = IntegerNumber(1, 3, [2, 4, 6])
        number_4 = IntegerNumber(1, 3, [1, 2, 3])
        number_5 = IntegerNumber(0, 2, [2, 3])
        number_6 = IntegerNumber(1, 3, [1, 0, 0])

        abs.return_value = NaturalNumber(3, [1, 2, 3])
        abs.return_value = NaturalNumber(3, [1, 2, 3])
        add.return_value = NaturalNumber(3, [2, 4, 6])
        self.assertEqual(number_3, number_1.add(number_2))

        abs.return_value = NaturalNumber(3, [1, 2, 3])
        abs.return_value = NaturalNumber(2, [2, 3])
        compare.return_value = 0
        subtract.return_value = NaturalNumber(3, [1, 0, 0])
        self.assertEqual(number_6, number_4.add(number_5))

    # TODO: there is will be Gleb test

    @patch.object(NaturalNumber, 'multiply')
    def test_multiply(self, multiply):
        number_1 = IntegerNumber(1, 2, [1, 9])  # -19
        number_2 = IntegerNumber(0, 3, [1, 1, 1])  # 111
        multiply.return_value = NaturalNumber(4, [2, 1, 0, 9])  # 2109
        self.assertEqual(str(IntegerNumber(1, 4, [2, 1, 0, 9])), str(IntegerNumber.multiply(number_1, number_2)))  # -2109

        number_3 = IntegerNumber(1, 2, [1, 0])  # -10
        number_4 = IntegerNumber(1, 3, [9, 9, 9])  # -999
        multiply.return_value = NaturalNumber(4, [9, 9, 9, 0])  # 9990
        self.assertEqual(str(IntegerNumber(0, 4, [9, 9, 9, 0])), str(IntegerNumber.multiply(number_3, number_4)))  # 9990

        number_5 = IntegerNumber(0, 5, [1, 2, 3, 4, 5])  # 12345
        number_6 = IntegerNumber(0, 3, [6, 6, 6])  # 666
        multiply.return_value = NaturalNumber(7, [8, 2, 2, 1, 7, 7, 0])  # 8221770
        self.assertEqual(str(IntegerNumber(0, 7, [8, 2, 2, 1, 7, 7, 0])),
                         str(IntegerNumber.multiply(number_5, number_6)))  # 8221770

    @patch.object(IntegerNumber, 'abs')
    @patch.object(IntegerNumber, 'is_positive')
    @patch.object(NaturalNumber, 'quotient')
    def test_quotient(self, quotient, is_positive, abs):
        number_1 = IntegerNumber(1, 2, [2, 0])
        number_2 = IntegerNumber(1, 1, [5])
        number_3 = NaturalNumber(1, [4])
        number_4 = IntegerNumber(0, 1, [0])
        is_positive.return_value = 2
        abs.return_value = NaturalNumber(2, [2, 0])
        abs.return_value = NaturalNumber(1, [5])
        quotient.return_value = NaturalNumber(1, [4])
        self.assertEqual(str(number_3), str(number_1.quotient(number_2)))
        is_positive.return_value = 0
        self.assertEqual(str('Error'), str(number_1.quotient(number_4)))

    @patch.object(IntegerNumber, 'quotient')
    @patch.object(IntegerNumber, 'multiply')
    @patch.object(IntegerNumber, 'subtract')
    @patch.object(IntegerNumber, 'multiply_by_minus_one')
    def test_remainder(self, multiply_by_minus_one, subtract, multiply, quotient):
        number_1 = IntegerNumber(0, 5, [1, 4, 6, 7, 1])  # 14671
        number_2 = IntegerNumber(0, 2, [5, 4])  # 54
        number_3 = IntegerNumber(0, 2, [3, 7])  # 37

        quotient.return_value = IntegerNumber(0, 3, [2, 7, 1])  # 271
        multiply.return_value = IntegerNumber(0, 5, [1, 4, 6, 3, 4])  # 14634
        subtract.return_value = IntegerNumber(0, 2, [3, 7])  # 37
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = IntegerNumber(0, 5, [1, 4, 6, 7, 1])  # 14671
        number_2 = IntegerNumber(0, 5, [1, 4, 6, 7, 0])  # 14670
        number_3 = IntegerNumber(0, 1, [1])  # 1

        quotient.return_value = IntegerNumber(0, 1, [1])  # 1
        multiply.return_value = IntegerNumber(0, 5, [1, 3, 6, 9, 0])  # 13690
        subtract.return_value = IntegerNumber(0, 1, [1])  # 1
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = IntegerNumber(0, 5, [1, 0, 3, 4, 0])  # 10340
        number_2 = IntegerNumber(0, 5, [1, 0, 3, 4, 1])  # 10341
        number_3 = IntegerNumber(0, 5, [1, 0, 3, 4, 0])  # 10340

        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = IntegerNumber(0, 5, [1, 8, 8, 7, 9])  # 18879
        number_2 = IntegerNumber(0, 1, [0])  # 0
        self.assertEqual('ERROR', str(number_1.remainder(number_2)))

        number_1 = IntegerNumber(1, 3, [5, 8, 9])  # -589
        number_2 = IntegerNumber(1, 3, [5, 9, 0])  # -590
        number_3 = IntegerNumber(1, 3, [5, 8, 9])  # -589
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = IntegerNumber(0, 2, [1, 7])  # 17
        number_2 = IntegerNumber(1, 1, [5])  # -5
        number_3 = IntegerNumber(0, 1, [2])  # 2
        multiply_by_minus_one.return_value = IntegerNumber(0, 1, [5])  # 5
        quotient.return_value = IntegerNumber(0, 1, [3])  # 3
        multiply.return_value = IntegerNumber(0, 2, [1, 5])  # 15
        subtract.return_value = IntegerNumber(0, 1, [2])  # 2
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = IntegerNumber(1, 2, [1, 7])  # -17
        number_2 = IntegerNumber(0, 1, [5])  # 5
        number_3 = IntegerNumber(0, 1, [2])  # 2
        c1 = IntegerNumber(0, 2, [1, 7])  # 17
        c2 = IntegerNumber(1, 2, [1, 7])  # -17
        a1 = IntegerNumber(1, 1, [4])  # -4
        a2 = IntegerNumber(0, 1, [3])  # 3
        multiply_by_minus_one.side_effect = [c1, c2]
        quotient.return_value = IntegerNumber(0, 1, [3])  # 3
        subtract.return_value.side_effect = [a1, a2]
        multiply.return_value = IntegerNumber(1, 2, [2, 0])  # -20
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

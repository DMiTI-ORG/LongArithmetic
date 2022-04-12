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
        
    def test_multiply_by_minus_one(self):
        number_1 = WholeNumber(1, 2, [4, 1])
        number_2 = WholeNumber(0, 2, [3, 0])
        number_3 = WholeNumber(0, 2, [4, 1])
        number_4 = WholeNumber(1, 2, [3, 0])

        self.assertEqual(str(number_3), str(number_1.multiply_by_minus_one()))
        self.assertEqual(str(number_4), str(number_2.multiply_by_minus_one()))

    @patch.object(WholeNumber, 'abs')
    @patch.object(WholeNumber, 'is_positive')
    @patch.object(NaturalNumber, 'quotient')
    def test_quotient(self, quotient, is_positive, abs):
        number_1 = WholeNumber(1, 2, [2, 0])
        number_2 = WholeNumber(1, 1, [5])
        number_3 = NaturalNumber(1, [4])
        number_4 = WholeNumber(0, 1, [0])
        is_positive.return_value = 2
        abs.return_value = NaturalNumber(2, [2, 0])
        abs.return_value = NaturalNumber(1, [5])
        quotient.return_value = NaturalNumber(1, [4])
        self.assertEqual(str(number_3), str(number_1.quotient(number_2)))
        is_positive.return_value = 0
        self.assertEqual(str('Error'), str(number_1.quotient(number_4)))

    @patch.object(WholeNumber, 'abs')
    @patch.object(NaturalNumber, 'add')
    @patch.object(NaturalNumber, 'compare')
    @patch.object(NaturalNumber, 'subtract')
    def test_add(self, subtract, compare, add, abs):
        number_1 = WholeNumber(1, 3, [1, 2, 3])
        number_2 = WholeNumber(1, 3, [1, 2, 3])
        number_3 = WholeNumber(1, 3, [2, 4, 6])
        number_4 = WholeNumber(1, 3, [1, 2, 3])
        number_5 = WholeNumber(0, 2, [2, 3])
        number_6 = WholeNumber(1, 3, [1, 0, 0])

        abs.return_value = NaturalNumber(3, [1, 2, 3])
        abs.return_value = NaturalNumber(3, [1, 2, 3])
        add.return_value = NaturalNumber(3, [2, 4, 6])
        self.assertEqual(number_3, number_1.add1(number_2))

        abs.return_value = NaturalNumber(3, [1, 2, 3])
        abs.return_value = NaturalNumber(2, [2, 3])
        compare.return_value = 0
        subtract.return_value = NaturalNumber(3, [1, 0, 0])
        self.assertEqual(number_6, number_4.add1(number_5))

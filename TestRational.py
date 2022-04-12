from unittest import TestCase
from unittest.mock import patch
from NaturalNumber import NaturalNumber
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
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    def test_to_whole(self):
        number_1 = RationalNumber((1, 4, [2, 3, 4, 5]),(1,[1])) #-2345/1
        number_2 = WholeNumber(1, 4, [2, 3, 4, 5]) #-2345
        self.assertEqual(str(number_2), str(number_1.to_whole()))

        number_1 = RationalNumber((1, 6, [2, 6, 4, 8, 3, 9]), (1, [1])) #-264839/1
        number_2 = WholeNumber(1, 6, [2, 6, 4, 8, 3, 9]) #-264839
        self.assertEqual(str(number_2), str(number_1.to_whole()))

        number_1 = RationalNumber((0, 8, [2, 4, 8, 1, 2, 9, 3, 6]), (1, [1])) #24812936/1
        number_2 = WholeNumber(0, 8, [2, 4, 8, 1, 2, 9, 3, 6]) #24812936
        self.assertEqual(str(number_2), str(number_1.to_whole()))

        number_1 = RationalNumber((1, 6, [2, 6, 4, 8, 3, 9]), (1, [7])) #-264839/7
        self.assertEqual('ERROR', str(number_1.to_whole()))

        number_1 = RationalNumber((0, 3, [4, 2, 9]), (1, [0])) #429/0
        self.assertEqual('ERROR', str(number_1.to_whole()))

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

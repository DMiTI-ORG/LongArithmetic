import imp
from unittest import TestCase
from unittest.mock import patch, Mock

from WholeNumber import WholeNumber
from NaturalNumber import NaturalNumber 
from RationalNumber import RationalNumber

class TestRational(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    def test_is_whole(self):
        number_one=RationalNumber([1, 4, [1, 2, 3, 9]], [3, [4, 1, 3]]) #-1239 413
        self.assertEqual(str(number_one.is_whole()), 'True')
     
        number_two=RationalNumber([1, 3, [1, 2, 3]], [3, [1, 2, 3]]) #-123 123
        self.assertEqual(str(number_two.is_whole()), 'True')

        number_free=RationalNumber([0, 4, [1, 2, 3, 9]], [5, [1, 5, 4, 1, 3]]) #1239 15413
        self.assertEqual(str(number_free.is_whole()), 'False')

        number_four=RationalNumber([0, 1, [0]], [5, [1, 5, 4, 1, 3]]) #0 15413
        self.assertEqual(str(number_four.is_whole()), 'True')

        number_five=RationalNumber([1, 3, [1,0,0]], [1, [2]])
        self.assertEqual(str(number_five.is_whole()), 'True') #-100 2

        number_six=RationalNumber([0, 6, [1, 2, 3, 2, 4, 6]], [3, [1, 2, 3]]) #123246 123
        self.assertEqual(str(number_six.is_whole()), 'True')



    @patch.object(WholeNumber, 'multiply')
    def test_divide(self, multiply):
        number_1=RationalNumber((1, 2, [2, 9]), (3, [1, 7, 2])) # -29/172
        number_2=RationalNumber((0, 2, [1, 3]), (2, [1, 9])) # 13/19
        multiply.side_effect=[WholeNumber(1, 3, [5, 5, 1]), WholeNumber(0, 4, [2, 2, 3, 6])]
        self.assertEqual(str(RationalNumber((1, 3, [5, 5, 1]), (4, [2, 2, 3, 6]))), str(number_1.divide(number_2))) # -551/2236

        number_1=RationalNumber((1, 2, [4, 5]), (2, [1, 1])) # -45/11
        number_2=RationalNumber((1, 3, [1, 0, 0]), (2, [9, 9])) # -100/99
        multiply.side_effect=[WholeNumber(1, 4, [4, 4, 5, 5]), WholeNumber(1, 4, [1, 1, 0, 0])]
        self.assertEqual(str(RationalNumber((0, 4, [4, 4, 5, 5]), (4, [1, 1, 0, 0]))), str(number_1.divide(number_2))) # 4455/1100
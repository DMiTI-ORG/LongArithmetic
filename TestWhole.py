import imp
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

    @patch.object(NaturalNumber, 'multiply')
    def test_multiply(self, multiply):
        number_1=WholeNumber(1, 2, [1, 9]) # -19
        number_2=WholeNumber(0, 3, [1, 1, 1]) # 111
        multiply.return_value=NaturalNumber(4, [2, 1, 0, 9]) # 2109
        self.assertEqual(str(WholeNumber(1, 4, [2, 1, 0, 9])), str(WholeNumber.multiply(number_1, number_2))) # -2109

        number_3=WholeNumber(1, 2, [1, 0]) # -10
        number_4=WholeNumber(1, 3, [9, 9, 9]) # -999
        multiply.return_value=NaturalNumber(4, [9, 9, 9, 0]) # 9990
        self.assertEqual(str(WholeNumber(0, 4, [9, 9, 9, 0])), str(WholeNumber.multiply(number_3, number_4))) # 9990

        number_5=WholeNumber(0, 5, [1, 2, 3, 4, 5]) # 12345
        number_6=WholeNumber(0, 3, [6, 6, 6]) # 666
        multiply.return_value=NaturalNumber(7, [8, 2, 2, 1, 7, 7, 0]) # 8221770
        self.assertEqual(str(WholeNumber(0, 7, [8, 2, 2, 1, 7, 7, 0])), str(WholeNumber.multiply(number_5, number_6))) # 8221770
        
        
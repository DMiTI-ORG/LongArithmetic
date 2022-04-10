from unittest import TestCase
from unittest.mock import patch
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

    @patch.object(WholeNumber, 'quotient')
    @patch.object(WholeNumber, 'multiply')
    @patch.object(WholeNumber, 'subtract')
    @patch.object(WholeNumber, 'multiply_by_minus_one')
    def test_remainder(self, multiply_by_minus_one, subtract, multiply, quotient):
        number_1 = WholeNumber(0, 5, [1, 4, 6, 7, 1]) #14671
        number_2 = WholeNumber(0, 2, [5, 4]) #54
        number_3 = WholeNumber(0, 2, [3, 7]) #37

        quotient.return_value = WholeNumber(0, 3, [2, 7, 1]) #271
        multiply.return_value = WholeNumber(0, 5, [1, 4, 6, 3, 4]) #14634
        subtract.return_value = WholeNumber(0, 2, [3, 7]) #37
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = WholeNumber(0, 5, [1, 4, 6, 7, 1]) #14671
        number_2 = WholeNumber(0, 5, [1, 4, 6, 7, 0]) #14670
        number_3 = WholeNumber(0, 1, [1]) #1

        quotient.return_value = WholeNumber(0, 1, [1]) #1
        multiply.return_value = WholeNumber(0, 5, [1, 3, 6, 9, 0]) #13690
        subtract.return_value = WholeNumber(0, 1, [1]) #1
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))


        number_1 = WholeNumber(0, 5, [1, 0, 3, 4, 0]) #10340
        number_2 = WholeNumber(0, 5, [1, 0, 3, 4, 1]) #10341
        number_3 = WholeNumber(0, 5, [1, 0, 3, 4, 0]) #10340

        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = WholeNumber(0, 5, [1, 8, 8, 7, 9]) #18879
        number_2 = WholeNumber(0, 1, [0]) #0
        self.assertEqual('ERROR', str(number_1.remainder(number_2)))

        number_1 = WholeNumber(1, 3, [5, 8, 9]) #-589
        number_2 = WholeNumber(1, 3, [5, 9, 0]) #-590
        number_3 = WholeNumber(1, 3, [5, 8, 9]) #-589
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = WholeNumber(0, 2, [1, 7]) #17
        number_2 = WholeNumber(1, 1, [5]) #-5
        number_3 = WholeNumber(0, 1, [2]) #2
        multiply_by_minus_one.return_value = WholeNumber(0, 1, [5]) #5
        quotient.return_value = WholeNumber(0, 1, [3]) #3
        multiply.return_value = WholeNumber(0, 2, [1, 5]) #15
        subtract.return_value = WholeNumber(0, 1, [2]) #2
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = WholeNumber(1, 2, [1, 7]) #-17
        number_2 = WholeNumber(0, 1, [5]) #5
        number_3 = WholeNumber(0, 1, [2]) #2
        c1 = WholeNumber(0, 2, [1, 7]) #17
        c2 = WholeNumber(1, 2, [1, 7]) #-17
        a1 = WholeNumber(1, 1, [4]) #-4
        a2 = WholeNumber(0, 1, [3]) #3
        multiply_by_minus_one.side_effect = [c1, c2]
        quotient.return_value = WholeNumber(0, 1, [3]) #3
        subtract.return_value.side_effect = [a1, a2]
        multiply.return_value = WholeNumber(1, 2, [2, 0]) #-20
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))




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
        number_1 = WholeNumber(0, 5, [1, 4, 6, 7, 1])
        number_2 = WholeNumber(0, 2, [5, 4])
        number_3 = WholeNumber(0, 2, [3, 7])

        quotient.return_value = WholeNumber(0, 3, [2, 7, 1])
        multiply.return_value = WholeNumber(0, 5, [1, 4, 6, 3, 4])
        subtract.return_value = WholeNumber(0, 2, [3, 7])
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = WholeNumber(0, 5, [1, 4, 6, 7, 1])
        number_2 = WholeNumber(0, 5, [1, 4, 6, 7, 0])
        number_3 = WholeNumber(0, 1, [1])

        quotient.return_value = WholeNumber(0, 1, [1])
        multiply.return_value = WholeNumber(0, 5, [1, 4, 6, 7, 0])
        subtract.return_value = WholeNumber(0, 1, [1])
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))


        number_1 = WholeNumber(0, 5, [1, 4, 6, 7, 0])
        number_2 = WholeNumber(0, 5, [1, 4, 6, 7, 1])
        number_3 = WholeNumber(0, 5, [1, 4, 6, 7, 0])

        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = WholeNumber(0, 5, [1, 8, 8, 7, 9])
        number_2 = WholeNumber(0, 1, [0])
        self.assertEqual('ERROR', str(number_1.remainder(number_2)))

        number_1 = WholeNumber(1, 3, [5, 8, 9])
        number_2 = WholeNumber(1, 3, [5, 9, 0])
        number_3 = WholeNumber(1, 3, [5, 8, 9])
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = WholeNumber(0, 2, [1, 7])
        number_2 = WholeNumber(1, 1, [5])
        number_3 = WholeNumber(0, 1, [2])
        multiply_by_minus_one.return_value = WholeNumber(0, 1, [5])
        quotient.return_value = WholeNumber(0, 1, [3])
        multiply.return_value = WholeNumber(0, 2, [1, 5])
        subtract.return_value = WholeNumber(0, 1, [2])
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))

        number_1 = WholeNumber(1, 2, [1, 7])
        number_2 = WholeNumber(0, 1, [5])
        number_3 = WholeNumber(0, 1, [2])
        c1 = WholeNumber(0, 2, [1, 7])
        c2 = WholeNumber(1, 2, [1, 7])
        a1 = WholeNumber(1, 1, [-4])
        a2 = WholeNumber(0, 1, [3])
        multiply_by_minus_one.side_effect = [c1, c2]
        quotient.return_value = WholeNumber(0, 1, [3])
        subtract.return_value.side_effect = [a1, a2]
        multiply.return_value = WholeNumber(1, 2, [2, 0])
        self.assertEqual(str(number_3), str(number_1.remainder(number_2)))




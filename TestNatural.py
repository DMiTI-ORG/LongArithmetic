import unittest
from unittest import TestCase
from NaturalNumber import NaturalNumber

class TestNatural(TestCase):
    """
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)
    """

    def test_quotient(self):
        # 999 // 988 = 1
        self.assertEqual(NaturalNumber(3, [9, 9, 9]).quotient(NaturalNumber(3, [9, 8, 8])).array,
                         NaturalNumber(1, [1]).array)
        # 10005 // 17 = 588
        self.assertEqual(NaturalNumber(5, [1, 0, 0, 0, 5]).quotient(NaturalNumber(2, [1, 7])).array,
                         NaturalNumber(3, [5, 8, 8]).array)
        # 9678 // 9678 = 1
        self.assertEqual(NaturalNumber(4, [9, 6, 7, 8]).quotient(NaturalNumber(4, [9, 6, 7, 8])).array,
                         NaturalNumber(1, [1]).array)




if __name__ == '__main__':
    unittest.main()
from unittest import TestCase
from unittest.mock import patch, Mock
from Polynomial import Polynomial
from WholeNumber import WholeNumber
from NaturalNumber import NaturalNumber
from RationalNumber import RationalNumber

class TestPolynomial(TestCase):
    '''
    Example test
    @patch.object(Calculator, 'bar')
    def test_sum(self, bar):
        bar.return_value = 1
        self.assertEqual(self.calc.foo(100, 200), 1)
        bar.return_value = 5
        self.assertEqual(self.calc.foo(100, 200), 5)'''

    @patch.object(Polynomial, 'subtract')
    @patch.object(Polynomial, 'multiply')
    @patch.object(Polynomial, 'quotient')
    def test_remainder(self, quotient, multiply, subtract):
        pol1 = Polynomial(2,[1,2,1]) #x^2+2x+1
        pol2 = Polynomial(1,[1,1])#x+1
        subtract.return_value = (0, [0])
        reuslt = (0, [0])
        multiply.return_value = Polynomial(2,[1,2,1])
        quotient.return_value = Polynomial(1,[1,1])
        self.assertEqual(pol1.remainder(pol2), reuslt)

        pol3 = Polynomial(2,[1,2,2]) #x^2+2x+1
        pol4 = Polynomial(1,[1,1]) #x+1
        reuslt2 = (0,[1])
        multiply.return_value = Polynomial(2, [1, 2, 1])
        quotient.return_value = Polynomial(1, [1, 1])
        subtract.return_value = (0, [1])
        self.assertEqual(pol3.remainder(pol4), reuslt2)
        
    @patch.object(RationalNumber, 'multiply')
    def test_multiply(self, multiply):
        number_1 = Polynomial(3, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [1]), (1, [1]))])
        number_2 = RationalNumber((0, 3, [2, 4, 1]), (1, [1]))
        number_3 = Polynomial(3, [RationalNumber((0, 3, [2, 4, 1]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 3, [2, 4, 1]), (1, [1]))])

        c1 = RationalNumber((0, 3, [2, 4, 1]), (1, [1]))
        c2 = RationalNumber((0, 1, [0]), (1, [1]))
        c3 = RationalNumber((0, 1, [0]), (1, [1]))
        c4 = RationalNumber((0, 3, [2, 4, 1]), (1, [1]))

        multiply.side_effect = [c1, c2, c3, c4]

        self.assertEqual(str(number_1.multiply_by_rational(number_2)), str(number_3))

        number_1 = Polynomial(3, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [1]), (1, [1]))])
        number_2 = RationalNumber((1, 3, [2, 4, 1]), (1, [1]))
        number_3 = Polynomial(3, [RationalNumber((1, 3, [2, 4, 1]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((0, 1, [0]), (1, [1])), RationalNumber((1, 3, [2, 4, 1]), (1, [1]))])

        c1 = RationalNumber((1, 3, [2, 4, 1]), (1, [1]))
        c2 = RationalNumber((0, 1, [0]), (1, [1]))
        c3 = RationalNumber((0, 1, [0]), (1, [1]))
        c4 = RationalNumber((1, 3, [2, 4, 1]), (1, [1]))

        multiply.side_effect = [c1, c2, c3, c4]

        self.assertEqual(str(number_1.multiply_by_rational(number_2)), str(number_3))

    @patch.object(Polynomial, 'multiply_by_rational')
    @patch.object(Polynomial, 'add')
    def test_multiply(self, add, multiply_by_rational):
        number_1 = Polynomial(1, [1, 1])
        number_2 = Polynomial(2, [1, -1, 1])
        number_3 = Polynomial(3, [1, 0, 0, 1])

        number_2.multiply_by_monomial = Mock(side_effect=[Polynomial(3, [1, -1, 1, 0]), Polynomial(2, [1, -1, 1])])
        multiply_by_rational.return_value = number_2
        add.return_value = number_3
        self.assertEqual(str(number_1.multiply(number_2)), str(number_3))

    def test_multiply_by_monomial(self):
        polynomial_1 = Polynomial(3, [2, 3, 4, 5])
        polynomial_2 = Polynomial(2, [1, 0, 0])
        polynomial_3 = Polynomial(0, [5])
        degree_1 = 0
        degree_2 = 3
        degree_3 = 2
        self.assertEqual(polynomial_1.multiply_by_monomial(degree_1), Polynomial(3, [2, 3, 4, 5]))
        self.assertEqual(polynomial_2.multiply_by_monomial(degree_2), Polynomial(5, [1, 0, 0, 0, 0, 0]))
        self.assertEqual(polynomial_3.multiply_by_monomial(degree_3), Polynomial(2, [5, 0, 0]))

    @patch.object(Polynomial, 'derivative')
    @patch.object(Polynomial, 'gcd')
    @patch.object(Polynomial, 'quotient')
    def test_multiple_roots_to_simple(self, quotient, gcd, derivative):
        number_1 = Polynomial(5, [1, -8, 25, -38, 28, 8])

        derivative.return_value = Polynomial(4, [5, -32, 75, -76, 28])
        gcd.return_value = Polynomial(3, [1, -5, 8, -4])
        quotient.return_value = Polynomial(2, [1, -3, 2])
        self.assertEqual(number_1.multiple_roots_to_simple(), Polynomial(2, [1, -3, 2]))

    @patch.object(Polynomial, 'remainder')
    def test_gcd(self, remainder):
        #x^3 – x^2 – 5x – 3
        number_1 = Polynomial(3, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((1, 1, [1]), (1, [1])),
                                  RationalNumber((1, 1, [5]), (1, [1])), RationalNumber((1, 1, [3]), (1, [1]))])
        #x^2 + x – 12
        number_2 = Polynomial(2, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [1]), (1, [1])),
                                  RationalNumber((1, 2, [1, 2]), (1, [1]))])
        #x - 3
        number_3 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((1, 1, [3]), (1, [1]))])

        #x - 3
        c1 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((1, 1, [3]), (1, [1]))])
        c2 = Polynomial(0, [])
        remainder.side_effect = [c1, c2]
        self.assertEqual(number_3, number_1.gcd(number_2))

        #x^2 + 2x - 24
        number_1 = Polynomial(2, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [2]), (1, [1])),
                                  RationalNumber((1, 2, [2, 4]), (1, [1]))])
        #x + 6
        number_2 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [6]), (1, [1]))])
        # x + 6
        number_3 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [6]), (1, [1]))])

        # x + 6
        c1 = Polynomial(1, [RationalNumber((0, 1, [1]), (1, [1])), RationalNumber((0, 1, [6]), (1, [1]))])
        c2 = Polynomial(0, [])
        remainder.side_effect = [c1, c2]
        self.assertEqual(number_3, number_1.gcd(number_2))

    @patch.object(RationalNumber, 'add')
    def test_add(self, add):
        num_1 = Polynomial(5, [RationalNumber(2, 3), RationalNumber(4, 6), RationalNumber(5, 2), RationalNumber(3, 4), RationalNumber(6, 7)])
        num_2 = Polynomial(3, [RationalNumber(3, 2), RationalNumber(2, 6), RationalNumber(2, 5)])
        res_num = Polynomial(5, [RationalNumber(2, 3), RationalNumber(4, 6), RationalNumber(8, 2), RationalNumber(17, 12), RationalNumber(44, 35)])

        num_1.add = Mock(side_effect=[RationalNumber(2, 3), RationalNumber(4, 6), RationalNumber(8, 2), RationalNumber(17, 12), RationalNumber(44, 35)])
        self.assertEqual(num_1.add(num_2), res_num)
        
    @patch.object(RationalNumber, 'subtract')
    def test_subtract(self, subtract):
        polynomial_1 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (1, [1])),
                                      RationalNumber((0, 2, [7, 5]), (1, [1])),
                                      RationalNumber((0, 2, [3, 5]), (1, [1]))])  # 81x^2 +75x +35

        polynomial_2 = Polynomial(1, [RationalNumber((0, 2, [4, 3]), (1, [1])),
                                      RationalNumber((0, 2, [3, 2]), (1, [1]))])  # 43x + 32

        polynomial_3 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (1, [1])),
                                      RationalNumber((0, 2, [3, 2]), (1, [1])),
                                      RationalNumber((0, 1, [3]), (1, [1]))])

        c1 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (1, [1])),
                            RationalNumber((0, 2, [7, 5]), (1, [1])),
                            RationalNumber((0, 2, [3, 5]), (1, [1]))])
        c2 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (1, [1])),
                            RationalNumber((0, 2, [3, 2]), (1, [1])),
                            RationalNumber((0, 2, [3, 5]), (1, [1]))])
        c3 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (1, [1])),
                            RationalNumber((0, 2, [3, 2]), (1, [1])),
                            RationalNumber((0, 1, [3]), (1, [1]))])
        subtract.side_effect = [c1, c2, c3]
        self.assertEqual(polynomial_1.subtract(polynomial_2), polynomial_3)

        polynomial_1 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (2, [1, 0])),
                                      RationalNumber((0, 2, [7, 5]), (2, [1, 0])),
                                      RationalNumber((0, 2, [3, 5]), (1, [1]))])  # 8.1x^2 +7.5x +35

        polynomial_2 = Polynomial(1, [RationalNumber((0, 2, [4, 3]), (2, [1, 0])),
                                      RationalNumber((0, 2, [3, 2]), (1, [1]))])  # 4.3x + 32

        polynomial_3 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (2, [1, 0])),
                                      RationalNumber((0, 2, [3, 2]), (2, [1, 0])),
                                      RationalNumber((0, 1, [3]), (1, [1]))])  # 8.1x^2 +3.2x +3

        c1 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (2, [1, 0])),
                            RationalNumber((0, 2, [7, 5]), (2, [1, 0])),
                            RationalNumber((0, 2, [3, 5]), (1, [1]))])
        c2 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (2, [1, 0])),
                            RationalNumber((0, 2, [3, 2]), (2, [1, 0])),
                            RationalNumber((0, 2, [3, 5]), (1, [1]))])
        c3 = Polynomial(2, [RationalNumber((0, 2, [8, 1]), (2, [1, 0])),
                            RationalNumber((0, 2, [3, 2]), (2, [1, 0])),
                            RationalNumber((0, 1, [3]), (1, [1]))])
        subtract.side_effect = [c1, c2, c3]
        self.assertEqual(polynomial_1.subtract(polynomial_2), polynomial_3)

        polynomial_1 = Polynomial(3, [RationalNumber((0, 2, [1, 0]), (1, [1])),
                                      RationalNumber((0, 2, [9, 8]), (2, [1, 0])),
                                      RationalNumber((0, 3, [5, 6, 2]), (2, [1, 0])),
                                      RationalNumber((0, 1, [0]), (1, [1]))])  # 10x^3 +9.8x^2 +56.2x +0

        polynomial_2 = Polynomial(2, [RationalNumber((0, 2, [1, 5]), (1, [1])),
                                      RationalNumber((0, 2, [1, 5]), (2, [1, 0])),
                                      RationalNumber((0, 1, [8]), (1, [1]))])  # 15x^2 +1.5x +8

        polynomial_3 = Polynomial(3, [RationalNumber((0, 2, [1, 0]), (1, [1])),
                                      RationalNumber((0, 2, [-5, 2]), (2, [1, 0])),
                                      RationalNumber((0, 3, [5, 4, 7]), (2, [1, 0])),
                                      RationalNumber((0, 1, [-8]), (1, [1]))])  # 10x^3 -5,2x^2 +54.7x -8

        c1 = Polynomial(3, [RationalNumber((0, 2, [1, 0]), (1, [1])),
                            RationalNumber((0, 2, [9, 8]), (2, [1, 0])),
                            RationalNumber((0, 3, [5, 6, 2]), (2, [1, 0])),
                            RationalNumber((0, 1, [0]), (1, [1]))])

        c2 = Polynomial(3, [RationalNumber((0, 2, [1, 0]), (1, [1])),
                            RationalNumber((0, 2, [-5, 2]), (2, [1, 0])),
                            RationalNumber((0, 3, [5, 6, 2]), (2, [1, 0])),
                            RationalNumber((0, 1, [0]), (1, [1]))])

        c3 = Polynomial(3, [RationalNumber((0, 2, [1, 0]), (1, [1])),
                            RationalNumber((0, 2, [-5, 2]), (2, [1, 0])),
                            RationalNumber((0, 3, [5, 4, 7]), (2, [1, 0])),
                            RationalNumber((0, 1, [0]), (1, [1]))])

        c4 = Polynomial(3, [RationalNumber((0, 2, [1, 0]), (1, [1])),
                            RationalNumber((0, 2, [-5, 2]), (2, [1, 0])),
                            RationalNumber((0, 3, [5, 4, 7]), (2, [1, 0])),
                            RationalNumber((0, 1, [-8]), (1, [1]))])
        subtract.side_effect = [c1, c2, c3, c4]
        self.assertEqual(polynomial_1.subtract(polynomial_2), polynomial_3)

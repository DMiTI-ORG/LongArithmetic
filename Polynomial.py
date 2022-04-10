from typing_extensions import Self
from NaturalNumber import NaturalNumber
from RationalNumber import RationalNumber


class Polynomial:
    def __init__(self, highest_degree: int, array: list):
        self.highest_degree = highest_degree
        self.array = array

    def add(self, polynomial: Self) -> Self:
        # P-1
        pass

    def subtract(self, polynomial: Self) -> Self:
        # P-2
        pass

    def multiply_by_rational(self, number: RationalNumber) -> Self:
        # P-3
        pass

    def multiply_by_monomial(self, k: int) -> Self:
        '''
        module: MUL_Pxk_P
        author: Teryokhina Sofya
        arguments:
            k: degree of monomial
        This method multiplies polynomial and monomial with natural degree
        '''
        new_array = self.array
        for i in range(k):
            new_array.append(0)
        new_polynomial = Polynomial(self.highest_degree + k, new_array)
        return new_polynomial

    def highest_coefficient(self) -> RationalNumber:
        # P-5
        pass

    def get_degree(self) -> NaturalNumber:
        # P-6
        pass

    def take_out_gdc_lcm(self) -> Self:
        # P-7
        pass

    def multiply(self, polynomial: Self) -> Self:
        """
        module: MUL_PP_P
        author: Smirnov Nikita

        arguments:
            number: an instance of the class Polynomial

        This method multiplies two polynomials
        """
        result = Polynomial(0, [])
        for i in range(self.highest_degree + 1):
            new_arr_2 = polynomial.multiply_by_rational(self.array[i])
            new_arr = new_arr_2.multiply_by_monomial(self.highest_degree - i)
            if i == 0:
                result = new_arr
            else:
                result = new_arr.add(result)

        return result

    def quotient(self, polynomial: Self) -> Self:
        # P-9
        pass

    def remainder(self, polynomial: Self) -> Self:
        # P-10
        pass

    def gcd(self, polynomial: Self) -> Self:
        # P-11
        pass

    def derivative(self) -> Self:
        # P-12
        pass

    def multiple_roots_to_simple(self) -> Self:
         '''
        module: NMR_P_P
        author: Teryokhina Sofya

        arguments: new_polynomial1: result of derivation of polynomial
                   new_polynomial2: gcd of polynomial and derivated polynomial
        This method converts multiple roots to simple.
        '''
        polynomial_highest = self.highest_degree
        polynomial_array = self.array
        polynomial = Polynomial(np_highest, np_array)
        new_polynomial1 = polynomial.derivative()
        new_polynomial2 = polynomial.gcd(new_polynomial1)
        new_polynomial_result = polynomial.quotient(new_polynomial2)
        return new_polynomial_result

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_degree == other.highest_degree)

    def __str__(self) -> str:
        string = ''
        for i in range(self.highest_degree):
            string += '{:+}'.format(self.array[i]) + 'x^' + f'{self.highest_degree - i}'
        string += '{:+}'.format(self.array[-1])
        return string
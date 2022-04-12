from typing_extensions import Self
from NaturalNumber import NaturalNumber
from RationalNumber import RationalNumber


class Polynomial:
    def __init__(self, highest_degree :int, array :list):
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
        # P-4
        pass


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
        # P-8
        pass


    def quotient(self, polynomial: Self) -> Self:
        # P-9
        pass


    def remainder(self, polynomial: Self) -> Self:
        '''
        module: MOD_PP_P
        author: Bunkevich Gleb
        argruments:
            self - polynomial
            polynomial - polynomial

        this function return remainder from dividing a polynomial by a polynomial when dividing with a remainder
        '''
    def remainder(self, polynomial: Self) -> Self:
	quotient =  self.quotient(polynomial)
        polynomial_without_remainder=  quotient.multiply(polynomial) 
        remainder = self.subtract(polynomial_without_remainder)
        return remainder


    def gcd(self, polynomial: Self) -> Self:
        # P-11
        pass


    def derivative(self) -> Self:
        # P-12
        pass


    def multiple_roots_to_simple(self) -> Self:
        # P-13
        pass

    
    def __str__(self) -> str:
        string = ''
        for i in range(self.highest_degree):
            string += '{:+}'.format(self.array[i]) + 'x^' + f'{self.highest_degree - i}'
        string += '{:+}'.format(self.array[-1])
        return string

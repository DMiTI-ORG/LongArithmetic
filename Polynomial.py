from typing_extensions import Self
from NaturalNumber import NaturalNumber
from RationalNumber import RationalNumber


class Polynomial:
    def __init__(self, highest_degree: int, array: list):
        self.highest_degree = highest_degree
        self.array = array

    def add(self, polynomial: Self) -> Self:
        num = [0] * abs(self.highest_degree - polynomial.highest_degree)   #Creating an array of zeros
        if self.highest_degree > polynomial.highest_degree:
            arr = num.extend(polynomial.array)   #Equating arrays
            i = 0
            res_arr = [0] * self.highest_degree
            while i < self.highest_degree:
                res_arr[i] = self.array[i].add(arr[i])   #Adding arrays
                res = Polynomial(self.highest_degree, res_arr)   #Creating a class instance
                i += 1
        elif self.highest_degree < polynomial.highest_degree:
            arr = num.extend(self.array)
            i = 0
            res_arr = [0] * polynomial.highest_degree
            while i < polynomial.highest_degree:
                res_arr[i] = polynomial.array[i].add(arr[i])
                res = Polynomial(polynomial.highest_degree, res_arr)
                i += 1
        else:
            i = 0
            res_arr = [0] * self.highest_degree
            while i < self.highest_degree:
                res_arr[i] = self.array[i].add(polynomial.array[i])
                res = Polynomial(self.highest_degree, res_arr)
                i += 1
        return res
        

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
        # P-13
        pass

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_degree == other.highest_degree)

    def __str__(self) -> str:
        string = ''
        for i in range(self.highest_degree):
            string += '{:+}'.format(self.array[i]) + 'x^' + f'{self.highest_degree - i}'
        string += '{:+}'.format(self.array[-1])
        return string
from typing_extensions import Self
from RationalNumber import RationalNumber
from RationalNumber import NaturalNumber

class Polynomial:
    def __init__(self, highest_degree: int, array: list) -> object:
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
        """
        module: SUB_PP_P
        author: Rakhmatulin Marat
        arguments:
            polynomial: an instance of the Polynomial
        This method subtracts from one polynomial another
        """
        if self.highest_degree >= polynomial.highest_degree:
            degree_difference = self.highest_degree - polynomial.highest_degree
            absent_degrees = list([0] * degree_difference)
            polynomial.array = absent_degrees + polynomial.array
            for i in range(0, self.highest_degree + 1):
                polynomial_1 = self.array[i].subtract(polynomial.array[i])
            return polynomial_1
        else:
            degree_difference = polynomial.highest_degree - self.highest_degree
            absent_degrees = list([0] * degree_difference)
            self.array = absent_degrees + self.array
            for i in range(0, polynomial.highest_degree + 1):
                polynomial_1 = self.array[i].subtract(polynomial.array[i])
            return polynomial_1

    def multiply_by_rational(self, number: RationalNumber) -> Self:

        """
            module: MUL_PQ_P
            author: Zhulanov Aleksandr

            arguments:
                number: an instance of the class Rational

            This method multiplies polynomial and rational
        """
        result = Polynomial(0, [])
        array_before = self
        for i in range(self.highest_degree + 1):
            num_before = array_before.array[i]
            num_after = num_before.multiply(number)
            array_before.array[i] = num_after
        result = array_before
        return result

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
        """
            module: MUL_PQ_P
            author: Zhulanov Aleksandr

            This method returned polynomial degree
        """
        result = NaturalNumber(len(str(self.highest_degree)), list(str(self.highest_degree)))
        return result

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
        """
        module: GCF_PP_P
        author: Azamatova Altana

        arguments:
            number: an instance of the class Polynomial

        this method finds the greatest common divisor
        """
        firstpoly = self
        while polynomial.highest_degree != 0:
            remainder1 = firstpoly
            firstpoly = polynomial
            polynomial = remainder1.remainder(polynomial)
        result = firstpoly
        return result

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


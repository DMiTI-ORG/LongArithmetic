from copy import deepcopy
from typing_extensions import Self
from .RationalNumber import RationalNumber
from .NaturalNumber import NaturalNumber

class Polynomial:
    def __init__(self, highest_degree: int, array: list):
        self.highest_degree = highest_degree
        self.array = array

    @staticmethod
    def str_to_num(string: str) -> Self:
        polynomial = string.split('+')
        highest_degree = int(polynomial[0].split('^')[-1])
        polynomial_array = [RationalNumber((0, 1, [0]), (1, [1])) for _ in range(highest_degree + 1)]
        for i in range(len(polynomial)):
            current_degree = int(polynomial[i].split('^')[-1])
            num = RationalNumber.str_to_num(polynomial[i].replace('(', '').split(')')[0])
            polynomial_array[highest_degree - current_degree] = num
        return Polynomial(highest_degree, polynomial_array)
                

    def add(self, polynomial: Self) -> Self:
        """
        module: ADD_PP_P
        author: Banit Maksim
        arguments:
            polynomial: an istance of the class Polynomial
        This is the method of adding two polynomials with rational coefficients
        """
        first_polynomial = deepcopy(self)
        second_polynomial = deepcopy(polynomial)
        different = abs(first_polynomial.highest_degree - second_polynomial.highest_degree)
        if first_polynomial.highest_degree > second_polynomial.highest_degree:
            second_polynomial.array = [RationalNumber((0, 1, [0]), (1, [1])) for _ in range(different)] + second_polynomial.array
        elif first_polynomial.highest_degree < second_polynomial.highest_degree:
            first_polynomial.array = [RationalNumber((0, 1, [0]), (1, [1])) for _ in range(different)] + first_polynomial.array
        result_array = [RationalNumber((0, 1, [0]), (1, [1])) for _ in range(len(first_polynomial.array))]
        for i in range(len(result_array)):
            result_array[i] = first_polynomial.array[i].add(second_polynomial.array[i])
        for i in result_array:
            print(str(i))
        i = 0
        while (i < len(result_array) - 1) and (result_array[i].numerator.is_positive() == 0):
            i += 1
        degree = len(result_array) - 1 - i
        result_array = result_array[i:]
        return Polynomial(degree, result_array)
        
    def subtract(self, polynomial: Self) -> Self:
        """
        module: SUB_PP_P
        author: Rakhmatulin Marat
        arguments:
            polynomial: an instance of the Polynomial
        This method subtracts from one polynomial another
        """
        first_polynomial = deepcopy(self)
        second_polynomial = deepcopy(polynomial)
        different = abs(first_polynomial.highest_degree - second_polynomial.highest_degree)
        if first_polynomial.highest_degree > second_polynomial.highest_degree:
            second_polynomial.array = [RationalNumber((0, 1, [0]), (1, [1])) for _ in range(different)] + second_polynomial.array
        elif first_polynomial.highest_degree < second_polynomial.highest_degree:
            first_polynomial.array = [RationalNumber((0, 1, [0]), (1, [1])) for _ in range(different)] + first_polynomial.array
        result_array = [RationalNumber((0, 1, [0]), (1, [1])) for _ in range(len(first_polynomial.array))]
        for i in range(len(result_array)):
            result_array[i] = first_polynomial.array[i].subtract(second_polynomial.array[i])

        i = 0
        while (i < len(result_array) - 1) and (result_array[i].numerator.is_positive() == 0):
            i += 1
        degree = len(result_array) - 1 - i
        result_array = result_array[i:]
        return Polynomial(degree, result_array)

    def multiply_by_rational(self, number: RationalNumber) -> Self:
        """
        module: MUL_PQ_P
        author: Zhulanov Aleksandr
 
        arguments:
            number: an instance of the class Rational
 
        This method multiplies polynomial and rational
        """
        array_before = self
        for i in range(len(self.array)):
            num_before = array_before.array[i]
            num_after = num_before.multiply(number)
            array_before.array[i] = num_after
 
        result = array_before
        return result

    def multiply_by_monomial(self, k: int) -> Self:
        """
        module: MUL_Pxk_P
        author: Teryokhina Sofya

        arguments:
            k: degree of monomial

        This method multiplies polynomial and monomial with natural degree
        """
        new_array = self.array
        zero = RationalNumber((0, 1, [0]), (1, [1]))
        for i in range(k):
            new_array.append(zero)
        new_polynomial = Polynomial(self.highest_degree + k, new_array)
        return new_polynomial

    def highest_coefficient(self) -> RationalNumber:
        """
        module: LED_P_Q
        author: Dolganov Ivan

        This method finds the highest coefficient of the polynomial
        """
        res = self.array[0]
        return res

    def get_degree(self) -> NaturalNumber:
        """
        module: MUL_PQ_P
        author: Zhulanov Aleksandr
 
        This method returned polynomial degree
        """
        result = NaturalNumber(len(str(self.highest_degree)), list(str(self.highest_degree)))
        return result

    def take_out_gdc_lcm(self) -> Self:
        """
        module: FAC_P_Q
        author: Shulegin Alexandr
 
        This method return lcm of numerators and gcd of denominators
        """
        denominator, numerator = NaturalNumber(1,[1]), NaturalNumber(1,[0])
        for i in range(self.highest_degree + 1):
            numerator = numerator.gcd(self.array[i].numerator.abs())
            denominator = denominator.lcm(self.array[i].denominator)
        result = RationalNumber((0, numerator.highest_position, numerator.array), (denominator.highest_position, denominator.array))
        return result

    def multiply(self, polynomial: Self) -> Self:
        """
        module: MUL_PP_P
        author: Smirnov Nikita

        arguments:
            number: an instance of the class Polynomial

        This method multiplies two polynomials
        """
        degree = len(self.array) + len(polynomial.array) - 2
        result = [RationalNumber((0, 1, [0]), (1, [1])) for _ in range(degree + 1)]
        for i in range(len(self.array)):
            for j in range(len(polynomial.array)):
                result[i + j] = result[i + j].add(self.array[i].multiply(polynomial.array[j]))
        return Polynomial(len(result) - 1, result)

    def quotient(self, polynomial: Self) -> Self:
        """
        module: DIV_PP_P
        author: Fomin Kirill
 
        arguments:
        polynomial: an instance of the class Polynomial
 
        This method returns quotient of dividing polynomials
        """
        result = Polynomial(0, [RationalNumber((0, 1, [0]), (1, [1]))])
        self_copy = Polynomial(self.highest_degree, self.array)
        polynomial_copy = Polynomial(polynomial.highest_degree, polynomial.array)
        if polynomial_copy.highest_degree == 0:
            for i in range(len(self_copy.array)):
                self_copy.array[i] = self_copy.array[i].divide(polynomial_copy.array[0])
            result = self_copy
        else:
            while self_copy.highest_degree >= polynomial_copy.highest_degree:
                temp = Polynomial(0, [self_copy.array[0].divide(polynomial_copy.array[0])])
                temp = temp.multiply_by_monomial(self_copy.highest_degree - polynomial_copy.highest_degree)
                result = result.add(temp)
                temp = temp.multiply(polynomial_copy)
                self_copy = self_copy.subtract(temp)
        return result

    def remainder(self, polynomial: Self) -> Self:
        """
        module: MOD_PP_P
        author: Bunkevich Gleb
        argruments:
            self - polynomial
            polynomial - polynomial
 
        this function return remainder from dividing a polynomial by a polynomial when dividing with a remainder
        """
        result = Polynomial(0, [RationalNumber((0, 1, [0]), (1, [1]))])
        self_copy = Polynomial(self.highest_degree, self.array)
        polynomial_copy = Polynomial(polynomial.highest_degree, polynomial.array)
        if polynomial_copy.highest_degree != 0:
            while self_copy.highest_degree >= polynomial_copy.highest_degree:
                temp = Polynomial(0, [self_copy.array[0].divide(polynomial_copy.array[0])])
                temp = temp.multiply_by_monomial(self_copy.highest_degree - polynomial_copy.highest_degree)
                temp = temp.multiply(polynomial_copy)
                self_copy = self_copy.subtract(temp)
                result = self_copy
        return result

    def gcd(self, polynomial: Self) -> Self:
        """
        module: GCF_PP_P
        author: Azamatova Altana

        arguments:
            number: an instance of the class Polynomial

        this method finds the greatest common divisor
        """
        firstpoly = deepcopy(self)
        while polynomial.highest_degree != 0:
            remainder1 = firstpoly
            firstpoly = polynomial
            polynomial = remainder1.remainder(polynomial)
        result = firstpoly
        return result

    def derivative(self) -> Self:
        """
        module: <DER_P_P>
        author: <Nickolay>
        This function calculates the derivative of a polynomial
        """
        result_degree = self.highest_degree - 1
        result = Polynomial(result_degree, [])
        current_degree = self.highest_degree
        for coefficient in self.array[:-1]:
            result.array.append(coefficient.multiply(RationalNumber((0, 1, [current_degree]), (1, [1]))))
            current_degree -= 1
            
        return result

    def multiple_roots_to_simple(self) -> Self:
        """
        module: NMR_P_P
        author: Teryokhina Sofya

        arguments: new_polynomial1: result of derivation of polynomial
                   new_polynomial2: gcd of polynomial and derivated polynomial
        This method converts multiple roots to simple.
        """
        polynomial_highest = deepcopy(self.highest_degree)
        polynomial_array = deepcopy(self.array)
        polynomial = Polynomial(polynomial_highest, polynomial_array)
        new_polynomial1 = polynomial.derivative()
        new_polynomial2 = polynomial.gcd(new_polynomial1)
        new_polynomial_result = polynomial.quotient(new_polynomial2)
        return new_polynomial_result

    def __eq__(self, other: Self) -> bool:
        return self.highest_degree == other.highest_degree and all(self.array[i] == other.array[i] for i in range(self.highest_degree))

    def __str__(self) -> str:
        string = ''
        for i in range(self.highest_degree + 1):
            if self.array[i].numerator.is_positive() != 0:
                string += f'{str(self.array[i])}x^{self.highest_degree - i} + '
        return string[:-2] if string else '0'

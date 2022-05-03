from os import stat_result
from .NaturalNumber import NaturalNumber
from .IntegerNumber import IntegerNumber
from typing_extensions import Self


class RationalNumber:
    def __init__(self, numerator = (), denominator = ()):
        if numerator and denominator:
            self.numerator = IntegerNumber(*numerator)
            self.denominator = NaturalNumber(*denominator)
        else:
            self.numerator = IntegerNumber(0, 1, [1])
            self.denominator = NaturalNumber(1, [1])

    @staticmethod
    def str_to_num(string: str) -> Self:
        numerator, denominator = string.split('/')
        num = RationalNumber()
        num.numerator = IntegerNumber.str_to_num(numerator)
        num.denominator = NaturalNumber.str_to_num(denominator)
        return num


    def reduce(self) -> Self:
        """
        module: TRANS_N_Z
        author: Shulegin Alexandr

        This method reduce fraction
        """
        sign = self.numerator.sign
        numerator = self.numerator.abs()
        nod = numerator.gcd(self.denominator)
        numerator = IntegerNumber.natural_to_integer(numerator)
        denominator = IntegerNumber.natural_to_integer(self.denominator)
        nod = IntegerNumber.natural_to_integer(nod)
        numerator = numerator.quotient(nod)
        denominator = denominator.quotient(nod)
        print(numerator, denominator)
        result = RationalNumber((sign, numerator.highest_position, numerator.array), (denominator.highest_position, denominator.array))

        return result

    def is_integer(self) -> bool:
        """
        module: INT_Q_B
        author: Chadina Alena
        arguments: absent
        This method check the fraction for integer
        """
        if self.denominator.highest_position == 1 and self.denominator.array[0] == 0:
            return "Error"
        else:
            numerator = self.numerator
            flag = 0
            result = None
            if numerator.highest_position == 1 and numerator.array[0] == 0:
                result = True
                flag = 1
            elif numerator.highest_position < self.denominator.highest_position:
                flag = 1
                result = False
            while flag == 0:
                for i in range(numerator.highest_position - self.denominator.highest_position,
                               numerator.highest_position):  # number subtraction
                    numerator.array[i] -= self.denominator.array[
                        i - (numerator.highest_position - self.denominator.highest_position)]
                for i in range(numerator.highest_position - 1, 0, -1):
                    if numerator.array[i] < 0:
                        numerator.array[i] += 10
                        numerator.array[i - 1] -= 1
                check = 0
                for i in range(numerator.highest_position):  # number check
                    if numerator.array[i] == 0:
                        check += 1
                    if numerator.array[i] < 0:
                        flag = 1
                        result = False
                if check == numerator.highest_position:  # all digits zero
                    flag = 1
                    result = True

            return result

    @staticmethod
    def integer_to_rational(number: IntegerNumber) -> Self:
        """
        module TRANS_Z_Q
        author Bunkevich Gleb
 
        this metod converts integer to rational
        """
        num_sign = number.sign
        num_highest_position = number.highest_position
        num_array = number.array
        denom_highest_position = 1
        denom_array = [1]
        result = RationalNumber((num_sign, num_highest_position, num_array),(denom_highest_position,denom_array))

        return result
        
    def to_integer(self) -> IntegerNumber:
        """
        module: TRANS_Q_Z
        author: Azamatova Altana

        this method returns the numerator of the fraction
        """
        if self.denominator == NaturalNumber(1, [1]):
            result = self.numerator
        else:
            result = 'ERROR'
        return result

    def add(self, number: Self) -> Self:
        """
        module: ADD_QQ_Q
        author: Dolganov Ivan

        arguments:
            number: an instance of the class NaturalNumber

        This method adds fractions
        """
        denom = self.denominator.lcm(number.denominator)
        numer1 = denom.quotient(self.denominator)
        numer2 = denom.quotient(number.denominator)
        frac1 = self.numerator.multiply(numer1)
        frac2 = number.numerator.multiply(numer2)
        numer = frac1.add(frac2)
        res = RationalNumber(numer, denom)

        return res

    def subtract(self, number: Self) -> Self:
        """
        module: <SUB_Q_Q>
        author: <Nickolay>
        Arguments:
        self: число из которого вычитают
        number: число которое вычитают
        This function allows you to subtract from one rational number another
        """
        common_denominator = self.denominator.lcm(number.denominator)
        fac1 = common_denominator.quotient(self.denominator)
        fac1 = IntegerNumber(0, fac1.highest_position, fac1.array)
        new_numerator1 = self.numerator.multiply(fac1)
        fac2 = common_denominator.quotient(number.denominator)
        fac2 = IntegerNumber(0, fac2.highest_position, fac2.array)
        new_numerator2 = number.numerator.multiply(fac2)
        result_numerator = new_numerator1.subtract(new_numerator2)
        result_rational = RationalNumber((result_numerator.sign,
                                          result_numerator.highest_position,
                                          result_numerator.array),
                                         (common_denominator.highest_position,
                                          common_denominator.array))
        if result_rational.numerator.array[0] != 0:
            result_rational = result_rational.reduce()
        return result_rational

    def multiply(self, number: Self) -> Self:
        """
        module: MUL_QQ_Q
        author: Fomin Kirill

        arguments:
            number: an instance of the RationalNumber class

        This method multiplies self and number and returns the result
        """
        result = RationalNumber((0, 0, []), (0, []))
        result.numerator = self.numerator.multiply(number.numerator)
        result.denominator = self.denominator.multiply(number.denominator)
        return result

    def divide(self, number: Self) -> Self:
        """
        module DIV_QQ_Q
        author: Chadina Alena
        arguments:
            number: an instance of the class RationalNumber
        This method divide self number on another number
        """
        result = RationalNumber((0, 0, []), (0, []))
        result.numerator = IntegerNumber((self.numerator.sign + number.numerator.sign) % 2, 0, [])
        result.denominator = NaturalNumber(0, [])
        denominator_1 = IntegerNumber(0, self.denominator.highest_position, self.denominator.array)
        denominator_2 = IntegerNumber(0, number.denominator.highest_position, number.denominator.array)
        new_numerator = self.numerator.multiply(denominator_2)
        new_denominator = denominator_1.multiply(number.numerator)
        result.numerator.highest_position = new_numerator.highest_position
        result.numerator.array = new_numerator.array
        result.denominator.highest_position = new_denominator.highest_position
        result.denominator.array = new_denominator.array

        return result

    def __eq__(self, other: Self) -> bool:
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self) -> str:
        return str(self.numerator) + '/' + str(self.denominator)
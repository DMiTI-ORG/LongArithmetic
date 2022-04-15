from NaturalNumber import NaturalNumber
from WholeNumber import WholeNumber
from typing_extensions import Self


class RationalNumber:
    def __init__(self, numerator: tuple, denominator: tuple):
        self.numerator = WholeNumber(*numerator)
        self.denominator = NaturalNumber(*denominator)

    def reduce(self) -> Self:
        """
        module: TRANS_N_Z
        author: Shulegin Alexandr

        This method reduce fraction
        """
        sign = self.numerator.sign
        numerator = self.numerator.abs()
        nod = numerator.gcd(self.denominator)
        numerator = WholeNumber.natural_to_whole(numerator)
        denominator = WholeNumber.natural_to_whole(self.denominator)
        nod = WholeNumber.natural_to_whole(nod)
        numerator = numerator.quotient(nod)
        denominator = denominator.quotient(nod)
        result = RationalNumber((sign, numerator.highest_position, numerator.array), (denominator.highest_position, denominator.array))

        return result

    def is_whole(self) -> bool:
        """
        module: INT_Q_B
        author: Chadina Alena
        arguments: absent
        This method check the fraction for whole
        """

        if self.denominator.highest_position == 1 and self.denominator.array[0] == 0:
            return ArithmeticError
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
    def whole_to_rational(number: WholeNumber) -> Self:
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
        
    def to_whole(self) -> WholeNumber:
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
        new_numerator1 = self.numerator.multiply(common_denominator.quotient(self.denominator))
        new_numerator2 = number.numerator.multiply(common_denominator.quotient(number.denominator))
        result_numerator = new_numerator2.subtract(new_numerator2)
        result_rational = RationalNumber((result_numerator.sign,
                                          result_numerator.highest_position,
                                          result_numerator.array),
                                         (common_denominator.highest_position,
                                          common_denominator.array))

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
        result.numerator = WholeNumber((self.numerator.sign + number.numerator.sign) % 2, 0, [])
        result.denominator = NaturalNumber(0, [])
        denominator_1 = WholeNumber(0, self.denominator.highest_position, self.denominator.array)
        denominator_2 = WholeNumber(0, number.denominator.highest_position, number.denominator.array)
        new_numerator = WholeNumber.multiply(self.numerator, denominator_2)
        new_denominator = WholeNumber.multiply(denominator_1, number.numerator)
        result.numerator.highest_position = new_numerator.highest_position
        result.numerator.array = new_numerator.array
        result.denominator.highest_position = new_denominator.highest_position
        result.denominator.array = new_denominator.array

        return result

    def __eq__(self, other: Self) -> bool:
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self) -> str:
        line = f'\n{"-" * max(self.numerator.highest_position, self.denominator.highest_position)}\n'
        return str(self.numerator) + line + str(self.denominator)
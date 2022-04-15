from NaturalNumber import NaturalNumber
from WholeNumber import WholeNumber
from typing_extensions import Self

class RationalNumber:
    def __init__(self, numerator :tuple, denominator :tuple):
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
        # Q-2
        pass

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
        module: ADD_ZZ_Z
        author: Dolganov Ivan

        arguments:
            number: an instance of the class NaturalNumber

        This method adds fractional numbers
        """
        denom = self.denominator.lcm(number.denominator)  # функция нока
        frac1 = self.numerator.multiply(denom)  # фунция умножения целых чисел
        frac2 = number.numerator.multiply(denom)  # фунция умножения целых чисел
        numer = frac1.add(frac2)  # функция сложения чисел
        res = RationalNumber((numer.sign, numer.highest_position, numer.array), (denom.highest_position, denom.array))
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

        result_rational.reduce()
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
        # Q-8
        pass

    def __eq__(self, other: Self) -> bool:
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self) -> str:
        line = f'\n{"-" * max(self.numerator.highest_position, self.denominator.highest_position)}\n'
        return str(self.numerator) + line + str(self.denominator)
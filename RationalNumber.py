from NaturalNumber import NaturalNumber
from WholeNumber import WholeNumber
from typing_extensions import Self

class RationalNumber:
    def __init__(self, numerator :tuple, denominator :tuple):
        self.numerator = WholeNumber(*numerator)
        self.denominator = NaturalNumber(*denominator)


    def reduce(self) -> Self:
        # Q-1
        pass


    def is_whole(self) -> bool:
        # Q-2
        pass


    def whole_to_rational(self) -> Self:
        # Q-3
        pass


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

        denom = lcm(self.denominator, number.denominator)  # функция нока
        frac1 = multiply(self.numerator, ((denom)))  # фунция умножения целых чисел
        frac2 = multiply(number.numerator, ((denom)))  # фунция умножения целых чисел
        numer = add(frac1, frac2)  # функция сложения чисел
        res = RationalNumber(numer, denom)
        return res


    def subtract(self, number: Self) -> Self:
        # Q-6
        pass


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
        return self.numerator == other.numerator


    def __str__(self) -> str:
        line = f'\n{"-" * max(self.numerator.highest_position, self.denominator.highest_position)}\n'
        return str(self.numerator) + line + str(self.denominator)
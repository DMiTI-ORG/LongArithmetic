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
        # Q-4
        pass


    def add(self, number: Self) -> Self:
        # Q-5
        pass


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
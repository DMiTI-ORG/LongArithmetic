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
        # Q-5
        pass


    def subtract(self, number: Self) -> Self:
        # Q-6
        pass


    def multiply(self, number: Self) -> Self:
        # Q-7
        pass


    def divide(self, number: Self) -> Self:
        # Q-8
        pass

    
    def __eq__(self, other: Self) -> bool:
        return self.numerator == other.numerator


    def __str__(self) -> str:
        line = f'\n{"-" * max(self.numerator.highest_position, self.denominator.highest_position)}\n'
        return str(self.numerator) + line + str(self.denominator)
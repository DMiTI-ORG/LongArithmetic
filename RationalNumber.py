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
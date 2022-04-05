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
        """
        module: <SUB_Q_Q>
        author: <Nickolay>

        Arguments:
            self: число из которого вычитают
            number: число которое вычитают

        This function allows you to subtract from one rational number another
               """
        # find the common denominator
        common_denominator = self.denominator.lcm(number.denominator)
        # find the new numerator of the first fraction
        new_numerator1 = self.numerator.multiply(common_denominator.quotient(self.denominator))
        # find the new numerator of the second fraction
        new_numerator2 = number.numerator.multiply(common_denominator.quotient(number.denominator))
        # find the common numerator by subtracting the two obtained
        result_numerator = new_numerator2.subtract(new_numerator2)
        # get the result of subtraction
        result_rational = RationalNumber((result_numerator.sign,
                                          result_numerator.highest_position,
                                          result_numerator.array),
                                         (common_denominator.highest_position,
                                          common_denominator.array))
        # reduce it and output
        result_rational.reduce()
        return result_rational


    def multiply(self, number: Self) -> Self:
        # Q-7
        pass


    def divide(self, number: Self) -> Self:
        # Q-8
        pass


    def __str__(self) -> str:
        line = f'\n{"-" * max(self.numerator.highest_position, self.denominator.highest_position)}\n'
        return str(self.numerator) + line + str(self.denominator)
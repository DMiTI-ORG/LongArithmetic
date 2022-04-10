from NaturalNumber import NaturalNumber
from typing_extensions import Self


class WholeNumber:
    def __init__(self, sign :int, highest_position: int, array: list):
        self.sign = sign
        self.highest_position = highest_position
        self.array = array


    def abs(self) -> NaturalNumber:
        # Z-1
        pass


    def is_positive(self) -> int:
        # Z-2
        pass


    def multiply_by_minus_one(self) -> Self:
        # Z-3
        pass


    def natural_to_whole(self) -> Self:
        # Z-4
        pass


    def to_natural(self) -> NaturalNumber:
        # Z-5
        pass


    def add(self, number: Self) -> Self:
        # Z-6
        pass


    def subtract(self, number: Self) -> Self:
        # Z-7
        pass


    def multiply(self, number: Self) -> Self:
        # Z-8
        pass


    def quotient(self, number: Self) -> Self:
        # Z-9
        pass


    def remainder(self, number: Self) -> Self:
        """
        module: MOD_ZZ_Z
        author: Azamatova Altana

        arguments:
            number: an instance of the class WholeNumber

        this method finds the remainder of the division of integers
        """
        result = WholeNumber(0, 0, [])
        one = WholeNumber(0, 1, [1])
        first_Z = int(''.join(map(str, self.array)))
        second_Z = int(''.join(map(str, number.array)))
        if self.sign == 0 and number.sign == 0:
            if second_Z == 0:
                return 'ERROR'
            elif first_Z == second_Z:
                result = WholeNumber(0, 1, [0])
            elif ((self.highest_position > number.highest_position) or(first_Z > second_Z)):
                div = self.quotient(number)
                mul = number.multiply(div)
                result = self.subtract(mul)
            elif ((self.highest_position < number.highest_position) or (first_Z < second_Z)):
                result = self
        elif self.sign == 1 and number.sign == 0:
            self.multiply_by_minus_one()
            if second_Z == 0:
                return 'ERROR'
            elif first_Z == second_Z:
                result = WholeNumber(1, 1, [0])
            elif ((self.highest_position > number.highest_position) or(first_Z > second_Z)):
                div = self.quotient(number)
                div.sign = 1
                sub = div.subtract(one)
                mul = number.multiply(sub)
                self.multiply_by_minus_one()
                result = self.subtract(mul)
            elif ((self.highest_position < number.highest_position) or (first_Z < second_Z)):
                result = self.subtract(number)

        elif self.sign == 0 and number.sign == 1:
            number.multiply_by_minus_one()
            if second_Z == 0:
                return 'ERROR'
            elif first_Z == second_Z:
                result = WholeNumber(1, 1, [0])
            elif ((self.highest_position > number.highest_position) or (first_Z > second_Z)):
                div = self.quotient(number)
                mul = number.multiply(div)
                result = self.subtract(mul)
            elif ((self.highest_position < number.highest_position) or (first_Z < second_Z)):
                result = self

        if self.sign == 1 and number.sign == 1:
            if second_Z == 0:
                return 'ERROR'
            elif first_Z == second_Z:
                result = WholeNumber(0, 1, [0])
            elif ((self.highest_position < number.highest_position) or (first_Z < second_Z)):
                result = self
            elif ((self.highest_position > number.highest_position) or (first_Z > second_Z)):
                div = self.quotient(number)
                mul = number.multiply(div)
                result = self.subtract(mul)

        return result

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position) and (self.sign == other.sign)


    def __str__(self) -> str:
        return ('-' if self.sign else '') + ''.join(map(str, self.array))
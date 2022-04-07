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
        if self.sign == 0:
            number = NaturalNumber(self.highest_position, self.array)
            return number
        else:
            return 'Error'


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
        # Z-10
        pass

    
    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position) and (self.sign == other.sign)


    def __str__(self) -> str:
        return ('-' if self.sign else '') + ''.join(map(str, self.array))
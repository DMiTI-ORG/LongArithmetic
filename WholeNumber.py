from NaturalNumber import NaturalNumber
from typing_extensions import Self


class WholeNumber:
    def __init__(self, sign :int, highest_position: int, array: list):
        self.sign = sign
        self.highest_position = highest_position
        self.array = array


    def abs(self) -> NaturalNumber:
        '''
        module: ABS_Z_N
        author: Banit Maxim
        
        This method returns an instance of the class NaturalNumber
        '''
        number = NaturalNumber(self.highest_position, self.array)
        return number


    def is_positive(self) -> int:
        '''
        module: POZ_Z_D
        author: Banit Maxim

        This method determines whether a number is positive|negative or zero
        '''
        if self.sign == 0 and all(x != 0 for x in self.array):
            return 2
        elif self.sign == 1 and all(x != 0 for x in self.array):
            return 1
        else:
            return 0


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
        # Z-10
        pass

    
    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position) and (self.sign == other.sign)


    def __str__(self) -> str:
        return ('-' if self.sign else '') + ''.join(map(str, self.array))
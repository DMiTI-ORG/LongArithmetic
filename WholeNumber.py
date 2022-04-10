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
            """
         module: MUL_ZM_Z
         author: Rakhmatulin Marat
         arguments:
         new_sign: new number sign
         This method multiplies the number by minus one
            """
            if self.sign == 1:
                new_sign = 0
            else:
                new_sign = 1
            return WholeNumber(new_sign, self.highest_position, self.array)

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
        """
        module: DIV_ZZ_Z
        author: Rakhmatulin Marat
        arguments:
             number: an instance of the WholeNumber
        This method divides one integer by another that is not equal to zero
        """
        if number.is_positive() != 0:
            number_1 = self.abs()
            number_2 = number.abs()
            number_3 = number_1.quotient(number_2)
            return number_3
        else:
            return 'Error'


    def remainder(self, number: Self) -> Self:
        # Z-10
        pass

    
    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position) and (self.sign == other.sign)


    def __str__(self) -> str:
        return ('-' if self.sign else '') + ''.join(map(str, self.array))
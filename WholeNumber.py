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


    def add1(self, number: Self) -> Self:
        """
        module: ADD_ZZ_Z
        author: Smirnov Kirill

        arguments:
            number: an instance of the class NaturalNumber
            digit: one digit to mutiply with number

        Add up integers
        """
        if self.sign == number.sign:
            number_1 = self.abs()
            number_2 = number.abs()
            new_number = number_1.add(number_2)
            return WholeNumber(self.sign, new_number.highest_position, new_number.array)
        else:
            number_1 = self.abs()
            number_2 = number.abs()
            comp = number_1.compare(number_2)
            if comp == 1:
                t = number_1
                self = number
                number_2 = t
            new_number = number_1.subtract(number_2)
            return WholeNumber(self.sign, new_number.highest_position, new_number.array)


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
        return (self.array == other.array) and (self.highest_position == other.highest_position) and \
               (self.sign == other.sign)


    def __str__(self) -> str:
        return ('-' if self.sign else '') + ''.join(map(str, self.array))
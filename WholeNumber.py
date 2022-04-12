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
        '''
        module: SUB_ZZ_Z
        author: Bunkevich Gleb
        argruments:
            number - integer number
            self - integer number

        this function does subtraction of two integers by splitting by signs into cases
        '''

        if (self.is_positive() == 2 and number.is_positive() == 2):   
            if self.abs().compare(number.abs()) == 2: return self.abs().subtract(number.abs())  
            elif self.abs().compare(number) == 0: return 0 
            else: 
                TemporAbsResult = number.abs().subtract(self.abs())
                result = WholeNumber(WholeNumber(0, TemporAbsResult.hihgest_position, [TemporAbsResult.array]))
                return result.multiply_by_minus_one()

        elif (self.is_positive() == 2 and number.is_positive() == 1): 
            return self.abs().add(number.abs())
        elif (self.is_positive() == 1 and number.is_positive() == 2):
            TemporAbsResult = self.abs().add(number.abs())
            result = WholeNumber(0, TemporAbsResult.hihgest_position, [TemporAbsResult.array])
            return result.multiply_by_minus_one()
        elif  (self.is_positive() == 0 and number.is_positive() == 0): return 0 
        else: 
            if self.abs().compare(number.abs()) == 1: return number.abs().subtract(self.abs())
            elif self.abs().compare(number.abs()) == 0: return 0 
            else:                 TemporAbsResult = self.abs().subtract(number.abs())
                result = WholeNumber(0, TemporAbsResult.hihgest_position, [TemporAbsResult.array])
                return result.multiply_by_minus_one()


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

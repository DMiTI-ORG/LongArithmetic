from typing_extensions import Self
from . import NaturalNumber


class WholeNumber:
    def __init__(self, sign :int, highest_position: int, array: list):
        self.sign = sign
        self.highest_position = highest_position
        self.array = array

    def abs(self) -> NaturalNumber:
        """
        module: ABS_Z_N
        author: Banit Maxim
        
        This method returns an instance of the class NaturalNumber
        """
        number = NaturalNumber.NaturalNumber(self.highest_position, self.array)
        return number

    def is_positive(self) -> int:
        """
        module: POZ_Z_D
        author: Banit Maxim

        This method determines whether a number is positive|negative or zero
        """
        if self.sign == 0 and self.array.count(0) != self.highest_position:
            return 2
        elif self.sign == 1 and self.array.count(0) != self.highest_position:
            return 1
        else:
            return 0

    def multiply_by_minus_one(self) -> Self:
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

    @staticmethod
    def natural_to_whole(number: NaturalNumber) -> Self:
        """
        module: TRANS_N_Z
        author: Shulegin Alexandr

        arguments:
            number: one number to transforf it to whole

        This method transform natural number to whole number
        """
        sign = 0
        highest_position = number.highest_position
        array = number.array
        result = WholeNumber(sign,highest_position,array)
        return result

    def to_natural(self) -> NaturalNumber:
        """
        module: TRANS_Z_N
        author: Fomin Kirill

        arguments:
            number: an instance of the WholeNumber class

        Transfers an instance of WholeNumber class into a NaturalNumber class
        """
        if self.sign == 0:
            number = NaturalNumber.NaturalNumber(self.highest_position, self.array)
            return number
        else:
            return 'Error'

    def add(self, number: Self) -> Self:
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
        """
        module: SUB_ZZ_Z
        author: Bunkevich Gleb
        argruments:
            number - integer number
            self - integer number

        this function does subtraction of two integers by splitting by signs into cases
        """
        if self.is_positive() == 2 and number.is_positive() == 2:
            if self.abs().compare(number.abs()) == 2:
                return self.abs().subtract(number.abs())
            elif self.abs().compare(number) == 0:
                return 0
            else: 
                tempor_abs_result = number.abs().subtract(self.abs())
                result = WholeNumber(WholeNumber(0, tempor_abs_result.hihgest_position, [tempor_abs_result.array]))
                return result.multiply_by_minus_one()

        elif self.is_positive() == 2 and number.is_positive() == 1:
            return self.abs().add(number.abs())
        elif self.is_positive() == 1 and number.is_positive() == 2:
            tempor_abs_result = self.abs().add(number.abs())
            result = WholeNumber(0, tempor_abs_result.hihgest_position, [tempor_abs_result.array])
            return result.multiply_by_minus_one()
        elif self.is_positive() == 0 and number.is_positive() == 0: return 0
        else: 
            if self.abs().compare(number.abs()) == 1: return number.abs().subtract(self.abs())
            elif self.abs().compare(number.abs()) == 0: return 0 
            else:
                tempor_abs_result = self.abs().subtract(number.abs())
                result = WholeNumber(0, tempor_abs_result.hihgest_position, [tempor_abs_result.array])
                return result.multiply_by_minus_one()

    def multiply(self, number: Self) -> Self:
        """
        module: MUL_ZZ_Z
        author: Chadina Alena
        arguments:
            number: an instance of the class WholeNumber
        This method multiply two whole numbers
        """
        result = WholeNumber((self.sign + number.sign) % 2, 0, [])
        self_copy = NaturalNumber.NaturalNumber(self.highest_position, self.array)
        number_copy = NaturalNumber.NaturalNumber(number.highest_position, number.array)
        result_natural = NaturalNumber.NaturalNumber.multiply(self_copy, number_copy)  # multiply two natural numbers
        result.highest_position = result_natural.highest_position
        result.array = result_natural.array
        return result

    def quotient(self, number: Self) -> Self:
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
        """
        module: MOD_ZZ_Z
        author: Azamatova Altana

        arguments:
            number: an instance of the class WholeNumber

        this method finds the remainder of the division of integers
        """
        result = WholeNumber(0, 0, [])
        one = WholeNumber(0, 1, [1])
        first_z = int(''.join(map(str, self.array)))
        second_z = int(''.join(map(str, number.array)))
        if self.sign == 0 and number.sign == 0:
            if second_z == 0:
                return 'ERROR'
            elif first_z == second_z:
                result = WholeNumber(0, 1, [0])
            elif (self.highest_position > number.highest_position) or (first_z > second_z):
                div = self.quotient(number)
                mul = number.multiply(div)
                result = self.subtract(mul)
            elif (self.highest_position < number.highest_position) or (first_z < second_z):
                result = self
        elif self.sign == 1 and number.sign == 0:
            self.multiply_by_minus_one()
            if second_z == 0:
                return 'ERROR'
            elif first_z == second_z:
                result = WholeNumber(1, 1, [0])
            elif (self.highest_position > number.highest_position) or(first_z > second_z):
                div = self.quotient(number)
                div.sign = 1
                sub = div.subtract(one)
                mul = number.multiply(sub)
                self.multiply_by_minus_one()
                result = self.subtract(mul)
            elif (self.highest_position < number.highest_position) or (first_z < second_z):
                result = self.subtract(number)

        elif self.sign == 0 and number.sign == 1:
            number.multiply_by_minus_one()
            if second_z == 0:
                return 'ERROR'
            elif first_z == second_z:
                result = WholeNumber(1, 1, [0])
            elif (self.highest_position > number.highest_position) or (first_z > second_z):
                div = self.quotient(number)
                mul = number.multiply(div)
                result = self.subtract(mul)
            elif (self.highest_position < number.highest_position) or (first_z < second_z):
                result = self

        if self.sign == 1 and number.sign == 1:
            if second_z == 0:
                return 'ERROR'
            elif first_z == second_z:
                result = WholeNumber(0, 1, [0])
            elif (self.highest_position < number.highest_position) or (first_z < second_z):
                result = self
            elif (self.highest_position > number.highest_position) or (first_z > second_z):
                div = self.quotient(number)
                mul = number.multiply(div)
                result = self.subtract(mul)

        return result

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position) and (self.sign == other.sign)

    def __str__(self) -> str:
        return ('-' if self.sign else '') + ''.join(map(str, self.array))

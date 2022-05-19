from typing_extensions import Self
from .NaturalNumber import NaturalNumber


class IntegerNumber:
    def __init__(self, sign :int, highest_position: int, array: list):
        self.sign = sign
        self.highest_position = highest_position
        self.array = array


    @staticmethod
    def str_to_num(string):
        sign = 0
        if string[0] == '-':
            sign = 1
            string = string[1:]
        elif string[0] == '+':
            string = string[1:]
        return IntegerNumber(sign, len(string), list(map(int, string)))


    def abs(self) -> NaturalNumber:
        """
        module: ABS_Z_N
        author: Banit Maxim
        
        This method returns an instance of the class NaturalNumber
        """
        number = NaturalNumber(self.highest_position, self.array)
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
        return IntegerNumber(new_sign, self.highest_position, self.array)

    @staticmethod
    def natural_to_integer(number: NaturalNumber) -> Self:
        """
        module: TRANS_N_Z
        author: Shulegin Alexandr

        arguments:
            number: one number to transforf it to integer

        This method transform natural number to integer number
        """
        sign = 0
        highest_position = number.highest_position
        array = number.array
        result = IntegerNumber(sign,highest_position,array)
        return result

    def to_natural(self) -> NaturalNumber:
        """
        module: TRANS_Z_N
        author: Fomin Kirill

        arguments:
            number: an instance of the IntegerNumber class

        Transfers an instance of IntegerNumber class into a NaturalNumber class
        """
        if self.sign == 0:
            number = NaturalNumber(self.highest_position, self.array)
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
            return IntegerNumber(self.sign, new_number.highest_position, new_number.array)
        else:
            number_1 = self.abs()
            number_2 = number.abs()           
            if number_1.compare(number_2) == 2:
                new_number = number_1.subtract(number_2)
                return IntegerNumber(self.sign, new_number.highest_position, new_number.array)
            elif number_1.compare(number_2) == 0:
                return IntegerNumber(0, 1, [0])
            else: 
                new_number = number_1.subtract(number_2)
                return IntegerNumber(number.sign, new_number.highest_position, new_number.array)


    def subtract(self, number: Self) -> Self:
        """
        module: SUB_ZZ_Z
        author: Bunkevich Gleb
        argruments:
            number - integer number
            self - integer number
 
        this function does subtraction of two integers by splitting by signs into cases
        """
        if (self.is_positive() != 0 and number.is_positive() == 0):
            return IntegerNumber(self.sign, self.highest_position, self.array)
        elif (self.is_positive() == 0 and number.is_positive() == 2): return IntegerNumber(1, number.highest_position, number.array)
        elif (self.is_positive() == 2 and number.is_positive() == 2):
            if self.abs().compare(number.abs()) == 2:
                temp = self.abs().subtract(number.abs())
                return IntegerNumber(0, temp.highest_position, temp.array)
            elif self.abs().compare(number) == 0:
                return IntegerNumber(0,1,[0])
            else: 
                temp = number.abs().subtract(self.abs())
                return IntegerNumber(1, temp.highest_position, temp.array)
 
        elif (self.is_positive() == 2 and number.is_positive() == 1):
            temp = self.abs().add(number.abs())
            return IntegerNumber(0, temp.highest_position, temp.array)
 
        elif (self.is_positive() == 1 and number.is_positive() == 2):
            temp = self.abs().add(number.abs())
            return IntegerNumber(1, temp.highest_position, temp.array)
 
        elif (self.is_positive() == 0 and number.is_positive() == 0):
            return IntegerNumber(0,1,[0])
 
        else:
            comp = self.abs().compare(number.abs())
            if comp == 1:
                temp = number.abs().subtract(self.abs())
                return IntegerNumber(0, temp.highest_position, temp.array)
            elif comp == 0:
                return IntegerNumber(0,1,[0])
            else:
                temp = self.abs().subtract(number.abs())
                return IntegerNumber(1, temp.highest_position, temp.array)

    def multiply(self, number: Self) -> Self:
        """
        module: MUL_ZZ_Z
        author: Chadina Alena
        arguments:
            number: an instance of the class IntegerNumber
        This method multiply two integer numbers
        """
        result = IntegerNumber((self.sign + number.sign) % 2, 0, [])
        self_copy = NaturalNumber(self.highest_position, self.array)
        number_copy = NaturalNumber(number.highest_position, number.array)
        result_natural = NaturalNumber.multiply(self_copy, number_copy)  # multiply two natural numbers
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
            if number_1.compare(number_2) == 1:
                return IntegerNumber(0, 1, [0])
            else:
                number_3 = number_1.quotient(number_2)
                if self.sign == number.sign:
                    return IntegerNumber(0, number_3.highest_position, number_3.array)
                else:
                    return IntegerNumber(1, number_3.highest_position, number_3.array)
        else:
            return 'Error'

    def remainder(self, number: Self) -> Self:
        """
        module: MOD_ZZ_Z
        author: Azamatova Altana
 
        arguments:
            number: an instance of the class IntegerNumber
 
        this method finds the remainder of the division of integers
        """
        result = IntegerNumber(0, 0, [])
        one = IntegerNumber(0, 1, [1])
        first_z = int(''.join(map(str, self.array)))
        second_z = int(''.join(map(str, number.array)))
        if self.sign == 0 and number.sign == 0:
            if second_z == 0:
                return 'ERROR'
            elif first_z == second_z:
                result = IntegerNumber(0, 1, [0])
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
                result = IntegerNumber(1, 1, [0])
            elif (self.highest_position > number.highest_position) or(first_z > second_z):
                print("ok")
                div = self.quotient(number)
                div.sign = 1
                sub = div.subtract(one)
                mul = number.multiply(sub)
                self.multiply_by_minus_one()
                result = self.subtract(mul)
            elif (self.highest_position < number.highest_position) or (first_z < second_z):
                if first_z < second_z:
                    result = self.abs()
                else:
                    result = self.subtract(number)
 
        elif self.sign == 0 and number.sign == 1:
            number.multiply_by_minus_one()
            if second_z == 0:
                return 'ERROR'
            elif first_z == second_z:
                result = IntegerNumber(1, 1, [0])
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
                result = IntegerNumber(0, 1, [0])
            elif (self.highest_position < number.highest_position) or (first_z < second_z):
                result = self
            elif (self.highest_position > number.highest_position) or (first_z > second_z):
                div = self.quotient(number)
                div = div.add(one)
                mul = number.multiply(div)
                result = self.abs().subtract(mul)
        return result

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position) and (self.sign == other.sign)

    def __str__(self) -> str:
        return ('-' if self.sign else '') + ''.join(map(str, self.array))
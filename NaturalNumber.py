from typing_extensions import Self


class NaturalNumber:
    def __init__(self, highest_position: int, array: list):
        self.highest_position = highest_position
        self.array = array

    def compare(self, number: Self) -> int:
        # N-1
        pass

    def is_zero(self) -> bool:
        # N-2
        pass

    def add_one(self) -> Self:
        # N-3
        pass

    def add(self, number: Self) -> Self:
        # N-4
        pass

    def subtract(self, number: Self) -> Self:
        # N-5
        pass

    def multiply_digit(self, digit: int) -> Self:
        # N-6
        pass

    def multiply_by_powered_ten(self, digit: int) -> Self:
        # N-7
        pass

    def multiply(self, number: Self) -> Self:
        # N-8
        pass

    def subtract_k_by_number(self, number: Self, digit: int) -> Self:
        """
        module: SUB_NDN_N
        author: Smirnov Nikita

        arguments:
            number: an instance of the class NaturalNumber
            digit: one digit to multiply with number

        This method subtract from self number another number multiplied with digit
        """

        new_num = number.multiply_digit(digit)
        if self.compare(new_num) != 1:
            return self.subtract(new_num)
        else:
            return 'Error'


    def first_division_digit(self, number: Self, digit: int) -> Self:
        # N-10
        pass

    def quotient(self, number: Self) -> Self:
        # N-11
        pass

    def remainder(self, number: Self) -> Self:
        # N-12
        pass

    def gcd(self, number: Self) -> Self:
        # N-13
        pass


    def lcm(self, number: Self) -> Self:
        """
        module: LCM_NN_N
        author: Zhulanov Aleksandr

        arguments:
        number: an instance of the class NaturalNumber

        This method passes lcm of the natural numbers
        """
        mult = number.multiply()
        nod = number.gcd()
        nok = 0
        new_number = 0
        if mult > 0 and nod != 0:
            while new_number < mult:
                new_number += nod
                nok += 1
            return nok
        else:
            return 'Error'

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position)

    def __str__(self) -> str:
        return ''.join(map(str, self.array))


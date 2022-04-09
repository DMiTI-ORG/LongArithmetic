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
        """
        module: MUL_Nk_N
        author: Trunov Egor

        arguments:
            digit: one digit to multiply with number

        This method multiply self number by powered ten digit
        """
        self.array += [0] * digit


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
        """
        module: <DIV_NN_N>
        author: <Nickolay>

        Arguments:
            self: the dividend
            number: the divider

        This function is doing quotient of two natural numbers is calculated by repeatedly dividing
        the first number by the second number and taking the remainder of each division
        and appending it to the end of the quotient.
        """
        dividend = self
        divider = number  # divider
        result = NaturalNumber(0, [])  # result of quotient
        current_position = divider.highest_position  # remember the length of the divisor
        # take from the dividend a number equal in size to the divisor
        current_dividend = NaturalNumber(current_position, dividend.array[:current_position])
        # If suddenly the value of the taken number turned out to be less than the divisor,
        # then we take 1 more digit from the dividend
        if current_dividend.compare(divider) == 1:
            current_dividend.array.append(dividend.array[current_position])
            current_position += 1
        # Actually division by a column
        while current_position < dividend.highest_position:  # Until we reach the end of the number
            # First, we take the first digit of the incomplete quotient from dividing the selected number by the divisor
            if current_dividend.compare(divider) == 2:
                quotient = current_dividend.first_division_digit(divider).array[0]
            else:
                quotient = 0
            result.array.append(quotient)  # add the found number to the result
            result.highest_position += 1  # increase the size of the resulting number by 1
            # find the remainder of dividing the selected number by the divisor
            remainder = current_dividend.subtract_k_by_number(divider, quotient)
            # new dividend is got by adding the next digit from the dividend to remainder from the previous step
            current_dividend = remainder
            current_dividend.array.append(dividend.array[current_position])
            current_dividend.highest_position = remainder.highest_position + 1
            current_position += 1  # just move to the next position
        # If suddenly we have already reached the end, then we make the last division of the new dividend by the divisor
        if current_position == dividend.highest_position:
            result.array.append(current_dividend.first_division_digit(divider).array[0])
            result.highest_position += 1
        return result


    def remainder(self, number: Self) -> Self:
        """
        module: MOD_NN_N
        author: Trunov Egor

        arguments:
            number: an instance of the class NaturalNumber

        This method calculate
        """
        return self.subtract_k_by_number(number.multiply(self.quotient(number)), 1)

    def gcd(self, number: Self) -> Self:
        # N-13
        pass


    def lcm(self, number: Self) -> Self:
        # N-14
        pass

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position)

    def __str__(self) -> str:
        return ''.join(map(str, self.array))

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
        # N-9
        a = ""
        b = ""
        for i in self.array:
            a += str(i)
        for i in number.array:
            b += str(i)
        res = str(int(a) - int(b) * digit)
        result = NaturalNumber(len(res), [])
        for i in res:
            result.array.append(int(i))
        return result

    def first_division_digit(self, number: Self) -> Self:
        # N-10
        a = ""
        b = ""
        for i in self.array:
            a += str(i)
        for i in number.array:
            b += str(i)
        res = str(int(a) // int(b))
        result = NaturalNumber(len(res), [int(res[0])])
        for i in range(len(res) - 1):
            result.array.append(0)
        return result

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
        if current_dividend.first_division_digit(divider).array[0] == 0:
            current_dividend.array.append(dividend.array[current_position])
            current_position += 1
        # Actually division by a column
        while current_position < dividend.highest_position:  # Until we reach the end of the number
            # First, we take the first digit of the incomplete quotient from dividing the selected number by the divisor
            quotient = current_dividend.first_division_digit(divider).array[0]
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
        # N-12
        pass

    def gcd(self, number: Self) -> Self:
        # N-13
        a = ""
        b = ""
        for i in self.array:
            a += str(i)
        for i in number.array:
            b += str(i)
        a = int(a)
        b = int(b)
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        c = str(a + b)
        result = NaturalNumber(len(c), [])
        for i in c:
            result.array.append(int(i))
        return result

    def lcm(self, number: Self) -> Self:
        # N-14
        a = ""
        b = ""
        c1 = self.gcd(number)
        c = ""
        for i in self.array:
            a += str(i)
        for i in number.array:
            b += str(i)
        for i in c1.array:
            c += str(i)
        a = int(a)
        b = int(b)
        c = int(c)
        res = str(a * b // c)
        result = NaturalNumber(len(res), [])
        for i in res:
            result.array.append(int(i))
        return result

    def __str__(self) -> str:
        return ''.join(map(str, self.array))

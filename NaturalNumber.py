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
        res = NaturalNumber(self.highest_position, [0] * self.highest_position)
        discharge = 0
        n = 0
        for i in reversed(range(self.highest_position)):
            n = self.array[i] * digit
            n = n + discharge
            discharge = 0
            if n // 10 >= 1:
                discharge += n // 10
                n = n % 10
            res.array[i] = n
        if discharge > 0:
            res.array.insert(0, discharge)

        return res



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
        """
                module: MUL_NN_N
                author: Starodubtsev Maxim
                arguments:
                    number: an instance of the class NaturalNumber

                This method multiplies two natural numbers

        """
        res = NaturalNumber(1, [0])
        num = NaturalNumber(1, [0])
        k = 0
        for i in reversed(range(self.highest_position)):
            num = number.multiply_digit(self.array[i])
            num = num.multiply_by_powered_ten(k)
            k = k + 1
            res = res.add(num)
        return res

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
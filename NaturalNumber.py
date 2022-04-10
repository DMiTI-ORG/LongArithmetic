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
        """
        module: GCF_NN_N
        author: Dolganov Ivan

        arguments:
            number: an instance of the class NaturalNumber

        This method finds the greatest common divisor of numbers
        """

        arrz = [0] * abs(self.highest_position - number.highest_position)
        i = 0
        if self.highest_position >= number.highest_position:
            res_arr = [0] * self.highest_position
            arr = arrz.extend(number.array)
            while i < self.highest_position:
                while self.array[i].is_zero() == 'yes' and arr[i].is_zero() == 'yes':
                    if (self.array[i].compare(arr[i]) == 0) or (self.array[i].compare(arr[i]) == 2):
                        self.array[i] = self.array[i].remainder(arr[i])
                        res_arr[i] = self.array[i]
                    else:
                        arr[i] = arr[i].remainder(self.array[i])
                        res_arr[i] = arr[i]
                i += 1
            res = NaturalNumber(self.highest_position, res_arr)
        else:
            res_arr = [0] * number.highest_position
            arr = arrz.extend(self.array)
            while i < number.highest_position:
                while arr[i].is_zero() == 'yes' and number.array[i].is_zero() == 'yes':
                    if (arr[i].compare(number.array[i]) == 0) or (arr[i].compare(number.array[i]) == 2):
                        arr[i] = arr[i].remainder(number.array[i])
                        res_arr[i] = arr[i]
                    else:
                        number.array[i] = number.array[i].remainder(arr[i])
                        res_arr[i] = number.array[i]
                i += 1
            res = NaturalNumber(number.highest_position, res_arr)
        return res


    def lcm(self, number: Self) -> Self:
        # N-14
        pass

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position)

    def __str__(self) -> str:
        return ''.join(map(str, self.array))

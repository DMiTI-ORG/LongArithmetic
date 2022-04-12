from typing_extensions import Self


class NaturalNumber:
    def __init__(self, highest_position: int, array: list):
        self.highest_position = highest_position
        self.array = array

    def compare(self, number: Self) -> int:
        position = 0
        answer = 0
        if self.highest_position > number.highest_position:
            answer = 2
        elif self.highest_position < number.highest_position:
            answer = 1
        else:
            while position < self.highest_position:
                if self.array[position] > number.array[position]:
                    answer = 2
                    position = self.highest_position
                elif self.array[position] < number.array[position]:
                    answer = 1
                    position = self.highest_position
                else:
                    position += 1
        return answer

    def is_zero(self) -> bool:
        if self.highest_position == 1:
            if self.array[0] == 0:
                return True
            else:
                return False
        else:
            return False

    def add_one(self) -> Self:
        # N-3
        pass

    def add(self, number: Self) -> Self:
        comparison = self.compare(number)
        if comparison == 1:
            x = self
            self = number
            number = x
        array_answer = [0] * self.highest_position

        dozens = 0

        if self.highest_position > number.highest_position:
            number.array = [0] * (self.highest_position - number.highest_position) + number.array
        elif self.highest_position < number.highest_position:
            self.array = [0] * (number.highest_position - self.highest_position) + self.array

        for i in range(self.highest_position - 1, -1, -1):
            array_answer[i] = self.array[i] + number.array[i] + dozens
            dozens = 0

            if array_answer[i] > 10:
                array_answer[i] = array_answer[i] % 10
                dozens = 1
        if dozens != 0:
            array_answer = [dozens] + array_answer

        return array_answer

    def subtract(self, number: Self) -> Self:
        """
        module: SUB_NN_N
        author: Smirnov Kirill

        arguments:
            number: an instance of the class NaturalNumber
            digit: one digit to muliply with number

        subtract one number from another
        """
        comp = self.compare(number)
        if comp == 1:
            t = self
            self = number
            number = t
        new_array = self.array
        posittion = self.highest_position - 1
        while posittion >= 0:
            if self.array[posittion] - number.array[posittion] >= 0:
                new_array[posittion] = self.array[posittion] - number.array[posittion]
            else:
                temporary_position = posittion - 1
                while new_array[temporary_position] != 0:
                    temporary_position -= 1
                new_array[temporary_position] - 1
                temporary_position += 1
                while temporary_position < posittion:
                    new_array[temporary_position] += 9
                    temporary_position += 1
                new_array[temporary_position] += 10
                new_array = self.array[posittion] - number.array[posittion]
            posittion -= 1
        posittion += 1
        while posittion < self.highest_position - 1 and new_array[0] == 0:
            new_array.pop(0)
            posittion += 1

        return NaturalNumber(self.highest_position - posittion, new_array)

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
        # N-14
        pass

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position)

    def __str__(self) -> str:
        return ''.join(map(str, self.array))

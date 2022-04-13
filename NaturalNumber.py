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
        """
        module: SUB_NDN_N
        author: Kirill Smirnov

        This method adds to the number 1
        """
        i = 1
        new_highest_position = self.highest_position
        new_array = [0]*self.highest_position
        position = self.highest_position
        while position > -1:
            position = self.highest_position - i
            if self.array[position] + 1 <= 9:
                new_array[position] = self.array[position] + 1
                position -= 1
                while position > -1:
                    new_array[position] = self.array[position]
                    position -= 1
            else:
                if self.highest_position - i < 0:
                    new_array.insert(0, 1)
                    new_highest_position += 1
                else:
                    new_array[position] = self.array[position] // 10
                    i += 1
        return NaturalNumber(new_highest_position, new_array)

    def add(self, number: Self) -> Self:
        # N-4
        pass

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
        """
        module: MUL_ND_N
        author: Starodubtsev Maxim

        arguments:
            digit: one digit to multiply with number

        this method multiplies a number by a digit
        """
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
        """
               module: DIV_NN_Dk
               author: Teryokhina Sofya

               arguments:
                   number: an instance of the class NaturalNumber

               This method returns the first digit of division of one NaturalNumber and a smaller NaturalNumber
        """
        new_array = self.array
        new_highest_position = self.highest_position
        new_number = NaturalNumber(new_hp, new_ar)
        result = 0
        degree = new_highest_position - number.highest_position
        while degree >= 0:
            number1 = number.multiply_by_powered_ten(k)
            if new_number.compare(number1) != 1:
                while new_number.compare(number1) != 1:
                    result += 1
                    new_number.subtract(number1)
                degree = -1
            else:
                degree -= 1
        result_highest_position = 1
        result_array = [1]
        result_array[0] = result
        return NaturalNumber(result_highest_position, result_array)

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

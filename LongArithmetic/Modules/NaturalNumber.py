from typing_extensions import Self
from copy import deepcopy
from unittest import result

class NaturalNumber:
    def __init__(self, highest_position: int, array: list):
        self.highest_position = highest_position
        self.array = array


    @staticmethod
    def str_to_num(string):
        return NaturalNumber(len(string), list(map(int, string)))


    def compare(self, number: Self) -> int:
        """
        module: COM_NN_D
        author: Krivenko Vlada

        arguments:
            number: an instance of the class NaturalNumber

        This method compares natural numbers: 2 - if the first is greater than the second, 0 if equal, 1 otherwise.
        """
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
        """
        module: NZER_N_B
        author: Krivenko Vlada
 
        arguments:
 
        This method checks a number for zero: if the number is not zero, then "yes" otherwise "no"
        """
        if any(self.array):
            return False
        else:
            return True

    def add_one(self) -> Self:
        """
        module: SUB_NDN_N
        author: Kirill Smirnov
        This method adds to the number 1
        """
        i = 1
        new_highest_position = self.highest_position
        new_array = [0] * self.highest_position
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
        """
        module: ADD_NN_N
        author: Krivenko Vlada

        arguments:
            number: an instance of the class NaturalNumber

        This method add natural numbers.
        """
        comparison = self.compare(number)
 
        a = self.array
        b = number.array
        a1 = self.highest_position
        a2 = number.highest_position
 
        if comparison == 1:
            a, b = b, a
            a1, a2 = a2, a1
        new_arr = [0] * a1
        if a1 > a2:
            while a1 - a2 != 0:
                b.insert(0, 0)
                a2 += 1
        i = a1 - 1
        g = 0
        while i >= 0:
            if a[i] + b[i] + g > 9 and i == 0:
                new_arr[i] = a[i] + b[i] - 10 + g
                new_arr.insert(0, 1)
            elif a[i] + b[i] + g > 9:
                new_arr[i] = a[i] + b[i] - 10 + g
                new_arr[i - 1] += 1
                g = 1
            else:
                new_arr[i] = a[i] + b[i] + g
                g = 0
            i -= 1
 
        return NaturalNumber(len(new_arr), new_arr)

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
        if self.highest_position > number.highest_position:
            while self.highest_position - number.highest_position != 0:
                number.array.insert(0, 0)
                number.highest_position += 1
        while posittion >= 0:
            if self.array[posittion] - number.array[posittion] >= 0:
                new_array[posittion] = self.array[posittion] - number.array[posittion]
            else:
                temporary_position = posittion - 1
                while new_array[temporary_position] == 0:
                    temporary_position -= 1
                new_array[temporary_position] -= 1
                temporary_position += 1
                while temporary_position < posittion:
                    new_array[temporary_position] += 9
                    temporary_position += 1
                new_array[temporary_position] += 10
                new_array[posittion] = self.array[posittion] - number.array[posittion]
            posittion -= 1
        posittion += 1
        if comp == 1:
            t = self
            self = number
            number = t
        # while posittion < self.highest_position - 1 and new_array[0] == 0:
        #     new_array.pop(0)
        #     posittion += 1
        for i in range(0, len(new_array)):
            if new_array[i] != 0:
                new_array = new_array[i:]
                break
        if not any(new_array): new_array = [0]

        return NaturalNumber(len(new_array), new_array)

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
        res.highest_position = len(res.array)

        return res

    def multiply_by_powered_ten(self, digit: int) -> Self:
        """
        module: MUL_Nk_N
        author: Trunov Egor
        arguments:
            digit: one digit to multiply with number
        This method multiply self number by powered ten digit
        """
        return NaturalNumber(self.highest_position + digit, self.array + [0] * digit)
        
        
    def multiply(self, number: Self) -> Self:
        """
        module: MUL_NN_N
        author: Starodubtsev Maxim
        arguments:
            number: an instance of the class NaturalNumber
        This method multiplies two natural numbers
        """
        if self.array == [0] or number.array == [0]:
            return NaturalNumber(1, [0])
        res = NaturalNumber(1, [0])
        num = NaturalNumber(1, [1])
        k = 0
        for i in reversed(range(self.highest_position)):
            num = number.multiply_digit(self.array[i])
            num = num.multiply_by_powered_ten(k)
            k = k + 1
            res = res.add(num)
        res.highest_position = len(res.array)
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

    def first_division_digit(self, number: Self) -> Self:
        """first_division_digit
        module: DIV_NN_Dk
        author: Teryokhina Sofya
        arguments:
            number: an instance of the class NaturalNumber
        This method returns the first digit of division of one NaturalNumber and a smaller NaturalNumber
        """
        num = deepcopy(self)
        new_number = NaturalNumber(num.highest_position, num.array)
        result = 0
        degree = num.highest_position
        while degree >= 0:
            number1 = number.multiply_by_powered_ten(degree)
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
        dividend = deepcopy(self)
        divider = deepcopy(number)
        initial_length1 = dividend.highest_position
        result = NaturalNumber(0, [])
        difference = dividend.highest_position - divider.highest_position + 1
        while difference > 0:
            difference -= 1
            if dividend.array[0] == 0:
                result.highest_position += 1
                result.array.append(0)
            else:
                current_divider = divider.multiply_by_powered_ten(difference)
                digit = (dividend.first_division_digit(current_divider)).array[0]
                result.highest_position += 1
                result.array.append(digit)
                dividend = dividend.subtract_k_by_number(current_divider, digit)
            if dividend.highest_position < initial_length1 - 1 and dividend.highest_position > 0:
                while dividend.highest_position < initial_length1 - 1 and difference > 0:
                    initial_length1 = initial_length1 - 1
                    result.array.append(0)
                    difference = difference - 1
            initial_length1 = initial_length1 - 1
        if result.array[0] == 0:
            result.array = result.array[1:]
            result.highest_position -= 1
        result.highest_position = len(result.array)
        return result

    def remainder(self, number: Self) -> Self:
        """
        module: MOD_NN_N
        author: Trunov Egor
        arguments:
            number: an instance of the class NaturalNumber
        This method calculate
        """
        quotient = self.quotient(number)
        num = number.multiply(quotient)
        return self.subtract(num)

    def gcd(self, number: Self) -> Self:
        """
        module: GCF_NN_N
        author: Dolganov Ivan
        arguments:
            number: an instance of the class NaturalNumber
        This method finds the greatest common divisor of numbers
        """
        self_copy = deepcopy(self)
        number_copy = deepcopy(number)
        print(self_copy.multiply(number_copy))
        while not (self_copy.multiply(number_copy).is_zero()):
            if self_copy.compare(number_copy) == 2:
                self_copy = self_copy.remainder(number_copy)
            else:
                number_copy = number_copy.remainder(self_copy)
        return self_copy.add(number_copy)

    def lcm(self, number: Self) -> Self:
        """
        module: LCM_NN_N
        author: Zhulanov Aleksandr
    
        arguments:
        number: an instance of the class NaturalNumber
 
        This method passes lcm of the natural numbers
        """
        self_copy = deepcopy(self)
        number_copy = deepcopy(number)

        #  NOK:=( x div NOD(x,y) ) * y;
        gcd = self_copy.gcd(number_copy)
        div = self.quotient(gcd)
        result = div.multiply(number_copy)
        return result





        # if self.compare(number) != 0:
        #     nok = NaturalNumber(1, [0])
        #     if self.compare(number) == 1:
        #         mult = number.multiply(self)
        #     else:
        #         mult = self.multiply(number)
        #     nod = self.gcd(number)

        #     while mult.is_zero() == False:

        #         mult = mult.subtract(nod)
        #         if nod.array[0] == 0 and nod.highest_position != mult.highest_position:
        #             nod_len = 0
        #             while nod.array[nod_len] == 0:
        #                 nod_len += 1
        #             nod_itog = NaturalNumber(nod.highest_position - nod_len, [])
        #             for i in range(nod_len, nod.highest_position):
        #                 nod_itog.array.append(nod.array[i])
        #             nod = nod_itog
        #         nok = nok.add_one()
        #     return nok
        # else:
        #     return self

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position)

    def __str__(self) -> str:
        return ''.join(map(str, self.array))
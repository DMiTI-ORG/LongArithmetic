from typing_extensions import Self
from copy import deepcopy

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
        if self.highest_position == 1:
            if self.array[0] == 0:
                return True
            else:
                return False
        else:
            return False

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
            print(self.highest_position, self.array, '|', number.highest_position, number.array)
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

        print('>>>>', len(new_array), new_array)
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
        res = NaturalNumber(1, [0])
        num = NaturalNumber(1, [1])
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
        if result.array[0] == 0:
            result.array = result.array[1:]
            result.highest_position -= 1
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
        """
        module: GCF_NN_N
        author: Dolganov Ivan
        arguments:
            number: an instance of the class NaturalNumber
        This method finds the greatest common divisor of numbers
 
        """
        if self.is_zero() == False and number.is_zero() == True: return number
        if self.is_zero() == True and number.is_zero() == False: return self
        if self.is_zero() == True and number.is_zero() == True: return NaturalNumber(1,[0])
        if self.compare(number)==0: return self
        self_copy = deepcopy(self)
        number_copy = deepcopy(number)
        while self_copy.is_zero() == False and number_copy.is_zero() == False:
            if (self_copy.compare(number_copy) == 2):
                self_copy = self_copy.remainder(number_copy)
            elif (self_copy.compare(number_copy) == 1):
                number_copy = number_copy.remainder(self_copy)
        if number_copy.is_zero() == True: return self_copy
        if self_copy.is_zero() == True: return number_copy

        
    def lcm(self, number: Self) -> Self:
        """
        module: LCM_NN_N
        author: Zhulanov Aleksandr
 
        arguments:
        number: an instance of the class NaturalNumber
 
        This method passes lcm of the natural numbers
        """
        mult = self.multiply(number)
        nod = self.gcd(number)
        nok = 0
        new_number = 0
        mult_number = ''
        nod_number = ''
        result = NaturalNumber(0, [])
        for i in range(mult.highest_position):
            mult_number += str(mult.array[i])
        for i in range(nod.highest_position):
            nod_number += str(nod.array[i])
        mult_number = int(mult_number)
        nod_number = int(nod_number)
        if mult_number > 0 and nod_number != 0:
            while new_number < mult_number:
                new_number += nod_number
                nok += 1
            result = NaturalNumber(len(str(nok)), list(str(nok)))
            for i in range(len(str(nok))):
                result.array[i] = int(result.array[i])
            return result
        else:
            return 'Error'

    def __eq__(self, other: Self) -> bool:
        return (self.array == other.array) and (self.highest_position == other.highest_position)

    def __str__(self) -> str:
        return ''.join(map(str, self.array))
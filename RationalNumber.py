from NaturalNumber import NaturalNumber
from WholeNumber import WholeNumber
from typing_extensions import Self

class RationalNumber:
    def __init__(self, numerator :tuple, denominator :tuple):
        self.numerator = WholeNumber(*numerator)
        self.denominator = NaturalNumber(*denominator)


    def reduce(self) -> Self:
        # Q-1
        pass


    def is_whole(self) -> bool:
        # Q-2
        pass


    def whole_to_rational(self) -> Self:
        # Q-3
        pass


    def to_whole(self) -> WholeNumber:
        # Q-4
        pass


    def add(self, number: Self) -> Self:
        # Q-5
        pass


    def subtract(self, number: Self) -> Self:
        #  находим общий знаменатель
        common_denominator = self.denominator.lcm(number.denominator)
        #  находим новый числитель первой дроби
        new_numerator1 = self.numerator.multiply(common_denominator.quotient(self.denominator))
        #  находим новый числитель второй дроби
        new_numerator2 = number.numerator.multiply(common_denominator.quotient(number.denominator))
        #  находим общий числитель, вычитая два полученных
        result_numerator = new_numerator2.subtract(new_numerator2)
        # получаем результат
        result_rational = RationalNumber((result_numerator.sign,
                                          result_numerator.highest_position,
                                          result_numerator.array),
                                         (common_denominator.highest_position,
                                          common_denominator.array))
        # сокращаем его и выводим
        result_rational.reduce()
        return result_rational


    def multiply(self, number: Self) -> Self:
        # Q-7
        pass


    def divide(self, number: Self) -> Self:
        # Q-8
        pass

    
    def __eq__(self, other: Self) -> bool:
        return self.numerator == other.numerator


    def __str__(self) -> str:
        line = f'\n{"-" * max(self.numerator.highest_position, self.denominator.highest_position)}\n'
        return str(self.numerator) + line + str(self.denominator)
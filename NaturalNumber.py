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
        pass


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


    def __str__(self) -> str:
        return ''.join(map(str, self.array))
from Natural_number import Natural_number
from Integer_number import Integer_number


class Rational_number:
    def __init__(self, numerator :tuple, denominator :tuple):
        self.numerator = Integer_number(*numerator)
        self.denomenator = Natural_number(*denominator)

    
    def __str__(self) -> str:
        return str(self.numerator) + f'\n{"-" * max(self.numerator.highest_position, self.denomenator.highest_position)}\n' + str(self.denomenator)
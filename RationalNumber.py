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
        """
        module: INT_Q_B
        author: Chadina Alena

        arguments: absent
        This method check the fraction for whole
        """

        if self.denominator.highest_position==1 and self.denominator.array[0]==0:
            return ArithmeticError
        else:
            numerator=self.numerator
            i=0; flag=0
            if numerator.highest_position==1 and numerator.array[0]==0:
                result=True; flag=1
            elif numerator.highest_position<self.denominator.highest_position:
                flag=1; result=False
            while (flag==0):
                for i in range(numerator.highest_position-self.denominator.highest_position, numerator.highest_position):#number subtraction
                    numerator.array[i]-=self.denominator.array[i-(numerator.highest_position-self.denominator.highest_position)]
                for i in range(numerator.highest_position-1, 0, -1):
                    if numerator.array[i]<0:
                        numerator.array[i]+=10
                        numerator.array[i-1]-=1
                check=0
                for i in range(numerator.highest_position):#number check
                    if numerator.array[i]==0:
                        check+=1
                    if numerator.array[i]<0:
                        flag=1
                        result=False
                if check==numerator.highest_position:#all digits zero
                    flag=1
                    result=True
            return result


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
        # Q-6
        pass


    def multiply(self, number: Self) -> Self:
        # Q-7
        pass


    def divide(self, number: Self) -> Self:
        """
        module DIV_QQ_Q
        author: Chadina Alena

        arguments:
            number: an instance of the class RationalNumber

        This method divide self number on another number
        """
        result=RationalNumber((0, 0, []),(0, []))
        result.numerator=WholeNumber((self.numerator.sign+number.numerator.sign)%2, 0, [])
        result.denominator=NaturalNumber(0, [])
        denominator_1=WholeNumber(0, self.denominator.highest_position, self.denominator.array)
        denominator_2=WholeNumber(0, number.denominator.highest_position, number.denominator.array)
        new_numerator=WholeNumber.multiply(self.numerator, denominator_2)
        new_denominator=WholeNumber.multiply(denominator_1, number.numerator)
        result.numerator.highest_position=new_numerator.highest_position
        result.numerator.array=new_numerator.array
        result.denominator.highest_position=new_denominator.highest_position
        result.denominator.array=new_denominator.array
        return result
    
    def __eq__(self, other: Self) -> bool:
        return self.numerator == other.numerator


    def __str__(self) -> str:
        line = f'\n{"-" * max(self.numerator.highest_position, self.denominator.highest_position)}\n'
        return str(self.numerator) + line + str(self.denominator)

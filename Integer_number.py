class Integer_number:
    def __init__(self, sign :int, highest_position: int, array: list):
        self.sign = sign
        self.highest_position = highest_position
        self.array = array


    def __str__(self) -> str:
        return ('-' if self.sign else '') + ''.join(map(str, self.array))
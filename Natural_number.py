class Natural_number:
    def __init__(self, highest_position: int, array: list):
        self.highest_position = highest_position
        self.array = array


    def __str__(self) -> str:
        return ''.join(map(str, self.array))
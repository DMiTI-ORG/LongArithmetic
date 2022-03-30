class Polynomial:
    def __init__(self, highest_degree :int, array :list):
        self.highest_degree = highest_degree
        self.array = array

    
    def __str__(self):
        string = ''
        for i in range(self.highest_degree):
            string += '{:+}'.format(self.array[i]) + 'x^' + f'{self.highest_degree - i}'
        string += '{:+}'.format(self.array[-1])
        return string
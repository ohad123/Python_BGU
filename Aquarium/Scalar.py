import Fish

SCALAR_WIDTH = 8
SCALAR_HEIGHT = 5


class Scalar(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.x = x
        self.y = y
        self.width = SCALAR_WIDTH
        self.height = SCALAR_HEIGHT

    def get_animal(self):
        scalare = []
        first_line = ['*', '*', '*', '*', '*', " ", " ", " "]
        second_line = [" ", " ", " ", " ", '*', '*', '*', " "]
        middle_line = [" ", " ", '*', '*', '*', '*', '*', '*']
        if self.directionH == 0:
            first_line = first_line [::-1]
            second_line = second_line[::-1]
            middle_line = middle_line[::-1]
        scalare.append(first_line)
        scalare.append(second_line)
        scalare.append(middle_line)
        scalare.append(second_line)
        scalare.append(first_line)
        return scalare

import Crab

SHRIMP_WIDTH = 7
SHRIMP_HEIGHT = 3


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = SHRIMP_WIDTH
        self.height = SHRIMP_HEIGHT

    def get_animal(self):
        shrimp = []
        head_lst = ['*', " ", '*', ' ', ' ', ' ', ' ']
        middle_lst = [" ", '*', '*', '*', '*', '*', '*']
        bottom_lst = [' ', ' ', '*', ' ', '*', ' ', ' ']
        if self.directionH == 1:
            head_lst = head_lst[::-1]
            middle_lst = middle_lst[::-1]
            bottom_lst = bottom_lst[::-1]
        shrimp.append(head_lst)
        shrimp.append(middle_lst)
        shrimp.append(bottom_lst)
        return shrimp

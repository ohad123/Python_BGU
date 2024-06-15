import Fish

MOLY_WIDTH = 8
MOLY_HIEGHT = 3


class Moly(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.x = x
        self.y = y
        self.width = MOLY_WIDTH
        self.height = MOLY_HIEGHT
        self.directionV = directionV  # random 0 - down / 1 - up

    def get_animal(self):
        moly = []
        middle_list = ['*'] * self.width
        row1_or3_list = [' ', '*', '*', '*', ' ', ' ', ' ', '*']
        if self.directionH == 1:
            middle_list = middle_list[::-1]
            row1_or3_list = row1_or3_list[::-1]
        moly.append(row1_or3_list)
        moly.append(middle_list)
        moly.append(row1_or3_list)
        return moly

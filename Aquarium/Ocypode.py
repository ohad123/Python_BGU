import Crab

OCYPODE_WIDTH = 7
OCYPODE_HIEGHT = 4


class Ocypode(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = OCYPODE_WIDTH
        self.height = OCYPODE_HIEGHT

    def get_animal(self):
        ocypode = []
        head_list = [' ', '*', ' ', ' ', ' ', '*', ' ']
        line2 = [' ', ' ', '*', '*', '*', ' ', ' ']
        full_line = ['*'] * 7
        legs_lst = ['*', ' ', ' ', ' ', ' ', ' ', '*']
        ocypode.append(head_list)
        ocypode.append(line2)
        ocypode.append(full_line)
        ocypode.append(legs_lst)
        return ocypode

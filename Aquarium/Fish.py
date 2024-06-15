import Animal

MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8


class Fish(Animal.Animal):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH)
        self.width = MAX_FISH_WIDTH
        self.height = MAX_FISH_HEIGHT
        self.directionV = directionV  # random 0 - down / 1 - up

    def __str__(self):
        st = "The fish " + str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        return st

    def up(self):   # update the coordinate for animal position after one step up
        self.y -= 1

    def down(self):   # update the coordinate for animal position after one step up
        self.y += 1

    def starvation(self):   # print a message that the fish die due to luck of food
        print("The fish " + str(self.name) + " died at the age of " + str(self.age) + " years Because he ran out of food!")

    def die(self):  # print a message that the fish die because it reaches the age of 120
        print(str(self.name) + "died in good health")

    def get_directionV(self):
        return self.directionV

    def set_directionV(self, directionV):
        self.directionV = directionV

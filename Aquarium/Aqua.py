import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = []
        self.build_tank()
        self.anim = []

    def build_tank(self):
        #   build all the rows
        for row_number in range(self.aqua_height - 1):
            if row_number == 2:
                self.board.append(["|"] + ["~" for space in range(self.aqua_width - 2)] + ["|"])
            else:
                self.board.append(["|"] + [" " for space in range(self.aqua_width - 2)] + ["|"])
        self.board.append(["\\"] + ["_" for space in range(self.aqua_width - 2)] + ["/"])

    def print_board(self):  # print the aquarium
        for animal in self.anim:
            self.print_animal_on_board(animal)
        for row_number in range(self.aqua_height):
            print()
            for column_number in range(self.aqua_width):
                print(self.board[row_number][column_number], end=" ")
        print()

    def get_board(self):
        return self.board

    def get_all_animal(self):
        """
        Returns the array that contains all the animals
        """
        return self.anim

    def is_collision(self, animal):
        """
        Returns True if the next step of the crab is a collision
        """
        flag = False
        x, y = animal.get_position()
        width, height = animal.get_size()
        if animal.get_directionH() == 1:
            # collision from right
            for row_index in range(MAX_CRAB_HEIGHT):
                if self.board[row_index + y][x + width] == "*":
                    flag = True
                if self.board[row_index + y][x + width: x + width + 2] == [" ", "*"]:
                    flag = True
        else:
            # collision from left
            for row_index in range(MAX_CRAB_HEIGHT):
                if self.board[row_index + y][x - 1] == "*":
                    flag = True
                if self.board[row_index + y][x - 2: x] == ["*", " "]:
                    flag = True

        return flag

    def print_animal_on_board(self, animal: Animal):
        # Update the board with the new animal
        x, y = animal.get_position()
        my_animal = animal.get_animal()
        for row_index in range(len(my_animal)):
            for col_index in range(len(my_animal[row_index])):
                self.board[row_index + y][x + col_index] = my_animal[row_index][col_index]

    def delete_animal_from_board(self, animal: Animal):
        # Remove an animal from the board
        x, y = animal.get_position()
        my_animal = animal.get_animal()
        for row_index in range(len(my_animal)):
            for col_index in range(len(my_animal[row_index])):
                self.board[row_index + y][x + col_index] = " "

    def fixing_location(self, animal: Animal, animaltype):
        #   When add animal fix the inserted coordinates to a legal location
        while animal.x + animal.width >= self.aqua_width:
            animal.set_x(animal.x - 1)
        if animaltype == 'sc' or animaltype == 'mo':
            while animal.y + animal.height >= self.aqua_height - MAX_CRAB_HEIGHT:
                animal.set_y(animal.y - 1)

    def check_coordinates(self, animal: Animal, animaltype):
        #   Check if the coordinates is legal and fix it or request a new coordinates
        self.fixing_location(animal, animaltype)
        while not self.check_if_free(animal.x, animal.y):
            print("The place is not available! Please try again later.")
            flag = True
            while flag:
                try:
                    x = float(input("Please enter an X axis location (1 - %d):" % (self.aqua_width - 1)))
                    if x % 1 == 0:
                        x = int(x)
                        flag = False
                    else:
                        continue
                except ValueError or TypeError:
                    continue
            animal.set_x(x)

            if animaltype == 'sc' or animaltype == 'mo':
                flag = True
                while flag:
                    try:
                        y = float(input("Please enter an Y axis location (%d - %d):" % (WATERLINE, self.aqua_height - 1)))
                        if y % 1 == 0:
                            y = int(y)
                            flag = False
                        else:
                            continue
                    except ValueError or TypeError:
                        continue
                animal.set_y(y)
            self.fixing_location(animal, animaltype)

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        """
        Adding fish to the aquarium
        """
        if fishtype == 'sc':
            new_scalar = Scalar.Scalar(name, age, x, y, directionH, directionV)
            self.check_coordinates(new_scalar, fishtype)
            self.anim.append(new_scalar)
            self.print_animal_on_board(new_scalar)
        else:
            new_moly = Moly.Moly(name, age, x, y, directionH, directionV)
            self.check_coordinates(new_moly, fishtype)
            self.anim.append(new_moly)
            self.print_animal_on_board(new_moly)
        return True

    def add_crab(self, name, age, x, y, directionH, crabtype):
        """
        Adding crab to the aquarium
        """
        if crabtype == 'oc':
            new_ocypode = Ocypode.Ocypode(name, age, x, y - 5, directionH)
            self.check_coordinates(new_ocypode, crabtype)
            self.anim.append(new_ocypode)
            self.print_animal_on_board(new_ocypode)
        else:
            new_shrimp = Shrimp.Shrimp(name, age, x, y - 4, directionH)
            self.check_coordinates(new_shrimp, crabtype)
            self.anim.append(new_shrimp)
            self.print_animal_on_board(new_shrimp)
        return True

    def check_if_free(self, x, y) -> bool:
        """
        method for checking whether the position is empty before inserting a new animal
        """
        flag = True
        try:
            for row_index in range(MAX_ANIMAL_HEIGHT):
                for col_index in range(MAX_ANIMAL_WIDTH):
                    if self.board[y + row_index][col_index + x] == "*":
                        flag = False
                        break
                    if self.board[y + row_index][col_index + x] == "|":
                        break
                if not flag:
                    break
        except IndexError:
            flag = True
        return flag

    def left(self, animal: Animal):
        # Move the animal one step left
        self.delete_animal_from_board(animal)
        animal.left()
        self.print_animal_on_board(animal)

    def right(self, animal: Animal):
        # Move the animal one step right
        self.delete_animal_from_board(animal)
        animal.right()
        self.print_animal_on_board(animal)

    def up(self, animal: Animal):
        # Move the animal one step up
        self.delete_animal_from_board(animal)
        animal.up()
        self.print_animal_on_board(animal)

    def down(self, animal: Animal):
        # Move the animal one step down
        self.delete_animal_from_board(animal)
        animal.down()
        self.print_animal_on_board(animal)

    def change_direction(self, animal: Animal):
        """
        The method change the direction when collision with borders and print the animal in the correct direction
        """
        if animal.get_directionH() == 1:
            animal.set_directionH(0)
            self.delete_animal_from_board(animal)
            self.print_animal_on_board(animal)
        else:
            animal.set_directionH(1)
            self.delete_animal_from_board(animal)
            self.print_animal_on_board(animal)

    def collision_with_borders(self, animal: Animal):
        """
        The method check if animal collision with borders and return true or false
        """
        x, y = animal.get_position()
        if animal.get_directionH() == 1:
            if self.board[y][x + animal.width] == "|":
                return True
        else:
            if self.board[y][x - 1] == "|":
                return True
        return False

    def all_crabs_collision(self):
        flag = True
        while flag:
            # only for crabs collision
            count_of_collision = 0
            list_crabs_that_col_border = []
            lst_crabs_collision = []
            for animal in self.anim:
                if isinstance(animal, Crab.Crab):
                    if self.is_collision(animal):
                        count_of_collision += 1
                        lst_crabs_collision.append(animal)
                    if self.collision_with_borders(animal):
                        list_crabs_that_col_border.append(animal)
                        self.change_direction(animal)

            for crabs in lst_crabs_collision:
                self.change_direction(crabs)

            if count_of_collision == 0:
                for animal in self.anim:
                    if isinstance(animal, Crab.Crab):
                        if self.collision_with_borders(animal):
                            list_crabs_that_col_border.append(animal)
                        if animal in list_crabs_that_col_border:
                            continue
                        if animal in lst_crabs_collision:
                            continue
                        else:
                            self.move_to_correct_side(animal)
                flag = False
        return flag

    def next_turn(self):
        """
        Managing a single step
        """
        for animal in self.anim:
            if animal.age == 120:
                animal.die()
                self.delete_animal_from_board(animal)
                self.anim.remove(animal)
            if animal.food == 0:
                animal.starvation()
                self.delete_animal_from_board(animal)
                self.anim.remove(animal)

        self.all_crabs_collision()
        for animal in self.anim:
            if isinstance(animal, Fish.Fish):
                if self.collision_with_borders(animal):
                    #   only for axis x
                    self.change_direction(animal)
                else:
                    self.move_to_correct_side(animal)
                # Take a step forward in axis y or change direction only for fish
                width, height = animal.get_size()
                x, y = animal.get_position()
                if animal.get_directionV() == 1 and y > WATERLINE:
                    self.up(animal)
                if y + height == self.aqua_height - MAX_CRAB_HEIGHT - 1:
                    animal.set_directionV(1)
                if animal.get_directionV() == 0 and y + height < self.aqua_height - MAX_CRAB_HEIGHT - 1:
                    self.down(animal)
                if y == WATERLINE:
                    animal.set_directionV(0)

        for animal in self.anim:
            #   Reduce amount of food and promote the age of the animal
            if self.turn == 0:
                animal.dec_food()
                animal.inc_age()
            if self.turn % 10 == 0:
                animal.dec_food()
            if self.turn % 100 == 0:
                animal.inc_age()
        self.turn += 1

    def move_to_correct_side(self, animal: Animal):
        if animal.get_directionH() == 1:
            self.right(animal)
        else:
            self.left(animal)

    def print_all(self):
        """
        Prints all the animals in the aquarium
        """
        for animal in self.anim:
            print(animal.__str__())

    def feed_all(self):
        """
        feed all the animals in the aquarium
        """
        for animal in self.anim:
            animal.food += FEED_AMOUNT

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
            return self.add_crab(name, age, x, y, directionH, animaltype)
        else:
            return False

    def several_steps(self) -> None:
        """
        Managing several steps
        """
        flag = True
        while flag:
            try:
                step = float(input("How many steps do you want to take?"))
                if step % 1 == 0:
                    step = int(step)
                    for turns in range(step):
                        self.next_turn()
                    flag = False
                else:
                    continue
            except ValueError or TypeError:
                continue

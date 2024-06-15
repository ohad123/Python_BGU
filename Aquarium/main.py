import time
import Aqua

WATERLINE = 3
SHRIMP_HEIGHT = 3
OCYPODE_HIEGHT = 4


def demo(myaqua):
    """
    Running a demo aquarium
    for example:
    """
    myaqua.add_animal("scalarfish1", 4, 10, 10, 1, 0, 'sc')
    myaqua.add_animal("molyfish2", 12, 35, 15, 0, 1, 'mo')
    myaqua.add_animal("shrimpcrab1", 3, 20, myaqua.aqua_height, 1, 0, 'sh')
    myaqua.add_animal("ocypodecrab2", 13, 41, myaqua.aqua_height, 0, 0, 'oc')

    myaqua.feed_all()
    for i in range(120):
        myaqua.next_turn()
        time.sleep(0.5)
        myaqua.print_board()


def add_animal(myaqua):
    choice = 0
    while not 1 <= choice <= 4:
        print("Please select:")
        print("1. Scalare")
        print("2. Moly")
        print("3. Ocypode")
        print("4. Shrimp")

        flag = True
        while flag:
            try:
                choice = int(input("What animal do you want to put in the aquarium?"))
                flag = False
            except ValueError or TypeError:
                continue

    name = input("Please enter a name:")
    age = 0
    while not 1 <= age <= 100:
        flag = True
        while flag:
            try:
                age = float(input("Please enter age:"))
                if age % 1 == 0:
                    age = int(age)
                    flag = False
                else:
                    continue
            except ValueError or TypeError:
                continue

    success = False
    while not success:
        x, y = 0, 1
        while not 1 <= x <= (myaqua.aqua_width - 1):
            flag = True
            while flag:
                try:
                    x = float(input("Please enter an X axis location (1 - %d):" % (myaqua.aqua_width - 1)))
                    if x % 1 == 0:
                        x = int(x)
                        flag = False
                    else:
                        continue
                except ValueError or TypeError:
                    continue

        if choice == 1 or choice == 2:
            while not WATERLINE <= y <= (myaqua.aqua_height - 1):
                flag = True
                while flag:
                    try:
                        y = float(input("Please enter an Y axis location (%d - %d):" % (WATERLINE, myaqua.aqua_height - 1)))
                        if y % 1 == 0:
                            y = int(y)
                            flag = False
                        else:
                            continue
                    except ValueError or TypeError:
                        continue

        directionH, directionV = -1, -1
        while not (directionH == 0 or directionH == 1):
            flag = True
            while flag:
                try:
                    directionH = float(input("Please enter horizontal direction (0 for Left, 1 for Right):"))
                    if directionH % 1 == 0:
                        directionH = int(directionH)
                        flag = False
                    else:
                        continue
                except ValueError or TypeError:
                    continue

        if choice == 1 or choice == 2:
            while not (directionV == 0 or directionV == 1):
                flag = True
                while flag:
                    try:
                        directionV = float(input("Please enter vertical direction  (0 for Down, 1 for Up):"))
                        if directionV % 1 == 0:
                            directionV = int(directionV)
                            flag = False
                        else:
                            continue
                    except ValueError or TypeError:
                        continue

        if choice == 1:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'sc')
        elif choice == 2:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'mo')
        elif choice == 3:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height, directionH, 0, 'oc')
        else:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height, directionH, 0, 'sh')
    return None


if __name__ == '__main__':
    width = 0
    height = 0

    print('Welcome to "The OOP Aquarium"')
    while width < 40:  # Minimum of aquarium width
        flag = True
        while flag:
            try:
                width = float(input("The width of the aquarium (Minimum 40): "))
                if width % 1 == 0:
                    width = int(width)
                    flag = False
                else:
                    continue
            except ValueError or TypeError:
                continue

    while height < 25:  # Minimum of aquarium height
        flag = True
        while flag:
            try:
                height = float(input("The height of the aquarium (Minimum 25): "))
                if height % 1 == 0:
                    height = int(height)
                    flag = False
                else:
                    continue
            except ValueError or TypeError:
                continue
    myaqua = Aqua.Aqua(width, height)

    while True:
        choice = 0
        while not 1 <= choice <= 7:
            print("Main menu")
            print("-" * 30)
            print("1. Add an animal")
            print("2. Drop food into the aquarium")
            print("3. Take a step forward")
            print("4. Take several steps")
            print("5. Demo")
            print("6. Print all")
            print("7. Exit")

            flag = True
            while flag:
                try:
                    choice = int(input("What do you want to do?"))
                    flag = False
                except ValueError or TypeError:
                    continue

        if choice == 1:
            add_animal(myaqua)
        elif choice == 2:
            myaqua.feed_all()
        elif choice == 3:
            myaqua.next_turn()
        elif choice == 4:
            myaqua.several_steps()
        elif choice == 5:
            demo(myaqua)
        elif choice == 6:
            myaqua.print_all()
        else:
            print("Bye bye")
            exit()

        myaqua.print_board()

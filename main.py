#!/usr/bin/python3
import functions
import os


# DEBUG
debug = 0

# init variables
end_while = 0
number_of_shots = 0
i = 0
j = 0

battlefield = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]

ship_position = functions.place_ship()

# instructions
print("Hello to BATTLESHIPS v1.0")
print("Simple game made in Python")
print("Game is released under GNU General Public License")
print("*** Instructions ***")
print("   1. There is one ship hidden on battlefield.")
print("   2. Ships is randomly placed horizontally or vertically")
print("   3. Ship have 3 pieces")
print("   4. Enjoy :)")
print("********************")

# main game loop
while True:
    input("Press Enter to continue...")
    os.system('cls||clear')

    if debug == 1: print(ship_position)  # DEBUG

    print("***BATTLE SITUATION MONITOR V 1.0***")
    functions.print_battlefield(battlefield)
    print("************************************")

    while True:
        try:
            j = int(input("Please give me X coordinate to attack: "))
        except ValueError:
            print("Sorry, you must give me coordinate number from 0 to 4")
            continue
        else:
            if j > 4 or j < 0:
                print("Sorry, you must give me coordinate number from 0 to 4")
                continue
            else:
                break

    while True:
        try:
            i = int(input("Please give me Y coordinate to attack: "))
        except ValueError:
            print("Sorry, you must give me coordinate number from 0 to 4")
            continue
        else:
            if i > 4 or i < 0:
                print("Sorry, you must give me coordinate number from 0 to 4")
                continue
            else:
                break

    functions.shot(int(i), int(j), battlefield, ship_position)
    number_of_shots += 1


    if functions.check_win_conditions(battlefield, ship_position) == 1:
        functions.print_battlefield(battlefield)
        print("Congratulations, you have sinked the ship :)")
        print("You have done it in "+str(number_of_shots)+" shots!")
        print("Game restarts")
        number_of_shots = 0
        ship_position = functions.place_ship()
        battlefield = [[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]]

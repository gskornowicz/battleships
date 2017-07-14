import random

random.seed()


###########
# place_ship()
# desc: places ship in random position on battlefield
# return: 3 co-ordinates in list [[i,j],[i,j],[i,j]]
# where i is verse and j is colums
###########

def place_ship():
    bool_value = random.randint(0, 1)  # randomize vertical or horizontal aligment

    if bool_value == 0:  # if 0 then place ship vertically
        i = random.randint(0, 2)
        j = random.randint(0, 4)
        ship_position = [[i, j],
                         [i + 1, j],
                         [i + 2, j]]

    else:  # if 1 then place ship horizontally
        i = random.randint(0, 4)
        j = random.randint(0, 2)
        ship_position = [[i, j],
                         [i, j + 1],
                         [i, j + 2]]
    return ship_position


###########
# shot(i,j, battlefield, ship_position)
# desc: using i and j int numbers from 0 to 4 checks if shot was succesfull,
#       missed or that co-ordinates were already attacked
# return:   0 - missed,
#           1 - hit,
#           2 - already attacked
###########

def shot(i, j, battlefield, ship_position):
    if battlefield[i][j] == 'X' or battlefield[i][j] == 1:
        print("Oh mate, you already tried to hit that place :(")
        return 2

    for cord in ship_position:
        if cord[0] == i:
            for cord in ship_position:
                if cord[1] == j:
                    battlefield[i][j] = 1
                    print("Congrats, you have hit the ship! :)")
                    return 1

    if battlefield[i][j] == 0:
        battlefield[i][j] = 'X'
        print("Oups, u missed :(")
        return 0


###########
# print_battlefield()
# desc: prints actual battlefield
###########

def print_battlefield(battlefield):
    i = 0
    print("  X 0 1 2 3 4")
    print("Y ___________")
    for item in battlefield:
        print(str(i) + " |", end='')
        i += 1
        for item2 in item:
            print(" " + str(item2), sep='', end='')
        print("\n", end='')
    print("\n")


###########
# check_win_conditions(battlefield, ship_position)
# desc: checks if player damaged whole ship,
#       uses actual battlefield state and ship position variable to determine
#       if whole ship have been destroyed
#
###########

def check_win_conditions(battlefield, ship_position):
    if (battlefield[ship_position[0][0]][ship_position[0][1]] and
            battlefield[ship_position[1][0]][ship_position[1][1]] and
                battlefield[ship_position[2][0]][ship_position[2][1]] == 1):
        return 1
    else:
        return 0

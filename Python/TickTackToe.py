import random

board = [" "]*9
winners = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7,], [2,5,8], [0,4,8], [2,4,6]]
xwin = 0
owin = 0
catwin = 0

userRecord = 0
compRecord = 0
catRecord = 0


def userPick():
    while True:
        loc = input("Pick a square (1-9): ")
        try:
            int(loc)
        except Exception:
            print("Invalid Input")
        else:
            loc = int(loc)
            if loc < 1 or loc > 9:
                print("Out of Range")
            elif board[loc-1] != ' ':
                print("This square is taken, try a different one")
            else:
                return loc-1


def randPick():
    while True:
        loc = random.randint(0,8)
        if board[loc] == ' ':
            return loc


def print_board():
    print(" %c | %c | %c " % (board[0], board[1], board[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[3], board[4], board[5]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[6], board[7], board[8]))
    print("   |   |   ")


def check_win():
    global xwin, owin

    for i in winners:
        xscore = 0
        oscore = 0
        for j in i:
            if board[j] == 'X':
                xscore += 1
            if board[j] == 'O':
                oscore += 1
        if xscore == 3:
            xwin = 1
        if oscore == 3:
            owin = 1


def check_cat():
    global catwin
    n = 0
    for i in board:
        if i != ' ':
            n += 1
    if n == 9:
        catwin = 1


def smartPick():
    for row in winners:
        oscore = 0
        for i in row:
            if board[i] == 'O':
                oscore += 1
        if oscore == 2:
            for loc in row:
                if board[loc] == ' ':
                    return loc

    for row in winners:
        xscore = 0
        for i in row:
            if board[i] == "X":
                xscore += 1
        if xscore == 2:
            for loc in row:
                if board[loc] == ' ':
                    return loc
    return randPick()


def gameReset():
    global board, xwin, owin, catwin

    board = [' ']*9
    xwin = 0
    owin = 0
    catwin = 0


while True:
    order = random.randint(0,2)

    if order != 1:
        print("User plays first")
        while xwin == 0 and owin == 0:
            print_board()

            board[userPick()] = 'X'
            check_win()
            if xwin == 1:
                break
            check_cat()
            if catwin == 1:
                break

            print("Computer move:")
            board[smartPick()] = 'O'
            check_win()
            if owin == 1:
                break
    else:
        print("Computer plays first")
        while xwin == 0 and owin == 0:
            board[smartPick()] = 'O'
            check_win()
            if owin == 1:
                break
            check_cat()
            if catwin == 1:
                break

            print_board()
            board[userPick()] = 'X'
            check_win()
            if xwin == 1:
                break

    print_board()
    print()
    if owin == 1:
        print("O has won")
        compRecord += 1
    elif xwin == 1:
        print("X has won")
        userRecord += 1
    else:
        print("The cat has won")
        catRecord += 1
    print("You are %s-%s-%s" % (userRecord, compRecord, catRecord))
    gameReset()

    replay = input("Type anything to play again or 'q' to quit: ")
    if replay.upper() == 'Q':
        quit()


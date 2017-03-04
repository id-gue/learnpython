'''Battelship exercise by codecademy
https://www.codecademy.com/courses/python-beginner-en-4XuFm/1/2?curriculum_id=4f89dab3d788890003000096'''

from random import randint

board = []

#build our ocean
for x in range(0,4):
    board.append(["O"] * 4)

def print_board(board):
    for row in board:
        print " ".join(row)

#find random position
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#save ship position
ship1_row = random_row(board)
ship1_col = random_col(board)

ship2_row = random_row(board)
ship2_col = random_col(board)

ship3_row = random_row(board)
ship3_col = random_col(board)

print "Let's play Battleship! Find one of my three ships in the 0-3 ocean"
print print_board(board)

#let user guess 4 times
for turn in range(3):
    print "Turn", turn + 1

    #let the user guess
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    #check if user is right, give feedback and print new board if nesessary
    if (guess_row == ship1_row and guess_col == ship1_col) \
    or (guess_row == ship2_row and guess_col == ship2_col) \
    or (guess_row == ship3_row and guess_col == ship3_col):
        print "Congratulations! You sunk a battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 3) \
        or (guess_col < 0 or guess_col > 3):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

        print_board(board) 

        #tell user he/she looses
        if turn == 2:
            print "Game Over"


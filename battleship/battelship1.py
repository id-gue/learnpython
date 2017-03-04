'''Battelship exercise by codecademy
https://www.codecademy.com/courses/python-beginner-en-4XuFm/1/2?curriculum_id=4f89dab3d788890003000096'''

from random import randint

board = []

#build our ocean
for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"

#hide our ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#save ship position
ship_row = random_row(board)
ship_col = random_col(board)

#let the user guess
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))
    
#let user guess 4 times
for turn in range(4):
    print "Turn", turn + 1

    #let the user guess
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    #check if user is right, give feedback and print new board if nesessary
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

        #tell user he/she looses
        if turn == 3:
            print "Game Over"

        print_board(board)

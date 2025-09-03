# Tic tac toe game made in python


# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Variables
winner = None
running = True
current_player = "X"


# Displaying the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Handling turns and inputting the game board
def handle_turns(player):
    # Getting input from the users
    pos = input("Choose a position from 1-9: ")

    valid = True
    while valid:

        # If pos is not equal to this then display this again and not show an error
        while pos not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            pos = input("Choose a position from 1-9: ")

        # Converting the pos to a number and subtracting 1
        pos = int(pos) - 1

        if board[pos] == "-":
            valid = False
        else:
            print("You cannot go there go again")

    # Putting the input into the game board
    board[pos] = player
    # Displaying the board again to show
    display_board()


# Checking if the rows are full
def check_rows():
    global running, winner

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    # If that is true then print who won and set running to false
    if row1 or row2 or row3:
        running = False
        if row1:
            winner = board[0]
            print(winner + " won!")
        elif row2:
            winner = board[3]
            print(winner + " won!")
        elif row3:
            winner = board[6]
            print(winner + " won!")


def check_columns():
    global running, winner

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        running = False
        if column1:
            winner = board[0]
            print(winner + " won!")
        elif column2:
            winner = board[1]
            print(winner + " won!")
        elif column3:
            winner = board[2]
            print(winner + " won!")


def check_diagonals():
    global running, winner

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        running = False
        if diagonal1:
            winner = board[0]
            print(winner + " won!")
        elif diagonal2:
            winner = board[2]
            print(winner + " won!")


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def tie():
    global winner, running

    if "-" not in board:
        running = False
        winner = "Tie"
        print(winner)


def game_over():
    check_rows()
    check_columns()
    check_diagonals()
    flip_player()
    tie()


def play_game():
    display_board()

    while running:
        handle_turns(current_player)

        game_over()


play_game()

#------Global variables---------

# Game Board
board = ["#", "-", "-", "-",
            "-", "-","-",
             "-", "-", "-"]


# If game is still going        
game_continues = True

# Won or Tie?
winner = None


# Whos turn is it?
def current_player():
    current_player = input('Welcome To Tic-Tac-Toe!\n Please choose X or O: ').upper()
    if current_player != 'X' or current_player != 'O':
        current_player = False

# The game........................
def play_game():
    #print('Welcome To Tic-Tac-Toe!')
    # Display initial board
    display_board()
    

    #While the game continues.....
    while game_continues:
        
        # Handle the turn of the current player
        handle_turn(current_player)
        
        # Check if the game is over
        check_game_over()

        # Flip to the other player
        flip_player()

    # The Game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('The Game Is A Tie.')


def display_board():
    bright_yellow = "\033[0;93m"
    green = "\033[0;32m"
    print(green  + '     |     |')
    print(green  + '7: ' + bright_yellow +  board[7] + green  +' |8: '+ bright_yellow  + board[8] + green  +' |9: '+ bright_yellow + board[9])
    print(green  + '     |     |')
    print(green  + '------------------')
    print(green  + '     |     |')
    print(green  + '4: ' + bright_yellow +  board[4] + green  +' |5: '+ bright_yellow  + board[5] + green  +' |6: '+ bright_yellow + board[6])
    print(green  + '     |     |')
    print(green  + '------------------')
    print(green  + '     |     |')
    print(green  + '1: ' + bright_yellow +  board[1] + green  +' |2: '+ bright_yellow  + board[2] + green  +' |3: '+ bright_yellow + board[3])
    print(green  + '     |     |')

def handle_turn(player):

    print(player + "'s turn.")
    position = input('Choose a position from 1-9: ')
    
    valid = False
    while not valid:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Try again. Choose a position from 1-9: ')

        position = int(position)

        if board[position] == "-":
            valid = True
        else:
            print("You can choose that one, try again: ")

    board[position] = player
    display_board()


def check_game_over():
    check_win()
    check_tie()


def check_win():

    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None

    return

def check_rows():
    # set global variable
    global game_continues
    # check if rows have same value and not '-'
    row_1 = board[7] == board[8] == board[9] != '-'
    row_2 = board[4] == board[5] == board[6] != '-'
    row_3 = board[1] == board[2] == board[3] != '-'
    
    # if column has a match, then flag there is a winner
    if row_1 or row_2 or row_3:
        game_continues = False
    
    # return the winner (X or O)
    if row_1:
        return board[7]
    elif row_2:
        return board[4]
    elif row_3:
        return board[1]

    return



def check_columns():
    # set global variable
    global game_continues
    # check if columns have same value and not '-'
    column_1 = board[1] == board[4] == board[7] != '-'
    column_2 = board[2] == board[5] == board[8] != '-'
    column_3 = board[3] == board[6] == board[9] != '-'

    # if column has a match, then flag there is a winner
    if column_1 or column_2 or column_3:
        game_continues = False

    # # return the winner (X or O)
    if column_1:
        return board[1]
    elif column_2:
        return board[2]
    elif column_3:
        return board[3]
    return


def check_diagonals():
    # set global variable
    global game_continues
    # check if diagonals have same value and not '-'
    diagonal_1 = board[1] == board[5] == board[9] != '-'
    diagonal_2 = board[3] == board[5] == board[7] != '-'
    
    # if diagonal has a match, then flag there is a winner
    if diagonal_1 or diagonal_2:
        game_continues = False

    # return the winner (X or O)
    if diagonal_1:
        return board[1]
    elif diagonal_2:
        return board[7]
    
    return


def check_tie():
    global game_continues
    if "-" not in board:
        game_continues = False
        
    return


def flip_player():
    # global variable we need
    global current_player
    # If current player was X, change to O
    if current_player == "X":
        current_player = "O"
    # If current player was O, change to X
    elif current_player == "O":
        current_player ="X"
    return



play_game()


# board
# display board
# play game
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player
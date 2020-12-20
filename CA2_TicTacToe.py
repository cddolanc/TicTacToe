#------Global variables---------

# Game Board - This is the initial values of the gameboard, # is used at position 0 as it caused 
# problems while checking for a tie in check_tie().
board = ["#", "-", "-", "-",
              "-", "-","-",
              "-", "-", "-"]


# If game is still going  - Boolean to check against if the game is on-going.
game_continues = True

# Won or Tie?   - Winner is initally set to None.
winner = None



# Whos turn is it?  - Initial value for current_player, changed when flip_player is called.
current_player = 'X'

       

# The game...................... The main steps called during the game.
def play_game():
    #print('Welcome To Tic-Tac-Toe!')

    # Display initial board - display the board (each square called from board[]).
    display_board()
    

    #While the game continues.....  -  a While loop calling each function until a winner or draw is declared.
    while game_continues:
        
        # Handle the turn of the current player - current_player = 'X' is the initial value assigned.
        handle_turn(current_player)
        
        # Check if the game is over  - If the game has more turns or not.
        check_game_over()

        # Flip to the other player  - if 'X' then 'O'.
        flip_player()

    # The Game has ended  - What happens when game is won or a draw.
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('The Game Is A Tie.')

# This is the board given to us in class, I've added colours to make the game board clearer.
def display_board():  
    bright_yellow = "\033[0;93m"      # This is a variable used for calling the colour.
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

# This function handles each player turn.
def handle_turn(player):
    
    # Declare who's turn it is.
    print(player + "'s turn.")

    # Get an input from the player for the square number.
    position = input('Choose a position from 1-9: ')
    
    #This While loop checks if the input is valid and checks if the square is empty.
    valid = False
    while not valid:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Try again. Choose a position from 1-9: ')

        position = int(position)

        if board[position] == "-":
            valid = True
        else:
            print("You can't choose that one, try again: ")

    # Sets the player's position on the board.
    board[position] = player
    # Calls the display_board function.
    display_board()

# Check if the game is over, by calling check_win and check_tie functions.
def check_game_over():
    check_win()
    check_tie()

# Check if there is a winner
def check_win():

    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    # If a winner is declared or not.
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
    
    # return the winner (X or O), depending on the value in board[].
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

    # Return the winner (X or O), depending on the value in board[].
    if column_1:
        return board[1]
    elif column_2:
        return board[2]
    elif column_3:
        return board[3]
    return

# Check for a diagonal winner.
def check_diagonals():
    # set global variable
    global game_continues
    # check if diagonals have same value and not '-'
    diagonal_1 = board[1] == board[5] == board[9] != '-'
    diagonal_2 = board[3] == board[5] == board[7] != '-'
    
    # if diagonal has a match, then flag there is a winner.
    if diagonal_1 or diagonal_2:
        game_continues = False

    # return the winner (X or O), depending on the value in board[].
    if diagonal_1:
        return board[1]
    elif diagonal_2:
        return board[7]
    
    return

# Checks if there are any more free spaces in the board, by checking for '-'.
def check_tie():
    global game_continues
    if "-" not in board:
        game_continues = False
        
    return

# This function flips from 'X' to 'O' or 'O' to 'X'.
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


# Call the game function - Start the game.
play_game()

#checklist:
# board
# display board
# play game
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player
board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceisfree(pos):
    return board[pos] == ' '



def printboard(board):
    bright_yellow = "\033[0;93m"
    green = "\033[0;32m"
    print(green  + '     |     |')
    print(green  + '1: ' + bright_yellow +  board[1] + green  +' |2: '+ bright_yellow  + board[2] + green  +' |3: '+ bright_yellow + board[3])
    print(green  + '     |     |')
    print(green  + '------------------')
    print(green  + '     |     |')
    print(green  + '4: ' + bright_yellow +  board[4] + green  +' |5: '+ bright_yellow  + board[5] + green  +' |6: '+ bright_yellow + board[6])
    print(green  + '     |     |')
    print(green  + '------------------')
    print(green  + '     |     |')
    print(green  + '7: ' + bright_yellow +  board[7] + green  +' |8: '+ bright_yellow  + board[8] + green  +' |9: '+ bright_yellow + board[9])
    print(green  + '     |     |')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(b,l):
    return (b[1] == l and b[2] == l and b[3] == l) or \
        (b[4] == l and b[5] == l and b[6] == l) or \
        (b[7] == l and b[8] == l and b[9] == l) or \
        (b[1] == l and b[4] == l and b[7] == l) or \
        (b[2] == l and b[5] == l and b[8] == l) or \
        (b[3] == l and b[6] == l and b[9] == l) or \
        (b[1] == l and b[5] == l and b[9] == l) or \
        (b[3] == l and b[5] == l and b[7] == l)

def playerMove():
    run = True
    while run:
        move = input('Choose a position fror X from 1-9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisfree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry this space is occupied. ')
            else:
                print('Please type a number between 1 and 9. ')

        except:
            print('Please type a number')



def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in [2, 4, 6, 8]:
        edgesOpen.append(i)

    if len(edgesOpen) > 0:
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def main():
    print('Welcome to Tic Tac Toe!')
    printboard

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printboard(board)
        else:
            print('Sorry you lose!')
            break

        if not(isWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(' ')
            else:
                insertLetter('O', move)
                print('Computer placed an O on position', move, ':')
                printboard(board)
            
        else:
            print('You Win!')



    if isBoardFull(board):
        print('Tie Game!')


while True:
    x= input('Do you want ot play again? y/n?')
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('---------------------')
        main()
    else:
        break

#Tic tac toe
import random
def display_board(board):

    row1 = board[7] + '|' +board[8]+ '|' + board[9]
    row2 = board[4] + '|' +board[5]+ '|' + board[6]
    row3 = board[1] + '|' +board[2]+ '|' + board[3]
    line = '-----'

    return row1 + '\n' +line + '\n'+row2 + '\n'+line + '\n'+row3

#board =  ['0','','O','X','O','X','O','X','O','X']

# tabla = display_function(board)
#print(tabla)

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#player_choice = player_input()
#print(player_choice)


def place_marker(board, marker, position):

    board[position] = marker



#place_marker(board, 'X', 5)
#tabla = display_board(board)
#print(tabla)


def win_check(board, mark):

    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))


#win = win_check(board,'X')
#print(win)

def choose_first():

    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


#rand = choose_first()
#print(rand)

def space_check(board, position):

    return board[position] == ' '

#n = space_check(board,1)
#print(n)


def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#n = full_board_check(board)
#print(n)

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('What is your next position: '))

    return position

#n = player_choice(board)
#print(n)

def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#x = replay()
#print(x)



print('Welcome to Tic Tac Toe!')

# Set the game up here
while True:
    board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input("Are you ready to play? Y or N ")

    if play_game[0]. lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn =='Player 1':
            print(display_board(board))
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board,player1_marker):
                print(display_board(board))
                print('Congratulations! Player 1 won!')
                game_on = False
            else:
                if full_board_check(board):
                    print(display_board(board))
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 2'


        else:
            print(display_board(board))
            position = player_choice(board)
            place_marker(board,player2_marker,position)

            if win_check(board, player2_marker):
                print(display_board(board))
                print('Congratulations! Player 2  won ')
                game_on = False
            else:
                if full_board_check(board):
                    print(display_board(board))
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break






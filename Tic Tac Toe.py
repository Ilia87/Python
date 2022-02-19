#### Step 1: Write a function that can print out a board.
#### Set up your board as a list, where each index 1-9 corresponds
#### with a number on a number pad, so you get a 3 by 3 board representation.

def display_board(board):
    print(' '*5)
    print('THE BOARD')
    print(' ' * 5)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-' * 5)
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-' * 5)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(' ' * 5)


#### Step 2: Write a function that can take in a player input
####  and assign their marker as 'X' or 'O'.
#### Think about using while loops to continually ask until you get a correct answer.

def player_input():
    marker = 'wrong'
    while marker not in ['X', 'O']:
        marker = input('Player1: Do you want to be X or O: ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


#### Step 3: a function that takes in the board list object, a marker ('X' or 'O'),
#### and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker


#### Step 4: a function that takes in a board and a mark (X or O)
#### and then checks to see if that mark has won.

def win_check(board, mark):
    return board[1] == board[2] == board[3] == mark or \
           board[4] == board[5] == board[6] == mark or \
           board[7] == board[8] == board[9] == mark or \
           board[1] == board[4] == board[7] == mark or \
           board[2] == board[5] == board[8] == mark or \
           board[3] == board[6] == board[9] == mark or \
           board[1] == board[5] == board[9] == mark or \
           board[3] == board[5] == board[7] == mark


#### Step 5: Write a function that uses the random module to randomly decide
#### which player goes first. You may want to lookup random.randint()
#### Return a string of which player went first.

import random
def choose_first():
    flip = (random.randint(1, 2))
    if flip == 1:
        return 'player1'
    else:
        return 'player2'


#### Step 6: Write a function that returns a boolean indicating
#### whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '


#### Step 7: Write a function that checks if the board is full
#### and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    check = ' ' not in (marks for marks in board)
    return check


#### Step 8: Write a function that asks for a player's next position (as a number 1-9)
#### and then uses the function from step 6 to check if it's a free position.
#### If it is, then return the position for later use.


def player_choice(board):
        position = 'wrong'
        with_range = False
        while position == 'wrong' or with_range == False:
            position = input(f'{turn}, pick a position to replace (1-9): ')
            if position.isdigit() == False:
                print(f'Sorry "{position}" is not a number')
            elif position.isdigit() == True:
                if int(position) in range(1,10):
                    with_range = True
                else:
                    print(f'Sorry "{position}" is not in range (1-9)')
                    with_range = False
        return position

#### Step 9: function that asks the player if they want to play again
#### and returns a boolean True if they do want to play again.
def replay():
    replay_game = input('do you wanna play again, y or n:')
    if replay_game == 'y':
        return True
    else:
        return False

##################GAME################
print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    display_board(board)
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')

    play_game = input('do you wanna play the game, y or n:')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'player1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker):
                display_board(board)
                print('player1 has won!')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print('Nobody won, because the board is full')
                game_on = False
            else:
                turn = 'player2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                display_board(board)
                print('player2 has won!')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print('Nobody won, because the board is full')
                game_on = False
            else:
                turn = 'player1'

    if not replay():
        print('Goodbye!')
        break
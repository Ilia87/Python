board = ['#', '', '', '', '', '', 'X', 'X', 'X', '']

#### Step 1: Write a function that can print out a board.
#### Set up your board as a list, where each index 1-9 corresponds
#### with a number on a number pad, so you get a 3 by 3 board representation.
#
# def display_board(board):
#     print(board[7] + '|' + board[8] + '|' + board[9])
#     print('-' * 5)
#     print(board[4] + '|' + board[5] + '|' + board[6])
#     print('-' * 5)
#     print(board[1] + '|' + board[2] + '|' + board[3])
#
#
# display_board(board)
#


#### Step 2: Write a function that can take in a player input
####  and assign their marker as 'X' or 'O'.
#### Think about using while loops to continually ask until you get a correct answer.

# def player_input():
#     marker = 'wrong'
#     while marker not in ['X', 'O']:
#         marker = input('Player1: Do you want to be X or O: ').upper()
#     player1 = marker
#     if player1 == 'X':
#         player2 = 'O'
#     else:
#         player2 = 'X'
#
#     print(player1, player2)
#     return player1, player2
#
#
# player_input()




#### Step 3: a function that takes in the board list object, a marker ('X' or 'O'),
#### and a desired position (number 1-9) and assigns it to the board.

# def place_marker(board, marker, position):
#     position = 'wrong'
#     with_range = False
#     while position == 'wrong' or with_range == False:
#         position = input('Pick a position to replace (1-9): ')
#         if position.isdigit() == False:
#             print(f'Sorry "{position}" is not a number')
#         elif position.isdigit() == True:
#             if int(position) in range(1,10):
#                 with_range = True
#             else:
#                 print(f'Sorry "{position}" is not a valid position (1-9)')
#                 with_range = False
#     board[int(position)] = marker
#
#
#     print(position)
#     print(board)
#     return(board)
#
# place_marker(board,'$',7)



#### Step 4: a function that takes in a board and a mark (X or O)
#### and then checks to see if that mark has won.

# def  win_check (board, mark):
#     if board[1] == board[2] == board[3] == mark or \
#        board[4] == board[5] == board[6] == mark or \
#        board[7] == board[8] == board[9] == mark or \
#        board[1] == board[4] == board[7] == mark or \
#        board[2] == board[5] == board[8] == mark or \
#        board[3] == board[6] == board[9] == mark or \
#        board[1] == board[5] == board[9] == mark or \
#        board[3] == board[5] == board[7] == mark:
#         print('win')
#     else:
#         print('next')
#
#
# win_check(board,'X')



#### Step 5: Write a function that uses the random module to randomly decide
#### which player goes first. You may want to lookup random.randint()
#### Return a string of which player went first.

# import random
# def choose_first():
#     flip = (random.randint(1,2))
#     if flip == 1:
#         print('player1')
#         return 'player1'
#     else:
#         print('player2')
#         return 'player2'
#
#
# choose_first()



#### Step 6: Write a function that returns a boolean indicating
#### whether a space on the board is freely available.

def space_check(board, position):

    print(board[position] == '')
    return board[position] == ''

#space_check(board,9)



#### Step 7: Write a function that checks if the board is full
#### and returns a boolean value. True if full, False otherwise.

# def full_board_check(board):
#     check = '' in (marks for marks in board)
#     print(check)
#     return check
#
#
# full_board_check(board)


#### Step 8: Write a function that asks for a player's next position (as a number 1-9)
#### and then uses the function from step 6 to check if it's a free position.
#### If it is, then return the position for later use.


def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Pick a position to replace (1-9): '))
    print(position)
    return position


player_choice(board)
    # print('Welcome to Tic Tac Toe!')
    # print('This is your board:')
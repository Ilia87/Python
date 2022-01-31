def display_board(board):
    print('Welcome to Tic Tac Toe!')
    print('This is your board:')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-' * 5)
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-' * 5)
    print(board[1] + '|' + board[2] + '|' + board[3])

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(board)


def player_x_o():
    choice
    player1 = input('Do you want to be X or O: ')
    print()


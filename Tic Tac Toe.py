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


def player_input():
    choice = 'wrong'
    while choice not in ['X', 'O']:
        choice = input('Player1: Do you want to be X or O: ')
        if choice not in ['X', 'O']:
            print("Sorry, I didn't understand. Please make sure to choose X or O.")
    if choice == 'X':
        print("Player1 will be first")
        return 'X'
    elif choice == 'O':
        print("Player1 will be second")
        return 'O'


player_input()




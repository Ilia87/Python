def display_board(board):


    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-' * 5)
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-' * 5)
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(test_board)

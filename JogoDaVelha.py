# Paulo Henrique Melo Teixeira e Pedro Henrique Bezerra Buarque de Paula



board = ['_'] * 9
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

print_board()
contador = 0
while True:
    x = input('Qual a jogada do jogador 1 (de 0 a 8)? ')
    x = int(x)
    if board[x] == 'X' or board[x] == 'O':
        print_board()
        print('Jogada inválida, tente novamente!')
    else:
        board[x] = 'X'
        print_board()
        if board[contador] == board[contador + 1] and board[contador + 2] == board[contador] and board[contador] == 'X' or board[contador] == 'O':
            print('Você ganhou!')
            break
        elif board[contador] == board[contador + 3] and board[contador + 5] == board[contador] and board[contador] == 'X' or board[contador] == 'O':
            print('Você ganhou!')
            break
        elif board[0] == board[4] and board[8] == board[0] and board[contador] == 'X' or board[contador] == 'O':
            print('Você ganhou!')
        elif board[2] == board[4] and board[6] == board[0] and board[contador] == 'X' or board[contador] == 'O':
            print('Você ganhou!')

    y = input('Qual a jogada do jogador 2 (de 0 a 8)? ')
    y = int(y)
    if board[y] == 'X' or board[y] == 'O':
        print_board()
        print('Jogada inválida, tente novamente!')
    else:
        board[y] = 'O'
        print_board()
        if board[contador] == board[contador + 1] and board[contador + 2] == board[contador] and board[contador] == 'X' or board[contador] == 'O':
            print('Você ganhou!')
            break
        elif board[contador] == board[contador + 3] and board[contador + 5] == board[contador] and board[contador] == 'X' or board[contador] == 'O':
            print('Você ganhou!')
            break
        elif board[0] == board[4] and board[8] == board[0] and board[contador] == 'X' or board[contador] == 'O':
            print('Você ganhou!')
        elif board[2] == board[4] and board[6] == board[0] and board[contador] == 'X' or board[contador] == 'O':
            print('Você ganhou!')




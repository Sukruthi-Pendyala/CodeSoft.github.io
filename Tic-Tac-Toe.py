def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(board[i][j] in ['X', 'O'] for i in range(3) for j in range(3))

def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move! That spot is already taken or out of range.")
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        player = players[turn % 2]
        row, col = get_move(board, player)
        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break
        
        turn += 1

play_game()

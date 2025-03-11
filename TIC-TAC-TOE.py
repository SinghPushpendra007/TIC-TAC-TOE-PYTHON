def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    """Checks if the specified player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    """Returns a list of available moves on the board."""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def play_tic_tac_toe():
    """Main function to run the Tic Tac Toe game between two players."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print("Welcome to Tic Tac Toe!")
    player1 = input("Enter the name of Player 1 (X): ")
    player2 = input("Enter the name of Player 2 (O): ")
    
    current_player = player1
    current_symbol = 'X'
    
    while True:
        print_board(board)
        
        if is_winner(board, 'X'):
            print(f"{player1} wins!")
            break
        if is_winner(board, 'O'):
            print(f"{player2} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # Current player's turn
        while True:
            try:
                row, col = map(int, input(f"{current_player}'s turn. Enter your move (row and column: 0 1 2): ").split())
                if board[row][col] == " ":
                    board[row][col] = current_symbol
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 2.")

        # Switch players
        if current_player == player1:
            current_player = player2
            current_symbol = 'O'
        else:
            current_player = player1
            current_symbol = 'X'

if __name__ == "__main__":
    play_tic_tac_toe()

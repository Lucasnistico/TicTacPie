# Tic Tac Toe Game in Python

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Check if the player has won."""
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)

def main():
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0  # Player 'X' starts
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        print(f"Player {players[current_player]}'s turn")
        
        # Get the player's move
        try:
            row, col = map(int, input("Enter row and column (0-2, separated by space): ").split())
            if board[row][col] != " ":
                print("Cell is already occupied. Try again!")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers between 0 and 2.")
            continue
        
        # Make the move
        board[row][col] = players[current_player]
        print_board(board)
        
        # Check for winner
        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break
        
        # Check for a tie
        if is_full(board):
            print("It's a tie!")
            break
        
        # Switch player
        current_player = 1 - current_player

if __name__ == "__main__":
    main()

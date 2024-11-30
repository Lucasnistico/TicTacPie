import tkinter as tk
from tkinter import messagebox

def check_winner():
    """Check if there's a winner."""
    for row in board:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            return row[0]["text"]
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != "":
            return board[0][col]["text"]
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        return board[0][0]["text"]
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        return board[0][2]["text"]
    return None

def is_tie():
    """Check if the board is full (tie)."""
    for row in board:
        for cell in row:
            if cell["text"] == "":
                return False
    return True

def handle_click(row, col):
    """Handle a button click."""
    global current_player
    if board[row][col]["text"] == "" and not game_over:
        board[row][col]["text"] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif is_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            label["text"] = f"Player {current_player}'s turn"

def reset_game():
    """Reset the game board."""
    global game_over, current_player
    for row in board:
        for cell in row:
            cell["text"] = ""
    current_player = "X"
    label["text"] = "Player X's turn"
    game_over = False

root = tk.Tk()
root.title("Tic Tac Toe")


current_player = "X"
game_over = False
board = []


for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                        command=lambda r=i, c=j: handle_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    board.append(row)

label = tk.Label(root, text="Player X's turn", font=("Arial", 18))
label.grid(row=3, column=0, columnspan=3)


root.mainloop()

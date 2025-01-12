import tkinter as tk
from tkinter import messagebox
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False
def button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_board()
        elif all(all(cell != "" for cell in row) for row in board):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_board()
        current_player = "O" if current_player == "X" else "X"
def reset_board():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")
root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=10, height=3, command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)


root.mainloop()

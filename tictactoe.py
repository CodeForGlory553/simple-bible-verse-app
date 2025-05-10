import random

board = [" " for _ in range(1, 9)]

def display_board():
    print("-" * 15)
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        print("--" * 15)

if __name__ == "__main__":
    display_board()
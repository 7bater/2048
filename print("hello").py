import random
import os

def get_score(board):
    return sum(sum(row) for row in board)

def get_max_tile(board):
    return max(max(row) for row in board)

def count_empty(board):
    return sum(cell == 0 for row in board for cell in row)
SIZE = 5

def init_board():
    board = [[0]*SIZE for _ in range(SIZE)]
    add_tile(board)
    add_tile(board)
    return board

def add_tile(board):
    empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = 4 if random.random() < 0.1 else 2

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print('\t'.join(str(num) if num else '.' for num in row))
    print()
def compress(row):
    new_row = [num for num in row if num]
    new_row += [0] * (SIZE - len(new_row))
    return new_row

def merge(row):
    for i in range(SIZE-1):
        if row[i] and row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    return row

def move_left(board):
    moved = False
    new_board = []
    for row in board:
        compressed = compress(row)
        merged = merge(compressed)
        final = compress(merged)
        if final != row:
            moved = True
        new_board.append(final)
    return new_board, moved

def move_right(board):
    reversed_board = [row[::-1] for row in board]
    moved_board, moved = move_left(reversed_board)
    return [row[::-1] for row in moved_board], moved

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_up(board):
    transposed = transpose(board)
    moved_board, moved = move_left(transposed)
    return transpose(moved_board), moved

def move_down(board):
    transposed = transpose(board)
    moved_board, moved = move_right(transposed)
    return transpose(moved_board), moved

def can_move(board):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return True
            if c < SIZE-1 and board[r][c] == board[r][c+1]:
                return True
            if r < SIZE-1 and board[r][c] == board[r+1][c]:
                return True
    return False

def main():
    board = init_board()
    while True:
        print_board(board)
        move = input("WASD (q=quit): ").lower()
        if move == 'q':
            break
        if move not in 'wasd':
            continue
        if move == 'a':
            new_board, moved = move_left(board)
        elif move == 'd':
            new_board, moved = move_right(board)
        elif move == 'w':
            new_board, moved = move_up(board)
        elif move == 's':
            new_board, moved = move_down(board)
        if moved:
            board = new_board
            add_tile(board)
        if not can_move(board):
            print_board(board)
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
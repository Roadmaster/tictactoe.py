#!/usr/bin/python3
board = [None for i in range(9)]
row_size = 3

def get_move(player, board):
    while True:
        raw_move = input("Player %s Move: " % player)
        if board[int(raw_move) - 1]:
            print("Position already taken")
            continue
        if len(board) > int(raw_move) - 1 >= 0:
            return int(raw_move) - 1


def print_board(board):
    for index, cell in enumerate(board):
        print(cell if cell else index+1, end="")
        if (index+1) % row_size == 0:
            print("")

def game_over(board):
    # Over if there's a line or board is full or no chances to complete
    # a line.
    # Method returns False if no winner yet, symbol for winner if someone
    # won, or True if game is over due to stalemate.
    # Diagonals
    line_specs = [(0, 4, 8), (2, 4, 6), (0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8)]
    lines = [list(board[i] for i in line) for line in line_specs]
    winnable_lines = 0
    for line in lines:
        if len(set(line)) == 1:
            return set(line).pop()
        if None in line and len(set([e for e in line if e is not None])) == 1:
            winnable_lines += 1
    if winnable_lines:
        return False
    return True


current_player_symbol = "O"
print_board(board)
while not game_over(board):
    move = get_move(current_player_symbol, board)
    print("Move is %s" % move)
    board[move] = current_player_symbol
    print_board(board)
    current_player_symbol = "O" if current_player_symbol == "X" else "X"

who_won = game_over(board)
if who_won is True:
    print("Stalemate!")
else:
    print("%s WINS!!!" % who_won)

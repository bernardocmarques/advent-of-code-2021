from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

    draw = lines[0].split(",")

    boards = []
    board = []
    for line in lines[2:]:
        if line == "":
            boards.append(board)
            board = []
        else:
            board.append([e for e in line.split(" ") if e != ""])
    boards.append(board)

draw_score = 0

for d in draw:

    for board in boards:
        for i in range(len(board)):
            board[i] = ["X" if e == d else e for e in board[i]]

    for board in boards:
        if check_win_board(board):
            boards.remove(board)

        if len(boards) == 0:
            board_score = get_board_score(board)
            print(int(d), board_score, int(d) * board_score)
            exit()

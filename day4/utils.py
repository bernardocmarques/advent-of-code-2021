def print_board(board):
    for line in board:
        print(line)


def print_boards(boards):
    for board in boards:
        print_board(board)
        print()


def check_win_row(board):
    for i in range(len(board)):
        if " ".join([e[i] for e in board]) == "X X X X X":
            return True
    return False


def check_win_line(board):
    for line in board:
        if " ".join(line) == "X X X X X":
            return True
    return False


def check_win_board(board):
    return check_win_row(board) or check_win_line(board)


def get_board_score(board):
    score = 0
    for line in board:
        for l in line:
            if l != "X":
                score += int(l)

    return score





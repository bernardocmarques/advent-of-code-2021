from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]


syntax_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

score_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0

for line in lines:
    to_close = []

    for char in line:
        if char in syntax_dict.keys():
            to_close.append(syntax_dict[char])
        else:
            next_char = to_close.pop()
            if char != next_char:
                print(f'Found a illegal {char}')
                score += score_dict[char]
                break

print(score)
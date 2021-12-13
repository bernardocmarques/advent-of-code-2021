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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


score_list = []
for line in lines:
    to_close = []

    for char in line:
        if char in syntax_dict.keys():
            to_close.append(syntax_dict[char])
        else:
            next_char = to_close.pop()
            if char != next_char:
                to_close = []
                break


    if to_close:
        to_close.reverse()
        score = 0
        for char_missing in to_close:
            score *= 5
            score += score_dict[char_missing]
        print(f'{"".join(to_close)} - {score}')
        score_list.append(score)

score_list.sort()
print(score_list[len(score_list)//2])
from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

lst = eval(lines[0])


for new_lst in lines[1:]:
    print(" ", lst)
    print("+", new_lst)

    lst = addiction(lst, eval(new_lst))

    exploded = True
    while exploded:
        exploded = explode(lst)
        # print(f"after explode: {lst}")
        if exploded:
            continue
        _, exploded, splitted = split(lst)
        while splitted and not exploded:
            _, exploded, splitted = split(lst)

        # print(f"after split: {lst}")
    print("=", lst)
    print()

print(magnitude(lst))


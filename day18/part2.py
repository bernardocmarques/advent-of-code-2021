import copy
import itertools

from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

lists = [eval(e) for e in lines]

permutations = list(itertools.permutations(lists, 2))

max_mag = -1

p = None

for permutation in permutations:
    lst_1 = copy.deepcopy(permutation[0])
    lst_2 = copy.deepcopy(permutation[1])

    lst = addiction(lst_1, lst_2)

    exploded = True
    while exploded:
        exploded = explode(lst)
        if exploded:
            continue
        _, exploded, splitted = split(lst)
        while splitted and not exploded:
            _, exploded, splitted = split(lst)

    max_mag = max(max_mag, magnitude(lst))

print(max_mag)


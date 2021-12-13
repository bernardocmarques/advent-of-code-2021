from utils import *
import time

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

max_x = -1
max_y = -1

dots = []

go_on = True
while go_on:
    line = lines.pop(0)
    if line == '':
        go_on = False
        break
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])

    max_x = max(max_x, x)
    max_y = max(max_y, y)

    dots.append((x, y))

folds = []

for line in lines:
    f = line.split("fold along ")[1]
    folds.append(tuple(f.split("=")))

print(dots)
print(folds)

grid = []

for y in range(max_y + 1):
    line = []
    for x in range(max_x + 1):
        if (x, y) in dots:
            line.append('#')
        else:
            line.append(".")
    grid.append(line)

print_grid(grid)

fold(grid, folds[0])


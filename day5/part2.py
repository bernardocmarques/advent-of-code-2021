from utils import *

with open("input.txt", "r") as input_file:
    lines_text = [e.replace("\n", "") for e in input_file.readlines()]
    lines = [[e.split(" -> ")[0].split(","), e.split(" -> ")[1].split(",")] for e in lines_text]

grid = {}

for line in lines:
    p1 = [int(e) for e in line[0]]
    p2 = [int(e) for e in line[1]]

    if p1[0] == p2[0]:
        for n in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            if not grid.get(n):
                grid[n] = {}

            if grid[n].get(p1[0]):
                grid[n][p1[0]] += 1
            else:
                grid[n].update({p1[0]: 1})
    elif p1[1] == p2[1]:
        for n in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):

            if not grid.get(p1[1]):
                grid[p1[1]] = {}

            if grid[p1[1]].get(n):
                grid[p1[1]][n] += 1
            else:
                grid[p1[1]].update({n: 1})
    else:
        d = abs(p1[1] - p2[1])
        s1 = int((p2[0] - p1[0]) / abs(p2[0] - p1[0]))
        s2 = int((p2[1] - p1[1]) / abs(p2[1] - p1[1]))

        for i in range(d+1):
            x = p1[0] + i*s1
            y = p1[1] + i*s2
            if not grid.get(y):
                grid[y] = {}

            if grid[y].get(x):
                grid[y][x] += 1
            else:
                grid[y].update({x: 1})

print_grid(grid)

count = 0
for line_key in grid:
    for point_key in grid[line_key]:
        if grid[line_key][point_key] >= 2:
            count += 1

print(count)